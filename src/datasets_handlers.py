import glob
import os
import pandas as pd

from conf import RAW_DATA_PATH


class DatasetHandler:
    def __init__(self, name: str):
        self.name = name
        self.raw_dataset_path = os.path.join(RAW_DATA_PATH, self.name)
        self.image_dir = os.path.join(self.raw_dataset_path, "images")
        self.meta_dir = os.path.join(self.raw_dataset_path, "meta")

    def fetch_metadata(self):
        """
        The fetch_metadata function reads the metadata file and returns a pandas dataframe.
        :return: A pandas dataframe
        """
        return pd.read_csv(self.meta_dir)


class Spt(DatasetHandler):
    def __init__(self):
        super().__init__("7pt")
        self.image_dir = os.path.join(self.raw_dataset_path, "release_v0", "images")
        self.meta_dir = os.path.join(self.raw_dataset_path, "release_v0", "meta", "meta.csv")


class Dermofit(DatasetHandler):
    def __init__(self):
        super().__init__("dermofit")
        self.image_dir = os.path.join(self.raw_dataset_path, "Dermofit Database")
        self.meta_dir = os.path.join(self.raw_dataset_path, "Dermofit Database", "lesionlist.txt")
        self


class Isic16Part3(DatasetHandler):
    def __init__(self):
        super().__init__("isic16")
        self.image_dir = os.path.join(self.raw_dataset_path, "ISBI2016_ISIC_Part3_Test_Data")
        self.meta_dir = os.path.join(self.raw_dataset_path, "ISBI2016_ISIC_Part3_Test_GroundTruth.csv")


class Isic17(DatasetHandler):
    def __init__(self):
        super().__init__("isic17")
        self.image_dir = os.path.join(self.raw_dataset_path, "ISIC-2017_Test_v2_Data")
        self.meta_dir = os.path.join(self.raw_dataset_path, "ISIC-2017_Test_v2_Part3_GroundTruth.csv")

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


class Isic18(DatasetHandler):
    def __init__(self):
        super().__init__("isic18")
        self.image_dir = os.path.join(self.raw_dataset_path, "ISIC-2018_Test_v2_Data")
        self.meta_dir = os.path.join(self.raw_dataset_path,
                                     "ISIC2018_Task3_Validation_GroundTruth",
                                     "ISIC2018_Task3_Validation_GroundTruth.csv")


class Isic19(DatasetHandler):
    def __init__(self):
        super().__init__("isic19")
        self.image_dir = os.path.join(self.raw_dataset_path, "ISIC_2019_Training_Input")
        self.meta_dir = os.path.join(self.raw_dataset_path, "ISIC2019_Training_GroundTruth.csv")

    def fetch_metadata(self):
        """
        The fetch_metadata method reads 'ISIC2019_Training_GroundTruth.csv' and 'ISIC_2019_Training_Metadata.csv'.
        Finally, both these dataframes are merged to a single dataframe based on image column and then returned.

        :return: A dataframe with the columns:
        """
        df1 = pd.read_csv(self.meta_dir, index_col=0)
        df2 = pd.read_csv(os.path.join(self.raw_dataset_path, "ISIC_2019_Training_Metadata.csv"), index_col=0)
        df = pd.concat([df1, df2], axis=1, ignore_index=True)
        df["image"] = df.index
        return df.reindex()


class Isic19Test(DatasetHandler):
    def __init__(self):
        super().__init__("isic19_test")
        self.image_dir = os.path.join(self.raw_dataset_path, "ISIC_2019_Test_Input")
        self.meta_dir = os.path.join(self.raw_dataset_path, "ISIC_2019_Test_Metadata.csv")


class Isic20(DatasetHandler):
    def __init__(self):
        super().__init__("isic20")
        self.image_dir = os.path.join(self.raw_dataset_path, "train")
        self.meta_dir = os.path.join(self.raw_dataset_path, "ISIC_2020_Training_GroundTruth_v2.csv")

    def _remove_duplicates(self):
        meta = pd.read_csv(self.meta_dir)
        duplicates = pd.read_csv(os.path.join(self.raw_dataset_path, "ISIC_2020_Training_Duplicates.csv"))
        return meta[~meta.loc[:, "image_name"].isin(duplicates["image_name_2"])]

    def fetch_metadata(self, remove_duplicates=True):
        return self._remove_duplicates() if remove_duplicates else pd.read_csv(self.meta_dir)


class Isic20Test(DatasetHandler):
    def __init__(self):
        super().__init__("isic20_test")
        self.image_dir = os.path.join(self.raw_dataset_path, "ISIC_2020_Test_Input")
        self.meta_dir = os.path.join(self.raw_dataset_path, "ISIC_2020_Test_Metadata.csv")


class Mednode(DatasetHandler):
    def __init__(self):
        super().__init__("mednode")
        self.image_dir = os.path.join(self.raw_dataset_path, "complete_mednode_dataset")
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


class Padufes(DatasetHandler):
    def __init__(self):
        super().__init__("padufes")
        self.image_dir = os.path.join(self.raw_dataset_path, "images")
        self.meta_dir = os.path.join(self.raw_dataset_path, "metadata.csv")
        map(lambda src: os.rename(src=src, dst=os.path.join(self.image_dir, os.path.basename(src))),
            glob.glob(os.path.join(self.raw_dataset_path, "imgs_part_*/**"), recursive=True))


class Ph2(DatasetHandler):
    def __init__(self):
        super().__init__("ph2")
        self.image_dir = os.path.join(self.raw_dataset_path, "PH2 Dataset images")
        self.meta_dir = os.path.join(self.raw_dataset_path, "PH2_Dataset.csv")
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
                                1: "Symetric in 1 axe",
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


class UP(DatasetHandler):  # TODO Setup UP dataset
    def __init__(self):
        super().__init__("up")


if __name__ == '__main__':
    a = Ph2()
