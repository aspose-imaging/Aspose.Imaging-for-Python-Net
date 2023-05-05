import aspose.pycore as aspycore
from aspose.imaging import Image, RasterImage
from aspose.imaging.fileformats.apng import ApngImage, ApngFrame
from aspose.imaging.fileformats.png import PngColorType
from aspose.imaging.imageoptions import ApngOptions
from aspose.imaging.sources import FileCreateSource
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
print("Running example CreateAPNGAnimationFromSinglePageImage")
animation_duration = 1000
frame_duration = 70
data_dir = os.path.join(get_data_root_dir(), 'apng')
file_name = "not_animated.png"
input_file_path = os.path.join(data_dir, file_name)
output_file_path = os.path.join(get_output_dir(), "raster_animation.png")
with aspycore.as_of(Image.load(input_file_path), RasterImage) as source_image:
	with ApngOptions() as create_options:
		create_options.source = FileCreateSource(output_file_path, False)
		create_options.default_frame_time = frame_duration
		create_options.color_type = PngColorType.TRUECOLOR_WITH_ALPHA
		with aspycore.as_of(Image.create(create_options, 
										 source_image.width, 
										 source_image.height), 
							ApngImage) as apng_image:
			num_of_frames = animation_duration // frame_duration
			num_of_frames2 = num_of_frames // 2
			apng_image.remove_all_frames()
			# add first frame
			apng_image.add_frame(source_image, frame_duration)

			# add intermediate frames
			for frame_index in range(1, num_of_frames):
				apng_image.add_frame(source_image, frame_duration)
				last_frame = aspycore.as_of(apng_image.pages[apng_image.page_count - 1],
											ApngFrame)
				gamma = num_of_frames - frame_index - 1 if frame_index >= num_of_frames2 else frame_index
				last_frame.adjust_gamma(gamma)

			# add last frame
			apng_image.add_frame(source_image, frame_duration)
			apng_image.save()

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_file_path)

print("Finished example CreateAPNGAnimationFromSinglePageImage")
