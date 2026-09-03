from aspose.pycore import as_of
from aspose.imaging import Image, RasterImage
from aspose.imaging.fileformats.png import PngImage
from aspose.imaging.fileformats.core.photo.hdr import HdrProcessor, HdrImageOptions
import os
from os.path import join as path_combine


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
print("Running example SupportOfHdrImages")

# The path to the documents directory.
data_dir = path_combine(get_data_root_dir(), 'jpeg')
out_file = path_combine(get_output_dir(), "hdr.jpg")

source_files = ["DSC_6918.jpg", "DSC_6919.jpg"]
images = []
for source_file in source_files:
    source_path = path_combine(data_dir, source_file)
    images.append(as_of(Image.load(source_path), RasterImage))

hdr_options = HdrImageOptions()
hdr_options.sample_count = 2
hdr_options.smooth_factor = 15
hdr_options.align_images = False

pixels = HdrProcessor.process(images, hdr_options)

with PngImage(images[0].width, images[0].height) as image:
    image.save_argb_32_pixels(image.bounds, pixels)
    image.save(out_file)

# disposing the images
for image in images:
    with image as _:
        pass

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example SupportOfHdrImages")
