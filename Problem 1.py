needed_experience = float(input())
battles_count = int(input())

curr_exp = 0
curr_battle = 1

for i in range(0, battles_count):
    experience = float(input())

    if (i + 1) % 3 == 0:
        curr_exp += experience + (experience * 0.15)

    elif (i + 1) % 5 == 0:
        curr_exp += experience - (experience * 0.1)

    elif (i + 1) % 15 == 0:
        curr_exp += experience + (experience * 0.05)

    else:
        curr_exp += experience

    curr_battle = i + 1

    if curr_exp >= needed_experience:
        break

if curr_exp < needed_experience:
    print(f'Player was not able to collect the needed experience, {(needed_experience - curr_exp):.2f} more needed.')
else:
    print(f'Player successfully collected his needed experience for {curr_battle} battles.')
