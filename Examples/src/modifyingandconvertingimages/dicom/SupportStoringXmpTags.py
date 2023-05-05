# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import *
from aspose.imaging.xmp import *
from aspose.imaging.xmp.schemas.dicom import DicomPackage
from aspose.imaging.fileformats.dicom import DicomImage
from aspose.imaging.imageoptions import DicomOptions
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
print("Running example SupportStoringXmpTags")
# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), 'dicom')
output_file = os.path.join(get_output_dir(), "output.dcm")
with aspycore.as_of(Image.load(os.path.join(data_dir, "file.dcm")), DicomImage) as image:
	xmp_packet_wrapper = XmpPacketWrapper()
	dicom_package = DicomPackage()
	dicom_package.set_equipment_institution("Test Institution")
	dicom_package.set_equipment_manufacturer("Test Manufacturer")
	dicom_package.set_patient_birth_date("19010101")
	dicom_package.set_patient_id("010101")
	dicom_package.set_patient_name("Test Name")
	dicom_package.set_patient_sex("M")
	dicom_package.set_series_date_time("19020202")
	dicom_package.set_series_description("Test Series Description")
	dicom_package.set_series_modality("Test Modality")
	dicom_package.set_series_number("01")
	dicom_package.set_study_date_time("19030303")
	dicom_package.set_study_description("Test Study Description")
	dicom_package.set_study_id("02")
	dicom_package.set_study_physician("Test Physician")
	xmp_packet_wrapper.add_package(dicom_package)
	obj_init = DicomOptions()
	obj_init.xmp_data = xmp_packet_wrapper
	image.save(output_file, obj_init)
	with aspycore.as_of(Image.load(output_file), DicomImage) as image_saved:
		original_dicom_info = image.file_info.dicom_info
		image_saved_dicom_info = image_saved.file_info.dicom_info
		tags_count_diff = abs(image_saved_dicom_info.length - original_dicom_info.length)
		print("tags_count_diff", tags_count_diff)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_file)
	
print("Finished example SupportStoringXmpTags")
