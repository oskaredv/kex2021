from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Question, Profile
import datetime 
from django.contrib import messages


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, **kwargs):
    if kwargs.get('created', True):
        grp = False
        if (instance.id % 2 == 0):
            grp = True
        Profile.objects.create(user=instance, group=grp)  

@receiver(pre_save, sender=Question)
def update_streak(sender, instance, **kwargs):
    profile = Profile.objects.get(user = instance.user)
    if kwargs.get('created', True):
        questions = Question.objects.filter(user=instance.user).order_by('-pub_date')
        if questions.exists():
            delta = (datetime.date.today() - questions.first().pub_date).days
            if delta == 1:
                profile.increment_streak()
            elif delta > 1:
                profile.streak = 1
        else: 
            profile.streak = 1
    profile.save()

@receiver(post_save, sender=Question)
def update_profile(sender, instance, **kwargs):
    profile = Profile.objects.get(user = instance.user)   
    if kwargs.get('created', True):
        profile.increment_num_questions()
        messages.success("test")
    profile.save()
       
