# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image, ResizeType, RotateFlipType, Rectangle
from aspose.imaging.fileformats.webp import WebPImage
import os


# Initialization
def get_data_root_dir_local():
	if 'BASE_DIR' in os.environ:
		return os.environ["BASE_DIR"]
	return "."


if 'get_data_root_dir' not in dir():
	get_data_root_dir = get_data_root_dir_local

if 'get_output_dir' not in dir():
	get_output_dir = get_data_root_dir_local

# Example code:

# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), 'WebPImage')
print("Running example OpenWebPFile")
input_file = os.path.join(data_dir, "Animation1.webp")
output_file = os.path.join(get_output_dir(), "Animation2.webp")
with aspycore.as_of(Image.load(input_file), WebPImage) as image:
	image.resize(300, 450, ResizeType.HIGH_QUALITY_RESAMPLE)
	image.crop(Rectangle(10, 10, 200, 300))
	image.rotate_flip_all(RotateFlipType.ROTATE_90_FLIP_X)
	image.save(output_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_file)

print("Finished example OpenWebPFile")
