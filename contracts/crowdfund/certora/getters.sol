 function getEndDonate() public view returns (uint) {
        return end_donate;
    }

    function getGoal() public view returns (uint) {
        return goal;
    }

    function getBalance() public view returns (uint) {
        return address(this).balance;
    }

    function getReceiver() public view returns (address) {
        return receiver;
    }
