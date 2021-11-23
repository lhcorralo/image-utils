from setuptools import setup, find_packages

setup(
    name='image-utils',
    version='0.1.0',
    packages=find_packages(include=['image_utils', 'image_utils.*']),
    install_requires=[
        'rasterio==1.1.0',
        'opencv-python-headless==4.5.4.58'
    ],
    entry_points={
        'console_scripts': ['imageutils=image_utils.image_utils:main']
    }
)
