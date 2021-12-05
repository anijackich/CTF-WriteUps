# Zip Random
[random.zip](random.zip)

### Solution
В архиве представлены 2 файла: зашифрованный флаг и бинарный исполняемый файл, шифрующий флаг. Методами обратной разработки, обнаруживаем, что каждый байт флага ксорится с ключом (результат вызова функции rand()). Следовательно нам необходимо восстановить ключ. Для этого нужно знать время, когда запускалась программа (для восстановления сида). 

С помощью утилиты `exiftool` узнаём, что архив был создан `Zip Modify Date: 2021:11:27 22:16:22`. Переводим время в unix формат: 1638033382

Теперь напишем скрипт, который инициализирует сид с данным временем и будет перебирать их (мы знаем, что флаг начинается с MSKCTF)

```python
from ctypes import CDLL

libc = CDLL("libc.so.6")
secs = 1638033382
file = list(open('flag.enc', 'rb').read())
while True:
    libc.srand(secs)
    res = file.copy()
    for i in range(0, len(file)):
        res[i] ^= libc.rand() % 255
    res = "".join(map(chr, res))
    if res.startswith("MSKCTF"):
        print(res)  # time is 1638033381
        break
    secs -= 1
```

Запускаем и получаем флаг: `MSKCTF{l1ter4ll9_r4ndom_fl4g_1n_rand0m_x0r}`