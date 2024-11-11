const {
  loadFixture,
} = require("@nomicfoundation/hardhat-toolbox/network-helpers");
const { expect } = require("chai");

beforeEach(async function () {
  this.Reentrancy = await ethers.deployContract("Reentrancy");
  this.ReentrancyAttack = await ethers.deployContract("ReentrancyAttack");
});

describe("Reentrancy", function() {
  async function deployContract() {
    const [owner] = await ethers.getSigners();

    const Reentrancy = await ethers.deployContract("Reentrancy");
    const ReentrancyAttack = await ethers.deployContract("ReentrancyAttack");

    return { Reentrancy, ReentrancyAttack};
  }
  it("The value of x is not 0 after the call to `f`", async function(){
    const { Reentrancy, ReentrancyAttack } = await loadFixture(deployContract);
    let reentrancyAttackAddress = ReentrancyAttack.getAddress();
    await Reentrancy.f(reentrancyAttackAddress);
    expect(await Reentrancy.getX()).not.to.equal(0);
  })
})