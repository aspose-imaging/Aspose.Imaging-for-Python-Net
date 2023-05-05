import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.fileformats.jpeg import JpegImage
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
data_dir = os.path.join(get_data_root_dir(), 'jpeg')
print("Running example JpegSavedQualityEstimation")
with aspycore.as_of(Image.load(os.path.join(data_dir, "test.jpg")), JpegImage) as image:
	is_not_default_quality = image.jpeg_options.quality != 75
	print("is_not_default_quality", is_not_default_quality)

print("Finished example JpegSavedQualityEstimation")
