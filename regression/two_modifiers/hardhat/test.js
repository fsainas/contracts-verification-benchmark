const {
  loadFixture,
} = require("@nomicfoundation/hardhat-toolbox/network-helpers");
const { expect } = require("chai");

describe("TwoModifiers", function() {
  async function deployContract() {
    const [owner] = await ethers.getSigners();

    const TwoModifiers = await ethers.deployContract("TwoModifiers");

    return { TwoModifiers };
  }
    it("checks that x does not hold the correct value after the call to `g`", async function(){
      const { TwoModifiers } = await loadFixture(deployContract);
      await TwoModifiers.g();
      expect(await TwoModifiers.getX()).not.to.equal(3);
    })
})