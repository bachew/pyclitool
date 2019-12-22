# pyclitool

Template for simple Python CLI tool.


## Setup

- Copy `pyclitool` directory to project directory
- Copy `env.sh` to project directory
- Edit `env.sh`, rename `YOURAPP` and `yourapp` to your own app name
- Copy `bin` directory to project directory
- Edit `$CLI_MODULE` in `bin/yapp` to use your own CLI module
- Rename `bin/yapp` to your own app program, assumed to be still `bin/yapp` in this doc
- Update `pyclitool/update-sys` to install system packages
- Update `pyclitool/update-conda` to install platform dependent python packages
- Update `pyclitool/update-venv` to install python packages
- Run `bin/yapp`, notice `env` and `tmp` directories created
- Include `/env` and `/tmp` in `.gitignore` so they won't be committed to git
- You might want to copy useful commands from `yourapp/__main__.py`
