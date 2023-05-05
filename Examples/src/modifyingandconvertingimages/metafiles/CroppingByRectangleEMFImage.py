# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image, Color, Rectangle
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
# Create an instance of Rasterization options
emf_rasterization_options = EmfRasterizationOptions()
emf_rasterization_options.background_color = Color.white_smoke
# Create an instance of PNG options
pdf_options = PdfOptions()
pdf_options.vector_rasterization_options = emf_rasterization_options
print("Running example CroppingByRectangleEMFImage")
out_file = os.path.join(get_output_dir(), "CroppingByRectangleEMFImage_out.pdf")
# Load an existing image into an instance of EMF class
with aspycore.as_of(Image.load(os.path.join(data_dir, "Picture1.emf")),
					EmfImage) as image:
	with open(out_file, "w+b") as output_stream:
		# Create an instance of Rectangle class with desired size and Perform the crop operation on object of Rectangle class and Set height and width and Save the results to disk
		image.crop(Rectangle(30, 50, 100, 150))
		pdf_options.vector_rasterization_options.page_width = round(image.width)
		pdf_options.vector_rasterization_options.page_height = round(image.height)
		image.save(output_stream, pdf_options)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example CroppingByRectangleEMFImage")
