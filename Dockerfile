FROM archlinux:latest

ARG UID=1000
ARG GID=1000

# Install dependencies
RUN pacman -Syu --noconfirm && \
    pacman -S --noconfirm base-devel python python-pip uv jdk-openjdk sbt git z3 sudo less npm vi

# Create a non-root user with sudo privileges
RUN groupadd -g ${GID} observant
RUN useradd -m -g observant -G wheel -u ${UID} observant

# Install eldarica
RUN git clone https://github.com/uuverifiers/eldarica.git /home/observant/eldarica; cd /home/observant/eldarica; sbt assembly
# Move the binary to /usr/local/bin
RUN ln -s /home/observant/eldarica/eld /usr/local/bin/eld

# Switch to the new user
USER observant
ENV USER=observant

WORKDIR /home/observant/

# Create and activate a virtual environment, then install the dependecies
RUN uv venv ~/venv; source ~/venv/bin/activate; uv pip install solc-select certora-cli

# Install solc-select and Solidity compiler version 0.8.29
RUN source ~/venv/bin/activate; solc-select install 0.8.29; solc-select use 0.8.29

WORKDIR /home/observant/shared
CMD ["/bin/bash", "-c", "source ~/venv/bin/activate && exec /bin/bash"]
