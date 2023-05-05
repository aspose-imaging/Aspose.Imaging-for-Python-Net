import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.fileformats.tiff import TiffImage
from aspose.imaging.fileformats.bmp import BmpImage
from aspose.imaging.imageoptions import BmpOptions
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
# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), 'ModifyingAndConvertingImages')
print("Running example ExtractTIFFFramesToBMPImageFormat")
out_files = []
with aspycore.as_of(Image.load(os.path.join(data_dir, "SampleTiff1.tiff")),
					TiffImage) as multi_image:
	# Create an instance of int to keep track of frames in TiffImage
	frame_counter = 0
	# Iterate over the TiffFrames in TiffImage
	for tiff_frame in multi_image.frames:
		multi_image.active_frame = tiff_frame
		# Load Pixels of TiffFrame into an array of Colors
		pixels = multi_image.load_pixels(tiff_frame.bounds)
		# Create an instance of bmpCreateOptions
		bmp_create_options = BmpOptions()
		bmp_create_options.bits_per_pixel = 24
		# Set the Source of bmpCreateOptions as FileCreateSource by specifying the location where output will be saved
		out_file = os.path.join(get_output_dir(),
							f"ConcatExtractTIFFFramesToBMP_out{frame_counter}.bmp")
		bmp_create_options.source = FileCreateSource(out_file, False)
		# Create a new bmpImage
		with aspycore.as_of(
					Image.create(bmp_create_options, 
								 tiff_frame.width,
								 tiff_frame.height),
							 BmpImage) as bmp_image:
			# Save the bmpImage with pixels from TiffFrame
			bmp_image.save_pixels(tiff_frame.bounds, pixels)
			bmp_image.save()

		frame_counter += 1
		out_files.append(out_file)


if 'SAVE_OUTPUT' not in os.environ:
	for file in out_files:
		os.remove(file)

print("Finished example ExtractTIFFFramesToBMPImageFormat")
