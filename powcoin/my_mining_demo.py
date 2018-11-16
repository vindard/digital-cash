import hashlib



def get_proof(header, nonce):
    preimage = f"{header}:{nonce}".encode()
    proof_hex = hashlib.sha256(preimage).hexdigest()
    return int(proof_hex, 16)


def mine(header, targer):
    nonce = 0
    while get_proof(header, nonce) >= target:
        nonce += 1 # new guess
    return nonce



if __name__ == "__main__":
    header = "hello"
    # number of leading bits we require
    difficulty_bits = 8
    target = 2 ** (256 - difficulty_bits)
    nonce = mine(header, target)
    print(nonce)