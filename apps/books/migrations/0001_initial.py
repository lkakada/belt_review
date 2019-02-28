# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-27 17:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('submitted_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='login.User')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=255)),
                ('rating', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('reviewing_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_reviews', to='books.Book')),
                ('reviewing_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_reviews', to='login.User')),
            ],
        ),
    ]