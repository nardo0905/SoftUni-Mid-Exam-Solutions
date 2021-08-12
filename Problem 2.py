parts = input().split('|')

command = input()

while not command == 'Done':

    command_data = command.split()

    if command == 'Check Even':
        for i in range(0, len(parts)):
            if i % 2 == 0:
                print(parts[i], end=' ')
        print()

    if command == 'Check Odd':
        for i in range(0, len(parts)):
            if not i % 2 == 0:
                print(parts[i], end=' ')
        print()

    if command_data[0] == 'Add':
        particle = command_data[1]
        index = int(command_data[2])
        if index < 0 or index > len(parts)-1:
            command = input()
            continue
        parts.insert(index, particle)

    if command_data[0] == 'Remove':
        index = int(command_data[1])
        if index < 0 or index > len(parts)-1:
            command = input()
            continue
        parts.remove(parts[index])

    command = input()

print(f'You crafted {"".join(parts)}!')
