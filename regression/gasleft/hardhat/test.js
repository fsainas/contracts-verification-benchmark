const {
  loadFixture,
} = require("@nomicfoundation/hardhat-toolbox/network-helpers");
const { expect } = require("chai");

beforeEach(async function () {
  this.GasLeft = await ethers.deployContract("GasLeft");
});

describe("GasLeft", function() {
  async function deployContract() {
    const [owner] = await ethers.getSigners();

    const GasLeft = await ethers.deployContract("GasLeft");

    return { GasLeft };
  }

  it("There is less or equal gas left after the assignment", async function(){
    const { GasLeft } = await loadFixture(deployContract);
    await GasLeft.f();
    expect(await GasLeft.getAfterAssignment()).to.be.lessThanOrEqual(await GasLeft.getG());
  })
})