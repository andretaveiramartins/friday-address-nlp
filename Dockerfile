# Use an official Python runtime as a base image
FROM python:3.6-jessie
# Get S3 Configuration file
WORKDIR /opt
RUN mkdir address-nlp-server
WORKDIR /opt/address-nlp-server
# Copy the current directory contents into the container at /opt
ADD app/requirements.txt /opt/address-nlp-server/
RUN pip install --upgrade pip && pip install -r /opt/address-nlp-server/requirements.txt

ADD app /opt/address-nlp-server/app
ADD samples /opt/address-nlp-server/samples
# Run the mock server
EXPOSE 5000
CMD ["python","-m","app"]
