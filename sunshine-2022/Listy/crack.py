#!/home/bhu/.virtualenvs/ansible/bin/python3

from subprocess import PIPE, Popen

def crack(key):
    p = Popen(["ansible-vault", "decrypt", "vault.txt", "--output", "key.json"], stdin=PIPE, stdout=PIPE)
    return p.communicate(input=f"test\n".encode())[0]

print(crack("no"))