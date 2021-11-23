Image Utils
===========

Introduction
------------

This repo contains a few tools for generating and processing images.
It is mean to use as test tools for CWL scripts.

Usage as python image
---------------------

Install with
```
pip install .
```

Run and show help with

```
python -m image_utils.image_utils -h
```

There are two tools: a producer, which generates GeoTIFF, 
and a blurrer, which takes n images and blur them.

Build as Docker image
---------------------

Build it with

```
docker build -t image-utils:latest .
```

Obtain help with

```
docker run image-utils:latest -h
```
