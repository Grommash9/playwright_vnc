FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y \
    xvfb \
    x11vnc \
    fluxbox \
    wget \
    net-tools \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libatspi2.0-0 \
    libcups2 \
    libdbus-1-3 \
    libdrm2 \
    libgbm1 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxkbcommon0 \
    libxrandr2 \
    xauth \
    xvfb && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt && \
    playwright install --with-deps chromium firefox webkit && \
    playwright install-deps

COPY tests/ ./tests/

EXPOSE 5900
EXPOSE 9323

CMD Xvfb :99 -screen 0 1280x720x16 & \
    export DISPLAY=:99 && \
    sleep 2 && \
    fluxbox & \
    x11vnc -display :99 -forever -nopw -shared & \
    sleep 2 && \
    echo "VNC server started on port 5900" && \
    tail -f /dev/null