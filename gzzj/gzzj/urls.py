from django.conf.urls import url
from django.contrib import admin

from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from worked import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'gzzj', views.GzzjViewSet)
router.register(r'gzzjlist', views.GzzjListViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('docs/', include_docs_urls(title="工作总结系统")),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
]
