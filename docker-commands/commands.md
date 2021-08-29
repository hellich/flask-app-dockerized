# Docker commands

## build docker image from Dockerfile

```
docker build -t image_name .
```

## get local docker images

```
docker images
```

## start a container from an image

```
docker run -d -p 5000:5000 image_name
``` 