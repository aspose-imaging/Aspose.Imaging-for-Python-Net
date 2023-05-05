import aspose.pycore as aspycore
from aspose.imaging import *
from aspose.imaging.fileformats.tiff import *
from aspose.imaging.imageoptions import *
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

print("Running example SetDPIInExportedTiff")
# The path to the documents directory.
file_path = os.path.join(get_data_root_dir(), 'tiff')
out_file = os.path.join(get_output_dir(), "result.pdf")
with aspycore.as_of(Image.load(os.path.join(file_path, "AFREY-Original.tif")),
					TiffImage) as image:
	pdf_options = PdfOptions()
	pdf_options.resolution_settings = ResolutionSetting(image.horizontal_resolution,
														image.vertical_resolution)
	image.save(out_file, pdf_options)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example SetDPIInExportedTiff")
