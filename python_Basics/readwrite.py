file = open('test.txt')
# # print(file.read())
# print(file.readline())
# print(file.readline())
# file.close()

#Read Line by line Using readLineMethod Program
line = file.readline()
while line != '':
    print(line)
    line = file.readline()

with open('test.txt','r') as reader:
    content=reader.readline()
    print(content)
    reversed(content)
    with open(r'test.txt','w') as writer:
        for line in reversed(content):
            writer.write(line)