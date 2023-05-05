import aspose.pycore as aspycore
from aspose.imaging import Image, Color, FontSettings
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
png_options = PngOptions()
png_options.vector_rasterization_options = emf_rasterization_options
out_path = os.path.join(get_output_dir(), "Picture1_default_fonts_out.png")
out_path2 = os.path.join(get_output_dir(), "Picture1_with_my_fonts_out.png")
# Load an existing EMF image
with aspycore.as_of(Image.load(os.path.join(data_dir, "Picture1.emf")),
					EmfImage) as image:
	image.cache_data()
	# Set height and width, Reset font settings
	png_options.vector_rasterization_options.page_width = 300.0
	png_options.vector_rasterization_options.page_height = 350.0
	FontSettings.reset()
	image.save(out_path, png_options)
	# Initialize font list
	fonts = list(FontSettings.get_default_fonts_folders())
	# Add new font path to font list and Assign list of font folders to font settings and Save the EMF file to PNG image with new font
	fonts.append(os.path.join(data_dir, "Fonts"))
	FontSettings.set_fonts_folders(fonts, True)
	image.save(out_path2, png_options)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_path)
	os.remove(out_path2)
