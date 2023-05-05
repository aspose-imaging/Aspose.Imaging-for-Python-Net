# GROUP: TEST_FILE_FORMATS
from aspose.imaging.exif import *
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

# Example code:
# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), 'jpeg')
print("Running example ReadJpegEXIFTags")
with aspycore.as_of(Image.load(os.path.join(data_dir, "aspose-logo.jpg")), JpegImage) as image:
	exif_data = image.exif_data
	print("Camera Owner Name: ", exif_data.camera_owner_name)
	print("Aperture Value: ", exif_data.aperture_value)
	print("Orientation: ", exif_data.orientation)
	print("Focal Length: ", exif_data.focal_length)
	print("Compression: ", exif_data.compression)

print("Finished example ReadJpegEXIFTags")
