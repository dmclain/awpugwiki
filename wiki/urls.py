from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView
from .models import Page
from .views import CreatePage, EditPage, ViewPage

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(model=Page), name='page_list'),
    url(r'^new$', CreatePage.as_view(), name='page_new'),
    url(r'^(?P<slug>[\w-]+)$', ViewPage.as_view(), name='page_view'),
    url(r'^(?P<slug>[\w-]+)/edit$', EditPage.as_view(), name='page_edit'),
    # url(r'^awpugwiki/', include('awpugwiki.foo.urls')),
)
