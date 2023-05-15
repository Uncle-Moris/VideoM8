from sshtunnel import SSHTunnelForwarder
import os.path
from dotenv import load_dotenv
load_dotenv()


SSH_HOST = str(os.getenv('SSH_HOST'))
SSH_PORT = int(os.getenv('SSH_PORT'))
SSH_USER = str(os.getenv('SSH_USER'))
SSH_KEY = str(os.getenv('SSH_KEY'))


def create_ssh_tunnel():
    ssh_host = SSH_HOST
    ssh_port = SSH_PORT
    ssh_user = SSH_USER
    ssh_key = SSH_KEY

    server = SSHTunnelForwarder(
        (ssh_host, ssh_port),
        ssh_username=ssh_user,
        ssh_pkey=ssh_key,
        remote_bind_address=('localhost', 5432),
        local_bind_address=('localhost', 0),
    )

    server.start()

    return server
