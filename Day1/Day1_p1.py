import os


cwd = os.getcwd()
work_file = open(cwd + '\Day1_p1.data', "r")
# work_file_line = work_file.readline()
work_file_list = work_file.readlines()
# print(work_file_line)
# print()
# print(work_file_list)

n = 0
prev_number = float('inf')
for item in work_file_list:
    # Do something!
    # print(f"{n}: {item}")
    # n = n + 1
    if prev_number < float(item):
        n += 1
    prev_number = float(item)

print(n)
