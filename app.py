import os
import subprocess

import cat_service

def main():
    print_welcome()
    # get or create output folder
    folder = get_or_create_output_folder()
    print(f"Found or created folder {folder}")

    # download cats
    download_cats(folder)

    # display cats
    display_cats(folder)

def print_welcome():
    print("-----------------")
    print("---cat factory---")
    print("-----------------")


def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'cats'
    full_path = os.path.join(base_folder, folder)
    print(full_path)
    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print(f"Creating new directory at {full_path}")
        os.mkdir(full_path)
    return full_path


def download_cats(folder):
    cat_count = 8
    for i in range(1, cat_count+1):
        name = f"lolcat {i}"
        cat_service.get_cat(folder, name)
    print("done")


def display_cats(folder):
    print("Displaying cats in os window")
    subprocess.call(["explorer", folder])




if __name__ == '__main__':
    main()