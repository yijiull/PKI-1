# Generated by Django 2.2.1 on 2019-06-19 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0003_auto_20190619_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(null=True, upload_to='imgs'),
        ),
    ]