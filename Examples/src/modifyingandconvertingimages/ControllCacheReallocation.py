import aspose.pycore as aspycore
from aspose.imaging import Image, Cache, ColorPalette, RasterImage, \
	CacheType, Color
from aspose.imaging.sources import StreamSource
from aspose.imaging.imageoptions import GifOptions
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

print("Running example ControllCacheReallocation")

cache_folder = os.path.join(get_output_dir(), "temp")

if not os.path.exists(cache_folder):
	os.mkdir(cache_folder)

# By default the cache folder is set to the local temp directory.  You can specify a different cache folder from the default this way:
old_cache_dir = Cache.cache_folder
print("old_cache_dir", old_cache_dir)
Cache.set_cache_folder(cache_folder)
# Auto mode is flexible and efficient
Cache.set_cache_type(CacheType.AUTO)
# The default cache max value is 0, which means that there is no upper limit
Cache.set_max_disk_space_for_cache(1073741824)
Cache.set_max_memory_for_cache(1073741824)
# We do not recommend that you change the following property because it may greatly affect performance
Cache.set_exact_reallocate_only(False)

# At any time you can check how many bytes are currently allocated for the cache in memory or on disk By examining the following properties
l1 = Cache.allocated_disk_bytes_count
l2 = Cache.allocated_memory_bytes_count
print("allocated_disk_bytes_count", l1, "allocated_memory_bytes_count", l2)

options = GifOptions()
options.palette = ColorPalette.create_with_colors([Color.red, Color.blue, Color.black, Color.white])
options.source = StreamSource()
with aspycore.as_of(Image.create(options, 100, 100), RasterImage) as image:
	pixels = [Color.white] * 10000
	
	image.save_pixels(image.bounds, pixels)
	# After executing the code above 40000 bytes are allocated to memory.
	disk_bytes = Cache.allocated_disk_bytes_count
	memory_bytes = Cache.allocated_memory_bytes_count
	print("disk_bytes", disk_bytes, "memory_bytes", memory_bytes)

# The allocation properties may be used to check whether all Aspose.Imaging objects were properly disposed. If you've forgotten to call dispose on an object the cache values will not be 0.
l1 = Cache.allocated_disk_bytes_count
l2 = Cache.allocated_memory_bytes_count
print("allocated_disk_bytes_count", l1, "allocated_memory_bytes_count", l2)
Cache.set_cache_type(CacheType.AUTO)
Cache.set_cache_folder(old_cache_dir)
os.rmdir(cache_folder)

print("Finished example ControllCacheReallocation")
