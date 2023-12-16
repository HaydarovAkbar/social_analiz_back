from django.db import models
from django.utils import timezone

from organization.models import Organization


class LevelType(models.Model):
    COLOR_CHOICES = (
        ('#FF0000', 'Красный (red)'),
        ('#FFA500', 'Оранжевый (orange)'),
        ('#FFFF00', 'Желтый (yellow)'),
        ('#008000', 'Зеленый (green)'),
        ('#0000FF', 'Синий (blue)'),
        ('#4B0082', 'Фиолетовый (purple)'),
        ('#800080', 'Фиолетовый (purple)'),
        ('#FFC0CB', 'Розовый (pink)'),
        ('#000000', 'Черный (black)'),
        ('#FFFFFF', 'Белый (white)'),
    )
    name = models.CharField(max_length=255)
    rate = models.IntegerField(default=0)
    color = models.CharField(max_length=255, default='#FF0000', choices=COLOR_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Level Types'
        verbose_name = 'Level Type'
        db_table = 'level_type'

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(LevelType, self).save(*args, **kwargs)
        return self


class LevelOrganization(models.Model):
    level = models.ForeignKey(LevelType, on_delete=models.SET_NULL, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    objects = models.Manager()

    def __str__(self):
        try:
            return self.level.name + " " + self.organization.id
        except:
            return self.level.name

    class Meta:
        verbose_name_plural = 'Level Organizations'
        verbose_name = 'Level Organization'
        db_table = 'level_organization'
        indexes = [
            models.Index(fields=['level', 'organization']),
        ]

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(LevelOrganization, self).save(*args, **kwargs)
        return self
