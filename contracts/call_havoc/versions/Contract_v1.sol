pragma solidity >= 0.8.2;

contract CallHavoc {
    uint y;
    
    function g() public {
        y = 1;
    }
    
    function f() public {
        y = 0;

        (bool succ,) = msg.sender.call{value: 0}("");
        require(succ);
    }
}

rule P {
    env e;
    f(e);

    assert currentContract.y == 0;
}

https://prover.certora.com/output/95211/4099a0e4788a418ab4e5a39be7d1f93a?anonymousKey=ad8995ea8af573c37651b11fc4a17faa032d09ff
