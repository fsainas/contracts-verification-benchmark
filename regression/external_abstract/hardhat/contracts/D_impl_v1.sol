pragma solidity ^0.8.25;

import "./ExternalAbstract_v1.sol";

contract DImpl is D {
    ExternalAbstract ext;
    function d() external override {
        ext.f();
    }

    function set_ext(ExternalAbstract e) public{
        ext = e;
    }
}