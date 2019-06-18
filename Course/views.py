from django.shortcuts import render

# Create your views here.

from .models import User

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .util import verify_password


def index(request):
    return render(request, 'index.html')


def login_verify(request):
    id = request.POST["userid"]
    password = request.POST["password"]
    # print(id, password)

    # user = get_object_or_404(User, u_id=id)
    try:
        user = User.objects.get(u_id=id)
    except User.DoesNotExist:
        return render(request, 'login.html', {'error': '好像不存在该学号:)'})
    if verify_password(user.u_pwdhash, password):
        return render(request, 'index.html', {'user': user})
        # return HttpResponseRedirect(reverse('Course:index', kwargs={'user': user}))
    else:
        return render(request, 'login.html', {'error': '密码错误:)<br>请重新输入密码~'})


def login(request):
    return render(request, 'login.html')
