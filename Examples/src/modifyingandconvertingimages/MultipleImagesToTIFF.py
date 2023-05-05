import aspose.pycore as aspycore
from aspose.imaging import Image, RasterImage, ResizeType
from aspose.imaging.fileformats.tiff import TiffImage, TiffFrame
from aspose.imaging.fileformats.tiff.enums import TiffExpectedFormat
from aspose.imaging.imageoptions import TiffOptions
from aspose.imaging.sources import StreamSource
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
data_dir = os.path.join(get_data_root_dir(), 'Multipage')
output_path = os.path.join(get_output_dir(), "output.tiff")

page = 0
with Image.load(os.path.join(data_dir, "elephant.png")) as temp_image:
	width = 500
	height = 500
	width = temp_image.width
	height = temp_image.height
	tiff_options = TiffOptions(TiffExpectedFormat.DEFAULT)
	tiff_options.source = StreamSource()
	# Create an instance of Image and initialize it with instance of BmpOptions by calling Create method
	with aspycore.as_of(Image.create(tiff_options, width, height), TiffImage) as tiff_image:
		# do some image processing
		files = os.listdir(data_dir)
		index = 0
		for file in files:
			if not file.lower().endswith(".img"):
				continue
			with Image.load(os.path.join(data_dir, file)) as input_image:
				input_image.resize(width, height, ResizeType.NEAREST_NEIGHBOUR_RESAMPLE)
				# var frame = TiffImage.ActiveFrame;
				if index > 0:
					newframe = TiffFrame(tiff_options, width, height)
					tiff_image.add_frame(newframe)
					cnt = tiff_image.page_count

				frame = tiff_image.frames[index]
				as_raster_image = (aspycore.as_of(input_image, RasterImage))
				frame.save_pixels(frame.bounds,
								  as_raster_image.load_pixels(input_image.bounds))
				index += 1

		# save all changes
		tiff_image.save(output_path)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_path)
