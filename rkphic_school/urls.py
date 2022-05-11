from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rkphic_school import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('about', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('admin/', admin.site.urls),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('api/', include(('api.urls', 'api'), namespace='api')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
