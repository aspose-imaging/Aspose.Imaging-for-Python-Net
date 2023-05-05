# GROUP: TEST_FILE_FORMATS
from aspose.imaging import Image
from aspose.imaging.fileformats.webp import WebPImage
from aspose.imaging.imageoptions import PdfOptions
from aspose.imaging.fileformats.pdf import PdfDocumentInfo
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
data_dir = os.path.join(get_data_root_dir(), 'WebPImage')
out_file = os.path.join(get_output_dir(), "Animation.pdf")
print("Running example WebPToPdfExample")
input_file = os.path.join(data_dir, "Animation.webp")
with aspycore.as_of(Image.load(input_file), WebPImage) as image:
	options = PdfOptions()
	options.pdf_document_info = PdfDocumentInfo()
	image.save(out_file, options)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example WebPToPdfExample")
