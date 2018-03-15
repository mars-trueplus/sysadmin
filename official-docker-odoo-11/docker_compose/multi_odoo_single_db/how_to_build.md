Multi Odoo instance (container) use one DB instance

1. Run new DB container
$ docker run -d -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=odoo --name db_sbmo  postgres:9.6


2. Run new Odoo container , link with created DB container above
$ docker run -p 8095:8069 --name odoo_sdmo1 --link db_sbmo:db odoo:11.0

3. Run another Odoo container, also link with above DB and more configuration (include update all modules)
$ docker run -v /home/xmars/Dev/sysadmin/official-docker-odoo-11/config/multi_odoo_single_db/odoo1:/etc/odoo -v /home/xmars/Dev/sysadmin/official-docker-odoo-11/addons/single_odoo:/mnt/extra-addons -p 8096:8069 --name odoo_sdmo2 --link db_sbmo:db odoo:11.0 --update all


*********NOTE*********
-- Reset container with more options : https://docs.docker.com/engine/reference/run/#entrypoint-default-command-to-execute-at-runtime
-- Need a solution to update specific module when restart container