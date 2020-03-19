# $0 is not this script because this is sourced, use ${BASH_SOURCE[0]} instead
export APP_HOME=$(dirname "${BASH_SOURCE[0]}")
export PYTHONPATH="$APP_HOME:$PYTHONPATH"
export PYCLITOOL_VENV_PROMPT="(app) "
