import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.fileformats.psd import *
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
print("Running example ApsToPsd")
# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), 'cdr')
input_file_name = os.path.join(data_dir, "SimpleShapes.cdr")
out_file = os.path.join(get_output_dir(), "result.psd")
# Export vector image to PSD format keeping vector shapes
# Aspose.Imaging allows to export vector image formats such as CDR, EMF, EPS, ODG, SVG, WMF to the PSD format, 
# while keeping vector properties of the original, utilizing PSD Shapes, Paths //and Vector Masks.
# Currently, export of not very complex shapes is supported, whithout texture brushes or open shapes with stroke, 
# which will be improved in the upcoming releases.
# Example
# Export from the CDR format to the PSD format preserving vector 
# properties is as simple as the following snippet:
with Image.load(input_file_name) as image:
	vect_options = PsdVectorizationOptions()
	vect_options.vector_data_composition_mode = VectorDataCompositionMode.SEPARATE_LAYERS
	image_options = PsdOptions()
	image_options.vector_rasterization_options = VectorRasterizationOptions()
	image_options.vectorization_options = vect_options
	image_options.vector_rasterization_options.page_width = float(image.width)
	image_options.vector_rasterization_options.page_height = float(image.height)
	image.save(out_file, image_options)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example ApsToPsd")

