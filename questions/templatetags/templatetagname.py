from django import template
from .models import Profile

register = template.Library()

@register.filter(name='has_gamification')
def has_gamification(user):
    profile = Profile.objects.get(user = user)
    return profile.group

