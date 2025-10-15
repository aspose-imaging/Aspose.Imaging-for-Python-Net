# GROUP: MODIFYING_AND_CONVERTING_IMAGES

from aspose.pycore import type_of
from aspose.imaging import Image
from aspose.imaging.imageoptions import PngOptions
from aspose.imaging.xmp import XmpPacketWrapper
from aspose.imaging.xmp.schemas.xmpbaseschema import XmpBasicPackage
from aspose.imaging.exif.enums import ExifOrientation
from aspose.imaging.exif import ExifData
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


def edit_source_image_metadata(input_path, output_path):
    with Image.load(input_path) as image:
        if image.xmp_data is not None:
            new_package = XmpBasicPackage()
            new_package.add_value("New key", "New value")
            image.xmp_data.add_package(new_package)

        if image.exif_data is not None:
            image.exif_data.orientation = ExifOrientation.RIGHT_TOP

        image.save(output_path)

        if 'SAVE_OUTPUT' not in os.environ:
            os.remove(output_path)


def export_source_image_metadata(input_path, output_path, output_options):
    with Image.load(input_path) as input_image:
        # Set KeepMetadata to true to export inputImage metadata profiles, if outputOptions instance does not contain ones.
        output_options.keep_metadata = True
        input_image.save(output_path, output_options)

        if 'SAVE_OUTPUT' not in os.environ:
            os.remove(output_path)
        

def overwrite_source_image_metadata(input_path, output_path, output_options):
    with Image.load(input_path) as image:
        new_metadata = get_new_metadata()
        # Try to set metadata, if the image format support metadata format type.
        for metadata in new_metadata:
            if output_options.try_set_metadata(metadata):
                print(f"{output_options.get_type().full_name} image supports {metadata.get_type().full_name}")

        # Or set metadata directly without image and metadata format compatibility check.
        output_options.exif_data = [it for it in new_metadata if it.get_type() == type_of(ExifData)][0]
        output_options.xmp_data = [it for it in new_metadata if it.get_type() == type_of(XmpPacketWrapper)][0]

        image.save(output_path, output_options)

        if 'SAVE_OUTPUT' not in os.environ:
            os.remove(output_path)


def get_new_metadata():
    xmpData = XmpPacketWrapper()
    xmpPackage = XmpBasicPackage()
    xmpPackage.add_value("User key", "User value")
    xmpData.add_package(xmpPackage)

    exif_data = ExifData()
    exif_data.orientation = ExifOrientation.RIGHT_TOP

    return (xmpData, exif_data)


# Example code:
# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), 'png')
file_path = os.path.join(data_dir, "00020.png")
output_path = os.path.join(get_output_dir(), "00020.edited.png") 

edit_source_image_metadata(file_path, output_path)
export_source_image_metadata(file_path, output_path + "_2.png", PngOptions())
overwrite_source_image_metadata(file_path, output_path + "_3.png", PngOptions())
