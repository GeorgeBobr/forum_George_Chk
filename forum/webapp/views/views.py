from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Group
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.utils.html import urlencode
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView, ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.models import Item
from webapp.forms import ItemForm

class ItemPageView(ListView):
    model = Item
    template_name = "items/index.html"
    context_object_name = "items"
    paginate_by = 5


class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'items/create.html'

    def get_success_url(self):
        return reverse('webapp:index')

class ItemDetailView(DetailView):
    model = Item
    template_name = 'items/detail.html'
    context_object_name = "items"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item = self.get_object()
        comments = item.comments.all()
        context['comments'] = comments
        return context