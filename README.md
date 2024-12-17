# Detect-Wildfire-Bot

TG bot для определения лесного пожара на спутниковом фото. Под капотом используется собственная модель.

## Запуск бота

### Клонируем репозиторий

`linux`  `window`

```bash
git clone https://github.com/KrakenN7/Ai-Fire-Detectet-Bot.git
```

### Создаём виртуальное окружение

`linux`

```bash
    python3 -m venv venv
```

`windows`

```shell
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

`linux`

```bash
    pip3 install -r requirements.txt
```

`windows`

```shell
    pip install -r requirements.txt
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

### Запускаем бота

`linux`

```bash
    python3 bot/main.py
```

`windows`

```shell
    python3 bot/main.py
```
