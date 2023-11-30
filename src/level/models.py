from django.db import models
from django.utils import timezone
from organization.models import Organization

class Level(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Levels'
        verbose_name = 'Level'
        db_table = 'level'

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(Level, self).save(*args, **kwargs)
        return self


class LevelCredantials(models.Model):
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True)
    score1 = models.PositiveIntegerField(default=1)
    score2 = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        try:
            return self.level.name + " " + self.score1 + "-" + self.score2
        except:
            return self.score1 + "-" + self.score2

    class Meta:
        verbose_name_plural = 'Level Credantials'
        verbose_name = 'Level Credantial'
        db_table = 'level_credantials'

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(LevelCredantials, self).save(*args, **kwargs)
        return self
