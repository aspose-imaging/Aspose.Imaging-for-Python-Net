# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.imageoptions import PngOptions
import os
import threading


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
print("Running example ParallelDJVUImagesProcessingUsingMultithreading")

delete_output = 'SAVE_OUTPUT' not in os.environ
num_threads = 20

# thread function
def thread_func(path, output_file):
	try:
		with Image.load(path) as image:
			image.save(output_file, PngOptions())
	finally:
		if delete_output:
			os.remove(output_file)

input_file = os.path.join(data_dir, "Sample.djvu")
threads = []
for task_num in range(1, num_threads):
	output_file = os.path.join(data_dir, f"Sample_task{task_num}.png")
	thread = threading.Thread(target=thread_func, args=(input_file, output_file))
	threads.append(thread)
	thread.start()

for thread in threads:
	thread.join()

print("Running example ParallelDJVUImagesProcessingUsingMultithreading")
