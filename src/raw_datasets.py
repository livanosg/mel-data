import glob
import os
import shutil
from multiprocessing.pool import ThreadPool
from multiprocessing import Manager
from zipfile import ZipFile
import requests
import tqdm as tqdm

from datasets_info import DatasetInfo, PH2


class RawDatasetsHandler:
    def __init__(self):
        """DatasetHandler class initialization. """
        self.all_datasets = {}

    def download_dataset(self, dataset_info: DatasetInfo, force: bool = False):
        """
        The download_dataset function downloads a dataset from the given url.
        :param force:
        :param dataset_info: The name of the dataset
        :return: None
        """
        if dataset_info.name in self.all_datasets:
            print(f"{dataset_info} already exists")
        else:
            self.set_dataset_info(dataset_info)

        if not os.path.exists(dataset_info.init_data_folder) or force == True:
            if force:
                print(f"Removing old data from {dataset_info.init_data_folder}...")
                shutil.rmtree(path=dataset_info.init_data_folder, ignore_errors=True)

            os.mkdir(dataset_info.init_data_folder)
            print(f"Downloading {dataset_info.name}...")

            def _download(_url, position):  # TODO fix progress bar on parallel calls
                filename = os.path.join(dataset_info.init_data_folder, os.path.basename(_url))
                print(f"Downloading {os.path.basename(_url)} to {dataset_info.init_data_folder}")
                resp = requests.get(_url, stream=True)
                total = int(resp.headers.get('content-length', 0))
                bar = tqdm.tqdm(desc=os.path.basename(_url), total=total, position=position, unit='iB', unit_scale=True,
                                unit_divisor=1024)
                with open(filename, 'wb') as file:
                    for data in resp.iter_content(chunk_size=1024):
                        size = file.write(data)
                        bar.update(size)
                bar.close()

            with ThreadPool(len(dataset_info.urls)) as pool:
                pool.starmap(_download, list(zip(dataset_info.urls, list(range(len(dataset_info.urls))))))
            print("Done!")
        else:
            print(f"{dataset_info.init_data_folder} already exists")

    def set_dataset_info(self, dataset_info: DatasetInfo):
        """
        The set_dataset_info function adds a DatasetInfo object to the dictionary
        that holds all datasets with key the name of the dataset.
        :param dataset_info: The DatasetInfo object
        :return: None
        """
        self.all_datasets[dataset_info.name] = dataset_info

    def get_dataset_info(self, name: str):
        """
        The get_dataset_info function returns a DatasetInfo object, given the name of the dataset.
        :param name: The name of the dataset
        :return: The DatasetInfo object
        """
        return self.all_datasets[name]

    def get_all_dataset_info(self):
        """
        The get_all_dataset_info function returns a dictionary that contains all datasets.
        :return: The dictionary of all datasets"""
        return self.all_datasets

    def remove_dataset_info(self, name: str):
        """
        The remove_dataset_info function removes a dataset from the dictionary.
        :param name: The name of the dataset
        :return: None
        """
        if name in self.all_datasets:
            del self.all_datasets[name]
        else:
            print(f"{name} not found")

    def extract_dataset(self, name: str):
        """
        The extract_dataset function extracts a dataset from the initial dataset folder to the data_folder.
        :param name: The name of the dataset
        :return: None
        """

        shutil.copytree(src=self.get_dataset_info(name).init_data_folder,
                        dst=self.get_dataset_info(name).data_folder)

        def _zip_extract(folder: str):
            for file in glob.glob(os.path.join(folder, "**/*.zip"), recursive=True):
                with ZipFile(file, "r") as zipObj:
                    zipObj.extractall(path=os.path.split(file)[0])
                os.remove(file)
            if glob.glob(os.path.join(folder, "**/*.zip"), recursive=True):
                _zip_extract(folder=folder)

        _zip_extract(self.get_dataset_info(name).data_folder)

    def extract_all_datasets(self):
        """
        The extract_all_datasets function extracts all datasets from the initial dataset folder to the data_folder.
        :return: None
        """
        for dataset_name in self.all_datasets:
            self.extract_dataset(dataset_name)


if __name__ == '__main__':
    ph2 = PH2
    handler = RawDatasetsHandler()

    handler.download_dataset(ph2, force=True)
