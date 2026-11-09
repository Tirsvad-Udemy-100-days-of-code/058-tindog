# Headless browser for the lecture screenshots. Used only to take the pictures
# in docs/images/; it is not part of the Python project.
#
# Build and run from the repository root:
#   docker build -t tindog-screenshots -f tools/screenshots/Dockerfile .
#   docker run --rm -v "$(pwd)/docs/images:/work/docs/images" tindog-screenshots
FROM mcr.microsoft.com/playwright/python:v1.49.1-noble

RUN pip install --no-cache-dir --break-system-packages playwright==1.49.1

WORKDIR /work
ENV PYTHONPATH=/work/src

COPY src ./src
COPY tools/screenshots/take_screenshots.py ./tools/screenshots/take_screenshots.py

CMD ["python3", "tools/screenshots/take_screenshots.py", "docs/images"]
