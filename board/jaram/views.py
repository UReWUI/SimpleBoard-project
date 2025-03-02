from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import ListView, DetailView
from .models import Post
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


def home(request):
    if request.user.is_authenticated:
        return redirect('jaram:post-list')
    return redirect('jaram:login')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "회원가입이 완료되었습니다. 로그인하세요.")
            return redirect('jaram:login')
        else:
            messages.error(request, "회원가입에 실패했습니다. 다시 시도해 주세요.")
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request,' 로그인 되었습니다.')
                return redirect('jaram:home')
            else:
                messages.error(request, '사용자 이름 또는 비밀번호가 잘못되었습니다.')
        else:
            messages.error(request, '사용자 이름 또는 비밀번호가 잘못되었습니다.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    for key in list(request.session.keys()):
        del request.session[key]
    return redirect('jaram:home')


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "게시글이 생성되었습니다.")
            return redirect('jaram:post-list')
    form = PostForm()  # 항상 새 폼을 반환
    return render(request, 'post_create.html', {'form': form})


@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # 게시글의 소유자 확인
    if post.author != request.user:
        messages.error(request, "이 게시글을 수정할 권한이 없습니다.")
        return redirect('jaram:post-list')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "게시글이 수정되었습니다.")
            return redirect('jaram:post-list')
    else:
        form = PostForm(instance=post)
    return render(request, 'post_create.html', {'form': form})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        messages.error(request, '권한이 없습니다.')
        return redirect('jaram:post-list')

    if request.method == 'POST':
        post.delete()
        messages.success(request, '게시글이 삭제되었습니다.')
        return redirect('jaram:post-list')
