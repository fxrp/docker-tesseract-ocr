FROM jitesoft/tesseract-ocr:alpine

# Become root to install packages
USER root
RUN apk add --no-cache python3 py3-pip

# App files
WORKDIR /app
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY app.py .

# (Optional) drop back to non-root; the common UID in jitesoft images is 10001
USER 10001

ENV PORT=8080
EXPOSE 8080
CMD ["python3", "app.py"]
