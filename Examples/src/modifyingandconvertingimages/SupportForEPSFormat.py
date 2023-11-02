import aspose.pycore as aspycore
from aspose.imaging.fileformats.eps import EpsImage
from aspose.imaging import Image
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
output_path = os.path.join(get_output_dir(), "anyEpsFile.png")
print("Running example SupportForEPSFormat")

eps_preview_files = []
with aspycore.as_of(Image.load(os.path.join(data_dir, "sample.eps")),
					EpsImage) as eps_image:
	for preview in eps_image.get_preview_images():
		previewPath = os.path.join(data_dir, "output." + preview.file_format.name.lower())
		preview.save(previewPath)
		eps_preview_files.append(previewPath)

if 'SAVE_OUTPUT' not in os.environ:
	for output_path in eps_preview_files:
		if os.path.exists(output_path):
			os.remove(output_path)

print("Finished example SupportForEPSFormat")
