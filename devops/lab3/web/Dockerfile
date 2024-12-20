FROM python:3.11-bookworm

RUN --mount=type=bind,source=/devops/lab3/web/requirements.txt,target=/tmp/requirements.txt \
    pip install --requirement /tmp/requirements.txt

COPY ../devops/lab3/web/ .

CMD ["python", "app.py"]