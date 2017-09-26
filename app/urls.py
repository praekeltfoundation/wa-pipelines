
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from wapipelines.api import views
from app.views import login, logout, login_error, ProfileView


router = routers.SimpleRouter()
router.register(r'pipelines', views.PipelineViewSet, 'pipeline')


urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^login/error/$', login_error, name='login-error'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^profile/$', login_required(
        ProfileView.as_view()), name='profile'),
    url(r'', include('social_django.urls', namespace='social')),
    url(r'^', include('wapipelines.urls', namespace='pipeline')),
    url(r'^api/v1/', include(router.urls, namespace='api')),
    url(r'^api/v1/docs/', include_docs_urls(title='Pipelines API'),
        name='api-docs'),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
