"""
7. Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1. Примеры запуска скриптов:

python add_sale.py 5978,5
python add_sale.py 8914,3
python add_sale.py 7879,1
python add_sale.py 1573,7
python show_sales.py
5978,5
8914,3
7879,1
1573,7
python show_sales.py 3
7879,1
1573,7
python show_sales.py 1 3
5978,5
8914,3
7879,1

7. * (вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта: передаём ему номер
записи и новое значение. При этом файл не должен читаться целиком — обязательное требование. Предусмотреть ситуацию,
когда пользователь вводит номер записи, которой не существует.
"""

import sys

if __name__ == '__main__':
    args = sys.argv
    with open("bakery.csv", "r", encoding="utf-8") as f:
        if len(args) == 1:
            for r in f.readlines():
                print(r.replace("\n", ""))
        elif len(args) == 2:
            f.seek(11*(int(args[1]) - 1))
            for r in f.readlines():
                print(r.replace("\n", ""))
        elif len(args) == 3:
            f.seek(11 * (int(args[1]) - 1))
            for r in f.readlines()[:int(args[2]) - int(args[1]) + 1]:
                print(r.replace("\n", ""))
