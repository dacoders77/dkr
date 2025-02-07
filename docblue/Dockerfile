FROM ubuntu:latest

# Set working directory
WORKDIR /home/bor

# Install Python and necessary tools
RUN apt-get update && \
    apt-get install -y python3.12 python3.12-venv python3.12-dev python3-pip git nano nginx && \
    echo "Dockerfile. Python and tools installed"

# Postgres deps for django
RUN apt-get -y install libpq-dev && echo "Dockerfile. Postgres deps for django installed"

# Virtual environment setup. Can't install to mounted dirs, they arn't ready on this step
RUN python3 -m venv /venv

# Install dependencies to virtual environment. No need to activate first
#RUN /venv/bin/pip install --no-cache-dir pip textual textual-dev
RUN /venv/bin/pip install pip textual textual-dev django









