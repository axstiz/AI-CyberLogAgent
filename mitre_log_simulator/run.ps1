$ErrorActionPreference = "Stop"

if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
    Write-Error "Docker is not installed or not in PATH"
}

$composeOk = $false
try {
    docker compose version *> $null
    if ($LASTEXITCODE -eq 0) {
        $composeOk = $true
    }
} catch {
    $composeOk = $false
}

if ($composeOk) {
    docker compose up --build --remove-orphans
    exit $LASTEXITCODE
}

if (Get-Command docker-compose -ErrorAction SilentlyContinue) {
    docker-compose up --build --remove-orphans
    exit $LASTEXITCODE
}

Write-Error "Neither 'docker compose' nor 'docker-compose' is available"
