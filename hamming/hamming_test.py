import unittest

from hamming import hamming


class HammingTest(unittest.TestCase):

    def test_no_difference_between_identical_strands(self):
        self.assertEqual(0, hamming('A', 'A'))

    def test_complete_hamming_distance_of_for_single_nucleotide_strand(self):
        self.assertEqual(1, hamming('A', 'G'))

    def test_complete_hamming_distance_of_for_small_strand(self):
        self.assertEqual(2, hamming('AG', 'CT'))

    def test_small_hamming_distance(self):
        self.assertEqual(1, hamming('AT', 'CT'))

    def test_small_hamming_distance_in_longer_strand(self):
        self.assertEqual(1, hamming('GGACG', 'GGTCG'))

    def test_large_hamming_distance(self):
        self.assertEqual(4, hamming('GATACA', 'GCATAA'))

    def test_hamming_distance_in_very_long_strand(self):
        self.assertEqual(9, hamming('GGACGGATTCTG', 'AGGACGGATTCT'))


if __name__ == '__main__':
    unittest.main()
