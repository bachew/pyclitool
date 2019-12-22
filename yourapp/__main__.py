from os import path as osp
import click
import subprocess
import yourapp


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
    base_dir = osp.dirname(osp.dirname(yourapp.__file__))
    rcfile = osp.join(base_dir, 'pyclitool/bashrc')
    cmd = [
        'bash',
        '--rcfile', rcfile,
        '-i',  # interactive
    ]
    status = subprocess.call(cmd)
    raise SystemExit(status)


@cli.command('run', context_settings=dict(
    ignore_unknown_options=True,
))
@click.pass_context
@click.argument('command', nargs=-1, type=click.UNPROCESSED)
def cli_run(ctx, command):
    '''
    Run a command in virtual environment.
    '''
    if not command:
        raise click.ClickException('Commnot not provided')

    try:
        status = subprocess.call(command)
    except FileNotFoundError:
        raise click.ClickException('Command not found: {}'.format(command[0]))
    else:
        raise SystemExit(status)


@cli.command('python', context_settings=dict(
    ignore_unknown_options=True,
))
@click.pass_context
@click.argument('args', nargs=-1, type=click.UNPROCESSED)
def cli_python(ctx, args):
    '''
    Run python in virtual environment.
    '''
    status = subprocess.call(['python'] + list(args))
    raise SystemExit(status)


cli(prog_name='yapp')
