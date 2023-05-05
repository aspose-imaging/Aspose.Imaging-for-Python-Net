import aspose.pycore as aspycore
from aspose.imaging import Image, Color
from aspose.imaging.imageoptions import WmfRasterizationOptions, PdfOptions
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
out_file = os.path.join(get_output_dir(), "ConvertWMFToPDF_out.pdf")
print("Running example ConvertWMFToPDF")
# Load an existing WMF image
with Image.load(os.path.join(data_dir, "input.wmf")) as image:
	# Create an instance of WmfRasterizationOptions class and set different properties
	wmf_rasterization_options = WmfRasterizationOptions()
	wmf_rasterization_options.background_color = Color.white_smoke
	wmf_rasterization_options.page_width = image.width
	wmf_rasterization_options.page_height = image.height
	# Create an instance of PdfOptions class and provide rasterization option
	pdf_options = PdfOptions()
	pdf_options.vector_rasterization_options = wmf_rasterization_options
	# Call the save method, provide output path and PdfOptions to convert the WMF file to PDF and save the output
	image.save(out_file, pdf_options)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example ConvertWMFToPDF")
