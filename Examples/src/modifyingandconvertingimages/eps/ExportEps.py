import aspose.pycore as aspycore
from aspose.imaging import Image, PdfComplianceVersion
from aspose.imaging.imageoptions import TiffOptions, PdfOptions
from aspose.imaging.fileformats.tiff.enums import TiffExpectedFormat
from aspose.imaging.fileformats.eps import EpsImage, EpsPreviewFormat, EpsBinaryImage
from aspose.imaging.fileformats.pdf import PdfCoreOptions
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
print("Running example ExportEps")
# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), 'eps')
out_file1 = os.path.join(get_output_dir(), "Sample.pdf")
out_file2 = os.path.join(get_output_dir(), "Sample1.tiff")
out_file3 = os.path.join(get_output_dir(), "Sample2.tiff")
with aspycore.as_of(Image.load(os.path.join(data_dir, "Sample.eps")), EpsImage) as image:
	obj_init = PdfCoreOptions()
	obj_init.pdf_compliance = PdfComplianceVersion.PDF_A1B
	options = PdfOptions()
	options.pdf_core_options = obj_init
	image.preview_to_export = EpsPreviewFormat.POST_SCRIPT_RENDERING
	image.save(out_file1, options)

with aspycore.as_of(Image.load(os.path.join(data_dir, "Sample.eps")), EpsBinaryImage) as image:
	# Tiff image export options
	options = TiffOptions(TiffExpectedFormat.TIFF_JPEG_RGB)
	# The first way:
	image.tiff_preview.save(out_file2, options)
	# The second way:
	image.preview_to_export = EpsPreviewFormat.TIFF
	image.save(out_file3, options)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file1)
	os.remove(out_file2)
	os.remove(out_file3)

print("Finished example ExportEps")
