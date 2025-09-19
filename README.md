# Docker Basics Tutorial

### Example 1: Build and Test the Application

```bash
# 1. Build the image
cd my-ubuntu/
docker build -t flask-tutorial:latest .

# 2. Run the container (in background with -d flag)
docker run -d -p 5000:5000 --name my-app flask-tutorial:latest

# 3. Test the application
curl http://localhost:5000          # Should return {"message": "Hello, world!"}
curl http://localhost:5000/health   # Should return "OK"

# 4. Debug inside the container
docker exec -it my-app /bin/bash
```

### Example 2: Development Workflow

```bash
# Build development version
docker build -t flask-tutorial:dev .

# Run with volume mount for live code changes (if needed)
docker run -d -p 5000:5000 --name dev-container flask-tutorial:dev

# Execute commands for debugging
docker exec dev-container python --version
docker exec dev-container pip list
docker exec -it dev-container /bin/bash
```

### Example 3: Container Management

```bash
# View running containers
docker ps

# View all containers (including stopped)
docker ps -a

# Stop the container
docker stop my-app

# Start stopped container
docker start my-app

# Remove container
docker rm my-app

# Remove container and image
docker rm my-app
docker rmi flask-tutorial:latest
```

## 6. Common Debugging Commands

```bash
# View container logs
docker logs flask-container
docker logs -f flask-container  # Follow logs in real-time

# Inspect container details
docker inspect flask-container

# View resource usage
docker stats flask-container

# Copy files to/from container
docker cp file.txt flask-container:/app/
docker cp flask-container:/app/logs.txt ./
```
