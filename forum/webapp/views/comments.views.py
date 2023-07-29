from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms import CommentForm
from webapp.models import Item, Comment


class CommentCreateView(CreateView):
    form_class = CommentForm
    template_name = "comments/comment_create.html"

    def form_valid(self, form):
        item = get_object_or_404(Item, pk=self.kwargs.get("pk"))
        comment = form.save(commit=False)
        comment.item = item
        comment.author = self.request.user
        comment.save()
        return redirect("webapp:detail", pk=item.pk)


class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "comments/comment_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["message"] = "test"
        return context

    def get_success_url(self):
        return reverse("webapp:detail", kwargs={"pk": self.object.item.pk})


class CommentDeleteView(DeleteView):
    model = Comment

    def get_success_url(self):
        return reverse("webapp:detail", kwargs={"pk": self.object.item.pk})

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)