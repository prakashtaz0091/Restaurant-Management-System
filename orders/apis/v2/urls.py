from .views import MenuItemViewset, CategoryViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'menuitems', MenuItemViewset, basename='menuitem')
router.register(r'categories', CategoryViewset, basename='category')
urlpatterns = router.urls