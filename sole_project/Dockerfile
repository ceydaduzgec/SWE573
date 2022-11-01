FROM python:3.10.2 as base
ENV PYTHONBUFFERED=1

WORKDIR /sole

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


COPY . .
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]