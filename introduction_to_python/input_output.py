# input and output
# https://realpython.com/lessons/functions-input-and-output/
for i in range(100):
    print(i, end=' ')
print()

file = open('test.txt', mode='w')
file.write('Hello world')
file.close()

file = open('test.txt', mode='r')
print(*file.readlines())
file.close()
