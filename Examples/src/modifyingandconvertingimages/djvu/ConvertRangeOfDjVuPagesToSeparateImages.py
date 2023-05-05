# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image, IntRange
from aspose.imaging.fileformats.djvu import DjvuImage
from aspose.imaging.imageoptions import BmpOptions, DjvuMultiPageOptions
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
print("Running example ConvertRangeOfDjVuPagesToSeparateImages")

# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), 'djvu')

# Load a DjVu image
with aspycore.as_of(Image.load(os.path.join(data_dir, "Sample.djvu")), DjvuImage) as image:
	# Create an instance of BmpOptions and Set BitsPerPixel for resultant images
	export_options = BmpOptions()
	export_options.bits_per_pixel = 32
	# Create an instance of IntRange and initialize it with range of pages to be exported
	range_ = IntRange(0, 2)
	counter = 0
	for it in range_.range:
		# Save each page in separate file, as BMP do not support layering
		export_options.multi_page_options = DjvuMultiPageOptions(it)
		out_file = os.path.join(get_output_dir(), f"{counter}_out.bmp")
		counter += 1
		image.save(out_file, export_options)

		if 'SAVE_OUTPUT' not in os.environ:
			os.remove(out_file)

print("Finished example ConvertRangeOfDjVuPagesToSeparateImages")
