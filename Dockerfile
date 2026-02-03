FROM public.ecr.aws/docker/library/python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Batch will run this by default unless overridden
CMD ["python", "app.py"]
