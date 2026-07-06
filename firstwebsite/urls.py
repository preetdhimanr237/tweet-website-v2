from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),

    path('tweet/', include('tweet.urls')),

    # Django auth (login/logout/register system)
    path('account/', include('django.contrib.auth.urls')),

    # root redirect
    path('', lambda request: redirect('tweet_list')),
]

# MEDIA (ONLY ONCE)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)