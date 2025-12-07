import unittest
from inmemorydatabase import InMemoryDatabase

class Fig2Test(unittest.TestCase):

    def test_case_fig2(self):
        inmemorydb = InMemoryDatabase()
        
        self.assertIsNone(inmemorydb.get("A"))
        
        with self.assertRaises(Exception):
            inmemorydb.put("A", 5)
            
        inmemorydb.begin_transaction()
        
        inmemorydb.put("A", 5)
        
        self.assertIsNone(inmemorydb.get("A"))
        
        inmemorydb.put("A", 6)
        
        inmemorydb.commit()
        
        self.assertEqual(inmemorydb.get("A"), 6)
        
        with self.assertRaises(Exception):
            inmemorydb.commit()
            
        with self.assertRaises(Exception):
            inmemorydb.rollback()
            
        self.assertIsNone(inmemorydb.get("B"))
        
        inmemorydb.begin_transaction()
        
        inmemorydb.put("B", 10)
        
        inmemorydb.rollback()
        
        self.assertIsNone(inmemorydb.get("B"))
        
if __name__ == '__main__':
    unittest.main()
