from os import path as osp
import click
import os
import subprocess


@click.group('')
def cli():
    '''
    Your app's description
    '''
    pass


@cli.command('bash')
def cli_bash():
    '''
    Spawn bash shell in virtual environment.
    '''
    base_dir = osp.dirname(osp.dirname(__file__))
    rcfile = osp.join(base_dir, 'pyclitool/bashrc')
    os.stat(rcfile)  # ensure file exists
    cmd = [
        'bash',
        '--rcfile', rcfile,
        '-i',  # interactive
    ]
    res = subprocess.run(cmd, check=False)
    raise SystemExit(res.returncode)


@cli.command('run', context_settings=dict(
    help_option_names=[],
    ignore_unknown_options=True,
))
@click.pass_context
@click.argument('command', nargs=-1, type=click.UNPROCESSED,
                metavar='PROGRAM [ARGS]...')
def cli_run(ctx, command):
    '''
    Run a command in virtual environment.
    '''

    def help_exit():
        print(ctx.get_help())
        raise SystemExit(1)

    if not command:
        help_exit()

    venv_prompt = os.environ.get('PYCLITOOL_VENV_PROMPT') or ''
    command_echo = '{}$ {}'.format(venv_prompt, subprocess.list2cmdline(command))
    print(command_echo)

    try:
        res = subprocess.run(command, check=False)
    except FileNotFoundError:
        click.echo('Error: command not found: {}'.format(command[0]), err=True)
        help_exit()
    else:
        raise SystemExit(res.returncode)


cli(prog_name='yapp')
