# GROUP: DRAWING_AND_FORMATTING_IMAGES
import aspose.pycore as aspycore
from aspose.imaging import Image, Graphics, Color, Pen, Rectangle, PointF, HatchStyle, \
GraphicsPath, Figure, RectangleF, Font, StringFormat
from aspose.imaging.brushes import HatchBrush
from aspose.imaging.shapes import EllipseShape, RectangleShape, TextShape
from aspose.imaging.imageoptions import BmpOptions
from aspose.imaging.sources import StreamSource
import os


# Initialization
def get_data_root_dir_local():
	if 'BASE_DIR' in os.environ:
		return os.environ["BASE_DIR"]
	return "."


if 'get_output_dir' not in dir():
	get_output_dir = get_data_root_dir_local

# Example code:
print("Running example DrawingUsingGraphicsPath")
# The path to the documents directory.
out_file = os.path.join(get_output_dir(), "sample_1.bmp")
# Create an instance of BmpOptions and set its various properties
with BmpOptions() as save_options:
	save_options.bits_per_pixel = 24
	# Set the Source for BmpOptions and create an instance of Image
	save_options.source = StreamSource() # create in memory
	with Image.create(save_options, 500, 500) as image:
		graphics = Graphics(image)
		graphics.clear(Color.white)
		# Create an instance of GraphicsPath and Instance of Figure, add EllipseShape, RectangleShape and TextShape to the figure
		graphicspath = GraphicsPath()
		figure = Figure()
		figure.add_shape(EllipseShape(RectangleF(0.0, 0.0, 499.0, 499.0)))
		figure.add_shape(RectangleShape(RectangleF(0.0, 0.0, 499.0, 499.0)))
		figure.add_shape(TextShape("Aspose.Imaging", 
						 RectangleF(170.0, 225.0, 170.0, 100.0), 
						 Font("Arial", 20.0), 
						 StringFormat.generic_typographic))
		graphicspath.add_figures([figure])
		graphics.draw_path(Pen(Color.blue), graphicspath)
		# Create an instance of HatchBrush and set its properties also Fill path by supplying the brush and GraphicsPath objects
		hatchbrush = HatchBrush()
		hatchbrush.background_color = Color.brown
		hatchbrush.foreground_color = Color.blue
		hatchbrush.hatch_style = HatchStyle.VERTICAL
		graphics.fill_path(hatchbrush, graphicspath)
		image.save(out_file)
		print("Processing completed successfully.")

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)
	
print("Finished example DrawingUsingGraphicsPath")
