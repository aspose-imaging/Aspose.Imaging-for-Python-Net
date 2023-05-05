import aspose.pycore as aspycore
from aspose.imaging import Image, FileFormat, RasterImage, ColorPaletteHelper, \
	ResolutionSetting, LoadOptions
from aspose.imaging.imageoptions import *
from aspose.imaging.fileformats.tiff.enums import *
from aspose.imaging.fileformats.png import PngColorType
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
file_path = os.path.join(get_data_root_dir(), 'png')

print("Running example ConvertTo1BitPng")


def export_image(source_image_file_path, output_image_file_path, target_format, rotate_angle, rotate_flip_type):
	obj_init = LoadOptions()
	obj_init.buffer_size_hint = 450 # 450 MB limit
	with aspycore.as_of(Image.load(source_image_file_path, obj_init),
						RasterImage) as image:

		if rotate_angle != 0:
			image.rotate(rotate_angle)

		if rotate_flip_type is not None:
			image.rotate_flip(rotate_flip_type)

		bits_per_pixel = image.bits_per_pixel
		bit_depth = 1 if bits_per_pixel == 1 else 8 if bits_per_pixel < 8 else 24
		export_options = None
		obj_init5 = TiffOptions(TiffExpectedFormat.DEFAULT)
		obj_init5.photometric = TiffPhotometrics.MIN_IS_WHITE
		obj_init5.palette = ColorPaletteHelper.create_monochrome()
		obj_init5.compression = TiffCompressions.CCITT_FAX4
		obj_init5.bits_per_sample = [1]
		obj_init6 = TiffOptions(TiffExpectedFormat.DEFAULT)
		obj_init6.photometric = TiffPhotometrics.MIN_IS_WHITE
		obj_init6.palette = ColorPaletteHelper.create_8_bit_grayscale(True)
		obj_init6.compression = TiffCompressions.DEFLATE
		obj_init6.bits_per_sample = [8]
		obj_init7 = TiffOptions(TiffExpectedFormat.DEFAULT)
		obj_init7.photometric = TiffPhotometrics.RGB
		obj_init7.compression = TiffCompressions.JPEG
		bits_per_sample = (bit_depth // 3)
		obj_init7.bits_per_sample = [bits_per_sample, bits_per_sample, bits_per_sample]

		tmp_switch = target_format
		if tmp_switch == FileFormat.JPEG:
			export_options = JpegOptions()
			if bit_depth <= 8:
				export_options.palette = ColorPaletteHelper.create_8_bit_grayscale(True)
				export_options.color_type = JpegCompressionColorMode.GRAYSCALE
		elif tmp_switch == FileFormat.PNG:
			export_options = PngOptions()
			export_options.progressive = False
			if bit_depth <= 8:
				export_options.color_type = PngColorType.GRAYSCALE
				export_options.bit_depth = bit_depth
		elif tmp_switch == FileFormat.TIFF:
			tmp_switch2 = bit_depth
			if tmp_switch2 == 1:
				export_options = obj_init5
			elif tmp_switch2 == 8:
				export_options = obj_init6
			else:
				export_options = obj_init7
		else:
			return
	
		export_options.buffer_size_hint = 2056 # MB limit
		export_options.resolution_settings = ResolutionSetting(50, 50)
		image.save(output_image_file_path, export_options)
	
	if 'SAVE_OUTPUT' not in os.environ:
		os.remove(output_image_file_path)

# Run
input_file_path = "00020.png"
output_file_path = "00020_png.png"
export_image(os.path.join(file_path, input_file_path), os.path.join(get_output_dir(), output_file_path), FileFormat.PNG, 0, None)
print("Finished example ConvertTo1BitPng")
