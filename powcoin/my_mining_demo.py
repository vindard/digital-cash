import time, hashlib



def get_proof(header, nonce):
    preimage = f"{header}:{nonce}".encode()
    proof_hex = hashlib.sha256(preimage).hexdigest()
    return int(proof_hex, 16)


def mine(header, target):
    nonce = 0
    while get_proof(header, nonce) >= target:
        nonce += 1 # new guess
    return nonce


def mining_demo(header):
    for difficulty_bits in range(1, 30):
        target = 2 ** (256 - difficulty_bits)        

        start_time = time.time()
        nonce = mine(header,target)
        proof = get_proof(header, nonce)
        elapsed_time = time.time() - start_time

        print(f"bits: {difficulty_bits} target: {target} elapsed time: {elapsed_time} nonce: {nonce} proof: {proof}\n")


if __name__ == "__main__":
    header = "hello"
    mining_demo(header)