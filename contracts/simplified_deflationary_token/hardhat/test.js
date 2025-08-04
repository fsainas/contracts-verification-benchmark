const {
    loadFixture,
  } = require("@nomicfoundation/hardhat-toolbox/network-helpers");
  const { expect } = require("chai");

  describe("SimplifiedDeflationaryToken", function() {
    async function deployContractv1() {
      const [owner, sender, receiver] = await ethers.getSigners();

      const sdtv1 = await ethers.getContractFactory("SimplifiedDeflationaryTokenV1");
      const SDTv1 = await sdtv1.connect(owner).deploy();

      const sdtv2 = await ethers.getContractFactory("SimplifiedDeflationaryTokenV2");
      const SDTv2 = await sdtv2.connect(owner).deploy();

      return { SDTv1, SDTv2, owner, sender, receiver };
    }
      it("Token duplication", async function(){
        const { SDTv1, owner, sender, receiver } = await loadFixture(deployContractv1);
        await SDTv1.connect(owner).transfer(sender.address, 100);
        
        await SDTv1.connect(sender).transfer(receiver.address, 100);
        
        let balanceOwner = await SDTv1.balanceOf(owner.address);
        let balanceSender = await SDTv1.balanceOf(sender.address);
        let balanceReceiver = await SDTv1.balanceOf(receiver.address);
        
        expect(
          balanceReceiver+balanceOwner+balanceSender
        ).to.be.gt(await SDTv1.totalSupply());
      })
      
      it("Unpaid Fee", async function(){
        const { SDTv2, owner, sender, receiver } = await loadFixture(deployContractv1);
        await SDTv2.connect(owner).transfer(sender.address, 100);
        
        let balanceBeforeOwner = await SDTv2.balanceOf(owner.address);

        await SDTv2.connect(sender).transfer(receiver.address, 9);
      
        expect(
          await SDTv2.balanceOf(owner.address)
        ).to.be.equal(balanceBeforeOwner);
      })
  })
