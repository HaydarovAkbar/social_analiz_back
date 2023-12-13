from django.utils import timezone

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from utils.models import State, Language, Category, Specialization, Region, District


class Organization(models.Model):
    fullname = models.CharField(_('fullname'), max_length=300, null=True)
    shortname = models.CharField(_('shortname'), max_length=100, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    address = models.TextField(_('Address input'), null=True)
    inn = models.CharField(_('INN'), max_length=9, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    phone_number = PhoneNumberField(
        _("Phone number"),
        help_text=_("Required. Only international format used."),
        error_messages={
            "unique": _("User with this phone number already exists.")
        },
        null=True, blank=True)
    accounter = models.CharField(_('accounter'), max_length=250, null=True)
    leader = models.CharField(_('leader'), max_length=250, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.shortname

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(Organization, self).save(*args, **kwargs)
        return self

    class Meta:
        verbose_name_plural = 'Organizations'
        verbose_name = 'Organization'
        db_table = 'organization'
        indexes = [
            models.Index(fields=['shortname']),
            models.Index(fields=['category']),
            models.Index(fields=['specialization']),
            models.Index(fields=['region']),
            models.Index(fields=['district']),
            models.Index(fields=['phone_number']),
        ]