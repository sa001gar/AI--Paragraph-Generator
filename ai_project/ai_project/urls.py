from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include the paragraph_generator URLs
    path('', include('paragraph_generator.urls')),  # This will handle all routes from the root URL
]