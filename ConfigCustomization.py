from textdatasetcleaner import Loader
files = ["configs/custom-config.yml", "/configs/config-filter.yml"]

for filename in files:
    ldr = Loader(filename, "input/input_file.txt", "output/output_file.txt")
    ldr.file_processing('PRE_PROCESSING')
    ldr.line_processing()
    ldr.file_processing('POST_PROCESSING')

    ldr.finish()
