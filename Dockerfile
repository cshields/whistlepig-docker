FROM phusion/baseimage:0.9.10
MAINTAINER cshields@mozilla.com

# Start with a fresh, up to date system
RUN apt-get update -y

# Install dependencies
RUN apt-get install -y python git python-setuptools mysql-client libmysqlclient-dev python-dev python-pip

# Populate the app data, install python packages, and syncdb
RUN git clone --recursive git://github.com/rtucker-mozilla/WhistlePig /data/WhistlePig
ADD local.py /data/WhistlePig/whistlepig/settings/local.py
WORKDIR /data/WhistlePig/
RUN pip install -r /data/WhistlePig/requirements/compiled.txt
RUN /data/WhistlePig/manage.py syncdb --noinput

EXPOSE 8000

# let's do this!
CMD ["/data/WhistlePig/manage.py", "runserver", "0.0.0.0:8000"]
