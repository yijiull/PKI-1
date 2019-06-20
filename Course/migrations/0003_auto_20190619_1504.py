# Generated by Django 2.2.1 on 2019-06-19 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0002_remove_user_salt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='picture',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='sc',
            name='absent_cnt',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='sc',
            name='grades',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('time', models.DateTimeField()),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Course.Course')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Course.User')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('time', models.DateTimeField()),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Course.Comment')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Course.User')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='about',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Course.Topic'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Course.User'),
        ),
    ]