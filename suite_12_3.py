import unittest

from test_12_3 import RunnerTest
from test_12_3 import TournamentTest

common_ts = unittest.TestSuite()
common_ts.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
common_ts.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(common_ts)
