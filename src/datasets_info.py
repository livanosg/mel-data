import os

from conf import INIT_DATA_PATH, RAW_DATA_PATH


class DatasetInfo:
    def __init__(self, name: str, urls: list[str]):
        """Initializes a DatasetInfo object.
        :param name: The name of the dataset
        :param urls: The URL of the dataset
        """
        self.name = name
        self.urls = urls
        self.init_data_folder = os.path.join(INIT_DATA_PATH, self.name)
        self.data_folder = os.path.join(RAW_DATA_PATH, self.name)


ISIC16 = DatasetInfo(name="isic16",
                     urls=
                     ["https://isic-challenge-data.s3.amazonaws.com/2016/ISBI2016_ISIC_Part3_Training_Data.zip",
                      "https://isic-challenge-data.s3.amazonaws.com/2016/ISBI2016_ISIC_Part3_Training_GroundTruth.csv",
                      "https://isic-challenge-data.s3.amazonaws.com/2016/ISBI2016_ISIC_Part3_Test_Data.zip",
                      "https://isic-challenge-data.s3.amazonaws.com/2016/ISBI2016_ISIC_Part3_Test_GroundTruth.csv"
                      ])

ISIC17 = DatasetInfo(name="isic17",
                     urls=
                     ["https://isic-challenge-data.s3.amazonaws.com/2017/ISIC-2017_Training_Data.zip",
                      "https://isic-challenge-data.s3.amazonaws.com/2017/ISIC-2017_Training_Part1_GroundTruth.zip",
                      "https://isic-challenge-data.s3.amazonaws.com/2017/ISIC-2017_Training_Part2_GroundTruth.zip",
                      "https://isic-challenge-data.s3.amazonaws.com/2017/ISIC-2017_Training_Part3_GroundTruth.csv",
                      "https://isic-challenge-data.s3.amazonaws.com/2017/ISIC-2017_Validation_Data.zip",
                      "https://isic-challenge-data.s3.amazonaws.com/2017/ISIC-2017_Validation_Part1_GroundTruth.zip",
                      "https://isic-challenge-data.s3.amazonaws.com/2017/ISIC-2017_Validation_Part2_GroundTruth.zip",
                      "https://isic-challenge-data.s3.amazonaws.com/2017/ISIC-2017_Validation_Part3_GroundTruth.csv",
                      "https://isic-challenge-data.s3.amazonaws.com/2017/ISIC-2017_Test_v2_Data.zip",
                      "https://isic-challenge-data.s3.amazonaws.com/2017/ISIC-2017_Test_v2_Part1_GroundTruth.zip",
                      "https://isic-challenge-data.s3.amazonaws.com/2017/ISIC-2017_Test_v2_Part2_GroundTruth.zip0",
                      "https://isic-challenge-data.s3.amazonaws.com/2017/ISIC-2017_Test_v2_Part3_GroundTruth.csv"
                      ])

ISIC18 = DatasetInfo(name="isic18",
                     urls=
                     ["https://isic-challenge-data.s3.amazonaws.com/2018/ISIC2018_Task1-2_Training_Input.zip",
                      "https://isic-challenge-data.s3.amazonaws.com/2018/ISIC2018_Task3_Training_Input.zip",
                      "https://isic-challenge-data.s3.amazonaws.com/2018/ISIC2018_Task3_Training_LesionGroupings.csv",
                      "https://isic-challenge-data.s3.amazonaws.com/2018/ISIC2018_Task1_Training_GroundTruth.zip",
                      "https://isic-challenge-data.s3.amazonaws.com/2018/ISIC2018_Task2_Training_GroundTruth_v3.zip",
                      "https://isic-challenge-data.s3.amazonaws.com/2018/ISIC2018_Task3_Training_GroundTruth.zip",
                      "https://isic-challenge-data.s3.amazonaws.com/2018/ISIC2018_Task1-2_Validation_Input.zip",
                      "https://isic-challenge-data.s3.amazonaws.com/2018/ISIC2018_Task3_Validation_Input.zip",
                      "https://isic-challenge-data.s3.amazonaws.com/2018/ISIC2018_Task1_Validation_GroundTruth.zip",
                      "https://isic-challenge-data.s3.amazonaws.com/2018/ISIC2018_Task2_Validation_GroundTruth.zip",
                      "https://isic-challenge-data.s3.amazonaws.com/2018/ISIC2018_Task3_Validation_GroundTruth.zip",
                      "https://isic-challenge-data.s3.amazonaws.com/2018/ISIC2018_Task1-2_Test_Input.zip",
                      "https://isic-challenge-data.s3.amazonaws.com/2018/ISIC2018_Task3_Test_Input.zip",
                      "https://isic-challenge-data.s3.amazonaws.com/2018/ISIC2018_Task1_Test_GroundTruth.zip",
                      "https://isic-challenge-data.s3.amazonaws.com/2018/ISIC2018_Task2_Test_GroundTruth.zip",
                      "https://isic-challenge-data.s3.amazonaws.com/2018/ISIC2018_Task3_Test_GroundTruth.zip",
                      ])

ISIC19 = DatasetInfo(name="isic19",
                     urls=
                     [
                         "https://isic-challenge-data.s3.amazonaws.com/2019/ISIC_2019_Training_Input.zip",
                         "https://isic-challenge-data.s3.amazonaws.com/2019/ISIC_2019_Training_Metadata.csv",
                         "https://isic-challenge-data.s3.amazonaws.com/2019/ISIC_2019_Training_GroundTruth.csv",
                         "https://isic-challenge-data.s3.amazonaws.com/2019/ISIC_2019_Test_Input.zip",
                         "https://isic-challenge-data.s3.amazonaws.com/2019/ISIC_2019_Test_Metadata.csv",
                     ])

ISIC20 = DatasetInfo(name="isic20",
                     urls=
                     [  # links with JPEG images
                         "https://isic-challenge-data.s3.amazonaws.com/2020/ISIC_2020_Training_JPEG.zip",
                         "https://isic-challenge-data.s3.amazonaws.com/2020/ISIC_2020_Training_GroundTruth_v2.csv",
                         "https://isic-challenge-data.s3.amazonaws.com/2020/ISIC_2020_Training_Duplicates.csv",
                         "https://isic-challenge-data.s3.amazonaws.com/2020/ISIC_2020_Training_GroundTruth.csv",
                         "https://isic-challenge-data.s3.amazonaws.com/2020/ISIC_2020_Test_JPEG.zip",
                         "https://isic-challenge-data.s3.amazonaws.com/2020/ISIC_2020_Test_Metadata.csv",
                     ])

MCLASS = DatasetInfo(name="mclass",
                     urls=
                     [
                         "https://skinclass.de/MClass/MClass-D.zip",
                         "https://skinclass.de/MClass/ResultsDermoscopic.xlsx",
                         "https://skinclass.de/MClass/DermoscopicNameSource.xlsx",
                         "https://skinclass.de/MClass/MClass-ND",
                         "https://skinclass.de/MClass/ResultsClinical.xlsx",
                         "https://skinclass.de/MClass/ClinicalNameSource.xlsx"])

PADUFES = DatasetInfo(name="padufes",
                      urls=
                      ["https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/zr7vgbcyr2-1.zip"])

MEDNODE = DatasetInfo(name="mednode",
                      urls=["https://www.cs.rug.nl/~imaging/databases/melanoma_naevi/complete_mednode_dataset.zip"])

PH2 = DatasetInfo(name="ph2",
                  urls=["https://uc638d0f0ca8f39a39d3da66a2b9.dl.dropboxusercontent.com/cd/0/get/B_cYflfhmLj5vft35tb9UBxdAtPjmiHib69YbVuBXmaqSJId8CIPV4v0tB0X44BcU4Lc6aZacDFViVZMRH_Xr8ldp3a2b1Oj29_ZxmRP_oUkZ8KdUj5WbqSX1Fmb17HobHYy6pTVliOjMRcXDaGNMARodZ2-rzOhPxQ0UGTIFqR7mQ/file?_download_id=068820136001941372943562332396237514187100261566616555272516924457&_notify_domain=www.dropbox.com&dl=1"])

