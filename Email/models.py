from django.db import models

# Create your models here.


class Email(models.Model):  #邮件
    senderID = models.CharField(max_length=20)
    receiverID = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.senderID + "-->" + self.receiverID + " title : "+self.title


class draft(models.Model):   #草稿
    senderID = models.CharField(max_length=20)
    receiver = models.CharField(max_length=50)
    isEncrypto = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.senderID + "-->" + self.receiverID + " title : " + self.title
