from minio import Minio
from django.conf import settings


class MinioClient:
    def __init__(self):
        self.client = Minio(
            settings.MINIO_HOST,
            access_key=settings.MINIO_ACCESS_KEY,
            secret_key=settings.MINIO_SECRET_KEY,
            secure=settings.MINIO_SECURE,
        )

    def add_file(self, file_id, file, file_extension, length):
        try:
            found = self.client.bucket_exists(settings.MINIO_BUCKET_NAME)
            if not found:
                self.client.make_bucket(settings.MINIO_BUCKET_NAME)
            else:
                print("Bucket 'asiatrip' already exists")
            self.client.put_object(settings.MINIO_BUCKET_NAME, f"{file_id}.{file_extension}", file, length)
            return True
        except Exception as e:
            print(e)
            return True

    def get_file(self, object_name):
        response = self.client.get_object(
            bucket_name=settings.MINIO_BUCKET_NAME,
            object_name=object_name,
        )
        return response.read()

    def remove_file(self, object_name):
        response = self.client.remove_object(
            bucket_name=settings.MINIO_BUCKET_NAME,
            object_name=object_name)
        return response

    # @staticmethod
    # def add_file(file_id, file, file_extension, length):
    #     client = Minio(
    #         settings.MINIO_HOST,
    #         access_key=settings.MINIO_ACCESS_KEY,
    #         secret_key=settings.MINIO_SECRET_KEY,
    #         secure=settings.MINIO_SECURE,
    #     )
    #     found = client.bucket_exists(settings.MINIO_BUCKET_NAME)
    #     if not found:
    #         client.make_bucket(settings.MINIO_BUCKET_NAME)
    #     else:
    #         print("Bucket 'asiatrip' already exists")
    #     client.put_object(settings.MINIO_BUCKET_NAME, f"{file_id}.{file_extension}", file, length)
    #     return True
    #
    # @staticmethod
    # def get_file(object_name):
    #     client = Minio(
    #         settings.MINIO_HOST,
    #         access_key=settings.MINIO_ACCESS_KEY,
    #         secret_key=settings.MINIO_SECRET_KEY,
    #         secure=settings.MINIO_SECURE,
    #     )
    #     response = client.get_object(
    #         bucket_name=settings.MINIO_BUCKET_NAME,
    #         object_name=object_name,
    #     )
    #     return response.read()
    #
    # @staticmethod
    # def remove_file(object_name):
    #     client = Minio(
    #         settings.MINIO_HOST,
    #         access_key=settings.MINIO_ACCESS_KEY,
    #         secret_key=settings.MINIO_SECRET_KEY,
    #         secure=settings.MINIO_SECURE,
    #     )
    #     response = client.remove_object(
    #         bucket_name=settings.MINIO_BUCKET_NAME,
    #         object_name=object_name)
    #     return response
