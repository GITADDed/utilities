file_path = '/home/slippa/gitrep/utilities/'
file_name = 'file1.8_changed_copy'
file_end = '.tap'
begin = 4
end = 19
axis = 'Y'
ch_val = 11
with open(file_path + file_name + file_end) as file:
    ch_f = open(file_path + file_name + '_changed_copy' + file_end, "w")
    commands_full = file.read()
    ch_commands = []
    num = ''
    commands = commands_full.split('\n')
    k = 0
    for command in commands:
        index = 0
        if begin <= k <= end:
            for letter in command:
                if letter == axis:
                    index += 1
                    break
                index += 1
            for i in range(index, len(command)):
                if command[i] == '.':
                    break
                num += command[i]
            if num != '':
                ch_num = int(num) + ch_val
                split_com = command.split(num)
                ch_string = ''
                for i in range(len(split_com)) :
                    if split_com[i].find(axis) != -1:
                        split_com[i] += str(ch_num)
                    elif i != len(split_com) - 1:
                        split_com[i] += num
                    ch_string += split_com[i]
                ch_commands.append(ch_string)
            else:
                ch_commands.append(command)

            num = ''
        else:
            ch_commands.append(command)
        k += 1

    ch_f.write('\n'.join(ch_commands) + '\n')