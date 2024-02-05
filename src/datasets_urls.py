DATASETS_INFO = {
    'isic16': {"urls": ["https://isic-challenge-data.s3.amazonaws.com/2016/ISBI2016_ISIC_Part3B_Training_Data.zip",
                        "https://isic-challenge-data.s3.amazonaws.com/2016/ISBI2016_ISIC_Part3B_Training_GroundTruth.csv",
                        "https://isic-challenge-data.s3.amazonaws.com/2016/ISBI2016_ISIC_Part3B_Test_Data.zip",
                        "https://isic-challenge-data.s3.amazonaws.com/2016/ISBI2016_ISIC_Part3B_Test_GroundTruth.csv"]
               },
    'isic17': {"urls": ["https://isic-challenge-data.s3.amazonaws.com/2017/ISIC-2017_Training_Data.zip",
                        "https://isic-challenge-data.s3.amazonaws.com/2017/ISIC-2017_Training_Part1_GroundTruth.zip",
                        "https://isic-challenge-data.s3.amazonaws.com/2017/ISIC-2017_Training_Part2_GroundTruth.zip",
                        "https://isic-challenge-data.s3.amazonaws.com/2017/ISIC-2017_Training_Part3_GroundTruth.csv",
                        "https://isic-challenge-data.s3.amazonaws.com/2017/ISIC-2017_Validation_Data.zip",
                        "https://isic-challenge-data.s3.amazonaws.com/2017/ISIC-2017_Validation_Part1_GroundTruth.zip",
                        "https://isic-challenge-data.s3.amazonaws.com/2017/ISIC-2017_Validation_Part2_GroundTruth.zip",
                        "https://isic-challenge-data.s3.amazonaws.com/2017/ISIC-2017_Validation_Part3_GroundTruth.csv",
                        "https://isic-challenge-data.s3.amazonaws.com/2017/ISIC-2017_Test_v2_Data.zip",
                        "https://isic-challenge-data.s3.amazonaws.com/2017/ISIC-2017_Test_v2_Part1_GroundTruth.zip",
                        "https://isic-challenge-data.s3.amazonaws.com/2017/ISIC-2017_Test_v2_Part2_GroundTruth.zip",
                        "https://isic-challenge-data.s3.amazonaws.com/2017/ISIC-2017_Test_v2_Part3_GroundTruth.csv"]
               },
    'isic18': {"urls": ["https://isic-challenge-data.s3.amazonaws.com/2018/ISIC2018_Task1-2_Training_Input.zip",
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
                        "https://isic-challenge-data.s3.amazonaws.com/2018/ISIC2018_Task3_Test_GroundTruth.zip"]
               },
    'isic19': {"urls": ["https://isic-challenge-data.s3.amazonaws.com/2019/ISIC_2019_Training_Input.zip",
                        "https://isic-challenge-data.s3.amazonaws.com/2019/ISIC_2019_Training_Metadata.csv",
                        "https://isic-challenge-data.s3.amazonaws.com/2019/ISIC_2019_Training_GroundTruth.csv",
                        "https://isic-challenge-data.s3.amazonaws.com/2019/ISIC_2019_Test_Input.zip",
                        "https://isic-challenge-data.s3.amazonaws.com/2019/ISIC_2019_Test_Metadata.csv"]
               },
    # ISIC20_URLS provides links of JPEG images, not DICOM
    'isic20': {"urls": ["https://isic-challenge-data.s3.amazonaws.com/2020/ISIC_2020_Training_JPEG.zip",
                        "https://isic-challenge-data.s3.amazonaws.com/2020/ISIC_2020_Training_GroundTruth_v2.csv",
                        "https://isic-challenge-data.s3.amazonaws.com/2020/ISIC_2020_Training_Duplicates.csv",
                        "https://isic-challenge-data.s3.amazonaws.com/2020/ISIC_2020_Training_GroundTruth.csv",
                        "https://isic-challenge-data.s3.amazonaws.com/2020/ISIC_2020_Test_JPEG.zip",
                        "https://isic-challenge-data.s3.amazonaws.com/2020/ISIC_2020_Test_Metadata.csv"]
               },
    'mclass': {"urls": ["https://skinclass.de/MClass/MClass-D.zip",
                        "https://skinclass.de/MClass/ResultsDermoscopic.xlsx",
                        "https://skinclass.de/MClass/DermoscopicNameSource.xlsx",
                        "https://skinclass.de/MClass/MClass-ND",
                        "https://skinclass.de/MClass/ResultsClinical.xlsx",
                        "https://skinclass.de/MClass/ClinicalNameSource.xlsx"]
               },
    'padufes': {"urls": ["https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/zr7vgbcyr2-1.zip"]
                },
    'mednode': {"urls": ["https://www.cs.rug.nl/~imaging/databases/melanoma_naevi"
                         "/complete_mednode_dataset.zip"]
                },
    'spc': {"urls": ["https://derm.cs.sfu.ca/restricted/release_v0.zip"]
            },
    'ph2': {"urls": ["https://www.dropbox.com/s/k88qukc20ljnbuo/PH2Dataset.rar"]
            }
}
