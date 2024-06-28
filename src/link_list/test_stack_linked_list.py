
import sys,os
sys.path.append(os.path.join(os.path.abspath('..'),"src"))
print(sys.path)
from unittest import TestCase
from stack_linked_list import Stack
class TestStack(TestCase):
    test_stack = None
    def setUpClass(cls):
        cls.test_stack = Stack()

    def test_insertion(self):
        self.assertEqual(TestStack.test_stack.add(12),1)
        self.assertEqual(TestStack.test_stack.add(15),1)
        self.assertEqual(TestStack.test_stack.add(11),1)
        self.assertEqual(TestStack.test_stack.add(19),1)
    
    def test_length(self):
        self.assertEqual(TestStack.test_stack.len, 4)
        self.assertEqual(TestStack.test_stack.length(),4)
    
