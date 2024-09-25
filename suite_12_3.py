import unittest
from test_12_3 import RunnerTest, TournamentTest
test_suite = unittest.TestSuite()

test_suite.addTest(unittest.makeSuite(RunnerTest))
test_suite.addTest(unittest.makeSuite(TournamentTest))


runner = unittest.TextTestRunner(verbosity=2)

if __name__ == '__main__':
    runner.run(test_suite)