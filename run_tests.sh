#!/bin/bash

# Config para rodar os testes no Container 
set -e

host="$1"
shift
cmd="$@"

until curl -sSf "$host:80/docs" >/dev/null; do
    echo "Aguardando o serviço FastAPI iniciar..."
    sleep 1
done

echo "Serviço FastAPI está pronto. Iniciando os testes..."
exec $cmd


# Local
# TESTS_DIR="tests"

# pytest "$TESTS_DIR/tests.py" # -> ok





