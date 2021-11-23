import argparse
import os
import rasterio as rio
import numpy as np
import cv2 as cv
import importlib.resources as pkg_resources
from . import resources



def get_castellon_image_path():
    path_ctx = pkg_resources.path(resources, 'castellon.tif')
    return path_ctx


def generate(base_name, count, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    with get_castellon_image_path() as castellon_path:
        with rio.Env():
            with rio.open(castellon_path) as src:
                for i in range(count):
                    name = os.path.join(output_folder, f'{base_name}_{i}.tif')
                    print(f"Generating {name}")
                    with rio.open(name, 'w', **src.profile) as dst:
                        for i in range(src.count):
                            data = src.read(i + 1)
                            dst.write(data, i + 1)


def blur(images, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    for image in images:
        _, file_name = os.path.split(image)
        file_name, extension = os.path.splitext(file_name)
        blur_file = os.path.join(output_folder, f'{file_name}.blur{extension}')
        kernel = np.ones((5, 5), np.float32) / 25
        with rio.Env():
            with rio.open(image) as src:
                with rio.open(blur_file, 'w', **src.profile) as dst:
                    print(f"blurring {blur_file}")
                    for i in range(src.count):
                        data = src.read(i + 1)
                        data = cv.filter2D(data, -1, kernel)
                        data = data.astype(src.profile['dtype'])
                        dst.write(data, i + 1)
        pass


def parse_args():
    import argparse

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="action", help='Actions available')

    generate_parser = subparsers.add_parser("generate")
    generate_parser.add_argument("-c", "--count", type=int, default=1, help="Number to images to export")
    generate_parser.add_argument("-n", "--base-name", default="image", help="Base name for the generated images")
    generate_parser.add_argument("-o", "--output-folder")

    blur_parser = subparsers.add_parser("blur")
    blur_parser.add_argument('-i', '--image', action='append', help='images to blur')
    blur_parser.add_argument("-o", "--output-folder")

    return parser.parse_args()


def main():
    args = parse_args()

    if args.action == 'generate':
        generate(args.base_name, args.count, args.output_folder)
    elif args.action == 'blur':
        blur(args.image, args.output_folder)


if __name__ == '__main__':
    main()
