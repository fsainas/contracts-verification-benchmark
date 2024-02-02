import report_gen.scoring as scoring
import unittest
import tempfile
import os


class TestComputeScore(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory and file for testing
        self.temp_dir = tempfile.TemporaryDirectory()
        self.scoring_schema = scoring.get_scoring_schema()
        self.cm_header = 'property,version,result,footnote'

    def tearDown(self):
        # Cleanup: close the temporary directory
        self.temp_dir.cleanup()

    def test_valid_cm(self):
        temp_cm_path = os.path.join(self.temp_dir.name, 'cm.csv')
        temp_cm = self.cm_header
        temp_cm += """
bar,v1,ND
bar,v2,TP!
foo,v1,TP!
foo,v2,TP!"""

        expected = (self.scoring_schema['TP!'] * 3 +
                    self.scoring_schema['ND'])

        with open(temp_cm_path, 'w') as f:
            f.write(temp_cm)

        score = scoring.compute_score(temp_cm_path)

        self.assertEqual(score, expected)

    def test_all_outcomes(self):
        temp_cm_path = os.path.join(self.temp_dir.name, 'cm.csv')
        temp_cm = self.cm_header
        temp_cm += """
bar,v1,UNK
bar,v2,ND
foo,v1,FN!
foo,v2,FP!
foo,v3,FN
foo,v4,FP
foo,v5,TN!
foo,v6,TP!
foo,v7,TN
foo,v8,TP"""

        expected = (self.scoring_schema['UNK'] +
                    self.scoring_schema['ND'] +
                    self.scoring_schema['FN!'] +
                    self.scoring_schema['FP!'] +
                    self.scoring_schema['FN'] +
                    self.scoring_schema['FP'] +
                    self.scoring_schema['TN!'] +
                    self.scoring_schema['TP!'] +
                    self.scoring_schema['TN'] +
                    self.scoring_schema['TP'])

        with open(temp_cm_path, 'w') as f:
            f.write(temp_cm)

        score = scoring.compute_score(temp_cm_path)

        self.assertEqual(score, expected)

    def test_empty_cm(self):
        temp_cm_path = os.path.join(self.temp_dir.name, 'cm.csv')
        temp_cm = self.cm_header

        expected = 0

        with open(temp_cm_path, 'w') as f:
            f.write(temp_cm)

        score = scoring.compute_score(temp_cm_path)

        self.assertEqual(score, expected)


class TestCountOutcomes(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory and file for testing
        self.temp_dir = tempfile.TemporaryDirectory()
        self.cm_header = 'property,version,result,footnote'

    def tearDown(self):
        # Cleanup: close the temporary directory
        self.temp_dir.cleanup()

    def test_valid_cm(self):
        temp_cm_path = os.path.join(self.temp_dir.name, 'cm.csv')
        temp_cm = self.cm_header
        temp_cm += """
bar,v1,ND
bar,v2,TP!
foo,v1,TP!
foo,v2,TP!"""

        expected = {'ND': 1, 'TP!': 3}

        with open(temp_cm_path, 'w') as f:
            f.write(temp_cm)

        score = scoring.count_outcomes(temp_cm_path)

        self.assertEqual(score, expected)

    def test_all_outcomes(self):
        temp_cm_path = os.path.join(self.temp_dir.name, 'cm.csv')
        temp_cm = self.cm_header
        temp_cm += """
bar,v1,UNK
bar,v2,ND
foo,v1,FN!
foo,v2,FP!
foo,v3,FN
foo,v4,FP
foo,v5,TN!
foo,v6,TP!
foo,v7,TN
foo,v8,TP"""

        expected = {'UNK':  1,
                    'ND':   1,
                    'FN!':  1,
                    'FP!':  1,
                    'FN':   1,
                    'FP':   1,
                    'TN!':  1,
                    'TP!':  1,
                    'TN':   1,
                    'TP':   1}

        with open(temp_cm_path, 'w') as f:
            f.write(temp_cm)

        score = scoring.count_outcomes(temp_cm_path)

        self.assertEqual(score, expected)

    def test_empty_cm(self):
        temp_cm_path = os.path.join(self.temp_dir.name, 'cm.csv')
        temp_cm = self.cm_header

        expected = {}

        with open(temp_cm_path, 'w') as f:
            f.write(temp_cm)

        score = scoring.count_outcomes(temp_cm_path)

        self.assertEqual(score, expected)


if __name__ == '__main__':
    unittest.main()
