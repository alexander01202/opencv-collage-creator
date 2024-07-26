# Bulk Collage Maker Using OpenCV

This python application uses opencv and tinker to create a collage of multiple images.

## How does it work?
* It first finds the screen resolutions
* Finds the maximum amount of columns that would fit all the images perfectly.
* Divides the width and height of the screen by this maximum amount to get the dimension of eah image
* Resizes each image
* Stacks them horizontally
* Stacks them vertically
* Displays the total collage

## Get Started
* Install Python
* Activate a virtual environment
```python -m venv venv```
* Install packages
    ```pip install -r requirements.txt```
* Create an image folder in the root directory and add images
* Run the script
    ```python main.py```