FROM jitesoft/tesseract-ocr:alpine
# Optional: add more languages (example: Spanish fast)
# RUN train-lang spa --fast

# Minimal Python + Flask
RUN apk add --no-cache python3 py3-pip
WORKDIR /app
COPY app.py /app/app.py
RUN pip install flask

# Railway will set PORT; Flask must bind to 0.0.0.0
ENV PORT=8080
CMD ["sh", "-lc", "python3 app.py --port=$PORT"]  # we'll override with flask run below via start command
