# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image, IntRange
from aspose.imaging.fileformats.djvu import DjvuImage
from aspose.imaging.fileformats.pdf import PdfDocumentInfo
from aspose.imaging.imageoptions import PdfOptions, DjvuMultiPageOptions
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
print("Running example ConvertDjVuToPDF")

# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), 'djvu')
out_file = os.path.join(data_dir, "ConvertDjVuToPDFFormat_out.pdf")
# Load a DjVu image
with aspycore.as_of(Image.load(os.path.join(data_dir, "Sample.djvu")), DjvuImage) as image:
	# Create an instance of PdfOptions and Initialize the metadata for Pdf document
	export_options = PdfOptions()
	export_options.pdf_document_info = PdfDocumentInfo()
	# Create an instance of IntRange and initialize it with the range of DjVu pages to be exported
	range_ = IntRange(0, 5)
	# Initialize an instance of DjvuMultiPageOptions with range of DjVu pages to be exported and Save the result in PDF format
	export_options.multi_page_options = DjvuMultiPageOptions(range_)
	image.save(out_file, export_options)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example ConvertDjVuToPDF")
