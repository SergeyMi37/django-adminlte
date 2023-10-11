FROM python:3.9

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
# install python dependencies
RUN pip install --upgrade pip

RUN apt-get update && apt-get install -y wget && \
 apt-get install -y gettext

RUN wget --continue https://github.com/intersystems-community/iris-driver-distribution/raw/main/DB-API/intersystems_irispython-3.2.0-py3-none-any.whl && \
    pip install intersystems_irispython-3.2.0-py3-none-any.whl && \
    rm intersystems_irispython-3.2.0-py3-none-any.whl

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# running migrations
RUN python manage.py migrate
RUN python manage.py createsuperuser --noinput --username adm --email adm@mswhost.com
RUN python manage.py createsuperuser --noinput --username developer --email dev@mswhost.com
RUN python manage.py loaddata db-init-param.json
# gunicorn
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "core.wsgi"]
