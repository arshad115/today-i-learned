# Docker Build and Push: docker build/push vs docker buildx

## Overview

Docker provides multiple ways to build and push images. The traditional `docker build` and `docker push` commands work for basic use cases, while `docker buildx` offers advanced features like multi-platform builds, improved caching, and better performance.

## Traditional Docker Build and Push

### Basic Build Command
```bash
# Build an image from a Dockerfile
docker build -t myapp:latest .

# Build with specific Dockerfile
docker build -f Dockerfile.prod -t myapp:prod .

# Build with build arguments
docker build --build-arg NODE_VERSION=18 -t myapp:latest .
```

### Basic Push Command
```bash
# Push to Docker Hub
docker push myapp:latest

# Push to private registry
docker push registry.company.com/myapp:latest

# Tag and push
docker tag myapp:latest myregistry/myapp:v1.0.0
docker push myregistry/myapp:v1.0.0
```

## Docker Buildx

Docker Buildx is an extended build command that provides additional features and better performance.

### Enable Buildx
```bash
# Create and use a new builder instance
docker buildx create --name mybuilder --use

# Inspect the builder
docker buildx inspect --bootstrap
```

### Advanced Build Features

#### Multi-Platform Builds
```bash
# Build for multiple architectures
docker buildx build --platform linux/amd64,linux/arm64 -t myapp:latest .

# Build and push multi-platform image
docker buildx build --platform linux/amd64,linux/arm64 -t myapp:latest --push .
```

#### Build and Push in One Command
```bash
# Build and push directly (no local image stored)
docker buildx build -t myapp:latest --push .

# Build for multiple platforms and push
docker buildx build --platform linux/amd64,linux/arm64 -t myapp:latest --push .
```

#### Advanced Caching
```bash
# Use cache from registry
docker buildx build --cache-from type=registry,ref=myapp:cache --cache-to type=registry,ref=myapp:cache -t myapp:latest .

# Use local cache
docker buildx build --cache-from type=local,src=/path/to/cache --cache-to type=local,dest=/path/to/cache -t myapp:latest .
```

## Key Differences

| Feature | docker build/push | docker buildx |
|---------|------------------|---------------|
| Multi-platform builds | ❌ | ✅ |
| Advanced caching | Limited | ✅ Enhanced |
| Build and push in one command | ❌ | ✅ |
| BuildKit by default | Depends on config | ✅ Always |
| Parallel builds | Limited | ✅ Better |
| Build secrets | Basic | ✅ Enhanced |
| Output formats | Image only | Multiple formats |

## Practical Examples

### Example 1: Simple Web App
```bash
# Traditional approach
docker build -t webapp:latest .
docker push webapp:latest

# Buildx approach
docker buildx build -t webapp:latest --push .
```

### Example 2: Multi-Platform Node.js App
```bash
# Only possible with buildx
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t nodeapp:latest \
  --push .
```

### Example 3: Using Build Cache
```bash
# Traditional (limited caching)
docker build -t myapp:latest .

# Buildx with registry cache
docker buildx build \
  --cache-from type=registry,ref=myapp:cache \
  --cache-to type=registry,ref=myapp:cache \
  -t myapp:latest \
  --push .
```

## Best Practices

1. **Use buildx for new projects** - Better performance and features
2. **Enable multi-platform builds** - Reach more users with ARM and AMD64 support
3. **Leverage cache** - Use registry or local cache for faster builds
4. **Build and push together** - Use `--push` flag to avoid storing large images locally
5. **Use build secrets** - Securely pass secrets during build time

```bash
# Example with secrets
docker buildx build \
  --secret id=mysecret,src=./secret.txt \
  -t myapp:latest \
  --push .
```

## When to Use Which

- **Use `docker build/push`** when:
  - Working with legacy systems
  - Simple single-platform builds
  - BuildKit is not available

- **Use `docker buildx`** when:
  - Need multi-platform support
  - Want better caching
  - Building for production
  - Need advanced features like secrets or custom outputs

## Conclusion

While traditional `docker build` and `docker push` commands work for basic scenarios, `docker buildx` provides significant advantages for modern containerized applications, especially when targeting multiple platforms or requiring advanced build features.