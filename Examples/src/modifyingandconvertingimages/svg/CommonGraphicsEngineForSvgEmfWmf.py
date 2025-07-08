# GROUP: TEST_FILE_FORMATS
from aspose.imaging import Graphics, Color, Pen, Rectangle, PointF, Font
from aspose.imaging.brushes import SolidBrush
from aspose.imaging.fileformats.svg import SvgImage    
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
output_path = get_output_dir()                                                       

fileName = "test.svg"
output_file = os.path.join(get_output_dir(), fileName)

with SvgImage(100,100) as vectorImage:
   g = Graphics(vectorImage)
   g.fill_rectangle(SolidBrush(Color.light_yellow), 10, 10, 80, 80)
   g.draw_rectangle(Pen(Color.red, 4), 10, 10, 80, 80)
   g.fill_ellipse(SolidBrush(Color.light_green), 20, 20, 60, 60)
   g.draw_ellipse(Pen(Color.green, 2), 20, 20, 60, 60)
   g.fill_pie(SolidBrush(Color.light_blue), Rectangle(30, 30, 40, 40), 0, 45)
   g.draw_pie(Pen(Color.blue, 1), Rectangle(30, 30, 40, 40), 0, 45)
   g.draw_line(Pen(Color.dark_red, 1), 10, 20, 90, 20)
   g.draw_lines_f(Pen(Color.dark_red, 1), [ PointF(10, 90), PointF(20, 80), PointF(30, 90) ])
   g.draw_polygon_f(Pen(Color.dark_red, 1), [ PointF(90, 90), PointF(80, 80), PointF(70, 90) ])
   g.draw_string("Hello World!", Font("Arial", 14), SolidBrush(Color.dark_blue), PointF(10, 50))
   g.draw_arc(Pen(Color.brown, 1), Rectangle(30, 30, 40, 40), 135, -90)

   vectorImage.save(output_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_file)
