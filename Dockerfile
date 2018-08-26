FROM python:3.6
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "test.py", "@namba_taxi_bot"]