file_path = "./files/test.txt"
file = open(file_path, "a")
file.writelines('\n'.join(["Hello World!", "Hi"]))
file.close()