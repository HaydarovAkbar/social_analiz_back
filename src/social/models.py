from django.db import models
from django.utils import timezone
from organization.models import Organization
from utils.models import Category, Specialization, State


class SocialTypes(models.Model):
    name = models.CharField(max_length=255)
    attr = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)

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
    link = models.CharField(max_length=255, null=True, blank=True)
    tg_group = models.CharField(max_length=255, null=True, blank=True)
    integration_id = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True)
    social_type = models.ForeignKey(SocialTypes, on_delete=models.SET_NULL, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)

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


class SocialPost(models.Model):
    post_date = models.DateTimeField(null=True, blank=True)
    post_id = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    media_group_id = models.CharField(max_length=24, null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    social_type = models.ForeignKey(SocialTypes, on_delete=models.SET_NULL, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True)

    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.social_type.name + " " + self.post_id

    class Meta:
        verbose_name_plural = 'Social Posts'
        verbose_name = 'Social Post'
        db_table = 'social_posts'
        indexes = [
            models.Index(fields=['post_date']),
            models.Index(fields=['social_type']),
            models.Index(fields=['organization']),
            models.Index(fields=['state']),
        ]

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(SocialPost, self).save(*args, **kwargs)
        return self


class SocialPostStats(models.Model):
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(default=0)
    shares = models.PositiveIntegerField(default=0)
    reactions = models.PositiveIntegerField(default=0)
    followers = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    post = models.ForeignKey(SocialPost, on_delete=models.CASCADE, null=True)
    social = models.ForeignKey(Social, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        try:
            return self.social.name + " " + str(self.created_at)
        except:
            return str(self.created_at)

    class Meta:
        verbose_name_plural = 'Social Stats'
        verbose_name = 'Social Stat'
        db_table = 'social_stats'
        indexes = [
            models.Index(fields=['social']),
            models.Index(fields=['created_at']),
            models.Index(fields=['post']),
        ]


class SocialPostComment(models.Model):
    comment_id = models.CharField(max_length=255, null=True, blank=True)
    media_group_id = models.CharField(max_length=24, null=True, blank=True)
    url = models.URLField(null=True, blank=True)


    created_at = models.DateTimeField(auto_now_add=True)

    social_type = models.ForeignKey(SocialTypes, on_delete=models.SET_NULL, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(SocialPost, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.social_type.name + " " + self.id

    class Meta:
        verbose_name_plural = 'Social Post Comments'
        verbose_name = 'Social Post Comment'
        db_table = 'social_post_comments'
        indexes = [
            models.Index(fields=['social_type']),
            models.Index(fields=['organization']),
            models.Index(fields=['post']),
        ]