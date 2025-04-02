//https://github.com/leonardoalt/cav_2022_artifact/blob/main/regression/inline_assembly/assembly_memory_write.sol

pragma solidity ^0.8.29;
contract AssemblyMstore {
	struct S {
		uint x;
	}

	S s;

	function f() public {
		s.x = 42;
		S memory sm = s;
		uint256 i = 7;
		assembly {
			mstore(sm, i)
		}
        s = sm;
	}
}