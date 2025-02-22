from ImageGoNord import GoNord
import datetime
import sys
import os


# E.g. Replace pixel by pixel
go_nord = GoNord()

output_dir = "../gallery/nord/"


def image_go_nord(source_dir, filename):
    print("nord begin", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    target_path = os.path.join(output_dir, filename)
    print(os.path.abspath(target_path))
    image = go_nord.open_image(os.path.join(source_dir, filename))
    go_nord.convert_image(
        image,
        save_path=target_path,
        parallel_threading=True,
    )
    print("nord end", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def parse_all_source_file(source_dir):
    for file in os.listdir(source_dir):
        if os.path.isfile(os.path.join(output_dir, file)):
            print("skip", file)
            continue
        image_go_nord(source_dir, file)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        source_dir = sys.argv[1]
    else:
        source_dir = "../gallery/original/"
        parse_all_source_file(source_dir)
    print()
    for file in os.listdir(output_dir):
        print("    - https://cdn.jsdelivr.net/gh/kawhicurry/picgo/gallery/nord/" + file)
