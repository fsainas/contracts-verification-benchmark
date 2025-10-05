const {
    loadFixture,
} = require("@nomicfoundation/hardhat-toolbox/network-helpers");
const { expect } = require("chai");


describe("Revert", function () {
    async function deployContract () {
        const Revert = await ethers.deployContract("Revert");

        return { Revert };
    }

    it("c-equals-a-with-b-true", async function () {
        const { Revert } = await loadFixture(deployContract);
        const a = 12;

        
        await expect(Revert.f(true, a)).to.be.reverted;
    })

    it("c-equals-a-with-b-false", async function() { 
        const { Revert } = await loadFixture(deployContract);
        const a = 12;
        await Revert.f(false, a);
        expect(await Revert.get_c()).to.not.be.equal(a);
    })
})