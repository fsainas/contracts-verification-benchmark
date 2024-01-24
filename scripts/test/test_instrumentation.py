from setup.instrumentation import instrument_contracts
import unittest
import tempfile
import os


class TestInstrumentContracts(unittest.TestCase):

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
        # Write a simple contract to the temporary file
        with open(self.temp_version_path, 'w') as f:
            f.write(self.temp_version)

    def tearDown(self):
        # Cleanup: close the temporary directory
        self.temp_dir.cleanup()

    def test_filename(self):
        temp_prop_path = os.path.join(self.temp_dir.name, 'prop-id.sol')

        with open(temp_prop_path, 'w') as f:
            f.write('.')     # Empty property

        contracts = instrument_contracts([self.temp_version_path], [temp_prop_path])

        for name in contracts:
            self.assertEqual(name, 'test_prop-id_v1.sol')

    def test_negation_header(self):
        temp_prop_path = os.path.join(self.temp_dir.name, 'temp-prop.sol')
        temp_prop = '''/// @custom:negate
/// @custom:invariant
function invariant() public {
    assert(x == 1);
}
'''
        expected = '''contract TestContract {
    uint x = 0;

    constructor() {
        x = 0;
    }

    function fun1() public {
        return 1;
    }

    /// @custom:negate
    /// @custom:invariant
    function invariant() public {
        assert(x == 1);
    }
}
'''
        with open(temp_prop_path, 'w') as f:
            f.write(temp_prop)

        contracts = instrument_contracts([self.temp_version_path], [temp_prop_path])

        for contract in contracts.values():
            self.assertEqual(contract, expected)

    def test_negation_middle(self):
        temp_prop_path = os.path.join(self.temp_dir.name, 'temp-prop.sol')
        temp_prop = '''/// @custom:invariant
function invariant() public {
    assert(x == 1);
    /// @custom:negate
}
'''
        expected = '''contract TestContract {
    uint x = 0;

    constructor() {
        x = 0;
    }

    function fun1() public {
        return 1;
    }

    /// @custom:invariant
    function invariant() public {
        assert(x == 1);
        /// @custom:negate
    }
}
'''
        with open(temp_prop_path, 'w') as f:
            f.write(temp_prop)

        contracts = instrument_contracts([self.temp_version_path], [temp_prop_path])

        for contract in contracts.values():
            self.assertEqual(contract, expected)

    def test_nondef(self):
        temp_prop_path = os.path.join(self.temp_dir.name, 'temp-prop.sol')
        temp_prop = '/// @custom:nondef This property is nondefinable.'
        expected = '''contract TestContract {
    uint x = 0;

    constructor() {
        x = 0;
    }

    function fun1() public {
        return 1;
    }

    /// @custom:nondef This property is nondefinable.
}
'''
        with open(temp_prop_path, 'w') as f:
            f.write(temp_prop)

        contracts = instrument_contracts([self.temp_version_path], [temp_prop_path])

        for contract in contracts.values():
            self.assertEqual(contract, expected)

    def test_nondef_header(self):
        temp_prop_path = os.path.join(self.temp_dir.name, 'temp-prop.sol')
        temp_prop = '''/// @custom:nondef nondefinable property
/// @custom:invariant
function invariant() public {
    assert(x == 1);
}
'''
        expected = '''contract TestContract {
    uint x = 0;

    constructor() {
        x = 0;
    }

    function fun1() public {
        return 1;
    }

    /// @custom:nondef nondefinable property
    /// @custom:invariant
    function invariant() public {
        assert(x == 1);
    }
}
'''
        with open(temp_prop_path, 'w') as f:
            f.write(temp_prop)

        contracts = instrument_contracts([self.temp_version_path], [temp_prop_path])

        for contract in contracts.values():
            self.assertEqual(contract, expected)

    def test_nondef_middle(self):
        temp_prop_path = os.path.join(self.temp_dir.name, 'temp-prop.sol')
        temp_prop = '''/// @custom:invariant
function invariant() public {
    assert(x == 1);
    /// @custom:nondef nondefinable property
}
'''
        expected = '''contract TestContract {
    uint x = 0;

    constructor() {
        x = 0;
    }

    function fun1() public {
        return 1;
    }

    /// @custom:invariant
    function invariant() public {
        assert(x == 1);
        /// @custom:nondef nondefinable property
    }
}
'''
        with open(temp_prop_path, 'w') as f:
            f.write(temp_prop)

        contracts = instrument_contracts([self.temp_version_path], [temp_prop_path])

        for contract in contracts.values():
            self.assertEqual(contract, expected)

    def test_constructor_precond(self):
        temp_prop_path = os.path.join(self.temp_dir.name, 'temp-prop.sol')
        temp_prop = '''/// @custom:precond constructor
require(x == 1);
'''
        expected = '''contract TestContract {
    uint x = 0;

    constructor() {
        /// @custom:precond constructor
        require(x == 1);
        x = 0;
    }

    function fun1() public {
        return 1;
    }

}
'''
        with open(temp_prop_path, 'w') as f:
            f.write(temp_prop)

        contracts = instrument_contracts([self.temp_version_path], [temp_prop_path])

        for contract in contracts.values():
            self.assertEqual(contract, expected)

    def test_constructor_postcond(self):
        temp_prop_path = os.path.join(self.temp_dir.name, 'temp-prop.sol')
        temp_prop = '''/// @custom:postcond constructor
assert(x == 0);
'''
        expected = '''contract TestContract {
    uint x = 0;

    constructor() {
        x = 0;
        /// @custom:postcond constructor
        assert(x == 0);
    }

    function fun1() public {
        return 1;
    }

}
'''
        with open(temp_prop_path, 'w') as f:
            f.write(temp_prop)

        contracts = instrument_contracts([self.temp_version_path], [temp_prop_path])

        for contract in contracts.values():
            self.assertEqual(contract, expected)

    def test_fun_precond(self):
        temp_prop_path = os.path.join(self.temp_dir.name, 'temp-prop.sol')
        temp_prop = '''/// @custom:precond function fun1
require(x == 1);
'''
        expected = '''contract TestContract {
    uint x = 0;

    constructor() {
        x = 0;
    }

    function fun1() public {
        /// @custom:precond function fun1
        require(x == 1);
        return 1;
    }

}
'''
        with open(temp_prop_path, 'w') as f:
            f.write(temp_prop)

        contracts = instrument_contracts([self.temp_version_path], [temp_prop_path])

        for contract in contracts.values():
            self.assertEqual(contract, expected)

    def test_fun_postcond(self):
        temp_prop_path = os.path.join(self.temp_dir.name, 'temp-prop.sol')
        temp_prop = '''/// @custom:postcond function fun1
assert(x == 0);
'''
        expected = '''contract TestContract {
    uint x = 0;

    constructor() {
        x = 0;
    }

    function fun1() public {
        /// @custom:postcond function fun1
        assert(x == 0);
        return 1;
    }

}
'''
        with open(temp_prop_path, 'w') as f:
            f.write(temp_prop)

        contracts = instrument_contracts([self.temp_version_path], [temp_prop_path])

        for contract in contracts.values():
            self.assertEqual(contract, expected)

    def test_plain_invariant(self):
        temp_prop_path = os.path.join(self.temp_dir.name, 'temp-prop.sol')
        temp_prop = '''function invariant() public {
    assert(x == 1);
}
'''
        expected = '''contract TestContract {
    uint x = 0;

    constructor() {
        x = 0;
    }

    function fun1() public {
        return 1;
    }

    function invariant() public {
        assert(x == 1);
    }
}
'''
        with open(temp_prop_path, 'w') as f:
            f.write(temp_prop)

        contracts = instrument_contracts([self.temp_version_path], [temp_prop_path])

        for contract in contracts.values():
            self.assertEqual(contract, expected)

    def test_invariant(self):
        temp_prop_path = os.path.join(self.temp_dir.name, 'temp-prop.sol')
        temp_prop = '''/// @custom:invariant
function invariant() public {
    assert(x == 1);
}
'''
        expected = '''contract TestContract {
    uint x = 0;

    constructor() {
        x = 0;
    }

    function fun1() public {
        return 1;
    }

    /// @custom:invariant
    function invariant() public {
        assert(x == 1);
    }
}
'''
        with open(temp_prop_path, 'w') as f:
            f.write(temp_prop)

        contracts = instrument_contracts([self.temp_version_path], [temp_prop_path])

        for contract in contracts.values():
            self.assertEqual(contract, expected)


if __name__ == '__main__':
    unittest.main()
