const {
    loadFixture,
  } = require("@nomicfoundation/hardhat-toolbox/network-helpers");
  const { expect } = require("chai");
  
  describe("DepositERC20_v1", function() {
    async function deployContractv1() {
      const [receiver] = await ethers.getSigners();
  
      const ERC20Factory = await ethers.getContractFactory("ERC20");
      const ERC20 = await ERC20Factory.deploy(100);
      const DepositERC20Factory = await ethers.getContractFactory("TokenTransfer");
      const DepositERC20 = await DepositERC20Factory.deploy(ERC20.getAddress());
  
      return { DepositERC20, ERC20, receiver };
    }
      it("wd-leq-init-bal: the overall withdrawn amount exceed the initial deposit", async function(){
        const { DepositERC20, ERC20, receiver } = await loadFixture(deployContractv1);
        await DepositERC20.deposit();

        await DepositERC20.connect(receiver).withdraw(100);
        await ERC20.connect(receiver).transfer(DepositERC20, 100);
        await DepositERC20.connect(receiver).withdraw(100);

        expect(await DepositERC20.getSent()).to.be.equal(200);  


      })
  })
