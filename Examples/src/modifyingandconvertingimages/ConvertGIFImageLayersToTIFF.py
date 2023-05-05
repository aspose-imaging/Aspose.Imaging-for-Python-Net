import aspose.pycore as aspycore
from aspose.imaging.fileformats.gif import GifImage
from aspose.imaging.fileformats.gif.blocks import GifFrameBlock
from aspose.imaging.fileformats.tiff.enums import TiffExpectedFormat
from aspose.imaging.imageoptions import TiffOptions
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
print("Running example ConvertGIFImageLayersToTIFF")
# Load a GIF image and Convert the image to GIF image
with Image.load(os.path.join(data_dir, "asposelogo.gif")) as obj_image:
	gif = aspycore.as_of(obj_image, GifImage)
	i = 0
	# Iterate through array of blocks in the GIF image
	for block in gif.blocks:
		# Check if gif block is then ignore it
		if not aspycore.is_assignable(block, GifFrameBlock):
			continue
		# Convert block to GifFrameBlock class instance
		gif_block = aspycore.as_of(block, GifFrameBlock)

		out_file = os.path.join(get_output_dir(), f"asposelogo{i}_out.tif")
		i += 1
		# Create an instance of TIFF Option class and Save the GIFF block as TIFF image
		obj_tiff = TiffOptions(TiffExpectedFormat.DEFAULT)
		gif_block.save(out_file, obj_tiff)

		if 'SAVE_OUTPUT' not in os.environ:
			os.remove(out_file)

print("Finished example ConvertGIFImageLayersToTIFF")
