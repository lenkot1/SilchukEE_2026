import os
import random
import msvcrt

from colorama import init, Fore, Style

init(autoreset=True)

WIDTH = 40
HEIGHT = 20

WALL = Fore.RED + "█" + Style.RESET_ALL
WATER = Fore.BLUE + "~" + Style.RESET_ALL
FOG = "▒"

PLAYER = Fore.YELLOW + "@" + Style.RESET_ALL
DOLPHIN = Fore.CYAN + "▷" + Style.RESET_ALL

SHARK = Fore.RED + "𓂁" + Style.RESET_ALL
TRAP = Fore.LIGHTBLUE_EX + "※" + Style.RESET_ALL

FISH_1 = Fore.CYAN + "$" + Style.RESET_ALL
FISH_2 = Fore.GREEN + ">" + Style.RESET_ALL
FISH_3 = Fore.LIGHTMAGENTA_EX + "&" + Style.RESET_ALL

PORTAL = Fore.MAGENTA + "O" + Style.RESET_ALL
PORTAL_KEY = Fore.LIGHTYELLOW_EX + "!" + Style.RESET_ALL

KEY_1 = Fore.LIGHTCYAN_EX + "⚷" + Style.RESET_ALL
KEY_2 = Fore.LIGHTGREEN_EX + "⚷" + Style.RESET_ALL
KEY_3 = Fore.LIGHTRED_EX + "⚷" + Style.RESET_ALL

CHEST = Fore.WHITE + "⌂" + Style.RESET_ALL
SWORD = Fore.RED + "️/" + Style.RESET_ALL
POTION = Fore.GREEN + "𖠞" + Style.RESET_ALL

player_x, player_y = 1, 1
player_hp = 100
inventory = []
fish_collection = []
secrest_chest_id = random.randint(1, 3)
'''
vertical_walls = sorted(random.sample(range(5, WIDTH - 5), 3))
horizontal_walls = sorted(random.sample(range(4, HEIGHT - 4), 2))
'''
vertical_walls = [10, 20, 30]
horizontal_walls = [6, 13]
maze = []
for y in range(HEIGHT):
    row = []
    for x in range(WIDTH):
        if y == 0 or y == HEIGHT - 1 or x == 0 or x == WIDTH - 1:
            row.append(WALL)
        else:
            row.append(WATER)
    maze.append(row)

for x in vertical_walls:
    for y in range(1, HEIGHT - 1):
        maze[y][x] = WALL

for y in horizontal_walls:
    for x in range(1, WIDTH - 1):
        maze[y][x] = WALL
'''
for x in vertical_walls:
    for door_y in random.sample(range(1, HEIGHT - 1), 2):
        maze[door_y][x] = WATER
        if door_y + 1 < HEIGHT - 1:
            maze[door_y + 1][x] = WATER

for y in horizontal_walls:
    for door_x in random.sample(range(1, WIDTH - 1), 3):
        maze[y][door_x] = WATER
        if door_x + 1 < WIDTH - 1:
            maze[y][door_x + 1] = WATER

for y in range(1, 4):
    for x in range(1, 4):
        if maze[y][x] == WALL:
            maze[y][x] = WATER
'''
'''
for x in vertical_walls:
    for y in horizontal_walls:
        maze[y][x] = WATER
        if y + 1 < HEIGHT - 1:
            maze[y + 1][x] = WATER
        if y - 1 > 0:
            maze[y - 1][x] = WATER
        if x + 1 < WIDTH - 1:
            maze[y][x + 1] = WATER
        if x - 1 > 0:
            maze[y][x - 1] = WATER
for x in vertical_walls:
    for door_y in (4, 10, 16):
        if door_y < HEIGHT - 1:
            maze[door_y][x] = WATER
for y in horizontal_walls:
    for door_x in (10, 20, 30):
        if door_x < WIDTH - 1:
            maze[y][door_x] = WATER
for y in range(1, 4):
    for x in range(1, 4):
        if maze[y][x] == WALL:
            maze[y][x] = WATER
'''



maze = []
for y in range(HEIGHT):
    row = []
    for x in range(WIDTH):
        if y == 0 or y == HEIGHT - 1 or x == 0 or x == WIDTH - 1:
            row.append(WALL)
        elif y % 2 == 0 and x % 2 == 0:
            row.append(WALL)
        else:
            row.append(WATER)
    maze.append(row)

for y in range(1, HEIGHT - 1):
    for x in range(1, WIDTH - 1):
        if maze[y][x] == WATER and random.random() < 0.28:
            maze[y][x] = WALL

for y in range(2, HEIGHT - 2, 2):
    for x in range(2, WIDTH - 2, 2):
        doors = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 < x+dx < WIDTH - 1 and 0 < y+dy < HEIGHT - 1:
                doors.append((x+dx, y+dy))
        if doors:
            door_x, door_y = random.choice(doors)
            maze[door_y][door_x] = WATER

for y in range(1, 4):
    for x in range(1, 4):
        maze[y][x] = WATER



for x in vertical_walls:
    for door_y in (4, 10, 16):
        if door_y < HEIGHT - 1:
            maze[door_y][x] = WATER
for y in horizontal_walls:
    for door_x in (10, 20, 30):
        if door_x < WIDTH - 1:
            maze[y][door_x] = WATER
for y in range(1, 4):
    for x in range(1, 4):
        if maze[y][x] == WALL:
            maze[y][x] = WATER

def place_item(item, count = 1, restrict_to_rooms = False):
    for _ in range(count):
        while True:
            x = random.randint(1, WIDTH - 2)
            y = random.randint(1, HEIGHT - 2)

            if maze[y][x] == WATER and (x > 5 or y > 5):
                if restrict_to_rooms:
                    pass
                    #if x in vertical_walls or y in horizontal_walls:
                        #continue
                maze[y][x] = item
                break

place_item(CHEST, count=3, restrict_to_rooms=True)
place_item(TRAP, count=4, restrict_to_rooms=True)
place_item(PORTAL, count=1, restrict_to_rooms=True)

place_item(KEY_1, count=1, restrict_to_rooms=True)
place_item(KEY_2, count=1, restrict_to_rooms=True)
place_item(KEY_3, count=1, restrict_to_rooms=True)

place_item(FISH_1, count=1, restrict_to_rooms=True)
place_item(FISH_2, count=1, restrict_to_rooms=True)
place_item(FISH_3, count=1, restrict_to_rooms=True)

place_item(SWORD, count=1, restrict_to_rooms=True)
place_item(POTION, count=3, restrict_to_rooms=True)

place_item(SHARK, count=4, restrict_to_rooms=False)
place_item(DOLPHIN, count=1, restrict_to_rooms=False)



def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_game():
    clear_screen()
    print(f"❤️ HP: {player_hp}")
    print(f"🎒 Инвентарь: {inventory}")
    print(f"🐠 Коллекция рыб: {fish_collection}\n")

    for y in range(HEIGHT):
        row_str = ""
        for x in range(WIDTH):
            if x == player_x and y == player_y:
                row_str += PLAYER + " "
            elif abs(x - player_x) <= 3 and abs(y - player_y) <= 3:
                row_str += maze[y][x] + " "
            else:
                row_str += FOG + " "
        print(row_str)

    print("\n" + "-" * 50)
    print("Управление:")
    print("[W/A/S/D] - Ход прямо. [Q/E/Z/C] - По диагонали")
    print("[I] - Управление инвентарем (выкинуть по ID)")
    print("[X] - Выйти из игры")
    print("-" * 50)

def manage_inventory():
    while True:
        clear_screen()
        print("=== МЕНЮ ИНВЕНТАРЯ ===")
        if not inventory:
            print("Ваш инвентарь пуст.")
        else:
            for idx, item in enumerate(inventory):
                print(f"[{idx}] - {item}")

        print("\nДействия:")
        print("1. Сортировать инвентарь (sort)")
        print("2. Перевернуть инвентарь (reverse)")
        print("3. Удалить предмет по его ID (pop)")
        print("0. Вернуться в игру")

        choice = input("\nВыберите действие: ").strip()

        if choice == "1":
            inventory.sort()
        elif choice == "2":
            inventory.reverse()
        elif choice == "3":
            if not inventory:
                print("Нечего удалять!")
                input("Нажмите Enter...")
                continue
            try:
                item_id = int(input("Введите ID (число) предмета для удаления: "))
                removed = inventory.pop(item_id)
                print(f"Вы выбросили: {removed}")
            except (ValueError, IndexError):
                print("Неверный ID! Введите существующий номер.")
            input("Нажмите Enter...")
        elif choice == "0":
            break

def move_sharks():
    global player_hp, player_x, player_y
    all_sharks = []

    for y in range(1, HEIGHT - 1):
        for x in range(1, WIDTH - 1):
            if maze[y][x] == SHARK:
                all_sharks.append((x, y))

    for sx, sy in all_sharks:

        dx = 1 if player_x > sx else (-1 if player_x < sx else 0)
        dy = 1 if player_y > sy else (-1 if player_y < sy else 0)

        new_sx = sx + dx
        new_sy = sy + dy

        if maze[new_sy][new_sx] == WATER:
            maze[sy][sx] = WATER

            dist_x = abs(new_sx - player_x)
            dist_y = abs(new_sy - player_y)
            maze[new_sy][new_sx] = SHARK
            if (abs(new_sx - player_x) == 1 and new_sy == player_y) or (abs(new_sy - player_y) == 1 and new_sx == player_x):
                if "⚔️ Меч" in inventory:
                    maze[new_sy][new_sx] = WATER
                    print("\n🦈 Вы наткнулись на акулу и отбились от неё мечом! (●'◡'●)")
                    input("Нажмите Enter...")
                else:
                    player_hp -= 30
                    maze[new_sy][new_sx] = WATER
                    print("\n🦈 Акула догнала вас и укусила! -30 HP")
                input("Нажмите Enter...")
            else:
                maze[new_sy][new_sx] = SHARK

running = True
while running:
    if player_hp <= 0:
        clear_screen()
        print("☠️ Вы погибли и пошли на корм акулам! Конец игры. (¬_¬')")
        break

    draw_game()

    key_pressed = msvcrt.getch().decode('utf-8', errors='ignore').lower()

    if key_pressed == 'x':
        clear_screen()
        print("=== ВЫХОД ИЗ ИГРЫ ===")
        choice = input("Вы точно хотите выйти? (0 - да, 1 - нет): ")
        if choice == "0":
            print("Выход из игры... До встречи!")
            break
        else:
            continue
    if key_pressed == 'i':
        manage_inventory()
        continue

    next_x, next_y = player_x, player_y
    if key_pressed == 'w': next_y -= 1
    elif key_pressed == 's': next_y += 1
    elif key_pressed == 'a': next_x -= 1
    elif key_pressed == 'd': next_x += 1
    elif key_pressed == 'q': next_y -= 1; next_x -= 1
    elif key_pressed == 'e': next_y -= 1; next_x += 1
    elif key_pressed == 'z': next_y += 1; next_x -= 1
    elif key_pressed == 'c': next_y += 1; next_x += 1
    else: continue

    cell = maze[next_y][next_x]

    if cell == WALL:
        continue

    player_x, player_y = next_x, next_y


    if cell == KEY_1:
        inventory.append("Ключ №1")
        maze[player_y][player_x] = WATER
    elif cell == KEY_2:
        inventory.append("Ключ №2")
        maze[player_y][player_x] = WATER
    elif cell == KEY_3:
        inventory.append("Ключ №3")
        maze[player_y][player_x] = WATER

    elif cell == CHEST:

        if "Ключ №1" in inventory:
            inventory.remove("Ключ №1")
            maze[player_y][player_x] = WATER
            if secrest_chest_id == 1:
                inventory.append("🔑 Ключ от портала")
                print("\n📦 Вы открыли сундук ключом №1 и нашли внутри ключ от портала!")
            else:
                inventory.append("Сокровище из сундука")
                print("\n📦 Вы открыли сундук ключом №1 и нашли сокровище!")
            input("Enter...")
        elif "Ключ №2" in inventory:
            inventory.remove("Ключ №2")
            maze[player_y][player_x] = WATER
            if secrest_chest_id == 2:
                inventory.append("🔑 Ключ от портала")
                print("\n📦 Вы открыли сундук ключом №2 и нашли внутри ключ от портала!")
            else:
                inventory.append("Сокровище из сундука")
                print("\n📦 Вы открыли сундук ключом №2 и нашли сокровище!")
            input("Enter...")
        elif "Ключ №3" in inventory:
            inventory.remove("Ключ №3")
            maze[player_y][player_x] = WATER
            if secrest_chest_id == 3:
                inventory.append("🔑 Ключ от портала")
                print("\n📦 Вы открыли сундук ключом №3 и нашли внутри ключ от портала!")
            else:
                inventory.append("Сокровище из сундука")
                print("\n📦 Вы открыли сундук ключом №3 и нашли сокровище!")
            input("Enter...")
        else:
            print("\n📦 Сундук заперт! Нужен любой Ключ от сундука.")
            input("Enter...")

    elif cell == FISH_1:
        fish_collection.append("🐠 Золотая рыбка")
        maze[player_y][player_x] = WATER
    elif cell == FISH_2:
        fish_collection.append("🐡 Рыба-фугу")
        maze[player_y][player_x] = WATER
    elif cell == FISH_3:
        fish_collection.append("🦈 Синий марлин")
        maze[player_y][player_x] = WATER

    elif cell == SWORD:
        inventory.append("⚔️ Меч")
        maze[player_y][player_x] = WATER
        print("\n⚔️ Вы нашли Оружие! Теперь акулы при встрече погибают ╰(*°▽°*)╯.")
        input("Enter...")

    elif cell == POTION:
        player_hp = min(100, player_hp + 30)
        maze[player_y][player_x] = WATER
        print("\n🧪 Вы выпили зелье исцеления. +30 HP! o((>ω< ))o")
        input("Enter...")

    elif cell == TRAP:
        player_hp -= 25
        maze[player_y][player_x] = WATER
        print("\n💥 Бабах! Вы наступили на ловушку в комнате. -25 HP! o(≧口≦)o")
        input("Enter...")

    elif cell == DOLPHIN:
        player_hp = min(100, player_hp + 40)
        maze[player_y][player_x] = WATER
        print("\n🐬 Дружелюбный дельфин подлечил вас на +40 HP! (❁´◡`❁)")
        input("Enter...")

    elif cell == SHARK:
        maze[player_y][player_x] = WATER
        if "⚔️ Меч" in inventory:
            maze[player_y][player_x] = WATER
            print("\n⚔️ Вы наткнулись на акулу и отбились от неё мечом! (●'◡'●)")
        else:
            player_hp -= 40
            print("\n🦈 Акула покусала вас! -40 HP (┬┬﹏┬┬)")
        input("Enter...")
        continue

    elif cell == PORTAL:
        if "🔑 Ключ от портала" in inventory:
            clear_screen()
            print("🎉 ПОБЕДА!!! Вы нашли ключ, открыли портал и успешно сбежали из лабиринта! 🎉 o(*^＠^*)o")
            print(f"Ваша коллекция достижений: {fish_collection}")
            break
        else:
            print("\n🌀 Это выход-портал! Но он заперт. Найдите Ключ от портала!")
            input("Enter...")

    move_sharks()