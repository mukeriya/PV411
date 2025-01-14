total_seconds_in_day = 24 * 60 * 60

seconds_passed = int(input("Vvedi kol-vo sekund: "))
if seconds_passed > total_seconds_in_day or seconds_passed < 0:
    print('Invalid value')
    exit()

print('1. In hours')
print('2. In minutes')
print('3. In seconds')

choice = input("Select: ")

remaining_seconds = total_seconds_in_day - seconds_passed

if choice == '1':
    print(remaining_seconds / 60 / 60)
elif choice == '2':
    print(remaining_seconds / 60)
elif choice == '3':
    print(remaining_seconds)
else:
    print('Invalid menu item')
