import os
import shutil
from multiprocessing.pool import ThreadPool

import requests

from tqdm import tqdm

from src.conf import DATA_PATH
from src.datasets_urls import DATASETS_INFO
from requests.auth import HTTPBasicAuth


def download_dataset(dataset: str, force: bool = False):
    """
    The download_dataset function downloads the dataset from given URLs.
    :param dataset:
    :param force: bool: Remove contents of the init_data and download of the dataset
    """

    urls: list = DATASETS_INFO[dataset].get("urls", None)
    credentials = DATASETS_INFO[dataset].get("credentials", (None, None))
    local_data_dir = os.path.join(DATA_PATH, dataset)
    if urls is None:
        raise ValueError(f"Invalid dataset: {dataset}. Please choose from {list(DATASETS_INFO.keys())}")

    def _request(_url, position):
        print(f"Downloading {os.path.basename(_url)} to {local_data_dir}")
        if "www.dropbox.com" in _url:
            _url = _url.replace("www.dropbox.com", "dl.dropboxusercontent.com").split("?")[0]

        resp = requests.get(_url, auth=HTTPBasicAuth(*credentials), stream=True)

        with tqdm(desc=os.path.basename(_url), total=int(resp.headers.get('content-length', 0)),
                  unit='iB', unit_scale=True, unit_divisor=1024, position=position) as bar:
            with open(os.path.join(local_data_dir, os.path.basename(_url)), 'wb') as file:
                for data in resp.iter_content(chunk_size=1024):
                    file.write(data)
                    bar.update(1024)

    if not os.path.exists(local_data_dir) or force:
        if force:
            print(f"Removing old data from {local_data_dir}...")
            shutil.rmtree(path=local_data_dir, ignore_errors=True)

        os.makedirs(local_data_dir, exist_ok=True)
        with ThreadPool(min(len(urls), len(os.sched_getaffinity(0)))) as pool:
            pool.starmap(_request, list(zip(urls, list(range(len(urls))))))

        print("Done!")
    else:
        print(f"{local_data_dir} is not empty.")
