FROM python:3.11-bookworm

RUN --mount=type=bind,source=/web/requirements.txt,target=/tmp/requirements.txt \
    pip install --requirement /tmp/requirements.txt

COPY ../web/ .

CMD ["python", "app.py"]