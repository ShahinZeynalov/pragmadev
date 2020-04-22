FROM python:3.6

COPY requirements.txt /code/requirements.txt

WORKDIR /code

RUN pip install -r requirements.txt

ADD . .

COPY uwsgi.ini /conf/uwsgi.ini

EXPOSE 8000


RUN if [ -f manage.py ]; then python manage.py collectstatic --noinput; fi

#CMD [ "gunicorn", "--bind", "0.0.0.0", "-p", "8000",  "pdproject.wsgi" ]

CMD ["uwsgi", "--ini", "/conf/uwsgi.ini"]
