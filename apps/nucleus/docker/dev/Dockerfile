# Stage 1: Build dependencies (The heavy lifting)
FROM python:3.11-slim as builder

WORKDIR /build

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

ENV VIRTUAL_ENV=/opt/venv/nexus-env
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy from the context root (NeuralOPSNexus/)
COPY apps/nucleus/docker/dev/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Final Runtime (The clean, dev-ready engine)
FROM python:3.11-slim

# 1. Setup 'ubuntu' user, sudo, AND your dev tools (micro, tmux)
RUN set -eux; \
    apt-get update && apt-get install -y --no-install-recommends \
    sudo \
    libpq-dev \
    # Dev binaries go here, NOT in requirements.txt
    micro \
    tmux \
    curl; \
    getent passwd ubuntu >/dev/null 2>&1 || adduser --disabled-password --gecos '' ubuntu; \
    usermod -aG sudo ubuntu; \
    grep -q '^%sudo ALL=(ALL) NOPASSWD:ALL' /etc/sudoers || echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers; \
    # Use the /nucleus path as we planned for the volume
    mkdir -p /nucleus && chown ubuntu:ubuntu /nucleus; \
    rm -rf /var/lib/apt/lists/*

# 2. Copy the Venv
COPY --from=builder /opt/venv/nexus-env /opt/venv/nexus-env
ENV VIRTUAL_ENV=/opt/venv/nexus-env
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# 3. Environment & Workspace
WORKDIR /nucleus
USER ubuntu

# Ensure local Python imports from /nucleus work
ENV PYTHONPATH=/nucleus

# 4. Command
# Uvicorn watches /nucleus/app for changes via the volume
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload", "--proxy-headers"]