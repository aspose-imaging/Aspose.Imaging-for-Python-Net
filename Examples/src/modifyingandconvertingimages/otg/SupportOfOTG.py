# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image, SizeF
from aspose.imaging.imageoptions import PngOptions, OtgRasterizationOptions, PdfOptions
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
data_dir = os.path.join(get_data_root_dir(), 'otg')

print("Running example SupportOfOTG")
file_name = "VariousObjectsMultiPage.otg"
input_file_name = os.path.join(data_dir, file_name)
options = [PngOptions(), PdfOptions()]
for item in options:
	file_ext = ".png" if aspycore.is_assignable(item, PngOptions) else ".pdf"
	out_file = os.path.join(get_output_dir(), "output" + file_ext)
	with Image.load(input_file_name) as image:
		otg_rasterization_options = OtgRasterizationOptions()
		otg_rasterization_options.page_size = aspycore.cast(SizeF, image.size)
		item.vector_rasterization_options = otg_rasterization_options
		image.save(out_file, item)
	
	if 'SAVE_OUTPUT' not in os.environ:
		os.remove(out_file)

print("Finished example SupportOfOTG")
