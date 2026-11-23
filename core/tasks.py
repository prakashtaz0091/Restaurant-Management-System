# from background_task import background
from .services import analyse_popular_items
from celery import shared_task


@shared_task
def udpate_popular_menu_items():
    print("------Updating popular items-------")
    analyse_popular_items()
    print("updated")
    