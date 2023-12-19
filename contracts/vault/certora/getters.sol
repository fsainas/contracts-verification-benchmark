function getBalance() public view returns (uint) {
    return address(this).balance;
}

function getOwner() public view returns (address) {
    return owner;
}

function getRecovery() public view returns (address) {
    return recovery;
}

function getWaitTime() public view returns (uint) {
    return wait_time;
}

function getReceiver() public view returns (address) {
    return receiver;
}

function getRequestTime() public view returns (uint) {
    return request_time;
}

function getAmount() public view returns (uint) {
    return amount;
}

function getState() public view returns (States) {
    return state;
}

