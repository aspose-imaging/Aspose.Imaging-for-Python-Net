# GROUP: MODIFYING_AND_CONVERTING_IMAGES
from aspose.pycore import as_of, is_assignable
from aspose.imaging.fileformats.dicom import DicomImage
from aspose.imaging import Image
from aspose.imaging.exif import IHasExifData
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

# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), 'dicom')
out_file1 = os.path.join(get_output_dir(), 'output.dcm')
out_file2 = os.path.join(get_output_dir(), 'output_remove.dcm')
out_file3 = os.path.join(get_output_dir(), 'output_modify.dcm')

def exportWithMetadata(inputPath, outputPath, exportOptions):
	with Image.load(inputPath) as image:
		exportOptions.keep_metadata = True
		image.save(outputPath, exportOptions)

def removeMetadata(inputPath, outputPath, exportOptions):
	with Image.load(inputPath) as image:
		image.remove_metadata()
		image.save(outputPath, exportOptions)

def modifyMetada(inputPath, outputPath, exportOptions):
	with Image.load(inputPath) as image:
		if is_assignable(image, IHasExifData):
			hasExif = as_of(image, IHasExifData)
			if hasExif.exif_data is not None:
				hasExif.exif_data.user_comment = f"Modified at {datetime.now()}"
			exportOptions.keep_metadata = True
			
		image.save(outputPath, exportOptions)

exportWithMetadata(os.path.join(data_dir, "file.dcm"), out_file1, DicomOptions())
removeMetadata(os.path.join(data_dir, "file.dcm"), out_file2, DicomOptions())
modifyMetada(os.path.join(data_dir, "file.dcm"), out_file3, DicomOptions())

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file1)
	os.remove(out_file2)
	os.remove(out_file3)
