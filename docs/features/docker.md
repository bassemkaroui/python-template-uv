# Docker

When `dockerfile: true` (the default), the template generates Docker configuration for both production and development use.

## Generated Files

| File | Purpose |
|------|---------|
| `Dockerfile` | Multi-stage production build |
| `compose.yaml` | Production service definition |
| `compose.override.yaml` | Development overrides (hot-reload, exposed ports) |

## Commands

/// tab | :simple-make: make

```bash
# Build Docker images
make docker-build

# Start services
make docker-start

# Stop and remove services
make docker-stop
```

///

/// tab | :material-wrench: mise

```bash
# Build Docker images
mise run docker:build

# Start services
mise run docker:start

# Stop and remove services
mise run docker:stop
```

///

## GPU Support

Enable GPU support by setting `gpus: true` during generation. This adds NVIDIA GPU configuration to the Docker setup:

- NVIDIA base image for CUDA support
- GPU device requests in compose files
- Appropriate runtime configuration

## Container Security

By default, the container runs as a non-root user matching your host UID/GID. Set `privileged_container: true` during generation if root access is required.

## Development Workflow

The `compose.override.yaml` file is loaded automatically by Docker Compose and adds:

- Volume mounts for live code reloading
- Exposed ports for local development
- Environment variable overrides
