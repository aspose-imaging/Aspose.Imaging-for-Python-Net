import aspose.pycore as aspycore
from aspose.imaging import Image, RasterImage
from aspose.imaging.imageoptions import TiffOptions
from aspose.imaging.fileformats.tiff import TiffImage
from aspose.imaging.fileformats.tiff.enums import TiffExpectedFormat, TiffPhotometrics
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
out_file = os.path.join(get_output_dir(), "AlignHorizontalAndVeticalResolutionsOfImage_out.tiff")
print("Running example AlignHorizontalAndVeticalResolutionsOfImage")
# Load an image and convert the image instance to TiffImage
with aspycore.as_of(Image.load(os.path.join(data_dir, "SampleTiff1.tiff")), TiffImage) as image:
	# Call the align resolution method and Save the results to output path.
	image.align_resolutions()
	image.save(out_file)
	
	for frame in image.frames:
		# All resolutions after alignment must be equal
		print("Horizontal and vertical resolutions are equal:", frame.vertical_resolution == frame.horizontal_resolution)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example AlignHorizontalAndVeticalResolutionsOfImage")
