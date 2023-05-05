# GROUP: TEST_FILE_FORMATS
from aspose.imaging.fileformats.jpeg import JpegImage
from aspose.imaging.exif import JpegExifData
import os


# Initialization
def get_data_root_dir_local():
	if 'BASE_DIR' in os.environ:
		return os.environ["BASE_DIR"]
	return "."


if 'get_output_dir' not in dir():
	get_output_dir = get_data_root_dir_local

# Example code:
# ExStart:AddThumbnailToEXIFSegment
# The path to the documents directory.
out_file = os.path.join(get_output_dir(), 'thumbnail_out.jpg')
print("Running example AddThumbnailToEXIFSegment")
with JpegImage(100, 100) as thumbnail_image:
	with JpegImage(1000, 1000) as image:
		image.exif_data = JpegExifData()
		image.exif_data.thumbnail = thumbnail_image
		image.save(out_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example AddThumbnailToEXIFSegment")
