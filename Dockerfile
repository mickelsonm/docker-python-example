FROM elyase/staticpython

COPY main.py /main.py

CMD ["python", "/main.py"]
