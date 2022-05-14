from django.urls import path
from django.conf.urls.static import static
from rkphic_school import settings
from . views import ( CreateCustomUserApiView, GetCreateContactMessages, GetNotifications )
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('signup', CreateCustomUserApiView.as_view(), name='signup'),
    path('signin', obtain_auth_token, name='signin'),
    path('messages', GetCreateContactMessages.as_view(), name='get-create-messages'),
    path('notifications', GetNotifications.as_view(), name='get-notifications'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
