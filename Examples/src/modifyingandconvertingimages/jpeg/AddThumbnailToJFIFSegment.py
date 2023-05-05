# GROUP: TEST_FILE_FORMATS
from aspose.imaging.fileformats.jpeg import JpegImage, JFIFData
import os


# Initialization
def get_data_root_dir_local():
	if 'BASE_DIR' in os.environ:
		return os.environ["BASE_DIR"]
	return "."


if 'get_output_dir' not in dir():
	get_output_dir = get_data_root_dir_local

# Example code:
# The path to the documents directory.
out_file = os.path.join(get_output_dir(), 'jfif_thumbnail_out.jpeg')
print("Running example AddThumbnailToJFIFSegment")
with JpegImage(100, 100) as thumbnail_image:
	with JpegImage(1000, 1000) as image:
		image.jfif = JFIFData()
		image.jfif.thumbnail = thumbnail_image
		image.save(out_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example AddThumbnailToJFIFSegment")
