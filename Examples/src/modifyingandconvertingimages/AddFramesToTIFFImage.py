import aspose.pycore as aspycore
from aspose.imaging.fileformats.tiff import TiffImage, TiffFrame
from aspose.imaging.fileformats.tiff.enums import TiffExpectedFormat, \
	TiffCompressions, TiffPhotometrics
from aspose.imaging.imageoptions import TiffOptions
from aspose.imaging.sources import StreamSource
from aspose.imaging import Image, RasterImage, ResizeType
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
print("Running example AddFramesToTIFFImage")
# To get proper output please apply a valid Aspose.Imaging License. You can purchase full license or get 30 day temporary license from https://purchase.aspose.com/buy ");
output_settings = TiffOptions(TiffExpectedFormat.DEFAULT)
output_settings.bits_per_sample = [1]
output_settings.compression = TiffCompressions.CCITT_FAX3
output_settings.photometric = TiffPhotometrics.MIN_IS_WHITE
output_settings.source = StreamSource() # in memory
new_width = 500
new_height = 500
path = os.path.join(get_output_dir(), "AddFramesToTIFFImage_out.tif")
with aspycore.as_of(Image.create(output_settings, new_width, new_height), TiffImage) as tiff_image:
	index = 0
	for file in os.listdir(data_dir):
		if not file.lower().endswith((".jpg", ".jpeg")):
			continue
		with aspycore.as_of(Image.load(os.path.join(data_dir, file)),
							RasterImage) as ri:
			ri.resize(new_width, new_height, ResizeType.NEAREST_NEIGHBOUR_RESAMPLE)
			
			if index > 0:
				frame = TiffFrame(TiffOptions(output_settings), new_width, new_height)
			else:
				frame = tiff_image.active_frame

			frame.save_pixels(frame.bounds, ri.load_pixels(ri.bounds))
			if index > 0:
				tiff_image.add_frame(frame)

			index += 1

	tiff_image.save(path)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(path)

print("Finished example AddFramesToTIFFImage")
