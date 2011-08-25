from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template.defaultfilters import slugify
from .forms import NewPageForm, EditPageForm
from .models import Page


class CreatePage(CreateView):
    form_class = NewPageForm
    model = Page

    def get_success_url(self):
        return reverse('page_view', kwargs={'slug': self.object.slug})

    def form_valid(self, form):
        page = form.save(commit=False)
        page.slug = slugify(page.title)
        page.user = self.request.user
        page.save()
        self.object = page
        return HttpResponseRedirect(self.get_success_url())


class EditPage(UpdateView):
    form_class = EditPageForm
    template = 'wiki/page_edit.html'

    def get_success_url(self):
        return reverse('page_view', kwargs={'slug': self.object.slug})

    def get_object(self):
        return Page.objects.filter(slug=self.kwargs['slug']).order_by('-date_modified')[0]

    def form_valid(self, form):
        self.object = Page()
        self.object.title = form.cleaned_data['title']
        self.object.slug = form.cleaned_data['slug']
        self.object.body = form.cleaned_data['body']
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ViewPage(DetailView):
    model = Page

    def get_object(self):
        if 'id' in self.kwargs:
            return Page.objects.get(id=self.kwargs['id'])
        return Page.objects.filter(slug=self.kwargs['slug']).order_by('-date_modified')[0]


class HistoryPage(ListView):
    model = Page
    template_name = 'wiki/page_history.html'

    def get_queryset(self):
        return Page.objects.filter(slug=self.kwargs['slug']).order_by('-date_modified')


class ListPage(ListView):
    model = Page

    def get_queryset(self):
        return Page.objects.values('title', 'slug').order_by('title').distinct()
