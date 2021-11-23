FROM python:3.7-slim
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt
COPY image_utils/ image_utils/
COPY setup.py setup.py
RUN pip install --no-cache-dir .
ENTRYPOINT ["python", "-m", "image_utils.image_utils"]