from textdatasetcleaner.loaders import Loader
from textdatasetcleaner.helpers import load_config
import time

#These files needed for the test

files = ["config1.yml", "config2.yml"]
input_file = "input_file.txt"
output_file = "output_file.txt"

#name_prefix for output_file
name_prefix = 1

with open(input_file) as f:
    line_count = 0
    for line in f:
        line_count +=1
f.close()

for filename in files:

    output_file = str(name_prefix) + output_file

    config = load_config(filename)
    ldr = Loader(config, input_file, output_file)

    #get start_time
    start_time = time.time()

    # ldr.file_processing('PRE_PROCESSING')
    ldr.line_processing()
    ldr.file_processing('POST_PROCESSING')
    ldr.finish()

    #get finish_time
    finish_time = time.time()
    print("Time for " + filename + " = %s seconds" % (start_time - finish_time) + "\n")
    print("Processing speed for " + filename + " = %s line/seconds" % (line_count/(start_time - finish_time)) + "\n")

    name_prefix = name_prefix + 1
