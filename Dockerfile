# Dockerfile - this is a comment. Delete me if you want.
FROM python:3.9.0a5
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["macServer.py"]
