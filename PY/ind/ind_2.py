import os
import argparse


def print_tree(dir_path, level=0):
    """
    Выводит дерево каталогов и файлов начиная с указанной директории
    """
    # Выводим имя текущей папки с отступом в зависимости от уровня вложенности
    print(' ' * level * 4 + os.path.basename(dir_path) + '/')

    # Увеличиваем уровень вложенности
    level += 1

    # Обходим все элементы в текущей папке
    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)

        # Если это папка, вызываем функцию рекурсивно для неё
        if os.path.isdir(item_path):
            print_tree(item_path, level)

        # Если это файл, выводим его имя с отступом в зависимости от уровня вложенности
        else:
            print(' ' * level * 4 + item)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Утилита вывода дерева каталогов файловой системы')
    parser.add_argument('dir', metavar='DIR', type=str, nargs='?', default='.', help='Директория, для которой нужно вывести дерево')
    parser.add_argument('-d', '--depth', type=int, default=-1, help='Глубина рекурсии')
    args = parser.parse_args()

    print(args.dir)
    print_tree(args.dir, args.depth)