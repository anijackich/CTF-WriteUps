# Снова в школу ч.2 - 20
_Решай задачи в удаленном терминале, 50 раундов и флаг твой_

_nc 62.84.118.87 9002_

### Solution
Задача: даны координаты центра окружности и ее радиус. В ответ пришлите количество пересечений этой окружности с осью Ox и Oy. От 0 до 4

Формула окружности: `(x - x0)^2 + (y - y0)^2 = r^2`

Существует 2 случая:
1. При y = 0, `(x - x0)^2 = r^2 - (y0)^2`:
   1. При `r^2 - (y0)^2 > 0`, x будет иметь 2 значения, то есть 2 пересечения с осью OX
   2. При `r^2 - (y0)^2 = 0`, x будет иметь 1 значения, то есть 1 пересечения с осью OX
   3. При `r^2 - (y0)^2 < 0`, x не будет иметь значений, то есть не будет пересечений с осью OX
2. При x = 0, `(x - x0)^2 = r^2 - (y0)^2`:
   1. При `r^2 - (x0)^2 > 0`, y будет иметь 2 значения, то есть 2 пересечения с осью OY
   2. При `r^2 - (x0)^2 = 0`, y будет иметь 1 значения, то есть 1 пересечения с осью OY
   3. При `r^2 - (x0)^2 < 0`, y не будет иметь значений, то есть не будет пересечений с осью OY

Теперь реализуем это в программе:

```python
from pwn import remote

r = remote("62.84.118.87", 9002)

for i in range(49):
    r.recvuntil("Раунд".encode())
    r.recvline()
    x, y, rad = map(int, r.recvline().strip().decode().split(";"))
    count = 0
    if rad ** 2 - y ** 2 > 0:
        count += 2
    elif rad ** 2 - y ** 2 == 0:
        count += 1
    if rad ** 2 - x ** 2 > 0:
        count += 2
    elif rad ** 2 - x ** 2 == 0:
        count += 1
    answer = str(count).encode()
    r.sendline(answer)
r.interactive()
```

Запускаем и получаем флаг: `CTF{oI6cZWXKBl9Ce62c}`