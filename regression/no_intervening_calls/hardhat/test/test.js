const {
    loadFixture
} = require("@nomicfoundation/hardhat-toolbox/network-helpers");
const { expect } = require("chai");

describe("NoInterveningCalls", function () {
    async function deployContract() {

        const NoInterveningCalls = await(ethers.deployContract("NoInterveningCalls"));

        return { NoInterveningCalls };
    }

    it("`g()` is called in between the two calls to `f()`, which results in the value of `b` changing", async function () {
        const { NoInterveningCalls } = await loadFixture(deployContract);

        await NoInterveningCalls.f();
        await NoInterveningCalls.g();
        await NoInterveningCalls.f();
        expect(await NoInterveningCalls.getB()).to.equal(false);
    })
});