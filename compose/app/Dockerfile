FROM pypy:3

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install --upgrade pip \
    && pip install -r /app/requirements.txt
