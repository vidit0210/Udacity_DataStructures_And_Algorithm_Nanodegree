import hashlib


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        return sha.hexdigest()


class BlockChain:
    def __init__(self):
        self.head = None
        self.length = 0

    # Blockchain is Append Only ledger

    def append(self, value):
        if value is None:
            return

        self.length += 1
        current = self.head

        if current is None:
            block = Block("1-1-2019", value, None)
            self.head = block
        else:
            while current.next:
                current = current.next
            current.next = Block("1-1-2019", value, current.hash)

#Test Cases
Bitcoin = BlockChain()
Bitcoin.append('1BTC')
Bitcoin.append('2BTC')
Bitcoin.append(' 3BTC')
Bitcoin.append(None)

print(Bitcoin.head.data)

b = Bitcoin.head.next
c = Bitcoin.head.next.next
print(b.hash == c.previous_hash)

print(c.data)
