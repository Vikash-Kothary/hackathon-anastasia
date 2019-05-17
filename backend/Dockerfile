FROM python:3.7-alpine

RUN apk add bash make

WORKDIR /root/

# Upgrade to latest version of pip.
RUN pip install --upgrade pip

# Copy and install all pip (python) requirements.
COPY requirements.txt ./
RUN pip install --no-cache-dir -r /root/requirements.txt

# Set working directory and command.
CMD [ "python", "src/main.py" ]
