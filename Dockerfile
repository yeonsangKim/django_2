FROM python:3.9.0

WORKDIR /home/


RUN git clone https://github.com/yeonsangKim/django_2.git


RUN echo "django-insecure-o@6hnon*ecf)=#2nn=3nfgl6yf*%nhc8i)mt!3z1_jl&acv1o7"  > .env

RUN pip install -r requirements.txt

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]