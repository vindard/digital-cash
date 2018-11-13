from uuid import uuid4

class Tx:

    def __init__(self, id, tx_ins, tx_outs):
        self.id  = id
        self.tx_outs = tx_outs
        self.tx_ins = tx_ins

    def sign_input(self, index, private_key):
        spend_message = self.tx_ins[index].spend_message()
        signature = private_key.sign(spend_message)
        self.tx_ins[index].signature = signature

class TxIn:
    def __init__(self, tx_id, index, signature):
        self.tx_id = tx_id
        self.index = index
        self.signature = signature

    def spend_message(self):
        return f"{self.tx_id}:{self.index}".encode()

class TxOut:
    def __init__(self, tx_id, index, amount, public_key):
        self.tx_id = tx_id
        self.index = index
        self.amount = amount
        self.public_key = public_key

class Bank:

    def __init__(self):
        self.txs = {}

    def issue(self, amount, public_key):

        id = uuid4()
        tx_ins = []

        tx_outs = [
            TxOut(tx_id = id, index=0, amount=amount, public_key=public_key)
        ]
        tx = Tx(id=id, tx_ins=tx_ins, tx_outs=tx_outs)
        self.txs[tx.id] = tx
        return tx

    def is_unspent(self, tx_in):
        pass

    def validate_tx(self, tx):
        in_sum = 0
        out_sum = 0

        for tx_in in tx.tx_ins:
            assert self.is_unspent(tx_in)

            tx_out = self.txs[tx_in.tx_id].tx_outs[tx_in.index]
            public_key = tx_out.public_key
            public_key.verify(tx_in.signature, tx_in.spend_message())

            in_sum += tx_out.amount

        for tx_out in tx.tx_outs:
            out_sum += tx_out.amount

        assert in_sum == out_sum

    def handle_tx(self, tx):
        self.validate_tx(tx)
        self.txs[tx.id] = tx