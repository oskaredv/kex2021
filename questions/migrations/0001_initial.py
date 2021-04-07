# Generated by Django 3.1.7 on 2021-04-07 09:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('choice_a', models.CharField(default='', max_length=200)),
                ('choice_a_correct', models.BooleanField(default=False)),
                ('choice_b', models.CharField(default='', max_length=200)),
                ('choice_b_correct', models.BooleanField(default=False)),
                ('choice_c', models.CharField(default='', max_length=200)),
                ('choice_c_correct', models.BooleanField(default=False)),
                ('choice_d', models.CharField(default='', max_length=200)),
                ('choice_d_correct', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.BooleanField(default=False)),
                ('points', models.IntegerField(default=0)),
                ('streak', models.IntegerField(default=0)),
                ('num_questions', models.IntegerField(default=0)),
                ('num_badges', models.IntegerField(default=0)),
                ('first_question', models.BooleanField(default=False)),
                ('five_questions', models.BooleanField(default=False)),
                ('ten_questions', models.BooleanField(default=False)),
                ('three_day_streak', models.BooleanField(default=False)),
                ('five_day_streak', models.BooleanField(default=False)),
                ('seven_day_streak', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
