import unittest2

def fun(x):
	return x+1

class MyTest(unittest2.TestCase):
	def test(self):
		self.assertEqual(fun(3),4)

if __name__ == '__main__':
	unittest2.main()

