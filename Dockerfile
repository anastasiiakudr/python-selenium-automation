FROM python:3.9-slim

# Установите зависимости
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    gnupg \
    chromium \
    && rm -rf /var/lib/apt/lists/*

# Установите ChromeDriver
RUN CHROME_DRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE) \
    && curl -sS -o /tmp/chromedriver.zip "https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip" \
    && unzip -q /tmp/chromedriver.zip -d /usr/local/bin/ \
    && rm /tmp/chromedriver.zip

# Установите порт дисплея, чтобы избежать краша
ENV DISPLAY=:99

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt



















