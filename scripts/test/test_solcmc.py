from tools.solcmc import run
import unittest
import tempfile
import os
from utils import (
        STRONG_POSITIVE,
        STRONG_NEGATIVE,
        WEAK_POSITIVE,
        WEAK_NEGATIVE,
        NONDEFINABLE,
        UNKNOWN,
        ERROR
        )


class TestRunFunction(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory and file for testing
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_version_path = os.path.join(self.temp_dir.name, 'test_v1.sol')
        self.temp_version = '''contract TestContract {
    uint x = 0;

    constructor() {
        x = 0;
    }

    function fun1() public {
        return 1;
    }

}
'''

    def tearDown(self):
        # Cleanup: close the temporary directory
        self.temp_dir.cleanup()

    def test_run_file_not_found(self):
        # Call the run function with a non-existent file
        file = 'nonexistent_file.sol'
        outcome, log = run(file)

        # Assert that the function returned the expected outcome and log for this case
        self.assertEqual(outcome, ERROR)
        self.assertEqual(log, f'{file} not found.')

    def test_tag_nondef(self):
        temp_contract_path = os.path.join(self.temp_dir.name, 'temp.sol')
        temp_contract = '''contract TestContract {
    uint x = 0;

    /// @custom:nondef This property is nondefinable.
}
'''
        with open(temp_contract_path, 'w') as f:
            f.write(temp_contract)

        outcome, log = run(temp_contract_path)

        self.assertEqual(outcome, NONDEFINABLE)
        self.assertEqual(log, 'This property is nondefinable.')

    def test_tag_negate(self):
        temp_contract_path = os.path.join(self.temp_dir.name, 'temp.sol')
        temp_contract = '''contract TestContract {
    uint x = 0;

    /// @custom:negate
    function invariant() public {
        assert(false);
    }

}
'''
        with open(temp_contract_path, 'w') as f:
            f.write(temp_contract)

        outcome, log = run(temp_contract_path)

        self.assertEqual(outcome, STRONG_POSITIVE)

    def test_strong_negative(self):
        temp_contract_path = os.path.join(self.temp_dir.name, 'temp.sol')
        temp_contract = '''contract TestContract {
    uint x = 0;

    function invariant() public {
        assert(false);
    }

}
'''
        with open(temp_contract_path, 'w') as f:
            f.write(temp_contract)

        outcome, log = run(temp_contract_path)

        self.assertEqual(outcome, STRONG_NEGATIVE)

    def test_strong_positive(self):
        temp_contract_path = os.path.join(self.temp_dir.name, 'temp.sol')
        temp_contract = '''contract TestContract {
    uint x = 0;

    function invariant() public {
        assert(true);
    }

}
'''
        with open(temp_contract_path, 'w') as f:
            f.write(temp_contract)

        outcome, log = run(temp_contract_path)

        self.assertEqual(outcome, STRONG_POSITIVE)

    def test_unknown(self):
        temp_contract_path = os.path.join(self.temp_dir.name, 'temp.sol')
        temp_contract = '''contract TestContract {
    mapping(address => uint) m;

    function f(address a, address b) public {
        require(a != b);
        m[a] = 1;
        assert(m[b] != 1);
    }

}
'''
        with open(temp_contract_path, 'w') as f:
            f.write(temp_contract)

        outcome, log = run(temp_contract_path, '0.0001s')

        self.assertEqual(outcome, UNKNOWN)

    def test_invalid_timeout(self):
        temp_contract_path = os.path.join(self.temp_dir.name, 'temp.sol')
        temp_contract = '''contract TestContract {
    uint x;

    function f(uint y) public {
        x = y;
    }

}
'''
        with open(temp_contract_path, 'w') as f:
            f.write(temp_contract)

        outcome, log = run(temp_contract_path, '10ms')

        self.assertEqual(outcome, ERROR)
        self.assertEqual(log, 'Invalid time interval "10ms".')

    def test_wrong_import_lib(self):
        temp_contract_path = os.path.join(self.temp_dir.name, 'temp.sol')
        temp_contract = '''import "lib/IERC20.sol";
contract TestContract {
    uint x;

    function f(uint y) public {
        x = y;
    }

}
'''
        with open(temp_contract_path, 'w') as f:
            f.write(temp_contract)

        outcome, log = run(temp_contract_path)

        self.assertEqual(outcome, ERROR)
        self.assertEqual(log, 'Use the dot to make a relative import: e.g. "./lib/lib.sol"')


if __name__ == '__main__':
    unittest.main()
