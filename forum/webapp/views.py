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
from webapp.forms import ItemForm, SearchForm

class ItemPageView(ListView):
    model = Item
    template_name = "items/index.html"
    context_object_name = "item"
    paginate_by = 5

    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context["form"] = self.form
        if self.search_value:
            context["query"] = urlencode({'search': self.search_value})
            context["search_value"] = self.search_value
        return context

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

    def get_queryset(self):
        queryset = super().get_queryset()
        print(self.search_value)
        if self.search_value:
            queryset = queryset.filter(Q(title__icontains=self.search_value) | Q(author__icontains=self.search_value))
        return queryset

class ItemCreateView(LoginRequiredMixin, CreateView):
    form_class = ItemForm
    template_name = 'items/create.html'
    model = Item

    def get_success_url(self):
        return reverse('webapp:index')

class ItemDetailView(DetailView):
    model = Item
    template_name = 'items/detail.html'
    context_object_name = "item"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item = self.get_object()
        comments = item.comments.all()
        context['comments'] = comments
        return context