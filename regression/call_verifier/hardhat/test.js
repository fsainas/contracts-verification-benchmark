const {
  loadFixture,
} = require("@nomicfoundation/hardhat-toolbox/network-helpers");
const { expect } = require("chai");

describe("CallVerifier", function () {
  async function deployContract() {

    const CallVerifier = await(ethers.deployContract("CallVerifier"));
    const Successful = await(ethers.deployContract("Successful"));
    const Failure = await(ethers.deployContract("Failure"));

    return { CallVerifier, Successful, Failure};
  }

  it("Successful External call", async function () {
    const { CallVerifier, _, Failure } = await loadFixture(deployContract);
    
    await CallVerifier.f(Failure.getAddress())
    expect(await CallVerifier.getCallSuccessful()).to.be.false;
  });

  it("Failure External call", async function () {
    const { CallVerifier, Successful, _ } = await loadFixture(deployContract);
    
    await CallVerifier.f(Successful.getAddress())
    expect(await CallVerifier.getCallSuccessful()).to.be.true;
  });

});
