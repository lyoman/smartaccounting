"""smartaccounting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.contrib import admin
from django.urls import include , path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token

admin.site.site_header = settings.ADMIN_SITE_HEADER
admin.site.site_title = "Smart Accounting"
admin.site.index_title = 'Smart Accounting Site Administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('/', admin.site.urls),
    # path('', include('accounts.urls')),

    #apis
    path('api/auth/token/', obtain_jwt_token),
    path('api/users/', include(("accounts.api.urls",'accounts-api'), namespace='accounts-api')),
    path('api/new_stock/', include(("newstock.api.urls",'newstock-api'), namespace='newstock-api')),
    # path('api/ims_05/', include(("ims_05.api.urls",'ims_05-api'), namespace='ims_05-api')),
    # path('api/ims_06/', include(("ims_06.api.urls",'ims_06-api'), namespace='ims_06-api')),
    # path('api/ims_07/', include(("ims_07.api.urls",'ims_07-api'), namespace='ims_07-api')),
    # path('api/ims_08/', include(("ims_08.api.urls",'ims_08-api'), namespace='ims_08-api')),
    # path('api/ims_09/', include(("ims_09.api.urls",'ims_09-api'), namespace='ims_09-api')),
    # path('api/ims_10/', include(("ims_10.api.urls",'ims_10-api'), namespace='ims_10-api')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
