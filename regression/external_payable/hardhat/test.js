const {
  loadFixture,
} = require("@nomicfoundation/hardhat-toolbox/network-helpers");
const { expect } = require("chai");

describe("External Payable", function () {
  async function deployContract() {
    const [owner] = await ethers.getSigners();

    const ExternalPayable = await ethers.deployContract("ExternalPayable");
    const PayableInterface = await ethers.deployContract("PayableInterface");
    

    await owner.sendTransaction({
      to: await ExternalPayable.getAddress(),
      value: ethers.parseEther("0.000000000000000100"), // 100 wei
    });

    return { ExternalPayable, PayableInterface};
  }

  it("after calling the function `PayableInterface.f()` the contract balance is not decreased by 10", async function(){
    const { ExternalPayable, PayableInterface } = await loadFixture(deployContract);

    await expect(ExternalPayable.g(PayableInterface)).to.be.revertedWith("Too much ether");
    expect(await ExternalPayable.balanceOf(ExternalPayable.getAddress())).not.to.equal(90);
  })

  it("[DEBUG] after calling the function `PayableInterface.f()` the contract balance is still 100", async function(){
    const { ExternalPayable, PayableInterface } = await loadFixture(deployContract);

    await expect(ExternalPayable.g(PayableInterface)).to.be.revertedWith("Too much ether");
    expect(await ExternalPayable.balanceOf(ExternalPayable.getAddress())).to.equal(100);
  })
});
