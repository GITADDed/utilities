file_path = 'C:\\Users\\Administrator\\PythonProgs\\test\\lidsorig\\'
file_path_ch = 'C:\\Users\\Administrator\\PythonProgs\\test\\lids\\'
file_name = '1.7'
postfix = '_changed_copy'
file_end = '.tap'


def cnc_move(commands, ch_x, ch_y, begin, end):
    k = 0
    for command in commands:
        index = 0
        xb = 0
        xe = 0
        yb = 0
        ye = 0
        if begin <= k <= end:
            print(str(begin) + ' ' + str(end))
            for letter in command:
                if letter == 'X':
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

            if not (xb == 0 or xe == 0):
                print(command[xb:xe + 1])
                orig_x = float(command[xb + 1:xe + 1])
                command = command.replace(command[xb:xe + 1], 'X' + "{:.3f}".format(orig_x + ch_x))

            index = 0
            for letter in command:
                if letter == 'Y':
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

            if not (yb == 0 or ye == 0):
                print(command[yb:ye + 1])
                orig_y = float(command[yb + 1:ye + 1])
                command = command.replace(command[yb:ye + 1], 'Y' + "{:.3f}".format(orig_y + ch_y))

            commands[k] = command
            print(str(xb) + ' ' + str(xe) + ' ' + str(yb) + ' ' + str(ye))
            print(command)
        k += 1


g_x_ch_val = 58
g_y_ch_val = 10

# [begin value, end value]
be_arr = [[3, 16], [43, 56], [82, 95], [121, 135], [162, 176]]

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
        cnc_move(g_commands, x, g_y_ch_val, g_begin, g_end)
        count += 1
    g_ch_f.write('\n'.join(g_commands))
g_file.close()
