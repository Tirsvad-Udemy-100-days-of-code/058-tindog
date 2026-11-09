# Headless browser for the lecture screenshots. Used only to take the pictures
# in docs/images/; it is not part of the Python project.
#
# Build and run from the repository root:
#   docker build -t tindog-screenshots -f tools/screenshots/Dockerfile .
#   docker run --rm --ipc=host -v "$(pwd)/docs/images:/work/docs/images" tindog-screenshots
#
# The base image is pinned to a digest (playwright/python v1.49.1, noble).
FROM mcr.microsoft.com/playwright/python:v1.49.1-noble@sha256:42e251ec3238672c931be6c3565ff279690ae072c3e22058128d0412494f6866

RUN pip install --no-cache-dir --break-system-packages playwright==1.49.1

WORKDIR /work
ENV PYTHONPATH=/work/src

COPY src ./src
COPY tools/screenshots/take_screenshots.py ./tools/screenshots/take_screenshots.py
RUN mkdir -p /work/docs/images && chown -R pwuser:pwuser /work

# Run as the unprivileged user that the image provides.
USER pwuser

CMD ["python3", "tools/screenshots/take_screenshots.py", "docs/images"]
