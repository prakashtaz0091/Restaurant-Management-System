
from django.contrib import admin
from django.urls import path, include
from core.views import (home_view, 
                        about_view, 
                        menu_view, 
                        cart_view,
                        order_view,
                        order_status_view,
                        payment_view,
                        payment_confirm_view,
                        )
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    path("admin/", admin.site.urls),
    path("", home_view, name="home-page"),
    path("about-us/", about_view),
    path("hotel-menu/tables/<table_id>/", menu_view, name="menu-page"),
    path("cart/", cart_view, name="cart-page"),
    path("order/", order_view, name="order-page"),
    path("order/status/<order_id>/", order_status_view, name="order-status-api"),
    path("payment/", payment_view, name="payment_view"),
    path("payment/confirm/", payment_confirm_view, name="payment_confirm_view"),
    
    path("accounts/", include("accounts.urls")),
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="accounts/password_reset_form.html",
            email_template_name="accounts/password_reset_email.html",
            subject_template_name="accounts/password_reset_subject.txt",
            success_url="/password-reset/done/",
        ),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="accounts/password_reset_done.html",
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/password_reset_confirm.html",
            success_url="/reset/done/",
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/password_reset_complete.html",
        ),
        name="password_reset_complete",
    ),
    
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )