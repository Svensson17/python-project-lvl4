from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _


# class User(AbstractUser):
#     def __str__(self):
#         return self.get_full_name()


class Status(models.Model):
    name = models.CharField(_('status_name'), max_length=30)

    def __str__(self):
        return self.name


class Label(models.Model):
    name = models.CharField(verbose_name=_('label_name'), max_length=30)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(verbose_name=_('task_name'), max_length=30)
    author = models.ForeignKey(get_user_model(), on_delete=models.PROTECT,
                               related_name='author',
                               verbose_name=_('author'),
                               blank=True, null=True)
    performer = models.ForeignKey(get_user_model(), on_delete=models.PROTECT,
                                  related_name='performer',
                                  verbose_name=_('performer'),
                                  blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT,
                               related_name='status',
                               verbose_name=_('status'),
                               blank=True, null=True)
    label = models.ManyToManyField(Label, related_name='label',
                                   verbose_name=_('label'),
                                   blank=True)
    created_at = models.DateTimeField(default=timezone.now, verbose_name=_('created_at'))
    description = models.TextField(verbose_name=_('description'), blank=True)
    end_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
