from tools.solcmc import run
import unittest
import tempfile
import os
from unittest.mock import patch
from utils import (
        STRONG_POSITIVE,
        STRONG_NEGATIVE,
        WEAK_POSITIVE,
        WEAK_NEGATIVE,
        NONDEFINABLE,
        ERROR
        )

class TestRunFunction(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory and file for testing
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_file = os.path.join(self.temp_dir.name, "test_contract.sol")

        # Write a simple contract to the temporary file
        with open(self.temp_file, "w") as f:
            f.write("contract TestContract {}")

    def tearDown(self):
        # Cleanup: close the temporary directory
        self.temp_dir.cleanup()

    '''
    def test_run_successful(self):
        # Mock subprocess.run to simulate a successful run
        with patch('subprocess.run') as mock_run:
            mock_run.return_value.stdout = "Mocked stdout"
            mock_run.return_value.stderr = "Mocked stderr"
            mock_run.return_value.returncode = 0

            # Call the run function with the temporary file
            outcome, log = run(self.temp_file)

        # Assert that the function returned the expected outcome and log
        self.assertEqual(outcome, "expected_outcome")
        self.assertEqual(log, "expected_log")
    '''

    def test_run_file_not_found(self):
        # Call the run function with a non-existent file
        file = 'nonexistent_file.sol'
        outcome, log = run(file)

        # Assert that the function returned the expected outcome and log for this case
        self.assertEqual(outcome, ERROR)
        self.assertEqual(log, f'{file} not found.')

    # Add more test methods as needed for different scenarios

if __name__ == '__main__':
    unittest.main()
