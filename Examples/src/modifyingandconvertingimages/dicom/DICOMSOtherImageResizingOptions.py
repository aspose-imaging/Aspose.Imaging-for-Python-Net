# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging.fileformats.dicom import DicomImage
from aspose.imaging.imageoptions import BmpOptions
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
print("Running example DICOMSOtherImageResizingOptions")
# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), 'dicom')
out_file1 = os.path.join(get_output_dir(), 'DICOMSOtherImageResizingOptions_out.bmp')
out_file2 = os.path.join(get_output_dir(), 'DICOMSOtherImageResizingOptions1_out.bmp')
with open(os.path.join(data_dir, "file.dcm"), "rb") as file_stream:
	with DicomImage(file_stream) as image:
		image.resize_height_proportionally(100, ResizeType.ADAPTIVE_RESAMPLE)
		image.save(out_file1, BmpOptions())

with open(os.path.join(data_dir, "file.dcm"), "rb") as file_stream:
	with DicomImage(file_stream) as image1:
		image1.resize_width_proportionally(150, ResizeType.ADAPTIVE_RESAMPLE)
		image1.save(out_file2, BmpOptions())

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file1)
	os.remove(out_file2)

print("Finished example DICOMSOtherImageResizingOptions")
