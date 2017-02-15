from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Directory
from .models import Notefile
from .models import Notecard
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .forms import NotefileForm
from .forms import DirectoryForm
from django.shortcuts import redirect
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('welcome')


def welcome_text(request):
    return render(request, 'srs/welcome.html',{})

def home_directory(request):
    notefiles = Notefile.objects.filter(author=request.user).filter(directory__isnull=True)
    directories = Directory.objects.filter(author=request.user).filter(parent_directory=2)
    #Edit sos dynamic
    return render(request, 'srs/directory_view.html', {'notefiles': notefiles, 'directories': directories})

def create_directory(request):
    if request.method == "POST":
        form = DirectoryForm(request.POST)
        if form.is_valid():
            directory = form.save(commit=False)
            directory.author = request.user
            directory.created_date = timezone.now()
            directory.save()
            return redirect('home_directory')
    else:
        form = DirectoryForm()
    return render(request, 'srs/create_directory.html', {'form': form})

def login(request):
    return render(request, 'srs/login.html')

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'srs/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'srs/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'srs/post_edit.html', {'form': form})

def create_account(request):
    return render(request, 'srs/create_account.html')

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'srs/post_edit.html', {'form': form})

def notefile_list(request):
    notefiles = Notefile.objects.filter(created_date__lte=timezone.now())
    return render(request, 'srs/notefile_list.html', {'notefiles': notefiles})

def notefile_detail(request, name):
    notefile = get_object_or_404(Notefile, name=name)
    return render(request, 'srs/notefile_detail.html', {'notefile': notefile})

def notefile_new(request):
    if request.method == "POST":
        form = NotefileForm(request.POST)
        if form.is_valid():
            notefile = form.save(commit=False)
            notefile.author = request.user
            notefile.created_date = timezone.now()
            notefile.save()
            return redirect('notefile_list')
    else:
        form = NotefileForm()
    return render(request, 'srs/create_notefile.html', {'form': form}) 

def get_notefile(request):
    return request.GET.get('name')

def notecard_list(request, name):
    notefile_Name = Notefile.objects.get(name=name)
    notecards = Notecard.objects.filter(notefile= notefile_Name )
    notecards_count = notecards.count()
    if notecards_count == 0: 
        return render(request, 'srs/notecard_list_empty.html', {})
    else:
        return render(request, 'srs/notecard_list.html', {'notecards': notecards})

def notecard_detail(request, pk):
    notecard = get_object_or_404(Notecard, pk=pk)
    return render(request, 'srs/notecard_detail.html', {'notecard': notecard})

def about(request):
    return render(request, 'srs/about.html')

def contact(request):
    return render(request, 'srs/contact.html')
