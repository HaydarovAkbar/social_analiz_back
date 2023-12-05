from django.utils import timezone

from django.db import models


class State(models.Model):
    name = models.CharField(max_length=50, null=True)
    displayname = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'States'
        verbose_name = 'State'
        db_table = 'state'


class Language(models.Model):
    code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Languages'
        verbose_name = 'Language'
        db_table = 'language'


class Category(models.Model):
    shortname = models.CharField(max_length=250)
    fullname = models.CharField(max_length=250, null=True, blank=True)
    ordercode = models.CharField(max_length=50, null=True)
    code = models.CharField(max_length=50, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True, related_name='categories', )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.shortname

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'
        db_table = 'category'

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(Category, self).save(*args, **kwargs)
        return self


class Specialization(models.Model):
    shortname = models.CharField(max_length=250)
    fullname = models.CharField(max_length=250, null=True, blank=True)
    ordercode = models.CharField(max_length=50, null=True)
    code = models.CharField(max_length=50, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True, related_name='specialization', )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.shortname

    class Meta:
        verbose_name_plural = 'Specializations'
        verbose_name = 'Specialization'
        db_table = 'specialization'

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(Specialization, self).save(*args, **kwargs)
        return self


class Region(models.Model):
    shortname = models.CharField(max_length=250)
    fullname = models.CharField(max_length=250, null=True, blank=True)
    order = models.IntegerField(null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True, related_name='region', )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    code = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.shortname

    class Meta:
        verbose_name_plural = 'Regions'
        verbose_name = 'Region'
        db_table = 'region'

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(Region, self).save(*args, **kwargs)
        return self


class District(models.Model):
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True, related_name='districts', )
    shortname = models.CharField(max_length=250)
    fullname = models.CharField(max_length=250, null=True, blank=True)
    order = models.IntegerField(null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True, related_name='district', )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    code = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.shortname

    class Meta:
        verbose_name_plural = 'Districts'
        verbose_name = 'District'
        db_table = 'district'

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(District, self).save(*args, **kwargs)
        return self
