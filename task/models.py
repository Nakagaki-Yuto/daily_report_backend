from django.db import models
from markdownx.models import MarkdownxField


class Task(models.Model):
    task = MarkdownxField() #タスクの内容
    priority = models.IntegerField() #優先度
    is_finished = models.BooleanField(default=False)  #完了/未完
    finished_date = models.DateField(blank=True, null=True, default="2021-01-01") #完了日
    
    def __str__(self):
        return self.task
        