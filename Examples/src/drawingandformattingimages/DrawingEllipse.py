# GROUP: DRAWING_AND_FORMATTING_IMAGES
import aspose.pycore as aspycore
from aspose.imaging import Image, Graphics, Color, Pen, Rectangle
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

print("Running example DrawingEllipse")
# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), "DrawingAndFormattingImages")
out_file = os.path.join(get_output_dir(), "DrawingEllipse_out.bmp")
# Create an instance of BmpOptions and set its various properties
with BmpOptions() as save_options:
	save_options.bits_per_pixel = 32
	# Set the Source for BmpOptions and create an instance of Image
	save_options.source = StreamSource() # create in memory
	with Image.create(save_options, 100, 100) as image:
		# Create an instance of BmpOptions and set its various properties
		save_options = BmpOptions()
		save_options.bits_per_pixel = 32
		save_options.source = StreamSource() # in memory
		# Create an instance of Image
		with Image.create(save_options, 100, 100) as image:
			# Create and initialize an instance of Graphics class and Clear Graphics surface                    
			graphic = Graphics(image)
			graphic.clear(Color.yellow)
			# Draw a dotted ellipse shape by specifying the Pen object having red color and a surrounding Rectangle
			graphic.draw_ellipse(Pen(Color.red), Rectangle(30, 10, 40, 80))
			# Draw a continuous ellipse shape by specifying the Pen object having solid brush with blue color and a surrounding Rectangle
			graphic.draw_ellipse(Pen(SolidBrush(Color.blue)), Rectangle(10, 30, 80, 40))
			image.save(out_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)
	
print("Finished example DrawingEllipse")

