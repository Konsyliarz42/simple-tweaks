import shutil
from pathlib import Path

FOLDERS = [
    Path("blockstates"),
    Path("models/block"),
    Path("textures/block")
]
ASSETS_FOLDER = Path("./assets/minecraft")


def rm_tree(pth: Path):
    for child in pth.iterdir():
        if child.is_file():
            child.unlink()
        else:
            rm_tree(child)

    pth.rmdir()


if __name__ == "__main__":
    if ASSETS_FOLDER.exists():
        rm_tree(ASSETS_FOLDER)

    for folder in FOLDERS:
        (ASSETS_FOLDER / folder).mkdir(parents=True)
        files = folder.glob("**/*")

        for file in files:
            if file.is_file():
                print(ASSETS_FOLDER/folder/file.name)
                shutil.copyfile(file, ASSETS_FOLDER/folder/file.name)

        print("-"*64)

    input("Press any key to continue...")
