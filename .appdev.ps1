function Invoke-Pip {
    docker compose exec app pip
}

function Invoke-Python {
    docker compose exec -w /opt/aviumlabs app python
}

function Invoke-Pytest {
    docker compose exec app pytest ../tests
}

Set-Alias -Name pip -Value Invoke-Pip
Set-Alias -Name python -Value Invoke-Python
Set-Alias -Name pytest -Value Invoke-Pytest