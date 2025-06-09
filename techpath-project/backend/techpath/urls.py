from django.contrib import admin
from django.urls import path, include # include is needed
from django.views.generic import TemplateView # To serve React app
from django.conf import settings # To access STATICFILES_DIRS
from django.conf.urls.static import static # To serve static files during development

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include your app's URLs
    # Catch-all for React routing, serves index.html
    # This should be the last URL pattern
    path('', TemplateView.as_view(template_name='index.html')), # Serves from 'build' dir
    path('<path:resource>', TemplateView.as_view(template_name='index.html')), # Handles any other path
]

# This is for DEVELOPMENT only, to serve static files from STATICFILES_DIRS.
# In production, WhiteNoise or your web server (like Nginx) would handle this.
# However, since 'build' is in STATICFILES_DIRS, Django's dev server will serve it.
# if settings.DEBUG:
#    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
