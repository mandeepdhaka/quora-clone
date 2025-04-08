from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from django.http import JsonResponse
from django.shortcuts import HttpResponseRedirect, get_object_or_404, redirect, render

from .forms import AnswerForm, QuestionForm, UserLoginForm, UserRegistrationForm
from .models import Answer, Like, Question


# User Registration View
def register(
    request
):
    if request.method == 'POST':
        form = UserRegistrationForm(
            request.POST
        )
        if form.is_valid():
            user = form.save()
            login(
                request,
                user
            )
            return redirect(
                'home'
            )
    else:
        form = UserRegistrationForm()
    return render(
        request,
        'questions/register.html',
        {
            'form': form,
        }
    )


# User Login View
def user_login(
    request
):
    if request.method == 'POST':
        form = UserLoginForm(
            request.POST
        )
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(
                    request, 
                    user
                )
                return redirect(
                    'home'
                )
    else:
        form = UserLoginForm()
    return render(
        request,
        'questions/login.html',
        {
            'form': form,
        }
    )


# User Logout View
@login_required
def user_logout(
    request
):
    logout(
        request,
    )
    return redirect(
        'login'
    )


# Home View (List Questions)
def home(
    request,
):
    questions = Question.objects.all()
    return render(
        request,
        'questions/home.html',
        {
            'questions': questions,
        }
    )


# Post Question View
@login_required(
    login_url='/login/'
)
def post_question(
    request,
):
    if request.method == 'POST':
        form = QuestionForm(
            request.POST
        )
        if form.is_valid():
            question = form.save(
                commit=False
            )
            question.created_by = request.user
            question.save()
            return redirect(
                'home'
            )
    else:
        form = QuestionForm()
    return render(
        request,
        'questions/post_question.html',
        {
            'form': form,
        }
    )


# Answer a Question View
def answer_question(
    request,
    question_id
):
    question = Question.objects.get(
        id=question_id
    )
    if request.method == 'POST':
        form = AnswerForm(
            request.POST,
        )
        if form.is_valid():
            answer = form.save(
                commit=False,
            )
            answer.question = question
            answer.created_by = request.user
            answer.save()
            return HttpResponseRedirect(
                request.META.get(
                    'HTTP_REFERER',
                    '/',
                )
            )
    else:
        
        form = AnswerForm()
        question = get_object_or_404(
            Question,
            id=question_id,
        )
        likes_queryset = Like.objects.filter(
            user=request.user.id,
        )
        answers = Answer.objects.filter(
            question=question
        ).prefetch_related(
            Prefetch(
                'likes',
                queryset=likes_queryset
            )
        )
        
    return render(
        request,
        'questions/answer_question.html',
        {
            'form': form,
            'question': question,
            'answers':answers,
        }
    )


# Like an Answer
@login_required(
    login_url='/login/'
)
def like_answer(
    request,
    answer_id,
):
    answer = Answer.objects.exclude(
        created_by=request.user
    ).filter(
        id=answer_id
    ).first()
    if answer:
        like, created = Like.objects.get_or_create(
            answer=answer,
            user=request.user,
        )
    return HttpResponseRedirect(
        request.META.get(
            'HTTP_REFERER',
            '/'
        )
    )


