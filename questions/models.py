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


    def save(self, *args, **kwargs):
        if not self.id:
            if self.user.id % 2 == 0:
                self.group == True
        super(Profile, self).save(*args, **kwargs)


    def increment_num_questions(self):
        self.increment_points()
        self.num_questions += 1
        self.check_question_badges()
        
    def check_question_badges(self):
        if self.num_questions == 10 :
            if not self.ten_question : 
                self.ten_question = True
                increment_num_badges(self)
                self.points += 500
        elif self.num_questions == 5 :
            if not self.five_questions :
                self.five_questions = True
                increment_num_badges(self)
                self.points += 300
        elif self.num_questions == 1 :
            if not self.first_question :
                self.first_questions = True
                increment_num_badges(self)
                self.points += 100

    def increment_points(self):
        if(self.streak == 0):
            self.points += 100
        else:    
            self.points += 100 * (0.9 + (self.streak/10))
    
    def increment_streak(self):
        self.streak += 1
        self.check_streak_badges()

    def check_streak_badges(self):
        if self.streak == 7 :
            if not seven_day_streak : 
                seven_day_streak = True
                increment_num_badges(self)
                self.points += 600
        elif self.streak == 5 :
            if not self.five_day_streak :
                self.five_day_streak = True
                increment_num_badges(self)
                self.points += 400
        elif self.streak == 3 :
            if not self.three_day_streak :
                self.three_day_streak = True
                increment_num_badges(self)
                self.points += 200

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
    choice_a = models.CharField(max_length=200, default="")
    choice_a_correct = models.BooleanField(default=False)
    choice_b = models.CharField(max_length=200, default="")
    choice_b_correct = models.BooleanField(default=False)
    choice_c = models.CharField(max_length=200, default="")
    choice_c_correct = models.BooleanField(default=False)
    choice_d = models.CharField(max_length=200, default="")
    choice_d_correct = models.BooleanField(default=False)


    #def save(self, *args, **kwargs):
    #    profile = Profile.objects.get(self.user)
         