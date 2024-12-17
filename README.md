# Detect-Wildfire-Bot

TG bot для определения лесного пожара на спутниковом фото. Под капотом используется собственная модель.

## Запуск бота

### Клонируем репозиторий

`linux`  `window`

```bash
git clone https://github.com/KrakenN7/Ai-Fire-Detectet-Bot.git
```

### Создаём виртуальное окружение

`linux` `windows`

```bash
python3 -m venv venv
```

### Активируем виртуальное окружение

`linux`

```bash
source venv/bin/activate
```

`windows`

```shell
venv\Scripts\activate.ps1
```

### Устанавливаем зависимости

`linux`  `windows`

```bash
pip3 install -r requirements.txt
```

### Создаём .env файл

`linux`

```bash
cp .env.template .env
```

`windows`

```shell
copy .env.template .env
```

В .env надо поместить Token полученый у [BotFather](https://t.me/BotFather)

### Создаём папку data

`linux`  `windows`

```
mkdir data
```

### Запускаем бота

`linux` `windows`

```bash
python3 bot/main.py
```
