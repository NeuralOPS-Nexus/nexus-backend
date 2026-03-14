# STAGE 1: The Builder (Compiles the code)
FROM golang:1.26-alpine AS builder

WORKDIR /app
# Copy the source code (including go.mod, cmd/, internal/)
COPY . .

# Compile the binary
# RUN go build -ldflags="-s -w" -o nexus-transport ./cmd/centrifugo
RUN go build -ldflags="-s -w" -o nexus-transport .

# STAGE 2: The Production Image (Small & Secure)
FROM alpine:3.18

# 1. Setup Security (Matches original intent)
ARG USER=centrifugo
ARG UID=1000
ARG GID=1000
RUN addgroup -S -g $GID $USER && \
    adduser -S -G $USER -u $UID $USER

# 2. Setup System
RUN apk --no-cache upgrade && \
    apk --no-cache add ca-certificates && \
    update-ca-certificates

# 3. Copy only the compiled binary from the builder
COPY --from=builder /app/nexus-transport /usr/local/bin/nexus-transport

USER $USER
WORKDIR /centrifugo

# No ENTRYPOINT, as we will run it from docker-compose