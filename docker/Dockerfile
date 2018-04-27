# Use an official Python runtime as a base image
FROM python:3.6-alpine
# Get S3 Configuration file
WORKDIR /opt
RUN mkdir demandware-sfdc-mock-server
WORKDIR /opt/demandware-sfdc-mock-server
# Copy the current directory contents into the container at /opt
ADD mock_server/requirements.txt /opt/demandware-sfdc-mock-server/
RUN pip install --upgrade pip && pip install -r /opt/demandware-sfdc-mock-server/requirements.txt

ADD mock_server /opt/demandware-sfdc-mock-server/mock_server
ADD samples /opt/demandware-sfdc-mock-server/samples
# Run the mock server
EXPOSE 5000
CMD ["python","-m","mock_server"]
