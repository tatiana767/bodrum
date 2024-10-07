
import module_12_4 as m1
import module_12_1 as m2
import unittest



runnertest = unittest.TestSuite()
runnertest.addTest(unittest.TestLoader().loadTestsFromTestCase(m1.TournamentTest))
runnertest.addTest(unittest.TestLoader().loadTestsFromTestCase(m2.RunnerTest))
run = unittest.TextTestRunner(verbosity=2)
run.run(runnertest)



