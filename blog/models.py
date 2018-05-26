#coding=utf-8
from django.db import models
from django.utils.six import python_2_unicode_compatible
from django.core.urlresolvers import reverse
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

@python_2_unicode_compatible
class Category(models.Model):
    #分类
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Tag(models.Model):
    #标签
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Post(models.Model):
   

    # 文章标题
    title = models.CharField(max_length=70)

    body = models.TextField()

    # 这两个列分别表示文章的创建时间和最后一次修改时间，存储时间的字段用 DateTimeField 类型。
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # 文章摘要，可以没有文章摘要，但默认情况下 CharField 要求我们必须存入数据，否则就会报错。
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)
    views = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])
