from aspose.imaging import Image, Graphics, PointF, Font, FontStyle, Color
from aspose.imaging.imageoptions import PngOptions
from aspose.imaging.brushes import SolidBrush
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
data_dir = os.path.join(get_data_root_dir(), 'ModifyingAndConvertingImages')
out_file = os.path.join(get_output_dir(), "AddWatermarkToImage_out.bmp")
print("Running example AddWatermarkToImage")
# Create an instance of Image and load an existing image
with Image.load(os.path.join(data_dir, "WaterMark.bmp")) as image:
	# Create and initialize an instance of Graphics class
	graphics = Graphics(image)
	# Creates an instance of Font
	font = Font("Times New Roman", 16.0, FontStyle.BOLD)
	# Create an instance of SolidBrush and set its various properties
	brush = SolidBrush()
	brush.color = Color.black
	# Draw a String using the SolidBrush object and Font, at specific Point and Save the image with changes.
	graphics.draw_string("Aspose.Imaging for Python via .Net", font, brush, 
						 PointF(image.width / 2, image.height / 2))
	image.save(out_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example AddWatermarkToImage")

