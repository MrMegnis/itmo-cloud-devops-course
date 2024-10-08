FROM python:3.11-bookworm

RUN --mount=type=bind,source=/frontend/requirements.txt,target=/tmp/requirements.txt \
    pip install --requirement /tmp/requirements.txt

COPY ../frontend/ .

CMD ["python", "main.py"]