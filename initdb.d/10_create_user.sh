#!/bin/bash
set -eux -o pipefail

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
	CREATE USER pythonapp LOGIN PASSWORD 'pythonapp';

EOSQL
