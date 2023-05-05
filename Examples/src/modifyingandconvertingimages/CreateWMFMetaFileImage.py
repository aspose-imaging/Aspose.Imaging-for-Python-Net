import aspose.pycore as aspycore
from aspose.imaging.fileformats.wmf.graphics import WmfRecorderGraphics2D
import aspose.pycore as aspycore
from aspose.imaging.brushes import SolidBrush, HatchBrush
from aspose.imaging import Image, SizeF, LineJoin, Point, Pen, \
	Rectangle, Size, LineCap, HatchStyle, DashStyle, Font
from aspose.imaging.imageoptions import EmfRasterizationOptions, PdfOptions
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
print("Running example CreateWMFMetaFileImage")
# WmfRecorderGraphics2D class provides you the frame or canvas to draw shapes on it.  Create an instance of WmfRecorderGraphics2D class. The constructor takes in 2 parameters:  1. Instance of Imaging Rectangle class 2. An integer value for inches            
graphics = WmfRecorderGraphics2D(Rectangle(0, 0, 100, 100), 96)
# Define background color
graphics.background_color = Color.white_smoke
# Init Create an instance of Imaging Pen class,  Brush class and mention its color.
pen = Pen(Color.blue)
brush = SolidBrush(Color.yellow_green)
# Polygon Fill polygon and then Draw a polygon             
graphics.fill_polygon(brush, [Point(2, 2), Point(20, 20), Point(20, 2)])
graphics.draw_polygon(pen, [Point(2, 2), Point(20, 20), Point(20, 2)])

brush = HatchBrush()
brush.hatch_style = HatchStyle.CROSS
brush.background_color = Color.white
brush.foreground_color = Color.silver
# Fill ellipse  and  Draw an ellipse
graphics.fill_ellipse(brush, Rectangle(25, 2, 20, 20))
graphics.draw_ellipse(pen, Rectangle(25, 2, 20, 20))

# Arc Define pen style by setting DashStyle value, Set color of the pen
pen.dash_style = DashStyle.DOT
pen.color = Color.black
# Draw an Arc by calling DrawArc method and set CubicBezier
graphics.draw_arc(pen, Rectangle(50, 2, 20, 20), 0, 180)
pen.dash_style = DashStyle.SOLID
pen.color = Color.red
# Draw an draw_cubic_bezier 
graphics.draw_cubic_bezier(pen, Point(10, 25), Point(20, 50), Point(30, 50), 
						   Point(40, 25))

# Image  Create an Instance of Image class.
with Image.load(os.path.join(data_dir, "WaterMark.bmp")) as image:
	# Cast the instance of image class to RasterImage.
	raster_image = aspycore.as_of(image, RasterImage)
	# Draw an image by calling draw_image method and passing parameters 
	# raster image and point.
	graphics.draw_image(raster_image, Point(50, 50))

# Line Draw a line by calling draw_line method and passing x,y coordinates 
# of 1st point and same for 2nd point along with color info as Pen.
graphics.draw_line(pen, Point(2, 98), Point(2, 50))

# Define settings of the brush object.
brush = SolidBrush(Color.green)
pen.color = Color.dark_goldenrod
# Fill pie by calling fill_pie method and passing parameters brush and an instance 
# of Imaging Rectangle class.
graphics.fill_pie(brush, Rectangle(2, 38, 20, 20), 0, 45)
# Draw pie by calling draw_pie method and passing parameters pen and an instance
# of Imaging Rectangle class.
graphics.draw_pie(pen, Rectangle(2, 38, 20, 20), 0, 45)
pen.color = Color.alice_blue
# Draw Polyline by calling draw_polyline method and passing parameters
# pen and points.
graphics.draw_polyline(pen, [Point(50, 40), Point(75, 40), Point(75, 45), 
					   Point(50, 45)])
# For having Strings Create an instance of Font class.
font = Font("Arial", 16.0)
# Draw String by calling DrawString method and passing parameters string 
# to display, color and X & Y coordinates.
graphics.draw_string("Aspose", font, Color.blue, 25, 75)
out_file = os.path.join(get_output_dir(), "CreateWMFMetaFileImage.wmf")
# Call end recording of graphics object and save WMF image by calling save method.
with graphics.end_recording() as image:
	image.save(out_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)
	
print("Finished example CreateWMFMetaFileImage")
