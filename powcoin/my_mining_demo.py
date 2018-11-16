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

        target_str = f"{target:.0e}"
        elapsed_time_str = f"{elapsed_time:.0e}"
        bin_proof_str = f"{proof:0256b}"

        print(f"bits: {difficulty_bits} target: {target_str} elapsed time: {elapsed_time_str} nonce: {nonce} proof: {bin_proof_str}\n")


if __name__ == "__main__":
    header = "hello"
    mining_demo(header)