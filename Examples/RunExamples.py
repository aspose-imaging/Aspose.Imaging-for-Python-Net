# Run all tests from the specified directory
# Author  : Evgeniy Sidenko
# Date    : 31 March 2023
# Version : 1.0
import sys
import os
from aspose.imaging import License
from datetime import datetime
import re

src_dir = ""
output_dir = ""
data_dir = ""
lic_file = ""
group_code = 0
group_filter = []
file_name_filter = None
save_output_files = False


def fill_groups(groups: int) -> None:
    group_dict = {
        1: 'DRAWING_AND_FORMATTING_IMAGES',
        2: 'MODIFYING_AND_CONVERTING_IMAGES',
        4: 'MEMORY_STRATEGIES',
        8: 'ADDITIONAL_FEATURES',
        16: 'TEST_FILE_FORMATS'
    }

    global group_filter

    for key, value in group_dict.items():
        if groups & key != 0:
            group_filter.append(value)
    del group_dict


def need_skip_by_name(file_path: str) -> bool:
    global file_name_filter
    if file_name_filter is None:
        return False
    return not file_name_filter.match(file_path)


def need_skip_by_group(code_txt: str) -> bool:
    if group_filter == "":
        return False
    first_line = code_txt.split('\n', 1)[0]
    if first_line.startswith("# GROUP: "):
        group_name = first_line[8:].strip()
        if group_name in group_filter:
            return False
    elif 'MODIFYING_AND_CONVERTING_IMAGES' in group_filter:
        return False

    return True


def parse_args():
    length = len(sys.argv)
    if (length - 1) % 2 != 0:
        usage()
        exit()

    params = {}

    # get value or default
    def get_dict_value_def(p_name, p_default=""):
        p_value = params.get(p_name)
        return p_value if p_value is not None else p_default

    for it in range(1, length, 2):
        t_name = sys.argv[it]
        value = sys.argv[it + 1]
        if not t_name.startswith('--'):
            usage()
            exit()
        params[t_name] = value

    global src_dir, data_dir, output_dir, lic_file, save_output_files, \
        file_name_filter, group_code
    src_dir = os.path.abspath(get_dict_value_def('--src-dir', "src"))
    data_dir = os.path.abspath(get_dict_value_def('--data-dir', "data"))
    output_dir = os.path.abspath(get_dict_value_def('--output-dir', "output"))
    lic_file = get_dict_value_def('--license')
    group_filter_str = get_dict_value_def('--groups', '255')
    file_name_filter_str = get_dict_value_def('--file-filter')
    save_output_files = get_dict_value_def('--save-output', 'false').lower() == 'true'

    if file_name_filter_str != "":
        file_name_filter = re.compile(file_name_filter_str)

    group_code = int(group_filter_str)
    fill_groups(group_code)

    del params, file_name_filter_str, group_filter_str


def usage():
    print("Using:")
    print("python", sys.argv[0], "Arguments")
    print("Arguments:")
    print("  --src-dir <path to the root example dir>")
    print("    Default: ./src")
    print("  --data-dir <path to the root data dir>")
    print("    Default: ./data")
    print("  --output-dir <path to the output dir>")
    print("    Default: ./output")
    print("  --license <path to a license file>")
    print("    Default: No license")
    print("  --save-output (true/false)")
    print("    Default: false")
    print("  --groups groups-flag")
    print("  	groups-flag can contains the following bit masks")
    print("  		 1 - Test drawing and formatting images")
    print("  		 2 - Test modifying and converting images")
    print("  		 4 - Test of memory strategies")
    print("  		 8 - Test additional Aspose.Imaging features")
    print("  		16 - Test file formats")
    print("  	Default: All")
    print("  --file-filter 'regex'")
    print("    Default: All files")
    print("  --help")


# Process the arguments
parse_args()

# Validate the paths
if not os.path.exists(src_dir):
    print("Does not exists path:", src_dir)
    usage()
    exit()

if not os.path.exists(data_dir):
    print("Does not exists path:", data_dir)
    usage()
    exit()

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

# Set license if it exists
if len(lic_file) > 0 and lic_file != "none":
    lic = License()
    lic.set_license(lic_file)


# function loads the source code for executing
def load_example(file_name):
    with open(file_name, "rb") as s_file:
        pref = s_file.read(3)

    with open(file_name, "rt") as s_file:
        # if we have a BOM then skip it
        if pref[0] == 0xef and pref[1] == 0xbb and pref[2] == 0xbf:
            s_file.seek(3)
        s_code = s_file.read()

    return s_code


def get_data_root_dir():
    return data_dir


def get_output_dir():
    return output_dir


globals_parameter = {'get_data_root_dir': get_data_root_dir, 'get_output_dir': get_output_dir}

src_dir_len = len(src_dir) + 1
file_count = 0

os.environ['TEMPLATE_DIR'] = data_dir
if save_output_files:
    os.environ['SAVE_OUTPUT'] = "1"

error_tests = {}


def print_header(text):
    print("|--------------------------------------------------")
    print("|", datetime.now())
    print("|", text)
    print("|--------------------------------------------------")


start_time = datetime.now()

print_header("STARTING...")

# Run all examples
for root, dirs, files in os.walk(src_dir):
    for name in files:
        if not name.endswith(".py"):
            continue
        src_file = os.path.join(root, name)
        if need_skip_by_name(src_file):
            continue
        code = load_example(src_file)
        if need_skip_by_group(code):
            continue
        print_header("RUN FILE: " + src_file[src_dir_len:])
        file_count += 1
        try:
            exec(code, globals_parameter, None)
        except Exception as ex:
            error_tests[src_file] = ex

err_count = len(error_tests)
print("|--------------------------------------------------")
if err_count == 0:
    print_header(f"\n| FINISHED! NO ERROR WAS FOUND!\n| PROCESSED: {file_count} FILES.\n|")
else:
    print_header(f"FINISHED WITH ERRORS! PROCESSED {file_count} files.")
    print("| ERROR COUNT", err_count)
    print("| ERROR LIST:")
    index = 1
    for file, error in error_tests.items():
        print(f"| {index} - {file}")
        print("|     ", error)
        index += 1
    print("|--------------------------------------------------")

print("|", "PROCESSING TIME:", (datetime.now() - start_time))
