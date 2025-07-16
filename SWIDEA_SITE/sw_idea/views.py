from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count, F
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CustomSignupForm, DevToolForm, IdeaForm
from .models import DevTool, Idea, IdeaStar

def signup_view(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('idea_list')
    else:
        form = CustomSignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('idea_list')

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET.get('next', 'idea_list'))

        messages.error(request, '아이디 또는 비밀번호가 올바르지 않습니다.')

    return render(request, 'accounts/login.html')



def logout_view(request):
    logout(request)
    return redirect('idea_list')


def idea_list(request):
    q        = request.GET.get('q', '').strip()
    tool_id  = request.GET.get('tool', '')
    sort     = request.GET.get('sort', 'latest') #최근이 디폹 값

    ideas = Idea.objects.all()

    if q:
        ideas = ideas.filter(title__icontains=q)

    if tool_id:
        ideas = ideas.filter(devtool_id=tool_id)

    if sort == 'likes':
        ideas = ideas.annotate(num_likes=Count('ideastar')).order_by('-num_likes', '-created_at')
    elif sort == 'title':
        ideas = ideas.order_by('title')
    elif sort == 'created':
        ideas = ideas.order_by('created_at')
    else:
        ideas = ideas.order_by('-created_at')

    page_obj = Paginator(ideas, 4).get_page(request.GET.get('page'))

    devtools = DevTool.objects.all() 

    return render(request, 'sw_idea/idea_list.html',
                  {'page_obj': page_obj, 'sort': sort,
                   'q': q, 'tool_id': tool_id, 'devtools': devtools})


def idea_detail(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    is_starred = False
    if request.user.is_authenticated:
        is_starred = IdeaStar.objects.filter(user=request.user, idea=idea).exists()
    return render(request, 'sw_idea/idea_detail.html', {
        'idea': idea,
        'is_starred': is_starred
    })

@login_required
def idea_create(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            idea = form.save()
            return redirect('idea_detail', pk=idea.pk)
    else:
        form = IdeaForm()
    return render(request, 'sw_idea/idea_form.html', {'form': form})

@login_required
def idea_edit(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            idea = form.save()
            return redirect('idea_detail', pk=idea.pk)
    else:
        form = IdeaForm(instance=idea)
    return render(request, 'sw_idea/idea_form.html', {'form': form})

@login_required
def idea_delete(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == 'POST':
        idea.delete()
        return redirect('idea_list')
    return render(request, 'sw_idea/idea_confirm_delete.html', {'idea': idea})

@login_required
def toggle_star(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    starred, created = IdeaStar.objects.get_or_create(user=request.user, idea=idea)
    if not created:
        starred.delete()
        return JsonResponse({'starred': False})
    return JsonResponse({'starred': True})

@login_required
def update_interest(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    action = request.POST.get('action')

    if action == 'plus':
        idea.interest = F('interest') + 1
    elif action == 'minus' and idea.interest > 0:
        idea.interest = F('interest') - 1
    idea.save()
    idea.refresh_from_db()

    return JsonResponse({'interest': idea.interest})

def devtool_list(request):
    devtools = DevTool.objects.all()
    return render(request, 'sw_idea/devtool_list.html', {'devtools': devtools})

def devtool_detail(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    ideas = devtool.ideas.all()
    return render(request, 'sw_idea/devtool_detail.html', {
        'devtool': devtool,
        'ideas': ideas
    })

@login_required
def devtool_create(request):
    if request.method == 'POST':
        form = DevToolForm(request.POST)
        if form.is_valid():
            devtool = form.save()
            return redirect('devtool_detail', pk=devtool.pk)
    else:
        form = DevToolForm()
    return render(request, 'sw_idea/devtool_form.html', {'form': form})

@login_required
def devtool_edit(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    if request.method == 'POST':
        form = DevToolForm(request.POST, instance=devtool)
        if form.is_valid():
            devtool = form.save()
            return redirect('devtool_detail', pk=devtool.pk)
    else:
        form = DevToolForm(instance=devtool)
    return render(request, 'sw_idea/devtool_form.html', {'form': form})

@login_required
def devtool_delete(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    if request.method == 'POST':
        devtool.delete()
        return redirect('devtool_list')
    return render(request, 'sw_idea/devtool_confirm_delete.html', {'devtool': devtool})