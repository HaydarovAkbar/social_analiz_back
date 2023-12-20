from modeltranslation.translator import TranslationOptions, register
from ..models import FileStatus, Files


@register(FileStatus)
class FileStatusTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Files)
class FilesTranslationOptions(TranslationOptions):
    fields = ('content', )