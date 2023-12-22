from django.db import models
from django.utils import timezone


class RatingCriteria(models.Model):
    title = models.CharField(max_length=255)

    state = models.ForeignKey('utils.State', on_delete=models.SET_NULL, null=True)
    social_type = models.ForeignKey('social.SocialTypes', on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Rating Criteria'
        verbose_name = 'Rating Criteria'
        db_table = 'rating_criteria'

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(RatingCriteria, self).save(*args, **kwargs)
        return self
