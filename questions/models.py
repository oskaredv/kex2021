from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.BooleanField(default=False)
    points = models.IntegerField(default=0)
    streak = models.IntegerField(default=0)
    num_questions = models.IntegerField(default=0)
    num_badges = models.IntegerField(default=0)
    first_question = models.BooleanField(default=False)
    five_questions = models.BooleanField(default=False)
    ten_questions = models.BooleanField(default=False)
    three_day_streak = models.BooleanField(default=False)
    five_day_streak = models.BooleanField(default=False)
    seven_day_streak = models.BooleanField(default=False)

    def increment_num_questions(self):
        self.num_questions += 1
        if self.num_questions == 10 :
            if not self.ten_question : 
                self.ten_question = True
                increment_num_badges(self)
        elif self.num_questions == 5 :
            if not self.five_questions :
                self.five_questions = True
                increment_num_badges(self)
        elif self.num_questions == 1 :
            if not self.first_question :
                self.first_questions = True
                increment_num_badges(self)

        # Hantera streaks

    def get_group(self):
        return self.group
    
    def get_points(self):
        return self.points

    def increment_num_badges(self):
        self.num_badges += 1
        
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField(auto_now_add=True, blank = True)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    correct_choice = models.BooleanField(default=False)
 
    
"""
class Badges(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_question = models.BooleanField(default=False)
    five_questions = models.BooleanField(default=False)
    ten_questions = models.BooleanField(default=False)
    three_day_streak = models.BooleanField(default=False)
    five_day_streak = models.BooleanField(default=False)
    seven_day_streak = models.BooleanField(default=False)

    def set_badge_true(user_id)
        User.objects.get(pk=user_id).update_num_badges
"""

