# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

from .models import User, Course, SC, Notice
import json
import shutil
import os

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, Http404
from django.urls import reverse

from django.core.files.base import ContentFile

from .util import verify_password, hash_password


def index(request):
    return render(request, 'Course/index.html')


def login_verify(request):
    id = request.POST["userid"]
    password = request.POST["password"]
    # print(id, password)

    # user = get_object_or_404(User, u_id=id)
    try:
        user = User.objects.get(u_id=id)
    except User.DoesNotExist:
        return render(request, 'Course/login.html', {'merror': '该学号不存在:)', });
    if verify_password(user.u_pwdhash, password):
        courses = []
        notices = []
        for sc in user.sc_set.all():
            course = Course.objects.get(id=sc.c_id_id)
            courses.append(course)

            #for notice in course.notice_set.all().order_by('-time')[:5]:
            #    notices.append(notice)

            notices += course.notice_set.all().order_by('-time')[:5]
        notices.sort(key=lambda x:x.time, reverse=True)

        return render(request, 'Course/index.html', {'user': user,
                                                     'course': courses,
                                                     'notice': notices})
        # return HttpResponseRedirect(reverse('Course:index', kwargs={'user': user}))
    else:
        return render(request, 'Course/login.html', {'merror': '密码错误:)<br>请重新输入密码~', })


def login(request):
    ip = request.META['REMOTE_ADDR']
    print(ip)
    return render(request, 'Course/login.html')


def register(request):
    return render(request, 'Course/reg.html')


def register_verify(request):
    userid = request.POST["userid"]
    username = request.POST["username"]
    sex = request.POST["sex"]
    role = request.POST["role"]
    tel = request.POST["tel"]
    email = request.POST["email"]
    dept = request.POST["dept"]
    birth = request.POST["birth"]
    password = request.POST["password"]
    repassword = request.POST["repassword"]
    if password != repassword:
        return render(request, 'Course/reg.html', {'error':'密码不一致:)',})
    password = hash_password(password)
    q = User(u_id=userid, u_name=username, sex=sex, role=role, tel=tel, email=email, dept=dept, u_pwdhash=password, birth=birth)
    try:
        q.save()
    except:
        raise Http404("注册失败!!")
    return render(request, 'Course/reg.html', {'error':'注册成功:)',})


def update_personal_info(request, userid):
    try:
        user = User.objects.get(u_id=userid)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'Course/updateInfo.html', {'user': user,})


def upload_pic(request, userid):
    try:
        user = User.objects.get(u_id=userid)
    except User.DoesNotExist:
        raise Http404("exist")
    pic = request.FILES.get("picture", "")
    if pic:
        os.remove(user.picture.path)
        file_content = ContentFile(pic.read())  # 创建File对象
        user.picture.save(hash_password(pic.name) + ".png", file_content)  # 保存文件到car的photo域, 必须是png后缀（奇怪）
        user.save()
        print("上传头像成功")
        return render(request, 'Course/updateInfo.html', {'user': user,})


def update_verify(request):
    userid = request.POST["userid"]
    username = request.POST["username"]
    sex = request.POST["sex"]
    role = request.POST["role"]
    tel = request.POST["tel"]
    email = request.POST["email"]
    dept = request.POST["dept"]
    birth = request.POST["birth"]
    password = request.POST["password"]
    repassword = request.POST["repassword"]
    if password != repassword:
        return render(request, 'Course/reg.html', {'error':'密码不一致:)',})
    password = hash_password(password)
    try:
        q = User.objects.get(u_id=userid)
    except User.DoesNotExist:
        raise Http404("exist")
    q.u_name=username
    q.sex=sex
    q.role=role
    q.tel=tel
    q.email=email
    q.dept=dept
    q.u_pwdhash=password
    q.birth=birth
    q.save()
    return render(request, 'Course/updateInfo.html', {'user': q, 'error': '修改成功',})


def get_files(filedir):
    res = []
    for par, dirs, files in os.walk(filedir):
        for f in files:
            res.append(os.path.join(par, f))
        for d in dirs:
            temp = get_files(os.path.join(par, d))
            res += temp
    return res


class Node:
    def __init__(self, filename):
        self.filename = filename
        self.child = []

class Tree:
    def __init__(self, course):
        self.rt = Node(course)

    def add(self, filepath):
        temp = filepath.split('/')
        q = self.rt
        for subdir in temp[temp.index(self.rt.filename)+1:]:
            ok = False
            for cur in q.child:
                if cur.filename == subdir:
                    q = cur
                    ok = True
                    break

            if not ok:
                node = Node(subdir)
                q.child.append(node)
                q = node

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                            sort_keys=True, indent=4)





def parse_files(files, course):
    tree = Tree(course)
    for f in files:
        tree.add(f)
    res = tree.toJson()
    print(res)
    return res



def course(request, courseid):
    course = Course.objects.get(c_id=courseid)
    course.c_visited += 1
    course.save()
    notice = course.notice_set.filter(type='NT')
    homework = course.notice_set.filter(type='HW')
    files = get_files('static/%s/' % course.c_name)
    files = parse_files(files, course.c_name)
    return render(request, 'Course/course.html', {'course': course,
                                                  'notice': notice,
                                                  'homework': homework,
                                                  'files': files,})


from django.http import FileResponse




def download(request, filepath):
    print(os.getcwd())
    a = filepath.split(':')
    filename = a[-1]
    filepath = '/'.join(a)
    file = open(filepath,'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename=\"' + filename + '\"'
    return response
