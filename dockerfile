FROM python:3.10.12

WORKDIR /flask_api

COPY . .

RUN pip install -r requirements.txt

ENV MONGO_DB_URI=${MONGO_DB_URI}
ENV MONGO_DB_NAME=${MONGO_DB_NAME}

EXPOSE ${PORT}

CMD ["python", "app/index.py", "-"]