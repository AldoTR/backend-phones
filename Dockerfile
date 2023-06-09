FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /phones
WORKDIR /phones
COPY requirements.txt /phones/
RUN pip install -r requirements.txt
COPY . /phones/
CMD python manage.py runserver --settings=settings.production 0.0.0.0:8080
