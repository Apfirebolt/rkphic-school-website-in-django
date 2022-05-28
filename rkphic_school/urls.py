from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rkphic_school import settings
from django.views.generic import TemplateView
from rkphic_school.views import NotificationListView, StudentListView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('about', TemplateView.as_view(template_name='about.html'), name='about'),
    path('about/director-message', TemplateView.as_view(template_name='director-message.html'), name='director-message'),
    path('about/admissions', TemplateView.as_view(template_name='admissions.html'), name='admissions'),
    path('contact', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('gallery', TemplateView.as_view(template_name='gallery.html'), name='gallery'),
    path('courses', TemplateView.as_view(template_name='courses.html'), name='courses'),
    path('notifications', NotificationListView.as_view(), name='notifications'),
    path('students', StudentListView.as_view(), name='students'),
    path('admin/', admin.site.urls),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('api/', include(('api.urls', 'api'), namespace='api')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
