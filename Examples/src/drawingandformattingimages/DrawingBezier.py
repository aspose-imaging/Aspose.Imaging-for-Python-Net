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

print("Running example DrawingBezier")
# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), "DrawingAndFormattingImages")
out_file = os.path.join(get_output_dir(), "DrawingBezier_out.bmp")
# Create an instance of BmpOptions and set its various properties
with BmpOptions() as save_options:
	save_options.bits_per_pixel = 32
	# Set the Source for BmpOptions and Create an instance of Image
	save_options.source = StreamSource() # in memory
	with Image.create(save_options, 100, 100) as image:
		# Create and initialize an instance of Graphics class and clear Graphics surface
		graphic = Graphics(image)
		graphic.clear(Color.yellow)
		# Initializes the instance of PEN class with black color and width
		black_pen = Pen(Color.black, 3)
		start_x = 10
		start_y = 25
		control_x1 = 20
		control_y1 = 5
		control_x2 = 55
		control_y2 = 10
		end_x = 90
		end_y = 25
		# Draw a Bezier shape by specifying the Pen object having black color and co-ordinate Points and save all changes.
		graphic.draw_bezier(black_pen, start_x, start_y, control_x1, control_y1, control_x2, control_y2, end_x, end_y)
		image.save(out_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)
	
print("Finished example DrawingBezier")
