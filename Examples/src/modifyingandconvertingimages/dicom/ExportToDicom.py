# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.fileformats.dicom import DicomImage
from aspose.imaging.imageoptions import PngOptions
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
print("Running example ExportToDicom")
data_dir = os.path.join(get_data_root_dir(), 'dicom')
file_name = "sample.jpg"
input_file_name_single = os.path.join(data_dir, file_name)
input_file_name_multipage = os.path.join(data_dir, "multipage.tif")
output_file_name_single_dcm = os.path.join(get_output_dir(), "output.dcm")
output_file_name_multipage_dcm = os.path.join(get_output_dir(), "outputMultipage.dcm")
# The next code sample converts JPEG image to DICOM file format
with Image.load(input_file_name_single) as image:
	image.save(output_file_name_single_dcm, DicomOptions())

# DICOM format supports multipage images. You can convert GIF or TIFF images to DICOM in the same way as JPEG images
with Image.load(input_file_name_multipage) as image:
	image.save(output_file_name_multipage_dcm, DicomOptions())

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_file_name_single_dcm)
	os.remove(output_file_name_multipage_dcm)
	
print("Finished example ExportToDicom")
