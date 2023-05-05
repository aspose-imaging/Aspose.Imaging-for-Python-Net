# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging.fileformats.psd import CompressionMethod, ColorModes
from aspose.imaging.imageoptions import PsdOptions
from aspose.imaging.sources import FileCreateSource
from aspose.imaging import Graphics, Color, Rectangle, Image, Pen, ColorPalette
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
data_dir = os.path.join(get_data_root_dir(), 'psd')
print("Running example CreateIndexedPSDFiles")
output_file = os.path.join(get_output_dir(), "Newsample_out.psd")
output_file2 = os.path.join(get_output_dir(), "CreateIndexedPSDFiles_out.psd")
# Create an instance of PsdOptions and set it's properties
with PsdOptions() as create_options:
	create_options.source = FileCreateSource(output_file, False)
	create_options.color_mode = ColorModes.INDEXED
	create_options.version = 5
	# Create a new color palette having RGB colors, Set Palette property & compression method
	palette_entries = [Color.red, Color.green, Color.blue]
	create_options.palette = ColorPalette.create_with_colors(palette_entries)
	create_options.compression_method = CompressionMethod.RLE
	# Create a new PSD with PsdOptions created previously
	with Image.create(create_options, 500, 500) as psd:
		# Draw some graphics over the newly created PSD
		graphics = Graphics(psd)
		graphics.clear(Color.white)
		graphics.draw_ellipse(Pen(Color.red, 6), Rectangle(0, 0, 400, 400))
		psd.save(output_file2)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_file)
	os.remove(output_file2)

print("Finished example CreateIndexedPSDFiles")
