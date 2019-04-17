# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
from os import mkdir, rmdir, path


def create_dir(dir_name):
    if path.exists(f'{dir_name}'):
        pass
    else:
        mkdir(f'{dir_name}')


def rm_dir(dir_name):
    if path.exists(dir_name):
        rmdir(dir_name)


for dir_num in range(1, 10):
    create_dir(f'./dir_{dir_num}')

for dir_num in range(1, 10):
    rm_dir(f'./dir_{dir_num}')

# rm_dir()


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
from os import listdir, path, chdir, rmdir

dirs = listdir('./')


# for dir in dirs:
#
#     if path.isfile(dir):
#         pass
#     else:
#         print(dir)

def files_in_dir(dir):
    files = listdir(dir)
    for d in files:
        print(d)


def files_in_dir_whith_num(dir):
    files = listdir(dir)
    for num, d in enumerate(files, 1):
        print(f'{num}. {d}')


def dir_in_dir_whith_num(dir):
    files = listdir(dir)
    dirs = []
    d_dirs = {}
    for d in files:
        if path.isfile(d):
            pass
        else:
            dirs.append(d)
    if len(dirs) > 0:
        for num, d in enumerate(dirs, 1):
            d_dirs.update({f'{num}': f'{d}'})
            print(f'{num}. {d}')

    else:
        return ''
    if d_dirs:
        return d_dirs


def go_to_folder(folder_name):
    chdir(folder_name)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

from sys import argv
from shutil import copyfile

cur_file = argv[0].split('/')[-1]
copy_file = f'{cur_file}.copy2'


def file_copy(from_file, to_file):
    f = open(to_file, 'w')
    copyfile(from_file, to_file)
    f.close()

if __name__ == '__main__':
    file_copy(cur_file, copy_file)
