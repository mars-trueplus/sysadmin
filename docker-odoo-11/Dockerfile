FROM ubuntu:17.10

ENV LANG C.UTF-8

ENV DEBIAN_FRONTEND=noninteractive

COPY ./requirements.txt /



# RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

# Dependencies
RUN apt-get update \
	&& apt-get -y install --no-install-recommends \
		wget \
		apt-utils \
		ca-certificates \
	    wkhtmltopdf \
		python3-pip \
		python3-setuptools \
		python3-renderpm \
        libssl1.0-dev \
        xz-utils \
	&& apt-get -y install build-essential \
		autoconf \
		libtool \
		python-dev \
#	&& pip3 install wheel
#	&& pip3 install -r requirements.txt

RUN apt-get update \
	&& apt-get install -y npm \
	&& npm install -g less

# Odoo source
RUN wget https://nightly.odoo.com/11.0/nightly/src/odoo_11.0.latest.tar.gz | tar xz odoo_11.0.latest.tar.gz

RUN mkdir -p /odoo/datadir/odoo_11 \
	&& chown -R odoo /odoo/datadir/odoo_11 \
	&& mkdir -p /odoo/extra_addons/odoo_11

# save filestore to persitent folder
VOLUME ["/odoo/datadir/odoo_11"]

EXPOSE 8070:8070

COPY ./odoo_11.conf /odoo/config/odoo_11.conf

USER odoo

RUN echo '&&&&&&&&&&&#####################@@@@@@@@@@@@@@@@@@@@@@'
RUN apt-cache policy apt-utils
	
	