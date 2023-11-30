from django.utils import timezone

from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from utils.models import State, Language, Category, Specialization, Region, District
from organization.models import Organization


class User(AbstractUser):
    phone_number = PhoneNumberField(
        _("Phone number"),
        help_text=_("Required. Only international format used. (998901234567)"),
        error_messages={
            "unique": _("Userth this phone number already exists.")
        },
        unique=True,
        blank=True,
        null=True, )
    pinfl = models.CharField(max_length=14, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True)

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_name="%(app_label)s_%(class)s_related",  # Change the related_name
        related_query_name="%(app_label)s_%(class)ss",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="%(app_label)s_%(class)s_related",  # Change the related_name
        related_query_name="%(app_label)s_%(class)ss",
    )

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name_plural = 'Users'
        verbose_name = 'User'
        db_table = 'user'
        indexes = [
            models.Index(fields=['username']),
            models.Index(fields=['phone_number']),
            models.Index(fields=['organization']),
        ]

    def save(self, *args, **kwargs):
        self.update_at = timezone.now()
        super(User, self).save(*args, **kwargs)
        return self
