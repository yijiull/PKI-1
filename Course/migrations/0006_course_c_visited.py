# Generated by Django 2.2.1 on 2019-06-19 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0005_auto_20190619_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='c_visited',
            field=models.IntegerField(default=0),
        ),
    ]
