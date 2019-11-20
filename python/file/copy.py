file_read = open("README")
file_write = open("REAMDE[Copy]", "w")

text = file_read.read()
file_write.write(text)

file_read.close()
file_write.close()
