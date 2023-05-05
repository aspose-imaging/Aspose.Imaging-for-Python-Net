import aspose.pycore as aspycore
from aspose.imaging import Image, Color
from aspose.imaging.imageoptions import WmfRasterizationOptions, PngOptions
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
output_path = os.path.join(get_output_dir(), "CreateEMFMetaFileImage_out.png")
print("Running example ResizeWMFFile")
# Load an existing WMF image
with Image.load(os.path.join(data_dir, "input.wmf")) as image:
	# Call the resize method of Image class and width,height values and Calculate new PNG image height
	image.resize(100, 100)
	k = (image.width * 1.00) / image.height
	# Create an instance of WmfRasterizationOptions class and set different properties
	wmf_rasterization = WmfRasterizationOptions()
	wmf_rasterization.background_color = Color.white_smoke
	wmf_rasterization.page_width = 100.0
	wmf_rasterization.page_height = round(100 / k)
	wmf_rasterization.border_x = 5.0
	wmf_rasterization.border_y = 10.0
	# Create an instance of PngOptions class and provide rasterization option
	image_options = PngOptions()
	image_options.vector_rasterization_options = wmf_rasterization
	# Call the save method, provide output path and PngOptions to convert the WMF file to PNG and save the output
	image.save(output_path, image_options)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_path)

print("Finished example ResizeWMFFile")

