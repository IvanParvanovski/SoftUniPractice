file_path = "files/File Opener/text.txt"

try:
    file = open(file_path, 'r')
    print("File found")

except:
    print("File not found")


