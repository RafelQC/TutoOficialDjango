from django.db import models
import datetime
from django.utils.timezone import now

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name='Texto')
    pub_date = models.DateTimeField(default=now, verbose_name='Fecha de publicación')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, verbose_name='Texto')
    votes = models.IntegerField(default=0, verbose_name='Votos')

    def __str__(self):
        return self.choice_text
