# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image, ResolutionSetting, ResolutionUnit
from aspose.imaging.fileformats.tiff import TiffImage
from aspose.imaging.imageoptions import JpegOptions
from aspose.imaging.fileformats.tiff.enums import TiffResolutionUnits
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

print("Running example ConvertTIFFToJPEG")
with aspycore.as_of(Image.load(os.path.join(data_dir, "source2.tif")), 
					TiffImage) as tiff_image:
	i = 0
	for tiff_frame in tiff_image.frames:
		save_options = JpegOptions()
		save_options.resolution_settings = ResolutionSetting(tiff_frame.horizontal_resolution, tiff_frame.vertical_resolution)
		frm_opts = tiff_frame.frame_options
		if frm_opts is not None:
			# Set the resolution unit explicitly.
			tmp_switch = frm_opts.resolution_unit
			if tmp_switch == TiffResolutionUnits.NONE:
				save_options.resolution_unit = ResolutionUnit.NONE
			elif tmp_switch == TiffResolutionUnits.INCH:
				save_options.resolution_unit = ResolutionUnit.INCH
			elif tmp_switch == TiffResolutionUnits.CENTIMETER:
				save_options.resolution_unit = ResolutionUnit.CM
			else:
				raise AssertionError("Wrong resolution unit!")

		file_name = f"source2.tif.frame.{i}.{save_options.resolution_unit}.jpg"
		i += 1
		out_file = os.path.join(get_output_dir(), file_name)
		tiff_frame.save(out_file, save_options)

		if 'SAVE_OUTPUT' not in os.environ:
			os.remove(out_file)

print("Finished example ConvertTIFFToJPEG")
