 function getBalance() public view returns (uint) {
        return address(this).balance;
}

function getTotalReleasable() public view returns (uint) {
        uint _total_releasable = 0;
        for (uint i = 0; i < payees.length; i++) {
            _total_releasable += releasable(payees[i]);
        }
        return _total_releasable;
}

function getPayee(uint index) public view returns (address) {
        require(index < payees.length);
        return payees[index];
}

function getShares(address addr) public view returns (uint) {
        return shares[addr];
}

