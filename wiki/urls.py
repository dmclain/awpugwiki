from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView
from .models import Page

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(model=Page), name='page_list'),
    url(r'^(?P<slug>\w+)$', DetailView.as_view(model=Page), name='page_view'),
    # url(r'^awpugwiki/', include('awpugwiki.foo.urls')),
)
