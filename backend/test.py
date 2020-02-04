import unittest

from app import check_distance

class TestGCDCalc(unittest.TestCase):

	def test_close(self):
		coordinates = [15.0, 10.0]

		self.assertTrue(check_distance(coordinates, 15.0, 10.0))
		self.assertTrue(check_distance(coordinates, 15.027, 10.0))
		self.assertTrue(check_distance(coordinates, 15.0, 9.98))

		self.assertFalse(check_distance(coordinates, 15.03, 9.0))
		self.assertFalse(check_distance(coordinates, 15.0, 9.97))

	def test_close_negative(self):
		coordinates = [-32.0, 72.0]

		self.assertTrue(check_distance(coordinates, -32.0, 72.0))
		self.assertTrue(check_distance(coordinates, -32.027, 72.0))
		self.assertTrue(check_distance(coordinates, -32.0, 72.02))

		self.assertFalse(check_distance(coordinates, -32.1, 72.0))
		self.assertFalse(check_distance(coordinates, -32.1, 72.1))

	def test_far(self):
		coordinates = [42.0, -42.0]

		self.assertFalse(check_distance(coordinates, 42.0, 42.0))
		self.assertFalse(check_distance(coordinates, 142.0, -42.0))
		
		# Trigonometric functions are periodic, allow overflow of typical
		#	geographical coordinates
		self.assertTrue(check_distance(coordinates, 42.0 + 360.0, -42.0))
		self.assertTrue(check_distance(coordinates, 42.0, -42.0 + 360))

if __name__ == "__main__":
	unittest.main()