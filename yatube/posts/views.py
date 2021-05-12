from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator

from .models import Post, Group, Follow
from .forms import PostForm, CommentForm

User = get_user_model()


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, "index.html", {'page': page, })


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.groups.all()[:10]
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request, "group.html", {
            "page": page, "group": group})


@login_required
def new_post(request):
    form = PostForm(request.POST or None,
                    files=request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = request.user
        obj.save()
        return redirect("index")
    return render(request, "new_post.html", {"form": form})


def profile(request, username):
    author = get_object_or_404(User, username=username)
    post_list = author.posts.all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request, "profile.html", {
            'page': page,
            'username': username,
            'author': author})


def post_view(request, username, post_id):
    post = get_object_or_404(Post,
                             id=post_id,
                             author__username=username)
    form = CommentForm()
    comments = post.comments.all()
    author = post.author
    posts_count = author.posts.count()
    return render(request, 'post.html', {'post': post,
                                         'form': form,
                                         'comments': comments,
                                         'posts_count': posts_count,
                                         'author': author})


@login_required
def post_edit(request, username, post_id):
    post = get_object_or_404(Post, id=post_id)
    if username != request.user.username:
        return redirect('post', username, post_id)
    form = PostForm(data=request.POST or None,
                    files=request.FILES or None,
                    instance=post)
    if form.is_valid():
        form.save()
        return redirect('post', username, post_id)
    return render(
        request, 'new_post.html', {
            'form': form, 'is_edit': True,
            'username': username,
            'post_id': post_id,
            'post': post})


def page_not_found(request, exception):
    return render(
        request,
        "misc/404.html",
        {"path": request.path},
        status=404
    )


def server_error(request):
    return render(request, "misc/500.html", status=500)


@login_required
def add_comment(request, username, post_id):
    post = get_object_or_404(Post,
                             author__username=username,
                             id=post_id)
    author = post.author
    posts_count = author.posts.count()
    form = CommentForm(request.POST or None)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.post = post
        new_comment.author = request.user
        new_comment.post_id = post_id
        new_comment.save()
        return redirect('post', username, post_id)
    return render(request, 'post.html', {'post': post,
                                         'form': form,
                                         'posts_count': posts_count})


@login_required
def follow_index(request):
    followed_objects = Follow.objects.filter(user=request.user)
    followed_authors = []
    for item in followed_objects:
        followed_authors.append(item.author)
    followed_posts = Post.objects.filter(author__in=followed_authors)
    paginator = Paginator(followed_posts, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'follow.html', {'page': page,
                                           'is_post_view': False})


@login_required
def profile_follow(request, username):
    user = User.objects.get(username=username)
    active_follow = Follow.objects.filter(user=request.user, author=user)
    if request.user != user and not active_follow:
        Follow.objects.create(user=request.user, author=user)
    return redirect('profile', username)


@login_required
def profile_unfollow(request, username):
    user = User.objects.get(username=username)
    Follow.objects.filter(user=request.user, author=user).delete()
    return redirect('profile', username)
