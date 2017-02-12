from django.conf.urls import url, include
from django.conf import settings, urls
from django.contrib import admin
from django.conf.urls.static import static
from rest_framework import routers
from todo.views import TodoViewset

router = routers.DefaultRouter()
router.register(r'todos', TodoViewset)

urlpatterns = [url(r'^', include(router.urls)), ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns.append(url(r'^api/', include('rest_framework.urls',
                                             namespace='rest_framework')))
    urlpatterns.append(url(r'^admin/', admin.site.urls))
