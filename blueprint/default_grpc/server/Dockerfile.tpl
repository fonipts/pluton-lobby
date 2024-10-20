FROM python:latest
WORKDIR /usr
COPY ./ /usr

EXPOSE 50051
RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r /usr/requirements.txt
CMD ["python", "/usr/main.py"]
