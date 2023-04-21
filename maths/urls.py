from django.urls import path,include
from . import views
urlpatterns = [
    path('greet', views.greet),
    path('operation', views.operation),
    path('assignment', views.assignment),
    path('delete_record', views.delete_record),
    path('update_record', views.update_record),
    path('', views.check),
]