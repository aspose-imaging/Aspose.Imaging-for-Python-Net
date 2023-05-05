# GROUP: DRAWING_AND_FORMATTING_IMAGES
import aspose.pycore as aspycore
from aspose.imaging import Image, Graphics, Color, Pen
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

print("Running example DrawingArc")
# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), "DrawingAndFormattingImages")
out_file = os.path.join(get_output_dir(), "DrawingArc_out.bmp")
# Create an instance of BmpOptions and set its various properties
with BmpOptions() as save_options:
	save_options.bits_per_pixel = 32
	# Set the Source for BmpOptions and create an instance of Image
	save_options.source = StreamSource() # create in memory
	with Image.create(save_options, 100, 100) as image:
		# Create and initialize an instance of Graphics class and clear Graphics surface
		graphic = Graphics(image)
		graphic.clear(Color.yellow)
		# Draw an arc shape by specifying the Pen object having red black color and coordinates, height, width, start & end angles                 
		width = 100
		height = 200
		start_angle = 45.0
		sweep_angle = 270.0
		# Draw arc to screen and save all changes.
		graphic.draw_arc(Pen(Color.black), 0, 0, width, height, start_angle, sweep_angle)
		image.save(out_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)
	
print("Finished example DrawingArc")

