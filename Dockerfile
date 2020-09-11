FROM ubuntu:18.04 as main
# Install general dependencies
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y \
    python3 \
    python3-pip \
    python3-all \
    build-essential \
    libssl-dev \
    libpq-dev \
    libjpeg-dev \
    libffi-dev \
    libxml2-dev \
    libxslt1-dev \
    gcc \
    musl-dev
# Install python dependencies
RUN apt-get install -y nginx uwsgi uwsgi-plugin-python3
# Remove unnecessary files
RUN apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
# Install and create virtual env
RUN pip3 install virtualenv
RUN virtualenv -p python3 /opt/app/env
# Install packaging tools
RUN /opt/app/env/bin/pip install -U pip setuptools wheel
# Copy flask application to a relevant folder
RUN mkdir -p /opt/app/src
COPY ./server /opt/app/src/server
WORKDIR /opt/app/src/server
RUN /opt/app/env/bin/python setup.py bdist_wheel
# Install flask app into local virtual env from built package
RUN /opt/app/env/bin/pip install /opt/app/src/server/dist/*.whl
RUN rm -rf /opt/app/src

RUN mkdir -p /opt/app/alembic
WORKDIR /opt/app/alembic
COPY ./server/migrations /opt/app/alembic/migrations
COPY ./server/alembic.ini /opt/app/alembic

# Copy infra files for uwsgi
COPY ./infrastructure/uwsgi/uwsgi.ini /etc/uwsgi/apps-enabled/test-api-uwsgi.ini
# Copy infra files for nginx and create a link
COPY infrastructure/nginx/nginx.conf /etc/nginx/sites-available/test-api
RUN ln -s /etc/nginx/sites-available/test-api /etc/nginx/sites-enabled
# Copy entrypoint script
COPY ./infrastructure/run.sh /run.sh

RUN chmod +x /run.sh
# Execute
ENTRYPOINT ["/run.sh"]
# Expose ports
EXPOSE ${APP_PORT}
# Start uwsgi app
CMD ["uwsgi", "--ini", "/etc/uwsgi/apps-enabled/test-api-uwsgi.ini"]
