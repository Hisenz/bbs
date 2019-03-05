from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from user.util import plateutil, tagutil, postutil, reviewutil, pageutil, randomutil, mailutil
from .models import User, Plate, Tag, Post, Review
from .util import userutil, requestutil


# Create your views here.


def login(request):
    request.session.clear()
    email = request.POST.get('email')
    password = request.POST.get('password')
    message = ''
    if email:
        user = userutil.login(email=email, password=password)
        if user:
            request.session['user'] = user.pk
            request.session.set_expiry(0)
            return index(request)
        else:
            message = '用户名不存在或者密码错误'

    context = {
        'message': message,
    }
    return render(request, 'user/login.html', context=context)


def dynamic_login(request):
    try:
        del request.session["user"]
    except:
        pass
    email = request.POST.get('email')
    captcha = request.POST.get('captcha')
    message = ''
    try:
        if email == request.session.get("email") and captcha == request.session.get("captcha"):
            user = userutil.get_user_for_email(email)
            request.session['user'] = user.pk
            request.session.set_expiry(0)
            return index(request)
        else:
            message = '用户名不存在或者验证码错误'
    except Exception as e :
        pass

    context = {
        'message': message,
    }
    return render(request, 'user/dynamiclogin.html', context=context)


def get_user(request):
    email = request.GET.get('email')
    if userutil.get_user_for_email(email):
        return HttpResponse(1)
    else:
        return HttpResponse(0)


def sendmail(request):
    email = request.GET.get('email')
    if userutil.get_user_for_email(email):
        captcha = randomutil.generate(4)
        if mailutil.senderEmail(captcha, email):
            request.session['email'] = email
            request.session['captcha'] = captcha
            return HttpResponse(1)
        else:
            return HttpResponse(0)
    else:
        return HttpResponse(0)


def signup(request):
    request.session.clear()
    return render(request, 'user/signup.html')


def register(request):
    context = {
        'result': False,
    }
    if userutil.add_user(email=request.POST.get('email'), password=request.POST.get('password'),
                         nickname=request.POST.get('nickname')):
        context['result'] = True

    return render(request, 'user/result.html', context=context)


def index(request):
    pk = requestutil.get_session(name='user', request=request)
    context = {
        'user': userutil.get_user(user_id=pk),
        'plates': Plate.objects.filter(audit=True),
        'latest': Post.objects.all().order_by('-create_time')[0:5],
        'hottest': Post.objects.all().order_by('-give_a_like')[0:5],
    }
    return render(request, 'index.html', context=context)


def logout(request):
    request.session.clear()
    return HttpResponseRedirect('/')


def create_plate(request):
    user_id = requestutil.get_session(name='user', request=request)
    user = userutil.get_user(user_id)
    context = {
        'user': user,
        'form': 'plate',
    }
    return render(request, 'plate/create.html', context=context)


def add_plate(request):
    description = request.POST.get('description')
    plate_name = request.POST.get('plate_name')
    id = requestutil.get_session(name='user', request=request)
    message = plateutil.add_plate(name=plate_name, description=description, user_id=id)
    return HttpResponse(message)


def create_tag(request):
    user_id = requestutil.get_session(name='user', request=request)
    user = userutil.get_user(user_id)
    context = {
        'user': user,
        'form': 'tag',
    }
    return render(request, 'plate/create.html', context=context)


def add_tag(request):
    description = request.POST.get('description')
    tag_name = request.POST.get('plate_name')
    id = requestutil.get_session(name='user', request=request)
    message = tagutil.add_tag(tag_name=tag_name, description=description, user_id=id)
    return HttpResponse(message)


def show_user(request):
    user_id = requestutil.get_session(name='user', request=request)
    show = request.GET.get('show')
    page = 1
    try:
        page = int(request.GET.get('page'))
        if page < 0:
            page = 1
    except:
        pass
    showuser = userutil.get_user(show)
    posts = postutil.get_posts_for_user(showuser)
    current_page = pageutil.get_one_page(posts, page, 5)
    context = {
        'user': userutil.get_user(user_id),
        'showuser': showuser,
        'current_page': current_page,
        'total_post': posts.count(),
    }
    return render(request, 'user/show.html', context=context)


def to_change(request):
    user_id = requestutil.get_session(name='user', request=request)
    user = userutil.get_user(user_id)
    context = {
        'user': user,
    }
    return render(request, 'user/change.html', context=context)


def modify(request):
    user_information = {
        'email': request.POST.get('email'),
        'password': request.POST.get('password'),
        'nickname': request.POST.get('nickname'),
        'avatar': request.FILES.get('avatar'),
        'gender': request.POST.get('gender'),
        'description': request.POST.get('description'),
    }
    message = userutil.modify_information(user_information)
    return HttpResponse(message)


def posting(request):
    user_id = requestutil.get_session(name='user', request=request)
    user = userutil.get_user(user_id)
    context = {
        'user': user,
        'plates': plateutil.get_for_audit(True),
        'tags': Tag.objects.all(),
    }
    return render(request, 'post/create.html', context=context)


def add_post(request):
    user_id = requestutil.get_session(name='user', request=request)
    new_post = {
        'headline': request.POST.get('headline'),
        'plate': request.POST.get('plate'),
        'tag_list': request.POST.get('tag_list'),
        'description': request.POST.get('description'),
        'text_choice': request.POST.get('text_choice'),
    }
    message = postutil.add(user_id=user_id, post=new_post)

    return HttpResponse(message)


def post(request):
    user_pk = requestutil.get_session(name='user', request=request)
    post_id = request.GET.get('post_id')
    post = postutil.get(pk=post_id)
    context = {
        'post': post,
        'user': userutil.get_user(user_id=user_pk),
        'reviews': Review.objects.filter(post=post).order_by('-time'),
        'posts': postutil.get_posts_for_user(post.user, order='-create_time')[0:5],
    }
    return render(request, 'post/show.html', context=context)


def add_like(request):
    post_pk = request.POST.get('post_pk')
    post = Post.objects.get(pk=post_pk)
    post.give_a_like = post.give_a_like + 1
    post.save()
    return HttpResponse(1)


def reduce_like(request):
    post_pk = request.POST.get('post_pk')
    post = Post.objects.get(pk=post_pk)
    post.give_a_like = post.give_a_like - 1
    post.save()
    return HttpResponse(1)


def add_review(request):
    review = request.POST.get('review')
    post_pk = request.POST.get('post_pk')
    user_pk = requestutil.get_session(name='user', request=request)
    respose = reviewutil.add_review(user_pk=user_pk, post_pk=post_pk, content=review)
    return HttpResponse(respose)


def show_posts(request):
    plate_pk = request.GET.get('plate')
    user_pk = requestutil.get_session(name='user', request=request)
    plate = plateutil.get(plate_pk)
    posts = postutil.get_posts_for_plate(plate_pk)
    context = {
        'plate': plate,
        'posts': posts,
        'hottest': posts.order_by('-give_a_like'),
        'latest': posts.order_by('-create_time'),
        'user': userutil.get_user(user_id=user_pk),
    }

    return render(request, 'plate/showpost.html', context=context)


def show_post_for_search(request):
    pass
