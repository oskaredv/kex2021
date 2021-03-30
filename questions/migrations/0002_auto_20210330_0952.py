# Generated by Django 3.1.7 on 2021-03-30 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='choice_a',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='question',
            name='choice_a_correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='choice_b',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='question',
            name='choice_b_correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='choice_c',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='question',
            name='choice_c_correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='choice_d',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='question',
            name='choice_d_correct',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
