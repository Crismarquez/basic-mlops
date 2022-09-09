FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install -U pip && pip install -r requirements.txt

COPY api/ ./api

COPY config/ ./config

COPY store/models/model.pkl ./store/models/model.pkl

COPY initializer.sh .

RUN chmod +x initializer.sh

EXPOSE 8000

ENTRYPOINT ["./initializer.sh"]