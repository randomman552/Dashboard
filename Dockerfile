FROM python:3.10.2-alpine

ENV DASHBOARD_PORT=80
ENV DASHBOARD_DATA_PATH=/data

COPY requirements.txt /
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app

EXPOSE $DASHBOARD_PORT

ENTRYPOINT [ "./gunicorn.sh" ]