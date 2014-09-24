from world import World
import unittest

class WorldTest(unittest.TestCase):
    
    def test_the_answer(self):
        print 'testing world functions'
        
        w = World()
        answer = w.the_answer()

        self.assertEqual('43', answer)


if __name__ == '__main__':
    unittest.main()