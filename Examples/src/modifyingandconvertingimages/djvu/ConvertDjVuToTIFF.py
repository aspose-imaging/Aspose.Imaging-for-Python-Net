# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.fileformats.djvu import DjvuImage
from aspose.imaging.fileformats.tiff.enums import TiffExpectedFormat
from aspose.imaging.imageoptions import TiffOptions, DjvuMultiPageOptions
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
print("Running example ConvertDjVuToTIFF")

# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), 'djvu')
out_file = os.path.join(data_dir, "ConvertDjVuToTIFFFormat_out.tiff")
# Load a DjVu image
with aspycore.as_of(Image.load(os.path.join(data_dir, "Sample.djvu")), DjvuImage) as image:
	# Create an instance of TiffOptions & use preset options for Black n While with Deflate compression
	export_options = TiffOptions(TiffExpectedFormat.TIFF_DEFLATE_BW)
	# Initialize the DjvuMultiPageOptions and Call Save method while passing instance of TiffOptions
	export_options.multi_page_options = DjvuMultiPageOptions()
	image.save(out_file, export_options)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)
	
print("Finished example ConvertDjVuToTIFF")
