FROM python:3.10.5
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN useradd appuser && chown appuser /app

RUN pip install --upgrade pip && pip install poetry==1.3.1

COPY --chown=appuser poetry.lock pyproject.toml /app/

RUN poetry export --without-hashes -f requirements.txt -o requirements.txt && \
    pip uninstall --yes poetry && \
    pip install -r requirements.txt && \
    pip install gunicorn==20.1.0 && \
    pip uninstall --yes poetry

USER appuser