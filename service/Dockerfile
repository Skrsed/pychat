# указываем образ python
# TODO: обновить версию
FROM python:3.9

# создаем директорию внутри контейнера
WORKDIR /code

# копируем туда зависимости
COPY ./requirements.txt /code/requirements.txt

# устанавливаем зависимости
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# копируем файлы прокта в контейнер
COPY ./app /code/app

# запускаем сервер используя uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]