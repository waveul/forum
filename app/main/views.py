from django.shortcuts import render, get_object_or_404
from .models import Board, Thread, User, Post
from .forms import RegistrationForm, CommentForm, ThreadForm
from django.http import HttpResponseRedirect
from django.db.models import Q


def index(request):
    Data = {
        'Boards1': Board.objects.all()[:3],
        'Boards2': Board.objects.all()[3:9],
        'Boards3': Board.objects.all()[9:13],
        'Boards4': Board.objects.all()[13:16],
        'Boards5': Board.objects.all()[16:19],
        'Threads': Thread.objects.all().order_by("-Time_Created")[:10],
        'Users': User.objects.all()
    }
    return render(request, "main/index.html", Data)


def index_board(request, id):
    Boards = get_object_or_404(Board, pk=id)
    form = ThreadForm
    if request.method == 'POST':
        form = ThreadForm(request.POST, UserID=request.user, Board=Boards)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    Data = {'Boards': Board.objects.get(pk=id), 'form': form, 'Threads': Thread.objects.all().order_by("-Time_Created")[:10]}
    return render(request, "main/index_board.html", Data)


def index_thread(request, id):
    thread = get_object_or_404(Thread, pk=id)
    form = CommentForm
    if request.method == 'POST':
        form = CommentForm(request.POST, UserID=request.user, ThreadID=thread)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    Data = {'thread': thread, "form": form, 'Threads': Thread.objects.all().order_by("-Time_Created")[:10]}
    return render(request, "main/index_thread.html", Data)


def index_user(request, username):
    Data = {'User': User.objects.get(username=username), 'Threads': Thread.objects.all().order_by("-Time_Created")[:10]}
    return render(request, "main/index_user.html", Data)


def index_posts(request):
    thread = Thread.objects.all().order_by("-Time_Created")
    query = request.GET.get('q', None)
    if query is not None:
        thread = thread.filter(Q(Tittle__icontains=query) | Q(Content__icontains=query))
    Data = {'Thread': thread, 'Threads': Thread.objects.all().order_by("-Time_Created")[:10]}
    return render(request, "main/index_posts.html", Data)


def index_users(request):
    Data = {'User': User.objects.all().order_by("-date_joined"), 'Threads': Thread.objects.all().order_by("-Time_Created")[:10]}
    return render(request, "main/index_users.html", Data)


def terms_and_conditions(request):
    Data = {'Threads': Thread.objects.all().order_by("-Time_Created")[:10]}
    return render(request, "main/terms_and_conditions.html", Data)


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, "main/register.html", {'form': form, 'Threads': Thread.objects.all().order_by("-Time_Created")[:10]})
