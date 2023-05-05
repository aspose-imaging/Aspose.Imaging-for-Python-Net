# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import *
from aspose.imaging.fileformats.tiff.enums import *
from aspose.imaging.imageoptions import *
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

def create_page_options(image):
	# Create page rasterization options for each page in the image
	options = []
	for page in image.pages:
		# Create the instance of rasterization options
		option = CmxRasterizationOptions()
		# Set the page size
		option.page_size = aspycore.cast(SizeF, page.size)
		options.append(option)
	return options


print("Running example CmxToTiffExample")
# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), 'cmx')
input_file = os.path.join(data_dir, "MultiPage2.cmx")
out_file = os.path.join(get_output_dir(), "MultiPage2.cmx.tiff")
with aspycore.as_of(Image.load(input_file), VectorMultipageImage) as image:
	# Create page rasterization options
	page_options = create_page_options(image)
	# Create TIFF options
	obj_init = MultiPageOptions()
	obj_init.page_rasterization_options = page_options
	options = TiffOptions(TiffExpectedFormat.TIFF_DEFLATE_RGB)
	options.multi_page_options = obj_init
	# Export image to TIFF format
	image.save(out_file, options)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example CmxToTiffExample")
