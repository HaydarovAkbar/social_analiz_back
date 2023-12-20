try:
    from .files import MinioClient
except ImportError:
    from files import MinioClient
