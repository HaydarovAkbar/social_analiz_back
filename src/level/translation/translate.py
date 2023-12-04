from modeltranslation.translator import translator, TranslationOptions, register
from ..models import Level


@register(Level)
class LevelTranslationOptions(TranslationOptions):
    fields = ('name',)
