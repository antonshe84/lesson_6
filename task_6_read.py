"""
6. Реализовать простую систему хранения данных о суммах продаж булочной. Должно быть два скрипта с интерфейсом
командной строки: для записи данных и для вывода на экран записанных данных. При записи передавать из командной
строки значение суммы продаж. Для чтения данных реализовать в командной строке следующую логику:
просто запуск скрипта — выводить все записи;
запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер, равный второму
числу, включительно.
"""

import sys

if __name__ == '__main__':
    args = sys.argv
    with open("bakery.csv", "r", encoding="utf-8") as f:
        if len(args) == 1:
            for s in f.readlines():
                s = s.replace("\n", "")
                print(float(s))
        elif len(args) == 2:
            for s in f.readlines()[int(args[1]) - 1:]:
                s = s.replace("\n", "")
                print(float(s))
        elif len(args) == 3:
            for s in f.readlines()[int(args[1]) - 1:int(args[2])]:
                s = s.replace("\n", "")
                print(float(s))
