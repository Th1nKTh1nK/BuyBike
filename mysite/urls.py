from django.urls import path
from blog import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('admin/', admin.site.urls),
]
