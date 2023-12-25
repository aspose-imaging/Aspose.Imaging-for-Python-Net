# GROUP: ADDITIONAL_FEATURES

from aspose.imaging import Image, Color, VectorImage, RemoveBackgroundSettings, SizeF
from aspose.imaging.imageoptions import VectorRasterizationOptions, PngOptions
from aspose.imaging.fileformats.png import PngColorType
from aspose.pycore import as_of, cast, is_assignable
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

data_dir = os.path.join(get_data_root_dir(), 'RemoveBackground')


# Utility function
def remove_background_example(file_name, settings):
	input_file_path = os.path.join(data_dir, file_name)
	out_file_path = os.path.join(get_output_dir(), "output")
	if not os.path.exists(out_file_path):
		os.makedirs(out_file_path)

	output_file = os.path.join(out_file_path, file_name + ".png")
	with Image.load(input_file_path) as image:
		options = PngOptions()
		vectors = VectorRasterizationOptions()
		vectors.background_color = Color.transparent
		vectors.page_size = cast(SizeF, image.size)
		options.vector_rasterization_options = vectors
		options.color_type = PngColorType.TRUECOLOR_WITH_ALPHA

		if is_assignable(image, VectorImage):
			vector_image = as_of(image, VectorImage)
			vector_image.remove_background(settings)

		image.save(output_file, options)

	if 'SAVE_OUTPUT' not in os.environ:
		os.remove(output_file)

# Example code:
# The path to the documents directory.
file_names = ["golfer.emf"]

obj1 = RemoveBackgroundSettings()
obj1.detection_level = 30
rbs = [ obj1 ]

for i, file_name in enumerate(file_names):
    remove_background_example(file_name, rbs[i])
