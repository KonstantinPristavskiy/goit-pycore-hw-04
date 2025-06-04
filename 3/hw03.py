import sys
from pathlib import Path
import colorama
from colorama import Fore, Style

# ініціалізувати колораму
colorama.init(autoreset=True)

# робимо список кольорів
LEVEL_COLORS = [
    Fore.RED,
    Fore.GREEN,
    Fore.YELLOW,
    Fore.BLUE,
    Fore.MAGENTA,
    Fore.CYAN,
]


def print_color(text, level):

    # кількість відступів
    indent = "   " * level

     # вибираємо колір, якщо кольори закінчились -- починаємо з початку списку
    color = LEVEL_COLORS[level % len(LEVEL_COLORS)]

    # виводимо прінт з кольором і після цього видаляємо налаштування кольору
    print(f"{indent}{color}{text}")


def iterate_through_folder(folder_path, level):
    # для кожного файлу і папки у переданій папці
    for path in folder_path.iterdir():
            # якщо елемент -- папка, виводимо її і рекурсивно проходимо її вміст
            if path.is_dir():
                 print_color(path.relative_to(folder_path), level)
                 iterate_through_folder(path, level+1)
            else:
                 # якщо це файл -- просто його виводимо
                 print_color(path.relative_to(folder_path), level)



def main():
    if len(sys.argv) > 1:
        # 0 аргумент -- назва файлу, тому передаємо елемент 1, який має бути абсолютним шляхом до папки
        absolute_path = Path(sys.argv[1])
        level = 0
        print_color(absolute_path.name, level)
        iterate_through_folder(absolute_path, level+1)



if __name__ == "__main__":
    main()