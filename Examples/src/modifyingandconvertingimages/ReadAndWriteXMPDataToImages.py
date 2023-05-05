from aspose.imaging.fileformats.tiff import TiffImage, TiffFrame
from aspose.imaging.fileformats.tiff.enums import TiffExpectedFormat, TiffPhotometrics
import aspose.pycore as aspycore
from aspose.imaging import Image, Rectangle
from aspose.imaging.imageoptions import TiffOptions
from aspose.imaging.extensions import StreamExtensions
from aspose.imaging.xmp import *
from aspose.imaging.xmp.schemas.dublincore import *
from aspose.imaging.xmp.schemas.photoshop import *
import os
import uuid
from datetime import datetime


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
print("Running example ReadAndWriteXMPDataToImages")
# Specify the size of image by defining a Rectangle 
rect = Rectangle(0, 0, 100, 200)
tiff_options = TiffOptions(TiffExpectedFormat.TIFF_JPEG_RGB)
tiff_options.photometric = TiffPhotometrics.MIN_IS_BLACK
tiff_options.bits_per_sample = [8]
# Create the brand new image just for sample purposes
with TiffImage(TiffFrame(tiff_options, rect.width, rect.height)) as image:
	# Create an instance of XMP-Header
	xmp_header = XmpHeaderPi(str(uuid.uuid4()))
	# Create an instance of Xmp-TrailerPi, XMPmeta class to set different attributes
	xmp_trailer = XmpTrailerPi(True)
	xmp_meta = XmpMeta()
	xmp_meta.add_attribute("Author", "Mr Smith")
	xmp_meta.add_attribute("Description", "The fake metadata value")
	# Create an instance of XmpPacketWrapper that contains all metadata
	xmp_data = XmpPacketWrapper(xmp_header, xmp_trailer, xmp_meta)
	# Create an instance of Photoshop package and set photoshop attributes
	photoshop_package = PhotoshopPackage()
	photoshop_package.set_city("London")
	photoshop_package.set_country("England")
	photoshop_package.set_color_mode(ColorMode.RGB)
	photoshop_package.set_created_date(datetime.now())
	# Add photoshop package into XMP metadata
	xmp_data.add_package(photoshop_package)
	# Create an instacne of DublinCore package and set dublinCore attributes
	dublin_core_package = DublinCorePackage()
	dublin_core_package.set_author("Charles Bukowski")
	dublin_core_package.set_title("Confessions of a Man Insane Enough to Live With the Beasts")
	dublin_core_package.add_value("dc:movie", "Barfly")
	# Add dublinCore Package into XMP metadata
	xmp_data.add_package(dublin_core_package)
	with StreamExtensions.create_memory_stream() as ms:
		# Update XMP metadata into image and Save image on the disk or in memory stream
		image.xmp_data = xmp_data
		image.save(ms)
		ms.seek(0)
		# Load the image from moemory stream or from disk to read/get the metadata
		with aspycore.as_of(Image.load(ms), TiffImage) as img:
			# Getting the XMP metadata
			img_xmp_data = img.xmp_data
			for package in img_xmp_data.packages:
				print(package)
				pass

print("Finished example ReadAndWriteXMPDataToImages")
