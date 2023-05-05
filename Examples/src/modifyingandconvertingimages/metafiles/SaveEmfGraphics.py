# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image, Color, Font, FontStyle, Rectangle, Size
from aspose.imaging.imageoptions import EmfOptions
from aspose.imaging.fileformats.emf.graphics import EmfRecorderGraphics2D
import os


# Initialization
def get_data_root_dir_local():
	if 'BASE_DIR' in os.environ:
		return os.environ["BASE_DIR"]
	return "."


if 'get_output_dir' not in dir():
	get_output_dir = get_data_root_dir_local

# Example code:
# The path to the documents directory.
print("Running example SaveEmfGraphics")
graphics = EmfRecorderGraphics2D(Rectangle(0, 0, 5000, 5000), Size(5000, 5000), Size(1000, 1000))
font = Font("Arial", 10.0, FontStyle.BOLD | FontStyle.UNDERLINE)
graphics.draw_string(font.name + " " + str(font.size) + " " + str(font.style), font, Color.brown, 10, 10)
graphics.draw_string("some text", font, Color.brown, 10, 30)
font = Font("Arial", 24.0, FontStyle.ITALIC | FontStyle.STRIKEOUT)
graphics.draw_string(font.name + " " + str(font.size) + " " + str(font.style), font, Color.brown, 20, 50)
graphics.draw_string("some text", font, Color.brown, 20, 80)
with graphics.end_recording() as image:
	path = os.path.join(get_output_dir(), "Fonts.emf")
	image.save(path, EmfOptions())

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(path)
	
print("Finished example SaveEmfGraphics")
