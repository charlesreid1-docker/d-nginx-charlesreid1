# d-nginx-charlesreid1

This repo contains docker containers
and a docker compose file for running
an nginx web server for static content
on charlesreid1.com.

This repo is used in 
[pod-charlesreid1](https://git.charlesreid1.com/docker/pod-charlesreid1.git).

The services are just:

* nginx

If you want to do SSL you can, but you have to 
run Let's Encrypt outside of the container
and bind-mount your certificates into the 
container at `/etc/letsencrypt`.

Pretty simple, right?

## Links

[documentation: d-nginx-charlesreid1 container](https://pages.charlesreid1.com/d-nginx-charlesreid1/) (you are here)

[source code on git.charlesreid1.com: d-nginx-charlesreid1](https://git.charlesreid1.com/docker/d-nginx-charlesreid1)

[source code on github.com: charlesreid1-docker/d-nginx-charlesreid1](https://github.com/charlesreid1-docker/d-nginx-charlesreid1)

