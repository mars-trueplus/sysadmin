FROM debian:stretch
MAINTAINER Odoo S.A. <info@odoo.com>

# Install some deps, lessc and less-plugin-clean-css, and wkhtmltopdf
RUN set -x; \
        apt-get update \
        && apt-get install -y --no-install-recommends \
            ca-certificates \
            curl \
            node-less \
            python3-pip \
            python3-setuptools \
            python3-renderpm \
            libssl1.0-dev \
            xz-utils \
        && curl -o wkhtmltox.tar.xz -SL https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz \
        && echo '3f923f425d345940089e44c1466f6408b9619562 wkhtmltox.tar.xz' | sha1sum -c - \
        && tar xvf wkhtmltox.tar.xz \
        && cp wkhtmltox/lib/* /usr/local/lib/ \
        && cp wkhtmltox/bin/* /usr/local/bin/ \
        && cp -r wkhtmltox/share/man/man1 /usr/local/share/man/

# Install Odoo
ENV ODOO_VERSION 11.0
ENV ODOO_RELEASE 20171013
RUN set -x; \
        curl -o odoo.deb -SL http://nightly.odoo.com/${ODOO_VERSION}/nightly/deb/odoo_${ODOO_VERSION}.${ODOO_RELEASE}_all.deb \
        && echo '596e01ef47fda076f086791a12eb360af42d9a14 odoo.deb' | sha1sum -c - \
        && dpkg --force-depends -i odoo.deb \
        && apt-get update \
        && apt-get -y install -f --no-install-recommends \
        && rm -rf /var/lib/apt/lists/* odoo.deb

# Copy entrypoint script and Odoo configuration file
COPY ./entrypoint.sh /
RUN chown odoo /entrypoint.sh \
        && chmod +x /entrypoint.sh
COPY ./odoo-11.conf /odoo/config/
RUN chown odoo /odoo/config/odoo-11.conf

# Mount /var/lib/odoo to allow restoring filestore and /odoo/extra-addons for users addons
RUN mkdir -p /odoo/extra-addons \
        && chown -R odoo /odoo/extra-addons \
        && mkdir -p /odoo/datadir/odoo_11 \
        && chown -R odoo /odoo/datadir/odoo_11

VOLUME ["/odoo/datadir/odoo_11", "/odoo/extra-addons/odoo_11"]

# Expose Odoo services, port in  docker-compose file must be use it
EXPOSE 8069

# Set the default config file
ENV ODOO_RC /etc/odoo/odoo-11.conf

# Set default user when running the container
USER odoo

ENTRYPOINT ["/entrypoint.sh"]
CMD ["odoo"]

ENV POSTGRESQL_PORT_NUMBER="odoo" \
    POSTGRESQL_HOST="postgresql" \
    POSTGRESQL_USER="odoo" \
    POSTGRESQL_PASSWORD="odoo"