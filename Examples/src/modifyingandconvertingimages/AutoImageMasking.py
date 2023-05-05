# GROUP: ADDITIONAL_FEATURES
import aspose.pycore as aspycore
from aspose.imaging import Image, RasterImage
from aspose.imaging.imageoptions import PngOptions
from aspose.imaging.sources import StreamSource
from aspose.imaging.fileformats.png import PngColorType
from aspose.imaging.masking import ImageMasking
from aspose.imaging.masking.options import MaskingOptions, AutoMaskingArgs, \
	SegmentationMethod
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

print("Running example AutoImageMasking")

source_file_name = os.path.join(data_dir, "Colored by Faith_small.png")
input_points_file_name = os.path.join(data_dir, "Colored by Faith_small.dat")
output_file_name = os.path.join(get_output_dir(), "Colored by Faith_small_auto.png")


# function

def read_int32(stream):
	return int.from_bytes(stream.read(4), byteorder='big', signed=True)


def fill_input_points(file_path, auto_masking_args):
	with open(file_path, "rb") as stream:
		has_object_rectangles = read_int32(stream) != 0
		has_object_points = read_int32(stream) != 0
		auto_masking_args.objects_rectangles = None
		auto_masking_args.objects_points = None
		if has_object_rectangles:
			length = read_int32(stream)
			rects = [None] * length
			for i in range(length):
				# firstly Y
				y = read_int32(stream)
				# secondly X
				x = read_int32(stream)
				# width
				width = read_int32(stream)
				# height
				height = read_int32(stream)
				rects[i] = Rectangle(x, y, width, height);

			auto_masking_args.objects_rectangles = rects
		if has_object_points:
			length = read_int32(stream)
			points = [None] * length
			for i in range(length):
				il = read_int32(stream)
				sub_points = [None] * il
				points[i] = sub_points
				for j in range(il):
					x = read_int32(stream)
					y = read_int32(stream)
					sub_points[j] = Point(x, y)
			auto_masking_args.objects_points = points


# start the example
masking_args = AutoMaskingArgs()
fill_input_points(input_points_file_name, masking_args)

with aspycore.as_of(Image.load(source_file_name), RasterImage) as image:
	png_opt = PngOptions()
	png_opt.color_type = PngColorType.TRUECOLOR_WITH_ALPHA
	png_opt.source = StreamSource()
	masking_options = MaskingOptions()
	masking_options.method = SegmentationMethod.GRAPH_CUT
	masking_options.args = masking_args
	masking_options.decompose = False
	masking_options.export_options = png_opt
	with ImageMasking(image).decompose(masking_options) as masking_results:
		with masking_results[1].get_image() as result_image:
			result_image.save(output_file_name)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_file_name)

print("Finished example AutoImageMasking")
