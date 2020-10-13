FROM python:3.7-alpine

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]