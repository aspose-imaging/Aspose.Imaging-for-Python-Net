# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image, RasterImage, Color
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
data_dir = os.path.join(get_data_root_dir(), 'png')
out_file = os.path.join(get_output_dir(), "ChangeBackgroundColor_out.jpg")
print("Running example ChangeBackgroundColor")
# Create an instance of Image class and load a PNG image
with Image.load(os.path.join(data_dir, "aspose_logo.png")) as img:
	# Create an instance of RasterImage and get the pixels array by calling method load_argb_32_pixels.
	raster_img = aspycore.as_of(img, RasterImage)
	if raster_img is not None:
		pixels = raster_img.load_argb_32_pixels(img.bounds)
		if pixels is not None:
			# Iterate through the pixel array and Check the pixel information that if it is a transparent color pixel and Change the pixel color to white
			transparent_color = raster_img.transparent_color.to_argb()
			white_color = Color.white.to_argb()
			for i in range(pixels.length):
				if pixels[i] == transparent_color:
					pixels[i] = white_color

			# Replace the pixel array into the image.
			raster_img.save_argb_32_pixels(img.bounds, pixels)

		# Save the updated image to disk.
		raster_img.save(out_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example ChangeBackgroundColor")
