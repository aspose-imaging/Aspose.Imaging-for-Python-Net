# GROUP: MEMORY_STRATEGIES
from aspose.imaging import Image
from aspose.imaging.sources import FileCreateSource
from aspose.imaging.imageoptions import WebPOptions
import os


# Initialization
def get_data_root_dir_local():
	if 'BASE_DIR' in os.environ:
		return os.environ["BASE_DIR"]
	return "."


if 'get_output_dir' not in dir():
	get_output_dir = get_data_root_dir_local

# Example code:
# The path to the documents directory.
out_file = os.path.join(get_output_dir(), "created.webp")
print("Running example OptimizationStrategyInWebP")
with WebPOptions() as image_options:
	image_options.source = FileCreateSource(out_file, False)
	image_options.buffer_size_hint = 50
	with Image.create(image_options, 1000, 1000) as image:
		# Do something with the created image
		image.save()

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)
	
print("Finished example OptimizationStrategyInWebP")
