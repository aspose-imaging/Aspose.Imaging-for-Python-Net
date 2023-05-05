import aspose.pycore as aspycore
from aspose.imaging import Image, ColorPaletteHelper
from aspose.imaging.fileformats.bmp import BitmapCompression
from aspose.imaging.imageoptions import BmpOptions
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
print("Running example BmpRLE4")
data_dir = os.path.join(get_data_root_dir(), "bmp")
out_file = os.path.join(get_output_dir(), "output.bmp")
with Image.load(os.path.join(data_dir, "Rle4.bmp")) as image:
	options = BmpOptions()
	options.compression = BitmapCompression.RLE4
	options.bits_per_pixel = 4
	options.palette = ColorPaletteHelper.create_4_bit()
	image.save(out_file, options)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)
	
print("Finished example BmpRLE4")
