import threading
from s3_file_manager import S3FileManager
from utility_manager import UtilityManager
import sys

from decouple import config

BASE_PDF_PATH = config('BASE_PDF_PATH')


def handler(prefix):
    s3_file_manager = S3FileManager()

    list_of_files = s3_file_manager.get_all_objects(prefix=prefix)
    print(list_of_files)
    for file in list_of_files:
        download_path = f'{BASE_PDF_PATH}{file.split("/")[-1]}'
        s3_file_manager.download_file(key=file, download_path=download_path)

    threads = []

    for file in list_of_files:
        utility_manager = UtilityManager(s3_pdf_file_path=file)
        thread = threading.Thread(target=utility_manager.pdf_processing)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    path_to_book = sys.argv[1]
    print(path_to_book)
    handler(prefix=path_to_book)
