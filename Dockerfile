FROM python:3.11-slim

# добавьте label, используя переменную среды
LABEL author=${AUTHOR}

# скопируйте файлы в Docker
# название директории внутри контейнера: churn_app
COPY . ./churn_app

# измените рабочую директорию Docker
WORKDIR churn_app

# инструкция для установки библиотек
RUN pip3 install -r requirements.txt

# инструкции для открытия порта, указанного в переменной среды
EXPOSE ${APP_PORT}

# примонтируйте том с моделями
VOLUME /models

# команда запуска, учитывая порт из .env
CMD uvicorn app.churn_app:app --reload --port ${APP_PORT} --host 0.0.0.0