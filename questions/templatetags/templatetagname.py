from django import template
from questions.models import Profile

register = template.Library()

@register.filter(name='has_gamification')
def has_gamification(user):
    profile = Profile.objects.get(user = user)
    return profile.group

@register.filter(name='get_gained_points')
def get_gained_points(user):
    profile = Profile.objects.get(user = user)
    return profile.points - profile.previous_points

