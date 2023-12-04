from modeltranslation.translator import translator, TranslationOptions, register
from ..models import Organization


@register(Organization)
class OrganizationTranslationOptions(TranslationOptions):
    fields = ('fullname', 'shortname', 'address')