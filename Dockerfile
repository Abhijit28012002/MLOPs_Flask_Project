# Use an official Python runtime as a parent image
FROM centos:7

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# install net-tools for ipaddress
RUN yum install net-tools -y

# install python3.6
RUN yum install python3 -y

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirments.txt

# Run python3 app.py when the container launches
CMD ["python3", "app.py"]
