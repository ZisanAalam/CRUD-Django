from django.urls import path
from django.urls.conf import include
from .import views

urlpatterns = [
    path('',views.add_show, name='addshow'),
    path('<int:id>/',views.update_data, name='updatedata'),
    path('delete/<int:id>/', views.delete_data, name='deletedata'),
]