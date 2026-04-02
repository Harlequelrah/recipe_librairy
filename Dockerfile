# Build stage
FROM python:3.14-slim AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY api/requirements.txt .

# Create wheels for dependencies
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt


# Final stage
FROM python:3.14-slim

WORKDIR /app

# Install runtime dependencies only
RUN apt-get update && apt-get install -y --no-install-recommends \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/* \
    && useradd -m -u 1000 apiuser

# Copy wheels from builder and install them
COPY --from=builder /app/wheels /wheels
COPY api/requirements.txt .
RUN pip install --no-cache /wheels/*

# Copy application code
COPY api/ .

# Change ownership to non-root user
RUN chown -R apiuser:apiuser /app

USER apiuser

# Expose API port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/api/').read()" || exit 1

# Run the application
CMD ["elrahapi","run"]
