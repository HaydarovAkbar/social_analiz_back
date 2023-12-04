from modeltranslation.translator import translator, TranslationOptions
from ..models import Level


class LevelTranslationOptions(TranslationOptions):
    fields = ('name',)
