"""Download the Ames Housing dataset (original De Cock version) into data/raw/."""
import urllib.request
from pathlib import Path

URL = "https://huggingface.co/datasets/cloderic/ames_iowa_housing/resolve/main/AmesHousing.csv"
DEST = Path(__file__).resolve().parent.parent / "data" / "raw" / "AmesHousing.csv"


def main():
    DEST.parent.mkdir(parents=True, exist_ok=True)
    if DEST.exists():
        print(f"Already exists: {DEST}")
        return
    print(f"Downloading to {DEST} ...")
    urllib.request.urlretrieve(URL, DEST)
    print("Done.")


if __name__ == "__main__":
    main()
