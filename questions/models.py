from django.db import models
from django.contrib.auth.models import User
import datetime 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.BooleanField(default=False)
    points = models.IntegerField(default=0)
    previous_points = models.IntegerField(default=0)
    streak = models.IntegerField(default=0)
    num_questions = models.IntegerField(default=0)
    num_badges = models.IntegerField(default=0)
    first_question = models.BooleanField(default=False)
    five_questions = models.BooleanField(default=False)
    ten_questions = models.BooleanField(default=False)
    two_day_streak = models.BooleanField(default=False)
    three_day_streak = models.BooleanField(default=False)
    four_day_streak = models.BooleanField(default=False)
    just_gainded_badge = models.BooleanField(default=False)

    def increment_num_questions(self):
        self.increment_points()
        self.num_questions += 1
        self.check_question_badges()
        
    def check_question_badges(self):
        if self.num_questions == 10 :
            if not self.ten_questions : 
                self.ten_questions = True
                self.just_gainded_badge = True
                self.increment_num_badges()
                self.increment_points_with_argument(500)
        elif self.num_questions == 5 :
            if not self.five_questions :
                self.five_questions = True
                self.just_gainded_badge = True
                self.increment_num_badges()
                self.increment_points_with_argument(300)
        elif self.num_questions == 1 :
            if not self.first_question :
                self.first_question = True
                self.just_gainded_badge = True
                self.increment_num_badges()
                self.increment_points_with_argument(100)
        else:
            self.just_gainded_badge = False

    def increment_points(self):
        self.previous_points = self.points
        if(self.streak == 0):
            self.points += 100
        else:    
            self.points += 100 * (0.9 + (self.streak/10))

    def increment_points_with_argument(self, points):
        self.previous_points = self.points
        self.points += points
    
    def increment_streak(self):
        self.streak += 1
        self.check_streak_badges()

    def check_streak_badges(self):
        if self.streak == 4 :
            if not four_day_streak : 
                four_day_streak = True
                self.just_gainded_badge = True
                self.increment_num_badges()
                self.increment_points_with_argument(600)
            else :
                self.just_gainded_badge = False
        elif self.streak == 3 :
            if not self.two_day_streak :
                self.two_day_streak = True
                self.just_gainded_badge = True
                self.increment_num_badges()
                self.increment_points_with_argument(400)
            else :
                self.just_gainded_badge = False
        elif self.streak == 2 :
            if not self.two_day_streak :
                self.two_day_streak = True
                self.just_gainded_badge = True
                self.increment_num_badges()
                self.increment_points_with_argument(200)
            else :
                self.just_gainded_badge = False
        else:
            self.just_gainded_badge = False
            
    def get_group(self):
        return self.group
    
    def get_gained_points(self):
        return self.points - self.previous_points
    
    def get_points(self):
        return self.points

    def increment_num_badges(self):
        self.num_badges += 1

    def get_badges(self):
        return [self.first_question, self.five_questions, self.ten_questions, self.two_day_streak, self.three_day_streak, self.four_day_streak]
      
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=500)
    pub_date = models.DateField(default=datetime.date.today, blank = True)
    choice_a = models.CharField(max_length=200, default="")
    choice_a_correct = models.BooleanField(default=False)
    choice_b = models.CharField(max_length=200, default="")
    choice_b_correct = models.BooleanField(default=False)
    choice_c = models.CharField(max_length=200, default="")
    choice_c_correct = models.BooleanField(default=False)
    choice_d = models.CharField(max_length=200, default="")
    choice_d_correct = models.BooleanField(default=False)