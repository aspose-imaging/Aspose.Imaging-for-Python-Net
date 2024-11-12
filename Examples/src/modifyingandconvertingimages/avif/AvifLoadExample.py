from aspose.imaging import Image
import os


# Initialization
def get_data_root_dir_local():
	if 'BASE_DIR' in os.environ:
		return os.environ["BASE_DIR"]
	return "."


if 'get_data_root_dir' not in dir():
	get_data_root_dir = get_data_root_dir_local

# Example code:
print("Running example AvifLoadExample")
data_dir = os.path.join(get_data_root_dir(), 'avif')
file_name = "example.avif"
input_file_path = os.path.join(data_dir, file_name)
with Image.load(input_file_path) as image:
	print(f"Avif image is loaded! Format: {image.file_format}")
	print(f"Size: {image.size}");

print("Finished example AvifLoadExample")
