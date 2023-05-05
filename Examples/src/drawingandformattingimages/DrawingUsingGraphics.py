# GROUP: DRAWING_AND_FORMATTING_IMAGES
import aspose.pycore as aspycore
from aspose.imaging import Image, Graphics, Color, Pen, Rectangle, PointF
from aspose.imaging.brushes import LinearGradientBrush
from aspose.imaging.imageoptions import BmpOptions
from aspose.imaging.sources import StreamSource
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
print("Running example DrawingUsingGraphics")
# The path to the documents directory.
out_file = os.path.join(get_output_dir(), "SampleImage_out.bmp")
# Create an instance of BmpOptions and set its various properties
with BmpOptions() as save_options:
	save_options.bits_per_pixel = 24
	# Set the Source for BmpOptions and create an instance of Image
	save_options.source = StreamSource() # create in memory
	with Image.create(save_options, 500, 500) as image:
		graphics = Graphics(image)
		# Clear the image surface with white color and Create and initialize a Pen object with blue color
		graphics.clear(Color.white)
		pen = Pen(Color.blue)
		# Draw Ellipse by defining the bounding rectangle of width 150 and height 100 also Draw a polygon using the LinearGradientBrush
		graphics.draw_ellipse(pen, Rectangle(10, 10, 150, 100))
		with LinearGradientBrush(image.bounds, Color.red, Color.white, 45.0) as linear_gradient_brush:
			graphics.fill_polygon(linear_gradient_brush, 
								  [PointF(200.0, 200.0), 
								   PointF(400.0, 200.0), 
								   PointF(250.0, 350.0)])

		image.save(out_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example DrawingUsingGraphics")

