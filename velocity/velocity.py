import sys
import json
import socket
import _socket

dns_cache = {}  # contains {hostname : ip} entries
addr_cache = {}  # contains socket.getaddrinfo's cached responses

cwd = sys.path[0]
dns_path = cwd + '/dns_cache.json'
addr_path = cwd + '/addr_cache.json'

def read_file(path):
    """Reads a given file, returns str(file_content)"""
    with open(path, 'a+') as f:
        f.seek(0, 0)
        return '\n'.join(f.readlines())


def flush_db():
    """Flushes local cache"""
    for path in [addr_path, dns_path]:
        with open(path, 'w+') as f:
            f.write('{}\n')


def save_db():
    """Saves in-memory cache locally"""
    for path, db in zip(
        [addr_path, dns_path],
            [addr_cache, dns_cache]):
        with open(path, 'w') as f:
            f.write(json.dumps(db))


def load_db():
    """Load locally saved cache"""
    try:
        addr_cache = json.loads(read_file(addr_path))
        dns_cache = json.loads(read_file(dns_path))
    except json.decoder.JSONDecodeError:
        pass


og_addr = socket.getaddrinfo
og_connect = _socket.socket.connect

def resolve(hostname, port=False):
    """
    Resolves hostname to IP address.
    IPv6 addresses get mapped to IPv6 if a port isn't supplied
    returns str(IP_address)
    """
    if port:
        return _socket.getaddrinfo(hostname, port)[0][4][0]
    else:
        return _socket.gethostbyname(hostname)

def cache(hostname, port=False):
    """Resolve and add hostname to cache"""
    dns_cache[hostname] = resolve(hostname, port) 

def patched_connect(sock, address):
    """
    Intercepting function for _socket.socket.connect
    returns _socket.socket.connect's result
    """
    hostname, port = address[:2]
    if hostname not in dns_cache:
        dns_cache[hostname] = resolve(hostname, port)
    hostname = dns_cache[hostname]
    return og_connect(sock, (hostname, port))

def patched_addr(host, *args, **kwargs):
    """
    Intercepting function for socket.getaddrinfo
    returns socket.getaddrinfo's result or
    its cached equivalent when available
    """
    if host in addr_cache:
        return addr_cache[host]
    addrlist = og_addr(host, *args, **kwargs)
    addr_cache[host] = addrlist
    return addrlist

socket.getaddrinfo = patched_addr
socket.socket.connect = patched_connect
