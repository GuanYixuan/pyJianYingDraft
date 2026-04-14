from minio import Minio
from minio.error import S3Error
from app.config import settings
import uuid
import base64


class StorageService:
    def __init__(self):
        self.client = Minio(
            settings.MINIO_ENDPOINT,
            access_key=settings.MINIO_ACCESS_KEY,
            secret_key=settings.MINIO_SECRET_KEY,
            secure=settings.MINIO_SECURE,
        )
        self.bucket = settings.MINIO_BUCKET
        self._ensure_bucket()

    def _ensure_bucket(self):
        try:
            if not self.client.bucket_exists(self.bucket):
                self.client.make_bucket(self.bucket)
        except S3Error as e:
            print(f"Error creating bucket: {e}")

    async def upload_file(self, path: str, data: bytes, content_type: str):
        try:
            self.client.put_object(
                self.bucket,
                path,
                data,
                len(data),
                content_type=content_type,
            )
        except S3Error as e:
            raise Exception(f"Failed to upload file: {e}")

    async def upload_file_from_path(self, path: str, file_path: str, content_type: str):
        try:
            self.client.fput_object(
                self.bucket,
                path,
                file_path,
                content_type=content_type,
            )
        except S3Error as e:
            raise Exception(f"Failed to upload file: {e}")

    async def download_file(self, path: str) -> bytes:
        try:
            response = self.client.get_object(self.bucket, path)
            data = response.read()
            response.close()
            response.release_conn()
            return data
        except S3Error as e:
            raise Exception(f"Failed to download file: {e}")

    async def delete_file(self, path: str):
        try:
            self.client.remove_object(self.bucket, path)
        except S3Error as e:
            raise Exception(f"Failed to delete file: {e}")

    async def get_presigned_url(self, path: str, expires_seconds: int = 3600) -> str:
        try:
            url = self.client.presigned_get_object(
                self.bucket,
                path,
                expires=expires_seconds,
            )
            return url
        except S3Error as e:
            raise Exception(f"Failed to generate presigned URL: {e}")

    async def get_upload_presigned_url(self, path: str, expires_seconds: int = 3600) -> str:
        try:
            url = self.client.presigned_put_object(
                self.bucket,
                path,
                expires=expires_seconds,
            )
            return url
        except S3Error as e:
            raise Exception(f"Failed to generate upload URL: {e}")
