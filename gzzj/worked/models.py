from django.db import models

# Create your models here.


class Gzzj(models.Model):
    user = models.ForeignKey('users.Users', related_name='gzzjs', on_delete=models.CASCADE, verbose_name="录入人")
    gzzj = models.TextField(max_length=256, verbose_name="工作总结")
    time = models.DateField(verbose_name="录入时间")

    def __str__(self):
        return self.gzzj

    class Meta(object):
        verbose_name = "工作总结"
        verbose_name_plural = verbose_name
