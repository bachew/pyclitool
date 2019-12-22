# $0 is not this script because this is sourced, use ${BASH_SOURCE[0]} instead
export YOURAPP_HOME=$(dirname "${BASH_SOURCE[0]}")
export PYTHONPATH="$YOURAPP_HOME:$PYTHONPATH"
export PYCLITOOL_VENV_PROMPT="(yourapp) "
