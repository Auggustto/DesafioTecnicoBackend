FROM python:3.9

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN chmod +x /app/run_tests.sh

EXPOSE 80

CMD ["python3", "main.py", "--host", "0.0.0.0", "--port", "80"]