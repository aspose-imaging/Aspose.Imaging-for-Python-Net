import aspose.pycore as aspycore
from aspose.imaging import Image, Color
from aspose.imaging.imageoptions import WmfOptions, EmfRasterizationOptions
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
out_file = os.path.join(get_output_dir(), "ConvertEMFToWMF_out.wmf")
# Load an existing EMF file as Image.
with Image.load(os.path.join(data_dir, "Picture1.emf")) as image:
	# Call the Save method of Image class & Pass instance of 
	# WmfOptions class to Save method.
	emf_rasterization = EmfRasterizationOptions()
	emf_rasterization.background_color = Color.yellow
	emf_rasterization.page_width = 100.0
	emf_rasterization.page_height = 100.0
	emf_rasterization.border_x = 5.0
	emf_rasterization.border_y = 10.0
	options = WmfOptions()
	options.vector_rasterization_options = emf_rasterization
	image.save(out_file, options)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)
