# import os
#
#
# cwd = os.getcwd()
# work_file2 = open(cwd + '\Day1_p1.data', "r")
work_file2 = open('Day1_p1.data', "r")
# work_file_line = work_file.readline()
work_file_list = work_file2.readlines()
# print(work_file_line)
# print()
# print(work_file_list)
work_file_list = list(map(int, work_file_list))


nx = ny = nz = 0
prev_number = float('inf')
# new_number = 0
final_count = 0
sub_list = []
x = y = z = 0
for index, item in enumerate(work_file_list):
    x += item
    nx += 1
    if index > 0:
        y += item
        ny += 1
    if index > 1:
        z += item
        nz += 1

    if nx % 3 == 0 and nx:
        sub_list.append(x)
        x = nx = 0

    if ny % 3 == 0 and ny > 0:
        sub_list.append(y)
        y = ny = 0

    if nz % 3 == 0 and nz > 0:
        sub_list.append(z)
        z = nz = 0

# print(sub_list)

# n = 0
# prev_number = float('inf')
for item2 in sub_list:
    # Do something!
    # print(f"{n}: {item}")
    # n = n + 1
    if prev_number < item2:
        final_count += 1
    prev_number = item2

print(final_count)
