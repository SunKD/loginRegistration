from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index, name='quote_index'),
    url(r'^newquote$', views.add_quote, name='add_quote'),
    url(r'^add_favorite$', views.favorite, name="add_favorite"),
    url(r'^remove_favorite$', views.remove_favorite, name="remove_favorite"),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete_quote'),
    url(r'^users/(?P<id>\d+)$', views.view_user, name="view_user"),
    url(r'^logout$', views.logout, name='logout'),
]