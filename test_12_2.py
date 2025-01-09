from runner_and_tournament import Runner,Tournament
import unittest

class TournamentTest(unittest.TestCase):


    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def setUpClass(cls):
        cls.counter = 0
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for i in range(1, max(cls.all_results.keys()) + 1):
            print(cls.all_results[i])

    def test_runners_1(self):
        TournamentTest.counter += 1
        t = Tournament(90, self.runner_1, self.runner_3)
        result = t.start()
        TournamentTest.all_results[TournamentTest.counter] = result
        self.assertTrue('Ник' == result[max(result.keys())])

    def test_runners_2(self):
        TournamentTest.counter += 1
        t = Tournament(90, self.runner_2, self.runner_3)
        result = t.start()
        TournamentTest.all_results[TournamentTest.counter] = result
        self.assertTrue('Ник' == result[max(result.keys())])

    def test_runners_3(self):
        TournamentTest.counter += 1
        t = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = t.start()
        TournamentTest.all_results[TournamentTest.counter] = result
        self.assertTrue('Ник' == result[max(result.keys())])


if __name__ == "__main__":
    unittest.main()
