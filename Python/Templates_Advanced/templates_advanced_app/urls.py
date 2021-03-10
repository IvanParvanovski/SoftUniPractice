from django.urls import path

from templates_advanced_app.views import create, server_private_file, IndexView

urlpatterns = (
    # path('', index, name='index'),
    path('', IndexView.as_view(), name='index'),
    path('create', create, name='create'),
    path('resources/<path:path_to_file>', server_private_file, name='private file')
)
