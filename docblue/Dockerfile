FROM ubuntu:latest

# Create directory and set permissions
# Works without creating the directory since it will be created during python3.12-venv installation
#RUN mkdir -p /home/bor/docblue && chmod -R 777 /home/bor/docblue

# Install Python and necessary tools
RUN apt-get update && \
    apt-get install -y python3.12 python3.12-venv python3-pip git nano && \
    echo "Python and tools installed."

# Set working directory
WORKDIR /home/bor/docblue

# Make sure is executable or set permissions manually in bash
RUN chmod +x custom-entrypoint.sh
