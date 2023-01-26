FROM python:3.10.9-alpine3.17

ENV PYTHONUNBUFFERED = 1

WORKDIR /ReservasHotel

RUN  apk update \
	&& pip install --upgrade pip

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

CMD ["python", "manage.py","runserver", "0.0.0.0:8000"]
