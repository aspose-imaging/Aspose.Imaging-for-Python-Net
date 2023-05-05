import aspose.pycore as aspycore
from aspose.imaging.brushes import SolidBrush, HatchBrush
from aspose.imaging.fileformats.emf.emf.consts import EmfBackgroundMode
from aspose.imaging.fileformats.emf.graphics import EmfRecorderGraphics2D
from aspose.imaging import Image, SizeF, LineJoin, Point, Pen, \
	Rectangle, Size, LineCap, HatchStyle
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
print("Running example CreateEMFMetaFileImage")
# EmfRecorderGraphics2D class provides you the frame or canvas to draw shapes on it.
graphics = EmfRecorderGraphics2D(Rectangle(0, 0, 1000, 1000), Size(1000, 1000), Size(100, 100))
# Create an instance of Imaging Pen class and mention its color.
pen = Pen(Color.bisque)
# Draw a line by calling DrawLine method and passing x,y coordinates of 1st point and same for 2nd point along with color infor as Pen.
graphics.draw_line(pen, 1, 1, 50, 50)
# Reset the Pen color Specify the end style of the line.
pen = Pen(Color.blue_violet, 3.0)
pen.end_cap = LineCap.ROUND
# Draw a line by calling DrawLine method and passing x,y coordinates of 1st point and same for 2nd point along with color infor as Pen and end style of line.
graphics.draw_line(pen, 15, 5, 50, 60)
# Specify the end style of the line.
pen.end_cap = LineCap.SQUARE
graphics.draw_line(pen, 5, 10, 50, 10)
pen.end_cap = LineCap.FLAT
# Draw a line by calling draw_line method and passing parameters.
graphics.draw_line(pen, Point(5, 20), Point(50, 20))
# Create an instance of HatchBrush class to define rectanglurar brush with with different settings.
hatch_brush = HatchBrush()
hatch_brush.background_color = Color.alice_blue
hatch_brush.foreground_color = Color.red
hatch_brush.hatch_style = HatchStyle.CROSS
# Draw a line by calling draw_line method and passing parameters.
pen = Pen(hatch_brush, 7.0)
graphics.draw_rectangle(pen, 50, 50, 20, 30)
# Draw a line by calling draw_line method and passing parameters with different mode.
graphics.background_mode = EmfBackgroundMode.OPAQUE
graphics.draw_line(pen, 80, 50, 80, 80)
# Draw a polygon by calling draw_polygon method and passing parameters with line join setting/style.
pen = Pen(SolidBrush(Color.aqua), 3.0)
pen.line_join = LineJoin.MITER_CLIPPED
graphics.draw_polygon(pen, [Point(10, 20), Point(12, 45), Point(22, 48), Point(48, 36), Point(30, 55)])
# Draw a rectangle by calling draw_rectangle method.
pen.line_join = LineJoin.BEVEL
graphics.draw_rectangle(pen, 50, 10, 10, 5)
pen.line_join = LineJoin.ROUND
graphics.draw_rectangle(pen, 65, 10, 10, 5)
pen.line_join = LineJoin.MITER
graphics.draw_rectangle(pen, 80, 10, 10, 5)
out_path = os.path.join(get_output_dir(), "CreateEMFMetaFileImage_out.pdf")
# Call end_recording method to produce the final shape. 
# end_recording method will return the final shape as EmfImage. 
with graphics.end_recording() as image:
	# Create an instance of PdfOptions class.
	options = PdfOptions()
	# Create an instance of EmfRasterizationOptions class and define 
	# different settings.
	rasterization_options = EmfRasterizationOptions()
	rasterization_options.page_size = aspycore.cast(SizeF, image.size)
	options.vector_rasterization_options = rasterization_options
	image.save(out_path, options)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_path)
	
print("Finished example CreateEMFMetaFileImage")
