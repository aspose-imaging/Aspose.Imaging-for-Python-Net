import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.imageoptions import WmfRasterizationOptions, SvgOptions
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
out_file = os.path.join(get_output_dir(), "ConvertWMFMetaFileToSVG_out.svg")
print("Running example ConvertWMFMetaFileToSVG")
# Create an instance of Image class by loading an existing .
with Image.load(os.path.join(data_dir, "input.wmf")) as image:
	# Create an instance of EmfRasterizationOptions class.
	options = WmfRasterizationOptions()
	options.page_width = float(image.width)
	options.page_height = float(image.height)
	# Call save method to convert WMF to SVG format by passing output file name and SvgOptions class instance.
	obj_init = SvgOptions()
	obj_init.vector_rasterization_options = options
	image.save(out_file, obj_init)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example ConvertWMFMetaFileToSVG")
