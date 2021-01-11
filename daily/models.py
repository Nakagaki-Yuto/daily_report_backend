from django.db import models
from markdownx.models import MarkdownxField


class Daily(models.Model):
    date = models.DateField() #日付
    study = MarkdownxField() #やったこと
    summary = MarkdownxField() #気付き
    other = MarkdownxField() #その他・備考
    evaluation = models.ForeignKey('Evaluation', on_delete=models.PROTECT) #1日の評価(外部キー)
    is_open = models.BooleanField(default=True)  #公開/非公開

    def __str__(self):
        date_str = self.date.strftime('%Y/%m/%d')
        return date_str


class Evaluation(models.Model):
    evaluation = models.CharField(max_length=255)

    def __str__(self):
        return self.evaluation


