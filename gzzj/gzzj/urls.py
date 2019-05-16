from django.conf.urls import url
from django.contrib import admin

from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from worked import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet, base_name='users')
router.register(r'usersadd', views.UserAddViewSet, base_name='usersadd')
router.register(r'usersupdate', views.UserUpdateViewSet, base_name='usersupdate')
router.register(r'userpassword', views.UserPasswordViewSet, base_name='userpassword')
router.register(r'gzzj', views.GzzjViewSet, base_name='gzzj')
router.register(r'gzzjlist', views.GzzjListViewSet, base_name='gzzjlist')
router.register(r'gzzjupdate', views.GzzjUpdateViewSet, base_name='gzzjupdate')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^login/', obtain_jwt_token),
    path('docs/', include_docs_urls(title="工作总结系统")),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
]
