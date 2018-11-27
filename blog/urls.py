from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

    url(r'^$', views.post_main, name = 'post_list'),
    #임시
    url(r'^folio/$', views.post_folio, name = 'post_folio'),

    url(r'^post/(?P<pk>\d+)$', views.post_details, name='post_details'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
