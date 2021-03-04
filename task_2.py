"""
1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список
кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:

[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]

Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего
задания.

Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами, размер
которых превышает объем ОЗУ компьютера.
"""

import sys

# ---Код для получения файла по ссылке
import requests
# site = "https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs"
# data = requests.get(site)
# s = data.text
# data.close()
# -------------------

# ---Генератор большого файла
# for _ in range(1000):
#     with open("nginx_logs.txt", "a", encoding="utf-8") as log_file:
#         log_file.write(s)
# -------------------

# Парсим данные и записываем в файл на лету,
# т.к. при большом рамере файла данных размер словаря может превысить объем ОЗУ
with open("nginx_logs.txt", "r", encoding="utf-8") as log_file:
    with open("nginx_logs_parce.txt", "w", encoding="utf-8") as parce_file:
        while True:
            txt = log_file.readline()
            if txt == '':
                break
            st = txt.split()
            t1 = st[5].replace('"', '')
            parce_file.writelines([f"{st[0]} {t1} {st[6]}\n"])
print("Парсинг завершен, результат в файле 'nginx_logs_parce.txt'")

# Из полученного файла nginx_logs_parce получаем словарь вида: {"уникальныq IP адрес": колличество его повторений}
# читаем данные последовательно, чтобы не превысить объем ОЗУ
with open("nginx_logs_parce.txt", "r", encoding="utf-8") as log_file:
    ip_count_dict = {}
    while True:
        txt = log_file.readline()
        if txt == '':
            break
        v = txt.split()[0]
        if ip_count_dict.get(v):
            ip_count_dict[v] = ip_count_dict.get(v) + 1
        else:
            ip_count_dict[v] = 1
print("Подсчет колличества запросов от IP завершен")
print(f"Размер в байтах словаря уникальных IP адресов: {sys.getsizeof(ip_count_dict)}")

# Если нужна сортировка словаря IP адресов по колличеству обращений:
ip_count_dict = {k: ip_count_dict[k] for k in sorted(ip_count_dict, key=ip_count_dict.get, reverse=True)}
# print(ip_count_dict)

# Нахождение IP с наибольшим колличеством запросов
max_ip = [0, 0]
for key, val in ip_count_dict.items():
    if val > max_ip[1]:
        max_ip[1] = val
        max_ip[0] = key
print(f"А вот и спамер года: IP {max_ip[0]} с колличеством запросов {max_ip[1]}")

