from aspose.imaging import Image
from aspose.imaging.imageoptions import PngOptions
from aspose.imaging.multithreading import InterruptMonitor
import os
import time
from datetime import datetime
from threading import Thread


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
data_dir = os.path.join(get_data_root_dir(), "DrawingAndFormattingImages")

# Tries to convert image from one format to another. Handles interruption.
def thread_proc(input_path, output_path, save_options, monitor):
	print("Work thread")
	with Image.load(input_path) as image:
		InterruptMonitor.set_thread_local_instance(monitor)
		try:
			image.save(output_path, save_options)
			print("Finished correctly")
		except RuntimeError as e:
			if "OperationInterruptedException" in str(e):
				print("The save thread #{0} finishes at {1}".format(thread.native_id, datetime.now()))
			# print(e)
		finally:
			InterruptMonitor.set_thread_local_instance(None)


out_file = os.path.join(get_output_dir(), "big_out.png")
save_options = PngOptions()
monitor = InterruptMonitor()
thread = Thread(target=thread_proc, args=(os.path.join(data_dir, "aspose-logo_tn.jpg"), \
	out_file, save_options, monitor))
try:
	thread.start()
	# The timeout should be less than the time required for full image conversion (without interruption).
	time.sleep(0.2)
	# Interrupt the process
	monitor.interrupt()
	print("Interrupting the save thread #{0} at {1}".format(thread.native_id, datetime.now()))
	# Wait for interruption...
	thread.join()
finally:
	# If the file to be deleted does not exist, no exception is thrown.
	if 'SAVE_OUTPUT' not in os.environ:
		os.remove(out_file)
