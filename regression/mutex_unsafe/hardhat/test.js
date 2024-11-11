const {
  loadFixture,
} = require("@nomicfoundation/hardhat-toolbox/network-helpers");
const { expect } = require("chai");

describe("MutexUnsafe", function () {
  async function deployContract() {

    const MutexUnsafe = await(ethers.deployContract("MutexUnsafe"));
    const Attack = await(ethers.deployContract("Attack"));

    return { MutexUnsafe, Attack};
  }

  it("The contract does not use mutexes correctly because function `f` is not marked as `mutex`, making it vulnerable to reentrancy attacks", async function () {
    const { MutexUnsafe, Attack } = await loadFixture(deployContract);
    
    await MutexUnsafe.f(Attack.getAddress())
    expect(await MutexUnsafe.getX()).not.to.equal(0);
  });
});
