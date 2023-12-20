from modeltranslation.translator import TranslationOptions, register
from ..models import TelevisionType, FileStatus, Files


@register(TelevisionType)
class TelevisionTypeTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(FileStatus)
class FileStatusTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Files)
class FilesTranslationOptions(TranslationOptions):
    fields = ('content',)