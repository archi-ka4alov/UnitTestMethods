from runner_and_tournament import Runner,Tournament
import unittest

class TournamentTest(unittest.TestCase):
    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = []


    @classmethod
    def tearDownClass(cls):
        for i in range(len(cls.all_results), 0, -1):
            print(cls.all_results[i - 1])


    def test_runners_1_and_3(self):
        t = Tournament(90, self.runner_1, self.runner_3)
        result = t.start()
        TournamentTest.all_results.append(result)
        self.assertTrue('Ник' == result[max(result.keys())])


    def test_runners_2_and_3(self):
        t = Tournament(90, self.runner_2, self.runner_3)
        result = t.start()
        TournamentTest.all_results.append(result)
        self.assertTrue('Ник' == result[max(result.keys())])


    def test_runners_1_and_2_and_3(self):
        t = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = t.start()
        TournamentTest.all_results.append(result)
        self.assertTrue('Ник' == result[max(result.keys())])


if __name__ == "__main__":
    unittest.main()