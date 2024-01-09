## Use odoo as parent image
FROM odoo:latest

USER root

RUN pip3 install pip --upgrade

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

USER odoo