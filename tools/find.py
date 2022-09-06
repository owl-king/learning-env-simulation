import os
import logging
import pathlib
import shutil

ENV_LOCATION = "/env/tools/find"


def create_directory_full(current_dir):
    """Build a sample directory with nested folders, files
    Tree structure
    - gaming/
        - dota.txt
        - dota2.txt
        - lol.mp4
        - dota/
            - demo/
                - last_hit.mp4
                - deny.mp4
                - deny1.mp4
                - deny2.mp4
                - lure.mp4
                - note.txt
        - lol/
            - demo/
                - last_hit.mp4
                - level_up.mp4
                - level_up1.avi
    """
    folders = ["gaming", "gaming/dota/demo", "gaming/lol/demo"]
    [os.makedirs(current_dir + "/" + folder, exist_ok=True) for folder in folders]

    files = [  # [ file_path, size ]
        ["dota.txt", 2],
        ["dota2.txt", 2],
        ["lol.mp4", 5],
        ["gaming/dota/demo/last_hit.mp4", 1],
        ["gaming/dota/demo/deny.mp4", 2],
        ["gaming/dota/demo/deny1.mp4", 2],
        ["gaming/dota/demo/deny2.mp4", 2],
        ["gaming/dota/demo/lure.mp4", 0.5],
        ["gaming/dota/demo/note.txt", 0.1],
        ["gaming/lol/demo/last_hit.mp4", 3],
        ["gaming/lol/demo/level_up.mp4", 1.4],
        ["gaming/lol/demo/level_up1.avi", 1.5],
    ]
    [_create_file(current_dir + "/" + file[0], file[1]) for file in files]


def _create_file(location, size_mb: int):
    with open(location, "w") as f:
        num_chars = 1024 * 1024 * size_mb
        f.write(int(num_chars) * "0")


def questions():
    questions = {
        1: "Find all mp4 files in current folder only",
        2: "Find all mp4 files in current folder recursively",
        3: "Find files which are larger than 1mb"
    }
    import random
    id = random.randint(1, len(questions.keys()))
    print(f"> Question id: {id}")
    print(f">> {questions[id]}")


def answer():
    id = input("Question id: ")
    if id:
        print("Upcoming version. Stay tuned!!!")


def clean_up_env(main_dir: str):
    shutil.rmtree(f"{main_dir}{ENV_LOCATION}")
    print("> Clean up Find environment successfully!")


def build_env(main_dir: str):
    print("> Start build Find environment")
    env_location = f"{main_dir}{ENV_LOCATION}"
    if not pathlib.Path(env_location).exists():
        os.makedirs(env_location, exist_ok=True)
    create_directory_full(env_location)
    print("> Finish build Find environment")
