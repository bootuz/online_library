FROM python:3.6
ENV PYTHONUNBUFFERED 1
ENV SECRET_KEY you_never_guess
RUN mkdir /online_library
WORKDIR /online_library
ADD requirements.txt /online_library/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /online_library/