from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs)
    if created:
        Profile.objects.create(user=instance.id)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()   


@receiver(post_save, sender=Question)
def update_profile(sender, instance, **kwargs)
    profile = Profile.objects.get(instance.user)
    questions = Question.objects.filter(user=instance.user).order_by('-pub_date')
    if questions.exists():
        delta = (datetime.now().date() - questions.first().pub_date.date()).days()
        if delta == 1:
            profile.increment_streak()
        elif delta > 1:
            profile.streak = 1
    else 
        profile.streak = 1
        
    profile.increment_num_questions()
    profile.save()
        
