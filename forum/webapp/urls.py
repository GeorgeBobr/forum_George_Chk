from django.urls import path

from webapp.views.views import ItemPageView, ItemCreateView, ItemDetailView
from webapp.views.comments_views import CommentCreateView, CommentDeleteView, CommentUpdateView
app_name = "webapp"

urlpatterns = [
    path('', ItemPageView.as_view(), name='index'),
    path('create/', ItemCreateView.as_view(), name='create'),
    path('item/detail/<int:pk>/', ItemDetailView.as_view(), name='detail'),

    path('item/comment/<int:pk>/', CommentCreateView.as_view(), name='comment'),
    path('comment/update/<int:pk>/', CommentUpdateView.as_view(), name='update_comment'),
    path('comment/delete/<int:pk>', CommentDeleteView.as_view(), name='delete_comment')
]