## Getting Started

First, you need to have [Docker](https://www.docker.com/products/docker-desktop/) installed, then

- Run

```bash
docker run -it -v ${IMAGES_PATH}:/usr/src/app/runs/detect dorrahsq/pollution_detection

# IMAGES_PATH -> refers to the source folder of the images that need to be tested in your local machine
```

Note: The result will be saved in `${IMAGES_PATH}/exp`

<br/>

## Environment variables

| variable | default value | usage       | example                                                                                                          |
| -------- | ------------- | ----------- | ---------------------------------------------------------------------------------------------------------------- |
| CONF     | 0.4           | -e CONF=0.5 | `docker run -it -v /Users/jon/Desktop/images:/usr/src/app/runs/detect -e CONF=0.5 dorrahsq/pollution_detection ` |
