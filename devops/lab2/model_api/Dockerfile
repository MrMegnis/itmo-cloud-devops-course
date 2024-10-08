FROM python:3.11-bookworm
#add concrete version

RUN --mount=type=bind,source=/model_api/requirements.txt,target=/tmp/requirements.txt \
    pip install --requirement /tmp/requirements.txt

#use temporarily added requirements.txt instad of copy it

COPY ../model_api/ .

CMD ["python", "main.py"]