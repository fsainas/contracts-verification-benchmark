methods {
       function getOwner() external returns (address) envfree;
       function getBalance() external returns (uint);
       function getStart() external returns (uint) envfree;
       function getIsCommitted() external returns (bool) envfree;
       function commit(bytes32) external;
       function reveal(string) external;
       function timeout() external;
}
