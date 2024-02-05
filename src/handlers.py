import glob
import os
import shutil
from zipfile import ZipFile

import pandas as pd

from conf import DATA_PATH, SETUP_DATA_PATH, URLS_CREDENTIALS
from datasets_urls import DATASETS_INFO


class DatasetHandler:
    def __init__(self, name: str):
        self.name = name
        self.urls = DATASETS_INFO[self.name]["urls"]
        self.raw_data_path = os.path.join(DATA_PATH, self.name)

    def fetch_metadata(self):
        """
        The fetch_metadata function is a placeholder to apply the logic of retrieving metadata for a given dataset.
        """
        pass

    def setup_dataset(self, force: bool = False):
        """
        The extract_dataset function extracts a dataset from the initial dataset folder to the data_folder.
        :param force:
        :return: None
        """
        if force:
            print(f"Removing old data from {self.setup_data_path}...")
            shutil.rmtree(path=self.setup_data_path, ignore_errors=True)
        print(f"Copying data from {self.init_data_path} to {self.setup_data_path}")
        shutil.copytree(src=self.init_data_path,
                        dst=self.setup_data_path)

        def _zip_extract(folder: str):
            print(f"Extracting {folder}...")
            for file in glob.glob(os.path.join(folder, "**/*.zip"), recursive=True):
                with ZipFile(file, "r") as zipObj:
                    zipObj.extractall(path=os.path.split(file)[0])
                os.remove(file)
            if glob.glob(os.path.join(folder, "**/*.zip"), recursive=True):
                _zip_extract(folder=folder)

        _zip_extract(self.setup_data_path)

    def split_data(self):
        pass


class Isic16Handler(DatasetHandler):
    def __init__(self):
        super().__init__(name="isic16", urls=ISIC16_URLS)
        self.image_dir = os.path.join(self.setup_data_path)
        self.meta_dir = os.path.join(self.setup_data_path)


class Isic17Handler(DatasetHandler):
    def __init__(self):
        super().__init__(name="isic17", urls=ISIC17_URLS)
        self.image_dir = os.path.join(self.setup_data_path)
        self.meta_dir = os.path.join(self.setup_data_path)

    def fetch_metadata(self):
        """
        The fetch_metadata method reads '2017_Test_v2_Part3_GroundTruth.csv' and 'ISIC-2017_Test_v2_Data_metadata.csv'.
        Finally, both these dataframes are merged to a single dataframe based on image column and then returned.

        :return: A dataframe with the columns:
        """

        df1 = pd.read_csv(self.meta_dir, index_col=0)
        df2 = pd.read_csv(os.path.join(self.image_dir, "ISIC-2017_Test_v2_Data_metadata.csv"), index_col=0)
        df = pd.concat([df1, df2], axis=1, ignore_index=True)
        df["image_id"] = df.index
        return df.reindex()


class Isic18Handler(DatasetHandler):
    def __init__(self):
        super().__init__(name="isic18", urls=ISIC18_URLS)
        self.image_dir = os.path.join(self.setup_data_path)
        self.meta_dir = os.path.join(self.setup_data_path)


class Isic19Handler(DatasetHandler):
    def __init__(self):
        super().__init__(name="isic19", urls=ISIC19_URLS)
        self.image_dir = os.path.join(self.setup_data_path)
        self.meta_dir = os.path.join(self.setup_data_path)

    def fetch_metadata(self):
        """
        The fetch_metadata method reads 'ISIC2019_Training_GroundTruth.csv' and 'ISIC_2019_Training_Metadata.csv'.
        Finally, both these dataframes are merged to a single dataframe based on image column and then returned.

        :return: A dataframe with the columns:
        """
        df1 = pd.read_csv(self.meta_dir, index_col=0)
        df2 = pd.read_csv(os.path.join(self.setup_data_path, "ISIC_2019_Training_Metadata.csv"), index_col=0)
        df = pd.concat([df1, df2], axis=1, ignore_index=True)
        df["image"] = df.index
        return df.reindex()


class Isic20Handler(DatasetHandler):
    def __init__(self):
        super().__init__(name="isic20", urls=ISIC20_URLS)
        self.image_dir = os.path.join(self.setup_data_path, "train")
        self.meta_dir = os.path.join(self.setup_data_path, "ISIC_2020_Training_GroundTruth_v2.csv")

    def _remove_duplicates(self):
        meta = pd.read_csv(self.meta_dir)
        duplicates = pd.read_csv(os.path.join(self.setup_data_path, "ISIC_2020_Training_Duplicates.csv"))
        return meta[~meta.loc[:, "image_name"].isin(duplicates["image_name_2"])]

    def fetch_metadata(self, remove_duplicates=True):
        return self._remove_duplicates() if remove_duplicates else pd.read_csv(self.meta_dir)


# DONE
class SPCHandler(DatasetHandler):
    def __init__(self):
        super().__init__(name="spc", credentials=URLS_CREDENTIALS["spc"], urls=SPC_URLS)
        self.image_folder = os.path.join(self.setup_data_path, "release_v0", "images")
        self.meta_folder = os.path.join(self.setup_data_path, "release_v0", "meta")
        self.meta_data_path = os.path.join(self.meta_folder, "meta.csv")

    def split_data(self):
        """
        The split_data function takes the metadata file and splits it into three separate dataframes:
        train, valid, and test. The function uses the train_indexes.csv, valid_indexes.csv,
        and test_indexes.csv files to determine which rows of the metadata file should be in each dataframe.

        :return: A tuple of train, valid and test dataframes
        """
        all_data = self.fetch_metadata()
        train_idx = pd.read_csv(os.path.join(self.meta_folder, "train_indexes.csv"))
        valid_idx = pd.read_csv(os.path.join(self.meta_folder, "valid_indexes.csv"))
        test_idx = pd.read_csv(os.path.join(self.meta_folder, "test_indexes.csv"))

        train = all_data[all_data.index.isin(train_idx["indexes"])]
        valid = all_data[all_data.index.isin(valid_idx["indexes"])]
        test = all_data[all_data.index.isin(test_idx["indexes"])]
        return train, valid, test


# DONE
class DermofitHandler(DatasetHandler):
    def __init__(self):
        super().__init__(name="dermofit")
        self.image_dir = self.setup_data_path
        self.meta_data_path = os.path.join(self.setup_data_path, "lesionlist.txt")

    def fetch_metadata(self):
        df = pd.read_csv(self.meta_data_path, index_col=0, header=None, sep="   ")
        df.columns = ["image", "lesion"]  # Set names of columns
        return df

    def split_data(self):
        pass


class MedNodeHandler(DatasetHandler):
    def __init__(self):
        super().__init__("mednode")
        self.image_dir = os.path.join(self.setup_data_path, "complete_mednode_dataset")
        self.meta_dir = None

    def fetch_metadata(self):
        """
        The fetch_metadata method is used to create a dataframe containing the image names and their corresponding
        labels. This method creates two dataframes, one for melanoma images and another for naevus images.
        These dataframes contain only one column each, which is a list of all image names in that particular class
        (melanoma or naevus). A second column is added to both these dataframes, which contains either True or False
        depending on whether it's a melanoma or naevus image respectively. Finally, both these dataframes are merged
        to a single dataframe and returned.

        :return: A pandas dataframe with the column names &quot;image&quot;, &quot;melanoma&quot; and &quot;naevus&quot;
        """
        melanoma_images = os.listdir(os.path.join(self.image_dir, "melanoma"))
        naevus_images = os.listdir(os.path.join(self.image_dir, "naevus"))
        melanoma_df = pd.DataFrame(melanoma_images, columns=["image"])
        melanoma_df["melanoma"] = True
        naevus_df = pd.DataFrame(naevus_images, columns=["image"])
        naevus_df["naevus"] = True
        return pd.concat([melanoma_df, naevus_df], axis=0, ignore_index=True).fillna(0)


class PadufesHandler(DatasetHandler):
    def __init__(self):
        super().__init__("padufes")
        self.image_dir = os.path.join(self.setup_data_path, "images")
        self.meta_dir = os.path.join(self.setup_data_path, "metadata.csv")
        map(lambda src: os.rename(src=src, dst=os.path.join(self.image_dir, os.path.basename(src))),
            glob.glob(os.path.join(self.setup_data_path, "imgs_part_*/**"), recursive=True))


class Ph2Handler(DatasetHandler):
    def __init__(self):
        super().__init__("ph2")
        self.image_dir = os.path.join(self.setup_data_path, "PH2 Dataset images")
        self.meta_dir = os.path.join(self.setup_data_path, "PH2_Dataset.csv")
        # Create if not exists the csv equivalent of PH2_Dataset.txt
        if not os.path.exists(self.meta_dir):
            with open("/home/giorgos/projects/mel-data/raw_data/ph2/PH2Dataset/PH2_dataset.txt", "r") as f:
                lines = []
                for i, line in enumerate(f.readlines()):
                    lines.append(line.replace("||", ",").replace("|", ",").replace(" ", "")
                                 .replace(",", "", 1).replace(",\n", "\n"))
                    if i > 200:
                        break

            with open(self.meta_dir, "a+") as meta_csv:
                meta_csv.writelines(lines)

    @staticmethod
    def _meta_legends():
        rest_legend = {"A": "Absent",
                       "AT": "Atypical",
                       "P": "Present",
                       "T": "Typical"}
        other_meta_features = ["PigmentNetwork", "Dots/Globules", "Streaks", "RegressionAreas", "Blue-WhitishVeil"]
        legends = {feature: rest_legend for feature in other_meta_features}
        legends["ClinicalDiagnosis"] = {0: "Common Nevus",
                                        1: "Atypical Nevus",
                                        2: "Melanoma"}
        legends["Asymmetry"] = {0: "Fully Symmetric",
                                1: "Symmetric in 1 axe",
                                2: "Fully Asymmetric"}
        legends["Colors"] = {1: "White",
                             2: "Red",
                             3: "Light - Brown",
                             4: "Dark - Brown",
                             5: "Blue - Gray",
                             6: "Black"}
        return legends

    def fetch_metadata(self):
        return pd.read_csv(self.meta_dir)


class UPHandler(DatasetHandler):  # TODO Setup UP dataset
    def __init__(self):
        super().__init__("up")


if __name__ == '__main__':
    isic16 = Isic16Handler()
    isic17 = Isic17Handler()
    isic18 = Isic18Handler()
    isic19 = Isic19Handler()
    isic20 = Isic20Handler()
    isic19.download_dataset()
    isic20.download_dataset()
    isic19.setup_dataset()
    isic20.setup_dataset()
