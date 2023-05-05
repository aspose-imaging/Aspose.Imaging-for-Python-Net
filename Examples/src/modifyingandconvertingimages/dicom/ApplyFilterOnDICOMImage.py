# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging.fileformats.dicom import DicomImage
from aspose.imaging.imageoptions import BmpOptions
from aspose.imaging.imagefilters.filteroptions import MedianFilterOptions
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
data_dir = os.path.join(get_data_root_dir(), 'dicom')
out_file = os.path.join(get_output_dir(), 'ApplyFilterOnDICOMImage_out.bmp')
print("Running example ApplyFilterDicom")
with open(os.path.join(data_dir, "file.dcm"), "rb") as file_stream:
	with DicomImage(file_stream) as image:
		# Supply the filters to DICOM image and Save the results to output path.
		image.filter(image.bounds, MedianFilterOptions(8))
		image.save(out_file, BmpOptions())

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example ApplyFilterDicom")
