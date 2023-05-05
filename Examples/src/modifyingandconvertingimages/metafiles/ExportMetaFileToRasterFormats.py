import aspose.pycore as aspycore
from aspose.imaging import Image, Color
from aspose.imaging.fileformats.emf import EmfImage
from aspose.imaging.fileformats.tiff.enums import TiffExpectedFormat
from aspose.imaging.imageoptions import *
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
outputfile = os.path.join(get_output_dir(), "file_out")
# Create EmfRasterizationOption class instance and set properties
emf_rasterization_options = EmfRasterizationOptions()
emf_rasterization_options.background_color = Color.papaya_whip
emf_rasterization_options.page_width = 300
emf_rasterization_options.page_height = 300
in_file = os.path.join(data_dir, "Picture1.emf")
# Load an existing EMF file as iamge and convert it to EmfImage class object
with aspycore.as_of(Image.load(in_file),
					EmfImage) as image:
	if not image.header.emf_header.valid:
		raise Exception(f"The file {in_file} is not valid")

	# Convert EMF to BMP, GIF, JPEG, J2K, PNG, PSD, TIFF and WebP
	obj_init = BmpOptions()
	obj_init.vector_rasterization_options = emf_rasterization_options
	image.save(outputfile + ".bmp", obj_init)
	obj_init2 = GifOptions()
	obj_init2.vector_rasterization_options = emf_rasterization_options
	image.save(outputfile + ".gif", obj_init2)
	obj_init3 = JpegOptions()
	obj_init3.vector_rasterization_options = emf_rasterization_options
	image.save(outputfile + ".jpeg", obj_init3)
	obj_init4 = Jpeg2000Options()
	obj_init4.vector_rasterization_options = emf_rasterization_options
	image.save(outputfile + ".j2k", obj_init4)
	obj_init5 = PngOptions()
	obj_init5.vector_rasterization_options = emf_rasterization_options
	image.save(outputfile + ".png", obj_init5)
	obj_init6 = PsdOptions()
	obj_init6.vector_rasterization_options = emf_rasterization_options
	image.save(outputfile + ".psd", obj_init6)
	obj_init7 = TiffOptions(TiffExpectedFormat.TIFF_LZW_RGB)
	obj_init7.vector_rasterization_options = emf_rasterization_options
	image.save(outputfile + ".tiff", obj_init7)
	obj_init8 = WebPOptions()
	obj_init8.vector_rasterization_options = emf_rasterization_options
	image.save(outputfile + ".webp", obj_init8)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(outputfile + ".bmp")
	os.remove(outputfile + ".gif")
	os.remove(outputfile + ".jpeg")
	os.remove(outputfile + ".j2k")
	os.remove(outputfile + ".png")
	os.remove(outputfile + ".psd")
	os.remove(outputfile + ".tiff")
	os.remove(outputfile + ".webp")
