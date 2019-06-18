# Create your views here.


from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from Course.models import User
from Email.models import Email
from Email.models import draft



def index(request):
    email_list = Email.objects.all()
    template = loader.get_template('Email/index.html')
    context = {
        'email_list': email_list,
    }
    return HttpResponse(template.render(context, request))



def writeEmail(request):
    return render(request, 'Email/writeEmail.html')


def draftBox(request):
    #保存草稿
    isEncrypto = request.POST['isEncrypto']  # 是否加密
    receiverStr = request.POST['receiver']
    title = request.POST['title']
    content = request.POST['content']
    d = draft(senderID="1", receiver=receiverStr, isEncrypto=isEncrypto, title=title, content=content)
    d.save()
    #print("db")
    return render(request, 'Email/writeEmail.html', {'saveDraft': '保存草稿成功'})


def sentEmail(request):
    return render(request, 'Email/sentEmail.html')


def postEmail(request):
    isEncrypto = request.POST['isEncrypto']  #是否加密
    receiverStr = request.POST['receiver']
    title = request.POST['title']
    content = request.POST['content']
    print(isEncrypto)
    print(receiverStr)
    print(title)
    print(content)
    try:
        receiver = User.objects.get(email=receiverStr)
    except User.DoesNotExist:
        return render(request, 'Email/writeEmail.html', {'noReceiver': '收信人不存在'})
    #检测收件人合法性
    if isEncrypto == "1":
        #加密
        print(1)
    else:
        #不加密
        email = Email(senderID="1", receiverID=receiver.u_id, title=title, content=content)
        email.save()
        print(email)
        print(0)
    return render(request, 'Email/writeEmail.html', {'sendEmail': '发送邮件成功'})

