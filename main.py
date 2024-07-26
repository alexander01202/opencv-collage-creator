import cv2 as cv
import os
import numpy as np
from functools import lru_cache
import queue
import tkinter as tk

queues = queue.Queue()
IMAGES_FILE_PATH = "./images"


def get_screen_resolution():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    return width, height


WIDTH_OF_COLLAGE, HEIGHT_OF_COLLAGE = get_screen_resolution()


@lru_cache(maxsize=1000)
def calculate_images_height_and_width(division: int) -> tuple[int, int]:
    width_of_images = int(WIDTH_OF_COLLAGE / division)
    height_of_images = int(HEIGHT_OF_COLLAGE / division)

    return width_of_images, height_of_images


@lru_cache(maxsize=1000)
def calculate_collage_rows_and_cols(no_of_images: int) -> int:
    nums = [2, 3, 4, 5, 6, 7, 8, 9]
    return max([num for num in nums if no_of_images % num == 0])


def display_image(image):
    # Display the stacked image
    cv.imshow('Stacked Image', image)
    cv.waitKey(0)
    cv.destroyAllWindows()


def main():
    images = os.listdir(IMAGES_FILE_PATH)
    no_of_images = len(images)

    maximum_collage_rows_and_cols = calculate_collage_rows_and_cols(no_of_images)
    if not maximum_collage_rows_and_cols or maximum_collage_rows_and_cols < 2:
        maximum_collage_rows_and_cols = calculate_collage_rows_and_cols(no_of_images + 1)
    dimensions = calculate_images_height_and_width(maximum_collage_rows_and_cols)

    resized_images = []
    v_stack = []

    for image in images:
        img = cv.imread(f'images/{image}')
        resized_img = cv.resize(img, dimensions)
        resized_images.append(resized_img)

        # check if the first column is full
        if len(resized_images) >= maximum_collage_rows_and_cols:
            v_stack.append(np.hstack(resized_images))
            resized_images.clear()

    collage = np.vstack(v_stack)  # compile all horizontal stacks into a vertical stack
    display_image(collage)


if "__main__" == __name__:
    main()
