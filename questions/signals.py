from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Question, Profile
import datetime 


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, **kwargs):
    if kwargs.get('created', True):
        grp = False
        if (instance.id % 2 == 0):
            grp = True
        Profile.objects.create(user=instance, group=grp)

'''@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()'''   

@receiver(pre_save, sender=Question)
def update_streak(sender, instance, **kwargs):
    if kwargs.get('created', True):
        profile = Profile.objects.get(user = instance.user)
        questions = Question.objects.filter(user=instance.user).order_by('-pub_date')
        if questions.exists():
            delta = (datetime.date.today() - questions.first().pub_date).days
            #delta = (datetime.now().date() - questions.first().pub_date.date()).days
            if delta == 1:
                profile.increment_streak()
            elif delta > 1:
                profile.streak = 1
        else: 
            profile.streak = 1
    profile.save()

@receiver(post_save, sender=Question)
def update_profile(sender, instance, **kwargs):
    if kwargs.get('created', True):
        profile = Profile.objects.get(user = instance.user)   
        profile.increment_num_questions()
    profile.save()
       
