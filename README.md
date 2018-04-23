# d-nginx-charlesreid1

This repo contains docker containers
and a docker compose file for running
an nginx web server for static content
on charlesreid1.com.

This repo is used in [pod-charlesreid1](https://git.charlesreid1.com/docker/pod-charlesreid1.git).

The services are just:
* nginx

If you want to do SSL you can, but you have to 
run Let's Encrypt outside of the container
and bind-mount your certificates into the 
container at `/etc/letsencrypt`.

Pretty simple, right?

## Config files

All `*.conf` files in the `conf.d/` directory will be picked up by nginx.

The config files must be named `*.conf`.

## Volumes

No data volumes are used.

* nginx static content is a bind-mounted host directory
* lets encrypt generates site certs, which will be bind-mounted into host directory

```
  web:
    volumes:
      - ./letsencrypt_certs:/etc/nginx/certs
      - ./letsencrypt_www:/var/www/letsencrypt

  letsencrypt:
    image: certbot/certbot
    command: /bin/true
    volumes:
      - ./letsencrypt_certs:/etc/letsencrypt
      - ./letsencrypt_www:/var/www/letsencrypt
```

## Certs and Secrets

Lets Encrypt should generate certificates at `/etc/letsencrypt/live/domain/`:

```
root@krash:/home/charles/codes/docker/pod-charlesreid1-site# ls -l /etc/letsencrypt/live/charlesreid1.blue/
total 4
lrwxrwxrwx 1 root root  41 Mar 27 01:03 cert.pem -> ../../archive/charlesreid1.blue/cert1.pem
lrwxrwxrwx 1 root root  42 Mar 27 01:03 chain.pem -> ../../archive/charlesreid1.blue/chain1.pem
lrwxrwxrwx 1 root root  46 Mar 27 01:03 fullchain.pem -> ../../archive/charlesreid1.blue/fullchain1.pem
lrwxrwxrwx 1 root root  44 Mar 27 01:03 privkey.pem -> ../../archive/charlesreid1.blue/privkey1.pem
-rw-r--r-- 1 root root 543 Mar 27 01:03 README
```

These certificate files will be bind-mounted into the nginx container.

## Backups

Site content comes from github.
Nothing to back up.

## Static Content

Question: should we bake the site's 
static content into the container,
and require rebuild/redeploy when
site content changes?

Answer: No. We clone a local copy of 
the gh-pages branch, and bind-mount 
that into the container.

This enables webhooks to update 
the static site contents
without disturbing the container.

