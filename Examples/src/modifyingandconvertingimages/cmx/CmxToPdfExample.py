# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image, Color, TextRenderingHint, SmoothingMode
from aspose.imaging.fileformats.cmx import CmxImage
from aspose.imaging.fileformats.pdf import PdfDocumentInfo
from aspose.imaging.imageoptions import PdfOptions, VectorRasterizationOptions
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
print("Running example CmxToPdfExample")
# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), 'cmx')
input_file = os.path.join(data_dir, "MultiPage.cmx")
out_file = os.path.join(get_output_dir(), "MultiPage.pdf")
with aspycore.as_of(Image.load(input_file), CmxImage) as image:
	options = PdfOptions()
	options.pdf_document_info = PdfDocumentInfo()
	# Set rasterization options for fileformat
	options.vector_rasterization_options = image.get_default_options([Color.white, image.width, image.height]).vector_rasterization_options
	options.vector_rasterization_options.text_rendering_hint = TextRenderingHint.SINGLE_BIT_PER_PIXEL
	options.vector_rasterization_options.smoothing_mode = SmoothingMode.NONE
	image.save(out_file, options)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example CmxToPdfExample")
