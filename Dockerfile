FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/interviews/scripts:${PATH}"

WORKDIR /interviews

COPY requirements.txt /interviews/

RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
        binutils \
        gcc \
        libpq-dev \
        python3-dev \
    ; \
    useradd -c "App User" \
        --home-dir /interviews \
        --shell /bin/sh \
        --create-home \
        --uid 1000 \
        app \
    ; \
    pip install --no-cache-dir --upgrade pip; \
    pip install --no-cache-dir --upgrade setuptools; \
    pip install --no-cache-dir -r requirements.txt; \
    chown -R app:app /interviews; \
    apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false; \
    rm -rf /var/lib/apt/lists/*

COPY . /interviews/

USER 1000

CMD ["entrypoint.sh"]
