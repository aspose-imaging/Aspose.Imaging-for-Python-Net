# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.fileformats.gif import GifImage
from aspose.imaging.fileformats.gif.blocks import GifFrameBlock
from aspose.imaging.fileformats.webp import WebPFrameBlock, WebPImage
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
data_dir = os.path.join(get_data_root_dir(), 'WebPImage')
out_file = os.path.join(get_output_dir(), "ConvertGIFFImageFrame_out.webp")
print("Running example ConvertGIFFImageFrame")
# Load GIFF image into the instance of image class.
with Image.load(os.path.join(data_dir, "asposelogo.gif")) as image:
	# Cast an instance to GifImage class.
	if aspycore.is_assignable(image, GifImage):
		gif = aspycore.as_of(image, GifImage)

		# Load an existing WebP image into the instance of WebPImage class.
		with WebPImage(image.width, image.height, None) as webp:
			# Loop through the GIFF frames
			for block in gif.blocks:
				# Convert GIFF block to GIFF Frame
				if not aspycore.is_assignable(block, GifFrameBlock):
					continue
				gif_block = aspycore.as_of(block, GifFrameBlock)
				
				# Create an instance of WebP Frame instance by passing GIFF frame to class constructor.
				web_block = WebPFrameBlock(gif_block)
				web_block.top = gif_block.top
				web_block.left = gif_block.left
				web_block.duration = gif_block.control_block.delay_time
				# Add WebP frame to WebP image block list
				webp.add_block(web_block)

			# Set Properties of WebP image.
			webp.options.anim_background_color = 0xf
			webp.options.anim_loop_count = 0
			webp.options.quality = 50
			webp.options.lossless = False
			# Save WebP image.
			webp.save(out_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)
	
print("Finished example ConvertGIFFImageFrame")
