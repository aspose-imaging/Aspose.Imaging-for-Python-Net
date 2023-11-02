import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.fileformats.eps import EpsImage, EpsPreviewFormat
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
print("Running example ExportEps")
# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), 'eps')
out_file = os.path.join(get_output_dir(), "Sample.tiff")

with aspycore.as_of(Image.load(os.path.join(data_dir, "Sample.eps")), EpsImage) as image:
	tiffPreview = image.get_preview_image(EpsPreviewFormat.TIFF)
	if tiffPreview is not None:
		tiffPreview.save(out_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example ExportEps")
