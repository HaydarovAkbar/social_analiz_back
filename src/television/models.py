from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from utils.models import State

class FileStatus(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('File status')
        verbose_name_plural = _('File statuses')
        db_table = 'file_status'


class TelevisionType(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Television type')
        verbose_name_plural = _('Television types')
        db_table = 'television_type'


class Files(models.Model):
    file_name = models.CharField(max_length=250)
    file_id = models.CharField(max_length=250, null=True, blank=True)
    file_extension = models.CharField(max_length=250, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True)

    organization = models.ForeignKey('organization.Organization', on_delete=models.SET_NULL, null=True, blank=True,
                                     related_name='files', verbose_name=_('Organization'))
    post_date = models.DateField(null=True, blank=True, verbose_name=_('Post date'))
    television_type = models.ForeignKey(TelevisionType, on_delete=models.SET_NULL, null=True, blank=True,
                                        related_name='files', verbose_name=_('Television type'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.file_name

    class Meta:
        verbose_name = _('File')
        verbose_name_plural = _('Files')
        db_table = 'files'
        indexes = [
            models.Index(fields=['file_name', ]),
            models.Index(fields=['post_date', ]),
        ]

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(Files, self).save(*args, **kwargs)
        return self
