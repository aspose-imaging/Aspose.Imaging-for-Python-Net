# GROUP: DRAWING_AND_FORMATTING_IMAGES
import aspose.pycore as aspycore
from aspose.imaging import Image, Graphics, Color, Pen, Point
from aspose.imaging.brushes import SolidBrush
from aspose.imaging.imageoptions import BmpOptions
from aspose.imaging.sources import StreamSource
import os

# Initialization
def get_data_root_dir_local():
	if 'BASE_DIR' in os.environ:
		return os.environ["BASE_DIR"]
	return "."
	
def get_output_dir_local():
	return get_data_root_dir_local()

if 'get_data_root_dir' not in dir():
	get_data_root_dir = get_data_root_dir_local

if 'get_output_dir' not in dir():
	get_output_dir = get_output_dir_local

# Example code:

print("Running example DrawingLines")
# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), "DrawingAndFormattingImages")
out_file = os.path.join(get_output_dir(), "SolidLines_out.bmp")
# Create an instance of BmpOptions and set its various properties
with BmpOptions() as save_options:
	save_options.bits_per_pixel = 32
	# Set the Source for BmpOptions and create an instance of Image
	save_options.source = StreamSource() # create in memory
	with Image.create(save_options, 100, 100) as image:
		# Create and initialize an instance of Graphics class and Clear Graphics surface
		graphic = Graphics(image)
		graphic.clear(Color.yellow)
		# Draw two dotted diagonal lines by specifying the Pen object having blue color and co-ordinate Points
		graphic.draw_line(Pen(Color.blue), 9, 9, 90, 90)
		graphic.draw_line(Pen(Color.blue), 9, 90, 90, 9)
		# Draw a four continuous line by specifying the Pen object having Solid Brush with red color and two point structures
		graphic.draw_line(Pen(SolidBrush(Color.red)), Point(9, 9), Point(9, 90))
		graphic.draw_line(Pen(SolidBrush(Color.aqua)), Point(9, 90), Point(90, 90))
		graphic.draw_line(Pen(SolidBrush(Color.black)), Point(90, 90), Point(90, 9))
		graphic.draw_line(Pen(SolidBrush(Color.white)), Point(90, 9), Point(9, 9))
		image.save(out_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example DrawingLines")
