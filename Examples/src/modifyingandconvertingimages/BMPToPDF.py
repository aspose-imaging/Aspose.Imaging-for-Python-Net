﻿import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.imageoptions import PdfOptions
from aspose.imaging.fileformats.bmp import BmpImage
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
data_dir = os.path.join(get_data_root_dir(), 'ModifyingAndConvertingImages')
out_file = os.path.join(get_output_dir(), "sample_out.pdf")
print("Running example BMPToPDF")
with aspycore.as_of(Image.load(os.path.join(data_dir, "sample.bmp")),
					BmpImage) as image:
	export_options = PdfOptions()
	export_options.pdf_document_info = PdfDocumentInfo()
	image.save(out_file, export_options)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example BMPToPDF")
