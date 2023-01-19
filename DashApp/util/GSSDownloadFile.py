import requests
import urllib3
import shutil
from pathlib import Path

URL = "https://gss.norc.org/documents/stata/GSS_stata.zip"
FILE_TO_SAVE_AS = "GSS_stata.zip"  # the name you want to save file as
DIRECTORY_TO_SAVE = Path().__dir__()

def download_link_save(url = None, dir = None):
    response = requests.get(URL, stream=True)  # making requests to server

    # with open(FILE_TO_SAVE_AS, "wb") as f:  # opening a file handler to create new file
    #     f.write(response.content)  # writing content to file


    # http = urllib3.PoolManager()
    #
    # with http.request('GET', url, preload_content=False) as r, open(path, 'wb') as out_file:
    #     shutil.copyfileobj(r, out_file)
    # response = http.request(..., preload_content=False)
    # buffered_response = io.BufferedReader(response, 2048)

if __name__ == '__main__':
    print(DIRECTORY_TO_SAVE)

def check_directory():
    print(DIRECTORY_TO_SAVE)

