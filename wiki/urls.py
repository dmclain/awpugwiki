from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView
from .models import Page
from .views import CreatePage, EditPage, ViewPage, ListPage, HistoryPage

urlpatterns = patterns('',
    url(r'^$', ListPage.as_view(), name='page_list'),
    url(r'^new$', CreatePage.as_view(), name='page_new'),
    url(r'^(?P<slug>[\w-]+)$', ViewPage.as_view(), name='page_view'),
    url(r'^(?P<slug>[\w-]+)/edit$', EditPage.as_view(), name='page_edit'),
    url(r'^(?P<slug>[\w-]+)/history$', HistoryPage.as_view(),
        name='page_history'),
    url(r'^(?P<slug>[\w-]+)/(?P<id>\d+)$', ViewPage.as_view(), name='page_view'),
    # url(r'^awpugwiki/', include('awpugwiki.foo.urls')),
)
