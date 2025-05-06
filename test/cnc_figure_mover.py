file_path = 'C:\\Users\\Administrator\\PythonProgs\\utilities\\test\\millingorig\\'
file_path_ch = 'C:\\Users\\Administrator\\PythonProgs\\utilities\\test\\milling\\'

file_name = '1.75'
postfix = '_changed_copy'
file_end = '.tap'


def cnc_move(commands, ch_x, ch_y, ch_z, begin, end):
    k = 0
    for command in commands:
        index = 0
        xb = 0
        xe = 0
        yb = 0
        ye = 0
        zb = 0
        ze = 0
        flagy = False
        flagx = False
        flagz = False
        if begin <= k <= end:
            #print(str(begin) + ' ' + str(end))
            for letter in command:
                if letter == 'X':
                    flagx = True
                    xb = index
                    break
                index += 1
            for j in range(xb + 1, len(command)):
                if command[j].isdigit() or command[j] == '.':
                    index += 1
                    if j + 1 == len(command):
                        xe = index
                else:
                    xe = index
                    break

            if flagx:
               # print(command[xb:xe + 1])
                orig_x = float(command[xb + 1:xe + 1])
                command = command.replace(command[xb:xe + 1], 'X' + "{:.3f}".format(orig_x + ch_x))

            index = 0
            for letter in command:
                if letter == 'Y':
                    flagy = True
                    yb = index
                    break
                index += 1
            for j in range(yb + 1, len(command)):
                if command[j].isdigit() or command[j] == '.':
                    index += 1
                    if j + 1 == len(command):
                        ye = index
                else:
                    ye = index
                    break

            if flagy:
               # print(command[yb:ye + 1])
                orig_y = float(command[yb + 1:ye + 1])
                command = command.replace(command[yb:ye + 1], 'Y' + "{:.3f}".format(orig_y + ch_y))

            index = 0
            for letter in command:
                if letter == 'Z':
                    flagz = True
                    zb = index
                    break
                index += 1
            for j in range(zb + 1, len(command)):
                if command[j].isdigit() or command[j] == '.' or command[j] == '-':
                    index += 1
                    if j + 1 == len(command):
                        ze = index
                else:
                    ze = index
                    break

            if flagz:
               # print(command[yb:ye + 1])
                orig_z = float(command[zb + 1:ze + 1])
                command = command.replace(command[zb:ze + 1], 'Z' + "{:.3f}".format(orig_z + ch_z))

            commands[k] = command
           # print(str(xb) + ' ' + str(xe) + ' ' + str(yb) + ' ' + str(ye))
            #print(command)
        k += 1


g_x_ch_val = 58
g_y_ch_val = -9.714
g_z_ch_val = 0

#g_x_ch_val = 0
#g_y_ch_val = 1
#g_z_ch_val = 0


#milling 1.7 
be_arr = [[4, 3626], [3628, 7250], [7252, 10874], [10876, 14498], [14500, 18122]]

# [begin value, end value]
# lids 1.75
#be_arr = [[4, 17], [43, 56], [83, 97], [123, 136], [163, 176]]
# lids 1.75, 1.65, 1.7(3)
#be_arr = [[43, 56], [82, 96], [122, 135], [162, 175]]
# lids 1.75
#be_arr = [[4, 17]]
# lids 1.6
#be_arr = [[3, 16], [42, 56], [83, 97], [124, 137], [163, 176]]
# lids 1.7
#be_arr = [[3, 16], [43, 56], [82, 95], [121, 135], [162, 176]]
#lids 1.8
#be_arr = [[4, 19], [45, 58], [84, 97], [124, 137]]
#lids 1.9
#be_arr = [[4, 19], [45, 58], [85, 99], [125, 139]]
#lids 2.0
#be_arr = [[4, 17], [44, 58], [85, 98], [124, 137]]
#lids 1.95
#be_arr = [[4, 18], [45, 58], [84, 98], [124, 138]]
#bottom 8_gr
#be_arr = [[103, 151]]
#lids 1.95(2) 1.85(2)
#be_arr = [[4, 18], [44, 58], [84, 97], [123, 137]]

#milling 1.8
#be_arr = [[4, 3506], [3507, 7009], [7010, 10512], [10513, 14014]]

#be_arr = [[150, 198]]

g_begin = be_arr[0][0]
g_end = be_arr[0][1]

g_file = open(file_path + file_name + file_end)
with open(file_path_ch + file_name + postfix + file_end, "w+") as g_ch_f:
    commands_full = g_file.read()
    g_commands = commands_full.split('\n')
    count = 0
    for range_ in be_arr:
        g_begin = range_[0]
        g_end = range_[1]
        x = g_x_ch_val
        
        if count % 2 == 1:
            x = g_x_ch_val * -1
        cnc_move(g_commands, x, g_y_ch_val, g_z_ch_val, g_begin, g_end)
        count += 1
    g_ch_f.write('\n'.join(g_commands))
g_file.close()
