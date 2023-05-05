import aspose.pycore as aspycore
from aspose.imaging import Image, Rectangle, Color
from aspose.imaging.imageoptions import WmfRasterizationOptions,PngOptions
from aspose.imaging.fileformats.wmf import WmfImage
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
out_file = os.path.join(get_output_dir(), "ConvertWMFToPNG_out.png")
print("Running example CroppingWMFFileWhileConvertingtoPNG")
# Load an existing WMF image
with aspycore.as_of(Image.load(os.path.join(data_dir, "file.wmf")), WmfImage) as image:
	image.crop(Rectangle(10, 10, 70, 70))
	# Create an instance of EmfRasterizationOptions class and set different properties
	wmf_rasterization = WmfRasterizationOptions()
	wmf_rasterization.background_color = Color.white_smoke
	wmf_rasterization.page_width = 1000.0
	wmf_rasterization.page_height = 1000.0
	# Create an instance of PngOptions class and provide rasterization option
	image_options = PngOptions()
	image_options.vector_rasterization_options = wmf_rasterization
	# Call the save method, provide output path and PngOptions to convert the cropped WMF file to PNG and save the output
	image.save(out_file, image_options)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example CroppingWMFFileWhileConvertingtoPNG")
