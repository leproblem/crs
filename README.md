# crs
Color-reducer-splitter in python

## Requirements and usage:

1. Get Python version of 3.8 or higher from https://www.python.org/downloads/
2. `pip install pillow==10.2.0 numpy==1.26.3`
3. Put the main.py into the folder with your images you want to split (for easier usage)
4. Run the app with `python main.py`
5. Enter the path to the image, if its in the same folder, just type its name with filetype like `image.jpg` or `C:\Users\test\Pictures\image.jpg` for absolute path
6. Enter the amount of colors you want to separate the image to, for high quality, pick from 10 to 30, you will also be able to see the final result in the result
7. Then type the folder's name in which all files will be saved into, it will be created if it doesn't exist same as the name basically
You can check the `reduced_base.png` that will be automatically saved as you split an image whether you like the result or no
