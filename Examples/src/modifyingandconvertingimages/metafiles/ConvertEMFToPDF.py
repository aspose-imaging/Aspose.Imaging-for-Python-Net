# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image, Color
from aspose.imaging.fileformats.emf import EmfImage
from aspose.imaging.imageoptions import PdfOptions, EmfRasterizationOptions
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
data_dir = os.path.join(get_data_root_dir(), 'metafiles')
file_paths = ["Picture1.emf"]
print("Running example ConvertEMFToPDF")
for file_path in file_paths:
	out_path = os.path.join(get_output_dir(), file_path + "_out.pdf")
	with aspycore.as_of(Image.load(os.path.join(data_dir, file_path)),
					    EmfImage) as image:
		with open(out_path, "w+b") as output_stream:
			if not image.header.emf_header.valid:
				raise Exception("The file {0} is not valid".format(out_path))

			emf_rasterization = EmfRasterizationOptions()
			emf_rasterization.page_width = float(image.width)
			emf_rasterization.page_height = float(image.height)
			emf_rasterization.background_color = Color.white_smoke
			pdf_options = PdfOptions()
			pdf_options.vector_rasterization_options = emf_rasterization
			image.save(output_stream, pdf_options)
	
	if 'SAVE_OUTPUT' not in os.environ:
		os.remove(out_path)

print("Finished example ConvertEMFToPDF")
