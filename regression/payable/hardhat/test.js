const {
  loadFixture,
} = require("@nomicfoundation/hardhat-toolbox/network-helpers");
const { expect } = require("chai");

describe("Payable", function() {
  async function deployContract() {
    const [owner] = await ethers.getSigners();

    const Payable = await ethers.deployContract("Payable");
    const SecondPayable = await ethers.deployContract("SecondPayable");
    

    await owner.sendTransaction({
      to: await Payable.getAddress(),
      value: ethers.parseEther("0.000000000000000100"), // 100 wei
    });

    return { Payable, SecondPayable};
  }
  it("after calling the function `g()` the contract balance is not decreased by 10", async function(){
    const { Payable, SecondPayable } = await loadFixture(deployContract);
    let secondPayableAddress = SecondPayable.getAddress();
    await Payable.g(secondPayableAddress);
    expect(await Payable.balanceOf(Payable.getAddress())).not.to.equal(90);
  })
})