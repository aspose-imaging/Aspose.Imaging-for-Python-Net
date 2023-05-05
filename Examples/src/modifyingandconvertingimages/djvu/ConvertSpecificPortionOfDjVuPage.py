# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Rectangle, Image
from aspose.imaging.fileformats.djvu import DjvuImage
from aspose.imaging.fileformats.png import PngColorType
from aspose.imaging.imageoptions import PngOptions, DjvuMultiPageOptions
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
print("Running example ConvertSpecificPortionOfDjVuPage")

# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), 'djvu')
out_file = os.path.join(data_dir, "ConvertSpecificPortionOfDjVuPage_out.png")
# Load a DjVu image
with aspycore.as_of(Image.load(os.path.join(data_dir, "Sample.djvu")), DjvuImage) as image:
	# Create an instance of PngOptions and Set ColorType to Grayscale
	export_options = PngOptions()
	export_options.color_type = PngColorType.GRAYSCALE
	# Create an instance of Rectangle and specify the portion on DjVu page
	export_area = Rectangle(0, 0, 500, 500)
	# Specify the DjVu page index and Initialize an instance of DjvuMultiPageOptions while passing index of DjVu page index and instance of Rectangle covering the area to be exported               
	export_page_index = 2
	export_options.multi_page_options = DjvuMultiPageOptions(export_page_index, export_area)
	image.save(out_file, export_options)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example ConvertSpecificPortionOfDjVuPage")
