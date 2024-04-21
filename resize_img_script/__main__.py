from pathlib import Path
import sys
from PIL import Image
import os
from tqdm import tqdm


def get_img_files(directory) -> list[Path]:
    image_files = list(directory.glob("*.jpg"))
    return image_files


def resize_image(input_image_path, output_image_path, target_filesize):
    original_image = Image.open(input_image_path)

    quality = 95  # Starting quality (high quality)

    # Iterate until desired file size is achieved
    while True:
        original_image.save(
            output_image_path, quality=quality, optimize=True, dpi=(72, 72)
        )

        filesize = os.path.getsize(output_image_path)

        if filesize <= target_filesize:
            break

        quality -= 5  # You can adjust this step size as needed

        if quality < 1:
            quality = 1
            break


def main():
    dir_path = Path(sys.argv[1])
    image_files = get_img_files(dir_path)

    result_path = dir_path / "resized"
    result_path.mkdir(exist_ok=True)

    for image_file in tqdm(image_files):
        output_image_path = result_path / image_file.name
        resize_image(image_file, output_image_path, 1500000)


main()
