from time import process_time
from memory_profiler import memory_usage
#imports input.txt
f = open('input.txt', 'r+')
content = [line.rstrip() for line in f.readlines()]
f.close()
#main body
content = "".join(str(content[1]).split())
content = content.split(',')
content = [int(x) for x in content]
def insertion_sort(content):
    insertion_range = range(1, len(content))
    for i in insertion_range:
        value_to_sort = content[i]
        while content[i-1] > value_to_sort and i>0:
            content[i], content[i-1] = content[i-1], content[i]
            i = i-1
    return content
insertion_sort(content)
#exports output.txt
s = ''
for i in insertion_sort(content):
    s += str(i) + ' '
print(s)
print(process_time())
print(memory_usage())