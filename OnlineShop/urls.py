"""OnlineShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include, re_path
from rest_framework_jwt.views import obtain_jwt_token

import xadmin
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from goods import views
# from OnlineShop.settings import MEDIA_ROOT
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register('goods', views.GoodsViewSet, base_name='goods')
router.register('categorys', views.CategoryViewSet, base_name='category')
# goods_list = GoodsViewSet.as_view({
#     'get': 'list',
# })

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', include(router.urls)),
    path('login/', obtain_jwt_token),
    path('api-auth/', include('rest_framework.urls')),
    # re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    path('docs/', include_docs_urls('title="b'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
