import unittest
from robustbase import*

class TestRobust(unittest.TestCase):

	def test_Qn(self):
		result = Qn([1,2,3,4,5,6])
		self.assertEqual(result, 4.4438)



if __name__ == '__main__':
	unittest.main()