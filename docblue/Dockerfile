FROM ubuntu:latest

# Create directory and set permissions
# Works without creating the directory since it will be created during python3.12-venv installation
#RUN mkdir -p /home/bor/docblue && chmod -R 777 /home/bor/docblue

# Install Python and necessary tools
RUN apt-get update && \
    apt-get install -y python3.12 python3.12-venv python3-pip git nano && \
    echo "Dockerfile. Python and tools installed"

# Copy files from host to container. Otherwise chmod wont work. Can copy only sh file as well if needed
# COPY . . # Stopped working by itself. Works fine on prod. Reason - line ending. Set to LF instead of CRLF!!!
COPY custom-entrypoint.sh /home/bor/docblue/

# Make sure is executable or set permissions manually in bash
#RUN chmod +x custom-entrypoint.sh
RUN chmod +x /home/bor/docblue/custom-entrypoint.sh

# Set working directory
WORKDIR /home/bor/b-dev



