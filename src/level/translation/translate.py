from modeltranslation.translator import translator, TranslationOptions, register
from ..models import LevelType


@register(LevelType)
class LevelTypeTranslationOptions(TranslationOptions):
    fields = ('name',)
