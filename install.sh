#!/bin/bash

proj_name="django-rest-base-boilerplate"

home="/home/devluci"
proj="${home}/${proj_name}"
venv="${proj}/venv"

nginx="/etc/nginx/sites-enabled"
pgbouncer="/etc/pgbouncer"
systemd="/etc/systemd/system"
nginx_list=("${proj_name}")
service_list=("${proj_name}")

sudo apt update --fix-missing
sudo apt install python3.8 python3.8-dev python3.8-venv nginx pgbouncer memcached -y

python3 -m venv ${venv}
source ${venv}/bin/activate
pip3 install -r ${proj}/requirements.txt

sudo rm ${nginx}/default ${nginx}/nginx_default.conf -f
sudo cp ${proj}/nginx/nginx_default.conf ${nginx}/
for conf in "${nginx_list[@]}"
do
    sudo rm ${nginx}/${conf}.conf -f
    sudo ln -s ${proj}/nginx/${conf}.conf ${nginx}/
done

sudo service nginx reload

sudo rm ${pgbouncer}/pgbouncer.ini
sudo rm ${pgbouncer}/pgbouncer.ini -f
sudo ln -s ${proj}/pgbouncer.ini ${pgbouncer}/

sudo service pgbouncer restart

for service in "${service_list[@]}"
do
    sudo rm ${systemd}/${service}.service -f
    sudo ln -s ${proj}/systemd/${service}.service ${systemd}/
done

sudo systemctl daemon-reload

for service in "${service_list[@]}"
do
    sudo systemctl enable ${service}.service
    sudo systemctl start ${service}.service
done

python3 ${proj}/manage.py collectstatic --no-input
deactivate
