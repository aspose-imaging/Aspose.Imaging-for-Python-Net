# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.fileformats.jpeg import JpegImage
import os
import inspect


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
print("Running example ReadAllEXIFTags")
with aspycore.as_of(Image.load(os.path.join(data_dir, "aspose-logo.jpg")), JpegImage) as image:
	exif_data = image.exif_data
	if exif_data is not None:
		type_ = exif_data.get_type()
		print("type =", type_)
		print("exif_data =", exif_data)

for i in inspect.getmembers(exif_data):
	# to remove private and protected
    # functions
    if not i[0].startswith('_'):
        # To remove other methods that
        # does not start with a underscore
        if not inspect.ismethod(i[1]):
            result = getattr(exif_data, i[0])
            if result is not None and type(result) in (int, str, list):
                print(i[0], result)

print("Finished example ReadAllEXIFTags")
