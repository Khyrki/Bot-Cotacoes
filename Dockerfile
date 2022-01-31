FROM python:3.9.5

WORKDIR /app

COPY dev-requirements.txt .

RUN pip install -r dev-requirements.txt

COPY . .

CMD python3 main.py

 