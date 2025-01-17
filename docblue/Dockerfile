FROM ubuntu:latest


# Set working directory
WORKDIR /home/bor

# Create directory and set permissions
# Works without creating the directory since it will be created during python3.12-venv installation
#RUN mkdir -p /home/bor/docblue && chmod -R 777 /home/bor/docblue

# Install Python and necessary tools
RUN apt-get update && \
    apt-get install -y python3.12 python3.12-venv python3-pip git nano && \
    echo "Dockerfile. Python and tools installed"

# Copy files from host to container. Otherwise chmod wont work. Can copy only sh file as well if needed
# COPY . . # Stopped working by itself. Works fine on prod. Reason - line ending. Set to LF instead of CRLF!!!
#COPY custom-entrypoint.sh /home/bor

# Make sure is executable or set permissions manually in bash
#RUN chmod +x /home/bor/custom-entrypoint.sh



# Virtual environment setup. Can't install to mounted dirs, they arn't ready on this step
RUN python3 -m venv /venv

# Install dependencies to virtual environment. No need to activate first
RUN /venv/bin/pip install --no-cache-dir pip textual textual-dev Flask

# Copy the application code
#COPY . .







