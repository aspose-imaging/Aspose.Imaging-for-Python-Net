from aspose.imaging import Image, SizeF
from aspose.imaging.imageoptions import PdfOptions
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
print("Running example SupportOfDPISettingsInPdfOptions")
file_name = "SampleTiff1.tiff"
input_file_name = os.path.join(data_dir, file_name)
out_file_name = os.path.join(get_output_dir(), file_name + ".pdf")
with Image.load(input_file_name) as image:
	pdf_options = PdfOptions()
	pdf_options.page_size = SizeF(612.0, 792.0)
	image.save(out_file_name, pdf_options)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file_name)

print("Finished example SupportOfDPISettingsInPdfOptions")
