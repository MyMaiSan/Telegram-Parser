<p align="center">
    <img src="https://gas-kvas.com/grafic/uploads/posts/2024-01/gas-kvas-com-p-logotip-telegram-na-prozrachnom-fone-21.png" width="100px"/>
    <h3 align="center">Telegram Parser</h3>
</p>

<p align="center">
  Парсинг пользователей
  <br/>
  из ваших чатов и каналов
</p>

<p align="center">
    <a href="https://stackoverflow.com/users/23589316/sakurajima-mai">
        <img src="https://img.shields.io/badge/-Stackoverflow-FE7A16?style=for-the-badge&logo=stack-overflow&logoColor=white"/></a>
    <a href="https://www.reddit.com/user/MyMaiSakurajima/">
        <img src="https://img.shields.io/badge/Reddit-%23FF4500.svg?style=for-the-badge&logo=Reddit&logoColor=white"/></a>
    <a href="https://t.me/MyMaiSakurajima">
        <img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"/></a>
    <a href="https://www.twitch.tv/mymaisakurajima">
        <img src="https://img.shields.io/badge/Twitch-%239146FF.svg?style=for-the-badge&logo=Twitch&logoColor=white"/></a>
    <a href="https://steamcommunity.com/id/MyMaiSakurajima/">
        <img src="https://img.shields.io/badge/steam-%23000000.svg?style=for-the-badge&logo=steam&logoColor=white"/></a>
</p>


## ⚡ Использование скрипта

1. Выполняем ```git clone https://github.com/MyMaiSan/Telegram-Parser.git```
2. Получаем ```api_id``` и ```api_hash``` с помощью [этого сайта](https://my.telegram.org/auth)
3. Вставляем полученные данные в ```config.ini```
4. Выполняем ```pip install -r requirements.txt```
5. Запускаем ```parser.py```
6. Вставляем пришедший от Telegram код
7. Выбираем чат, участников которого необходимо спарсить

## 🔧 Добавление проспама
```python
count = 0

message = 'text' #Текст сообщения для проспама
photo = 'photo.png' #Фото для проспама

with open('members.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if count < 5:
            if row[0] != "":
                client.send_file(row[0], photo, caption=message)

            time.sleep(2)
            count += 1

        elif count == 5:
            count = 0
            time.sleep(10)
```
