from django.urls import path

from . import views

urlpatterns = [
    path(
        '',
        views.home, name='home',
    ),
    path(
        'register/',
        views.register,
        name='register',
    ),
    path(
        'login/',
        views.user_login,
        name='login',
    ),
    path(
        'logout/',
        views.user_logout,
        name='logout',
    ),
    path(
        'post_question/',
        views.post_question,
        name='post_question',
    ),
    path(
        'answer_question/<int:question_id>/',
        views.answer_question,
        name='answer_question',
    ),
    path(
        'like_answer/<int:answer_id>/',
        views.like_answer,
        name='like_answer',
    ),
]
