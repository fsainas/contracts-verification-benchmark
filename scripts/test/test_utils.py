from utils import get_properties
import unittest
import tempfile
import os


class TestGetPropertiesFunction(unittest.TestCase):

    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.version_name = 'Test_v1.sol'
        self.version_path = os.path.join(self.dir.name, self.version_name)

    def tearDown(self):
        # Cleanup: close the temporary directory
        self.dir.cleanup()

    def test_no_specific_properties(self):
        property_names = ['p1.sol', 'abc.sol', 'prop-3.sol']
        expected_names = ['p1.sol', 'abc.sol', 'prop-3.sol']
        property_paths = [os.path.join(self.dir.name, pn) for pn in property_names]
        expected_paths = [os.path.join(self.dir.name, e) for e in expected_names]
        res = get_properties(self.version_path, property_paths)
        self.assertEqual(res, expected_paths)

    def test_all_specific(self):
        property_names = ['p1_v1.sol', 'abc_v1.sol', 'prop-3_v1.sol']
        expected_names = ['p1_v1.sol', 'abc_v1.sol', 'prop-3_v1.sol']
        property_paths = [os.path.join(self.dir.name, pn) for pn in property_names]
        expected_paths = [os.path.join(self.dir.name, e) for e in expected_names]
        res = get_properties(self.version_path, property_paths)
        self.assertEqual(res, expected_paths)

    def test_one_specific(self):
        property_names = ['p1_v1.sol', 'p1.sol', 'prop-3.sol']
        expected_names = ['p1_v1.sol', 'prop-3.sol']
        property_paths = [os.path.join(self.dir.name, pn) for pn in property_names]
        expected_paths = [os.path.join(self.dir.name, e) for e in expected_names]
        res = get_properties(self.version_path, property_paths)
        self.assertEqual(res, expected_paths)

    def test_two_specific1(self):
        property_names = ['p1_v1.sol', 'p1_v2.sol', 'prop-3.sol']
        expected_names = ['p1_v1.sol', 'prop-3.sol']
        property_paths = [os.path.join(self.dir.name, pn) for pn in property_names]
        expected_paths = [os.path.join(self.dir.name, e) for e in expected_names]
        res = get_properties(self.version_path, property_paths)
        self.assertEqual(res, expected_paths)

    def test_two_specific2(self):
        property_names = ['p1_v1.sol', 'abc_v2.sol', 'prop-3.sol']
        expected_names = ['p1_v1.sol', 'prop-3.sol']
        property_paths = [os.path.join(self.dir.name, pn) for pn in property_names]
        expected_paths = [os.path.join(self.dir.name, e) for e in expected_names]
        res = get_properties(self.version_path, property_paths)
        self.assertEqual(res, expected_paths)


if __name__ == '__main__':
    unittest.main()
