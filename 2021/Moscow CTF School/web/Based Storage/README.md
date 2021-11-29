# Based Storage
_http://based-storage.tasks.2021.ctf.cs.msu.ru/_


### Solution
В исходном коде (а именно в [storage.js](src/storage/storage.js)) наблюдаем интересную операцию:
```javascript
return path.resolve(this.dir, Buffer.from(filename).toString('base64'))
```

Все кажется надежным... если не знать, что в base64 есть символ '/' и что path.resolve без проблем переходит в другую директорию.

Зная, что флаг лежит в /app/flag, пытаемся подобрать такую комбинацию из слэшей, чтобы base64 был валидным и чтобы все байты строки можно было посылать.

*Райтап будет дописан*
`
Flag: MSKCTF{TO BE REDACTED}
`
