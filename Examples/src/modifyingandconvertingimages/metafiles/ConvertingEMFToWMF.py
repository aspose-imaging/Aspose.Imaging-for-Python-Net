import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.fileformats.emf import MetaImage
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
data_dir = os.path.join(get_data_root_dir(), 'metafiles')

# To get proper output please apply a valid Aspose.Imaging License. You can purchase full license or get 30 day temporary license from https:// www.aspose.com/purchase/default.aspx."
# List of existing EMF images. 
files = ["TestEmfPlusFigures.emf", "TestEmfBezier.emf"]
# Loop for each file name.
for file in files:
	# Input file name & path.
	file_path = os.path.join(data_dir, file)
	out_file = os.path.join(get_output_dir(), file + "_out.wmf")
	# Load the EMF image as image and convert it to MetaImage object.
	with aspycore.as_of(Image.load(file_path), MetaImage) as image:
		# Convert the EMF image to WMF image by creating and passing WMF image options class object.
		options = WmfOptions()
		options.vector_rasterization_options = EmfRasterizationOptions()
		image.save(out_file, options)
		
	if 'SAVE_OUTPUT' not in os.environ:
		os.remove(out_file)
