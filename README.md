# Django REST base / Boilerplate

Boilerplate project of [Django REST base](https://github.com/devluci/django-rest-base)


# Requirements

- Ubuntu 18.04 LTS



# Installation

```shell script
git clone https://github.com/devluci/django-rest-base-boilerplate.git
cd django-rest-base-boilerplate

(create config files using .example of each file)

./install.sh
```

### Config files
| File Name | Description |
| --------- | ----------- |
| .env      | Environment variables for Django|
| pgbouncer.ini | [PgBouncer config](https://www.pgbouncer.org/config.html) |
| systemd/django-rest-base-boilerplate.service | Uvicorn service configuration |
| nginx/django-rest-base-boilerplate.conf | Nginx configuration |
| nginx/cloudflare.pem.example | [Cloudflare](https://www.cloudflare.com/) origin certificate |
| nginx/cloudflare.key.example | Private key of [Cloudflare](https://www.cloudflare.com/) origin certificate |


### Customization

If you want to use this boilerplate without any change,
you must set your server's username as `devluci`.

Or, you can customize by alter some text in **all** codes and filenames.

| Original Text | Description |
| ------------- | ----------- |
| devluci       | Ubuntu username |
| project       | Django project name |
| django-rest-base-boilerplate | Project name |


