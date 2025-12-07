# Reference: https://www.dbvis.com/thetable/database-transactions-101-the-essential-guide/
# Reference: https://medium.com/@mithoonkumar/design-an-in-memory-nosql-database-ood-428d48b68dfa
# Reference: https://www.geeksforgeeks.org/java/java-util-hashmap-in-java-with-examples/
# Reference: https://www.geeksforgeeks.org/python/python-dictionary/

class InMemoryDatabase:
    def __init__(self):
        self.data = {}
        self.transaction = None
        
    def get(self, key):
        return self.data.get(key)
    
    def put(self, key, val):
        if self.transaction is None:
            raise Exception("the function put() is called but a transaction is not in progress")
        self.transaction[key] = val
        
    def begin_transaction(self):
        if self.transaction is not None:
            raise Exception("the function begin_transaction() is called but a transaction already in progress")
        self.transaction = {}
    
    def commit(self):
        if self.transaction is None:
            raise Exception("the function commit() is called but there is no transaction open")
        for key, val in self.transaction.items():
            self.data[key] = val
        self.transaction = None
        
    def rollback(self):
        if self.transaction is None:
            raise Exception("the function rollback() is called but there is no transaction ongoing")
        self.transaction = None
        