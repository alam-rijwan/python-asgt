# Read Sample File program
file = open("sample.txt", "r")
content = file.read()
print("Content of the file:")
print(content)
file.close()