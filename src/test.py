import os.path

import pandas as pd

df = pd.read_csv("/home/giorgos/projects/mel-data/zips/up/new_up/up.csv")
tst = "clinic/2/a/3.JPG"


def _path(path):
    splits = path.split("/")
    filename = splits[1] + splits[2] + os.path.splitext(splits[3])[1]
    filename = "0" * (9 - len(filename)) + filename
    filename = os.path.join(splits[0], filename)
    # print(filename)
    return filename


df["image"] = df["image"].map(_path)
df.to_csv("/home/giorgos/projects/mel-data/zips/up/new_up/up2.csv", index=False)