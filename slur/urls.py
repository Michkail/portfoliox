from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.homey, name="homey"),
    path('about/', views.aboutly, name="aboutly"),
    path('contact/', views.contactly, name="contactly")
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
