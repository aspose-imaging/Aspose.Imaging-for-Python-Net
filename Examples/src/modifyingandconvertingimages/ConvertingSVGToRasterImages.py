import aspose.pycore as aspycore
from aspose.imaging.fileformats.svg import SvgImage
from aspose.imaging.imageoptions import PngOptions
from aspose.imaging import Image
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
out_file = os.path.join(get_output_dir(), "ConvertingSVGToRasterImages_out.png")
print("Running example ConvertingSVGToRasterImages")
# Load the image
with aspycore.as_of(Image.load(os.path.join(data_dir, "aspose_logo.svg")), SvgImage) as image:
	# Create an instance of PNG options and Save the results to disk
	png_options = PngOptions()
	image.save(out_file, png_options)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example ConvertingSVGToRasterImages")
