file_path = '/home/slippa/gitrep/utilities/'
file_name = 'file1.8'
postfix = '_changed_copy'
file_end = '.tap'
g_begin = 4
g_end = 19
g_div = 39
g_count = 4
g_x_ch_val = 58
g_y_ch_val = 10


def cnc_move(commands, ch_x, ch_y, begin, end, div, count_begin, count, minus_val):
    for i in range(count_begin, count - 1):
        k = 0
        for command in commands:
            index = 0
            xb = 0
            xe = 0
            yb = 0
            ye = 0
            if begin + i * div <= k <= end + i * div:
                print(str(begin + i * div) + ' ' + str(end + i * div))
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
                    minus = minus_val
                    if i % 2 == 0:
                        minus = -1 * minus_val
                    command = command.replace(command[xb:xe + 1], 'X' + "{:.3f}".format(orig_x + ch_x * minus))

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

g_file = open(file_path + file_name + file_end)
g_ch_f = open(file_path + file_name + postfix + file_end, "w+")
commands_full = g_file.read()
g_commands = commands_full.split('\n')
cnc_move(g_commands, g_x_ch_val, g_y_ch_val, g_begin, g_end, g_div, 0, 2, -1)
g_begin = 45
g_end = 58
cnc_move(g_commands, g_x_ch_val, g_y_ch_val, g_begin, g_end, g_div, 0, 4, 1)
g_ch_f.write('\n'.join(g_commands))
g_file.close()