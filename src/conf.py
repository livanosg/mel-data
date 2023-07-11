import os

ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC_PATH = os.path.join(ROOT_PATH, "src")
INIT_DATA_PATH = os.path.join(ROOT_PATH, "init_data")
SETUP_DATA_PATH = os.path.join(ROOT_PATH, "setup_data")

URLS_CREDENTIALS = {"spc": tuple(os.environ["SPC_CREDS"].split(","))}
