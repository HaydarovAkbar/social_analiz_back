from django.db import models
from django.utils import timezone
from organization.models import Organization


class SocialTypes(models.Model):
    name = models.CharField(max_length=255)
    attr = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Social Types'
        verbose_name = 'Social Type'
        db_table = 'social_types'

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(SocialTypes, self).save(*args, **kwargs)
        return self


class Social(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True)
    social_type = models.ForeignKey(SocialTypes, on_delete=models.SET_NULL, null=True)
    link = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        try:
            return self.organization.shortname + " " + self.social_type.name
        except:
            return self.social_type.name

    class Meta:
        verbose_name_plural = 'Socials'
        verbose_name = 'Social'
        db_table = 'social'

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(Social, self).save(*args, **kwargs)
        return self
