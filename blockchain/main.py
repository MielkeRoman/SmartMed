class Blockchain(object):
    def __init__(self):
        self.chain = [] # зберігаємо в конструкторі наш блокчейн
        self.current_transactions = [] # зберігаємо в констукторі транзакції

    def new_block(self):
        # Створює новий блок та вносить його в data-ланцюг
        pass

    def new_block(self):
        # Вносить нову транзакцію в список транзакцій
        pass

    @staticmethod
    def hash(block):
        # Хешує блок
        pass

    @property
    def last_block(self):
        # Повертає останній блок в ланцюжку
        pass

    def new_transaction(self, sender, recipient, amount):
        # метод внесення транзакцій в блок.
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1