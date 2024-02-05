 function getEndDonate() public view returns (uint) {
        return end_donate;
    }

    function getGoal() public view returns (uint) {
        return goal;
    }

    function getBalance() public view returns (uint) {
        return address(this).balance;
    }

    function balanceOf(address a) public view returns (uint) {
        return a.balance;
    }

    function getDonated(address a) public view returns (uint) {
        return donors[a];
    }

    function getOwner() public view returns (address) {
        return owner;
    }
