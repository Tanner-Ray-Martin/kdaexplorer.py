class Height:
    def __init__(self, data):
        self.data = data
        self.value = data["height"]
        self.blocks = list()
        for block in data["blocks"]:
            try:
                self.blocks.append(Block(block))
            except:
                pass

        self.tx_qty = data["totalTransactions"]
        self.value_transfers = [
            ValueTransfer(value_transfer_data)
            for value_transfer_data in data["valuesTransferred"]
        ]
        self.fee_total = float(data["totalFees"])
        self.creation_time = CreationTime(data["creationTime"])


class Block:
    def __init__(self, data) -> None:
        self.data = data
        self.chain = Chain(self.data["chainId"])
        self.height = self.data["height"]
        self.value = self.data["hash"]
        self.parent_block_hash = self.data["parentBlockHash"]
        self.transactions = [
            Transaction(transaction) for transaction in self.data["transactions"]
        ]
        self.tx_qty = len(self.transactions)
        self.fee_total = self.data["totalFees"]
        self.value_transfers = [
            ValueTransfer(value_transfer_data)
            for value_transfer_data in self.data["valuesTransferred"]
        ]
        self.properties = Property(self.data["properties"])
        self.time = self.data["timestamp"]


class Property:
    def __init__(self, data) -> None:
        self.data = data


class Transaction:
    def __init__(self, data) -> None:
        self.data = data


class ValueTransfer:
    def __init__(self, data) -> None:
        self.data = data


class CreationTime:
    def __init__(self, creation_time) -> None:
        self.value = creation_time


class Chain:
    def __init__(self, chain_id) -> None:
        self.value = chain_id
