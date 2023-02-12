import requests

from pathlib import Path
from zipfile import ZipFile
from DashApp.util.Logger import log_info
from DashApp.exception.custom_exception import GssStataNotDownloaded

DATA_DOWNLOAD_URL = "https://gss.norc.org/documents/stata/GSS_stata.zip"
FILE_TO_SAVE_AS = "GSS_stata.zip"  # the name you want to save file as

MY_DASH_APP_DIRECTORY = Path().cwd().parent
UTIL_DIRECTORY = MY_DASH_APP_DIRECTORY.joinpath('util')

STATIC_DIRECTORY = MY_DASH_APP_DIRECTORY.joinpath('static')
STATIC_GSS_ZIP_FILE = STATIC_DIRECTORY.joinpath(FILE_TO_SAVE_AS)

STATIC_GSS_DATA_DIRECTORY = STATIC_DIRECTORY.joinpath('gss_data')
STATIC_GSS_DATASET = STATIC_GSS_DATA_DIRECTORY.joinpath('gss7221_r3a.dta')


def download_gss_stata_zip():
    response = requests.get(DATA_DOWNLOAD_URL, stream=True)  # making requests to server

    with open(STATIC_GSS_ZIP_FILE, "wb") as f:  # opening a file handler to create new file
        f.write(response.content)  # writing content to file

    log_info("Downloading Survey data is finished.")

    return STATIC_GSS_ZIP_FILE


def unzip_gss_stata_zip():
    if STATIC_GSS_ZIP_FILE.exists() and not STATIC_GSS_DATA_DIRECTORY.exists():
        log_info(f"{STATIC_GSS_ZIP_FILE.__str__()} already exist and it's not unzipped. Unzip the file.")
        with ZipFile(STATIC_GSS_ZIP_FILE, 'r') as zipObject:
            zipObject.extractall(STATIC_GSS_DATA_DIRECTORY)
        log_info("Unzip is done.")

    return STATIC_GSS_DATASET


def check_gss_stata_zip():
    create_gss_directory = input(f"{STATIC_GSS_ZIP_FILE.__str__()} doesn't exist. Download a folder and unzip it\n" +
                                 f"You may download the file yourself at {DATA_DOWNLOAD_URL} to " +
                                 f"{STATIC_DIRECTORY.__str__()} and the file name as {FILE_TO_SAVE_AS}\n"
                                 f"or type 'y/yes' to download the file.")

    if not create_gss_directory.lower() in ["yes", "y"]:
        raise GssStataNotDownloaded

    download_gss_stata_zip()

    return unzip_gss_stata_zip()


def get_gss_data_set():
    if STATIC_GSS_DATASET.exists():
        return STATIC_GSS_DATASET

    if STATIC_GSS_ZIP_FILE.exists():
        return unzip_gss_stata_zip()

    if not STATIC_GSS_ZIP_FILE.exists():
        return check_gss_stata_zip()


if __name__ == '__main__':
    print(get_gss_data_set().exists())