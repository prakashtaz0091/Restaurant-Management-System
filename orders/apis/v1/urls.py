from rest_framework.routers import DefaultRouter
from .views import MenuItemViewset, TableViewset, CategoryViewset

router = DefaultRouter()
router.register(r'menuitems', MenuItemViewset, basename='menuitem')
router.register(r'tables', TableViewset, basename='table')
router.register(r'categories', CategoryViewset, basename='category')

urlpatterns = router.urls