from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.


class Article(models.Model):
    title = models.CharField(verbose_name='标题', max_length=200)
    detail = UEditorField(
        verbose_name="内容", width=600, height=300, imagePath="course/ueditor/",
        filePath="course/ueditor/", default=""
    )

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "文章"
        verbose_name_plural = verbose_name