import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.fileformats.tiff.enums import TiffExpectedFormat
from aspose.imaging.imageoptions import BmpOptions, JpegOptions, PngOptions, \
		TiffOptions
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
out_file1 = os.path.join(get_output_dir(), "_output.bmp")
out_file2 = os.path.join(get_output_dir(), "_output.jpeg")
out_file3 = os.path.join(get_output_dir(), "_output.png")
out_file4 = os.path.join(get_output_dir(), "_output.tiff")
print("Running example ExportImageToDifferentFormats")
# Load an existing image (of type Gif) in an instance of the Image class
with Image.load(os.path.join(data_dir, "sample.gif")) as image:
	# Export to BMP, JPEG, PNG and TIFF file format using the default options
	image.save(out_file1, BmpOptions())
	image.save(out_file2, JpegOptions())
	image.save(out_file3, PngOptions())
	image.save(out_file4, TiffOptions(TiffExpectedFormat.DEFAULT))

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file1)
	os.remove(out_file2)
	os.remove(out_file3)
	os.remove(out_file4)

print("Finished example ExportImageToDifferentFormats")
