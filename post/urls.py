# urls.py
from django.urls import path
from post.views import PostView, PostDetailView, CommentView, UserView

urlpatterns = [
    # Cette route gère la liste et la création de posts.
    path('post/', PostView.as_view()),
    # Cette route gère un post spécifique, en utilisant un ID.
    path('post/<int:post_id>/', PostDetailView.as_view()),
    # Cette route gère la liste et la création des user.
    path('user/', UserView.as_view()),
    # Cette route gère la liste et la création des commentaire sur des posts.
    path('comment/', CommentView.as_view()),
]