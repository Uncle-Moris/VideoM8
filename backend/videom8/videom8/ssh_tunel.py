from sshtunnel import SSHTunnelForwarder

def create_ssh_tunnel():
    ssh_host = '172.105.88.119'
    ssh_port = 27119
    ssh_user = 'moris'
    ssh_key = '/Users/maurycywoznica/.ssh/id_ed25519_moris'

    server = SSHTunnelForwarder(
        (ssh_host, ssh_port),
        ssh_username=ssh_user,
        ssh_pkey=ssh_key,
        remote_bind_address=('localhost', 5432),
        local_bind_address=('localhost', 0),  # Automatically assign the local bind port
    )

    server.start()

    return server
