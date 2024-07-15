import boto3
from decouple import config

BUCKET_NAME = config('BUCKET_NAME')
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')


class S3FileManager:
    """ S3 File Manager"""

    def __init__(self):
        self.bucket_name = BUCKET_NAME
        self.aws_access_key_id = AWS_ACCESS_KEY_ID
        self.aws_secret_access_key = AWS_SECRET_ACCESS_KEY
        self.client = boto3.client(
            's3',
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key
        )

    def get_all_objects(self, prefix):
        try:
            response = self.client.list_objects(
                Bucket=self.bucket_name,
                Prefix=prefix
            )

            list_of_file_path = [obj['Key'] for obj in response.get('Contents', [])]
            return list_of_file_path
        except Exception as e:
            print(f"Error: {e}")

    def download_file(self, key: str, download_path: str) -> None:
        """ S3 File download"""
        try:
            response = self.client.get_object(Bucket=self.bucket_name, Key=key)

            with open(download_path, "wb") as f:
                for chunk in response['Body'].iter_chunks():
                    f.write(chunk)

            print(f"File downloaded successfully: {download_path}")

        except Exception as e:
            print(f"Error: {e}")

    def upload_file(self, key: str, local_text_path: str) -> None:
        """S3 File upload"""

        try:
            response = self.client.upload_file(local_text_path, self.bucket_name, key)
        except Exception as e:
            print(f"Error: {e}")



