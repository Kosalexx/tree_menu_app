from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import index_controller, tree_menu

urlpatterns = [
    path("", index_controller, name="menus-in-db"),
    path("<path:url>", tree_menu, name="tree_menu"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
