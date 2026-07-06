import logging
from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from django.core.files.base import ContentFile
from django.db.models import Sum, F
from orders.models import Order, OrderItem
from config.storages import PublicMediaStorage
from dateutil.relativedelta import relativedelta
from django.conf import settings

logger = logging.getLogger(__name__)

@shared_task(bind=True, max_retries=3)
def send_dummy_email(self, report_url=None):
    """
    Dummy task to confirm Celery + email pipeline works end-to-end.
    """
    try:
        send_mail(
            subject='Sales report generated',
            message=f'Please click the given link below to view the report: {report_url}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=["jikix20040@kinws.com"],
            fail_silently=False,
        )
        logger.info(f'Dummy email sent')
        return f'Email sent at {timezone.now()}'
    except Exception as exc:
        logger.error(f'Failed to send email: {exc}')
        raise self.retry(exc=exc, countdown=10)


@shared_task(bind=True, max_retries=3)
def generate_sales_report(self, start_date=None, end_date=None, period=None):
    """
    Generate a sales report HTML file and store it in the public media storage.
    Args:
        start_date (str or date, optional): Start date in YYYY-MM-DD format or date object.
                                            Defaults to today.
        end_date (str or date, optional): End date in YYYY-MM-DD format or date object.
                                          Defaults to today.
    Returns:
        str: Message with the URL of the generated report.
    """
    try:
        # Default to today's date if not provided
        if start_date is None:
            start_date = timezone.now().date()
        if end_date is None:
            end_date = timezone.now().date()
            
        if period is not None:
            if period == "weekly":
                start_date = timezone.now().date() - relativedelta(days=7)
            if period == "monthly":
                # logger.info("monthly")
                start_date = timezone.now().date() - relativedelta(months=1)
                # logger.info("monthly", start_date)
            if period == "quarterly":
                start_date = timezone.now().date() - relativedelta(months=3)
            if period == "semi-annualy":
                start_date = timezone.now().date() - relativedelta(months=6)
            if period == "annualy":
                start_date = timezone.now().date() - relativedelta(years=1)
            
        # Convert string dates to date objects if needed
        if isinstance(start_date, str):
            start_date = timezone.datetime.strptime(start_date, '%Y-%m-%d').date()
        if isinstance(end_date, str):
            end_date = timezone.datetime.strptime(end_date, '%Y-%m-%d').date()

        # Ensure start_date <= end_date
        if start_date > end_date:
            start_date, end_date = end_date, start_date

        # Filter orders created within the date range (inclusive)
        orders = Order.objects.filter(created_at__date__gte=start_date, created_at__date__lte=end_date)

        # Calculate aggregates
        total_revenue = OrderItem.objects.filter(order__in=orders).aggregate(
            total=Sum(F('price') * F('quantity'))
        )['total'] or 0
        total_orders = orders.count()
        total_items = OrderItem.objects.filter(order__in=orders).aggregate(
            total=Sum('quantity')
        )['total'] or 0

        now = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
        # Prepare HTML content
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
            <title>Sales Report</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 40px;
                    background-color: #f9f9f9;
                    color: #333;
                }}
                .container {{
                    max-width: 800px;
                    margin: 0 auto;
                    background: white;
                    padding: 20px;
                    box-shadow: 0 0 10px rgba(0,0,0,0.1);
                }}
                h1 {{
                    color: #2c3e50;
                    text-align: center;
                }}
                .info {{
                    margin: 20px 0;
                }}
                .info p {{
                    margin: 10px 0;
                    font-size: 1.1em;
                }}
                .footer {{
                    margin-top: 30px;
                    text-align: center;
                    font-size: 0.9em;
                    color: #7f8c8d;
                }}
                .print-button {{
                    display: block;
                    width: 200px;
                    margin: 20px auto;
                    padding: 10px;
                    background-color: #3498db;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    text-align: center;
                    cursor: pointer;
                }}
                .print-button:hover {{
                    background-color: #2980b9;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Sales Report</h1>
                <div class="info">
                    <p><strong>Period:</strong> {start_date} to {end_date}</p>
                    <p><strong>Total Revenue:</strong> Rs. {total_revenue}</p>
                    <p><strong>Total Orders:</strong> {total_orders}</p>
                    <p><strong>Total Items Sold:</strong> {total_items}</p>
                </div>
                <button class="print-button" onclick="window.print()">Print / Save as PDF</button>
                <div class="footer">
                    Generated on {now}
                </div>
            </div>
        </body>
        </html>
        """

        # Generate a filename
        if start_date == end_date:
            filename = f"sales_report/{period}_sales_report_{start_date}_{now}.html"
        else:
            filename = f"sales_report/{period}_sales_report_{start_date}_{end_date}_{now}.html"

        # Save to public media storage
        storage = PublicMediaStorage()
        # Save the file; the save method returns the actual filename used (which may be the same)
        saved_name = storage.save(filename, ContentFile(html_content.encode('utf-8')))
        # Get the URL
        file_url = storage.url(saved_name)

        logger.info(f'Sales report generated: {file_url}')
        
        send_dummy_email.delay(report_url=file_url)        
        return f'Sales report generated: {file_url}'

    except Exception as exc:
        logger.error(f'Failed to generate sales report: {exc}')
        raise self.retry(exc=exc, countdown=60)