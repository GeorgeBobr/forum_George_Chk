from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404

from accounts.forms import RegisterForm
from webapp.models import Item
class RegisterView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('webapp:index')
        return next_url

def profile_view(request, user_id):
    user_obj = get_object_or_404(User, pk=user_id)
    items = Item.objects.filter(author=user_obj)
    context = {
        'user_obj': user_obj,
        'items': items,
    }
    return render(request, 'user_room.html', context)