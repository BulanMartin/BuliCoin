from blockchain import Blockchain

class BuliCoin(Blockchain):

    def __init__(self):
        super().__init__()

        self.nodes = set()

