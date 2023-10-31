# Docker Beispiel

Dieses Beispiel soll zeigen, wie ein Dockerfile genutzt werden kann, um Software in einem Container auszufuehren.

## Voraussetzungen

Es muss eine Docker compatible Container Runtime auf der Maschine installiert sein. Dazu gehoeren:

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Podman](https://podman.io/)
- [Rancher Desktop](https://rancherdesktop.io/)

## Ausfuehren

```bash
# Bauen des Image
docker build -t myimage .

# Listen des gebauten image
docker image ls --filter "reference=myimage"

# Ausfuehren des Image
docker run -p 5555:5555 myimage

# Aufrufen des Services
curl 127.0.0.1:5555
```
