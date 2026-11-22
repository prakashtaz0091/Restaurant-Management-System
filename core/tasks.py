from background_task import background
from .services import analyse_popular_items


@background(schedule=0)
def udpate_popular_menu_items():
    print("------Updating popular items-------")
    analyse_popular_items()
    print("updated")
    