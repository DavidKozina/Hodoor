from os import path
import subprocess
THIS_FOLDER = path.dirname(path.abspath(__file__))

def reset_database(host):
    subprocess.check_call(
            ['fab', 'reset_database', '--host={}'.format(host)],
            cwd=THIS_FOLDER
    )


def create_session_on_server(host, username):
    return subprocess.check_output(
            [
                    'fab',
                    'create_session_on_server:username={}'.format(username),
                    '--host={}'.format(host),
                    '--hide=everything,status',
            ],
            cwd=THIS_FOLDER
    ).decode().strip()
