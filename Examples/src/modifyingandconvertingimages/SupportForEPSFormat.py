import aspose.pycore as aspycore
from aspose.imaging.imageoptions import PngOptions
from aspose.imaging.fileformats.eps import *
from aspose.imaging.fileformats.eps.consts import *
from aspose.imaging import Image
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
output_path = os.path.join(get_output_dir(), "anyEpsFile.png")
print("Running example SupportForEPSFormat")
with aspycore.as_of(Image.load(os.path.join(data_dir, "sample.eps")),
					EpsImage) as eps_image:
	# check if EPS image has any raster preview to proceed (for now only raster preview is supported)
	if eps_image.has_raster_preview:
		if eps_image.photoshop_thumbnail is not None:
			pass

		if eps_image.eps_type == EpsType.INTERCHANGE:
			# Get EPS Interchange subformat instance
			eps_interchange_image = aspycore.as_of(eps_image, EpsInterchangeImage)
			if eps_interchange_image.raster_preview is not None:
				print("Has raster_preview")
				pass
		else:
			# Get EPS Binary subformat instance
			eps_binary_image = aspycore.as_of(eps_image, EpsBinaryImage)
			if eps_binary_image.tiff_preview is not None:
				print("Has tiff_preview")
				pass

			if eps_binary_image.wmf_preview is not None:
				print("Has wmf_preview")
				pass

		# export EPS image to PNG (by default, best available quality preview is used for export)
		eps_image.save(output_path, PngOptions())

if 'SAVE_OUTPUT' not in os.environ:
	if os.path.exists(output_path):
		os.remove(output_path)

print("Finished example SupportForEPSFormat")
