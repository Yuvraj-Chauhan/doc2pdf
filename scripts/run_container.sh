
#!/bin/bash

# Build the Docker image
docker build -t doc-to-pdf-converter .

# Run the Docker container
docker run -p 8501:8501 doc-to-pdf-converter
        