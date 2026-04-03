#!/usr/bin/env bash
set -euo pipefail

if command -v docker >/dev/null 2>&1; then
  :
else
  echo "Docker is not installed or not in PATH"
  exit 1
fi

if docker compose version >/dev/null 2>&1; then
  docker compose up --build --remove-orphans
elif command -v docker-compose >/dev/null 2>&1; then
  docker-compose up --build --remove-orphans
else
  echo "Neither 'docker compose' nor 'docker-compose' is available"
  exit 1
fi
