#!/bin/sh

set -e

. /install/setup/.venv/bin/activate

exec "$@"
