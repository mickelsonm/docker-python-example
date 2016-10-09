FROM python:2.7

COPY main.py /tmp/main.py

CMD ["python", "/tmp/main.py"]
