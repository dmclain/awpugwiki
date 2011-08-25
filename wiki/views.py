from django.views.generic import CreateView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template.defaultfilters import slugify
from .forms import NewPageForm
from .models import Page

class CreatePage(CreateView):
    form_class = NewPageForm
    model = Page

    def get_success_url(self):
        return reverse('page_view', kwargs={'slug': self.object.slug})

    def post(self, request, *args, **kwargs):
        self.user = request.user
        return super(CreatePage, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        page = form.save(commit=False)
        page.slug = slugify(page.title)
        page.user = self.user
        page.save()
        self.object = page
        return HttpResponseRedirect(self.get_success_url())
