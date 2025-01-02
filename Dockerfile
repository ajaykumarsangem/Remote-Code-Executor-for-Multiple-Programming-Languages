FROM python:3.9-slim

# Update package lists and install Node.js and npm
RUN apt-get update \
    && apt-get install -y nodejs npm

# Install Golang
RUN apt-get install -y golang

# Java
RUN apt install -y default-jre
RUN apt-get install -y default-jdk

# Install Rust
RUN apt install -y curl
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# Install C 
RUN apt-get install -y gcc

RUN apt-get install -y g++

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY entrypoint.sh .

RUN chmod +x entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]
