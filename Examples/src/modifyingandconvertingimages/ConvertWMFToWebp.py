import aspose.pycore as aspycore
from aspose.imaging import Image, Color
from aspose.imaging.imageoptions import WmfRasterizationOptions, WebPOptions
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
out_file = os.path.join(get_output_dir(), "ConvertWMFToWebp_out.webp")
print("Running example ConvertWMFToWebp")
# Load an existing WMF image
with Image.load(os.path.join(data_dir, "input.wmf")) as image:
	# Calculate new Webp image height
	k = (image.width * 1.00) / image.height
	# Create an instance of EmfRasterizationOptions class and set different properties
	wmf_rasterization = WmfRasterizationOptions()
	wmf_rasterization.background_color = Color.white_smoke
	wmf_rasterization.page_width = 400.0
	wmf_rasterization.page_height = round(400.0 / k, 0)
	wmf_rasterization.border_x = 5.0
	wmf_rasterization.border_y = 10.0
	# Create an instance of WebPOptions class and provide rasterization option
	image_options = WebPOptions()
	image_options.vector_rasterization_options = wmf_rasterization
	# Call the save method, provide output path and WebPOptions to convert the WMF file to Webp and save the output
	image.save(out_file, image_options)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example ConvertWMFToWebp")
