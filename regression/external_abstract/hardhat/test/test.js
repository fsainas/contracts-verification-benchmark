const {
    loadFixture
} = require("@nomicfoundation/hardhat-toolbox/network-helpers");
const { expect } = require("chai");

describe("ExternalAbstract", function () {
    async function deployContract () {
        const DImpl = await ethers.deployContract("DImpl");
        const ExternalAbstract = await ethers.deployContract(
            "ExternalAbstract", [ DImpl ]
        );

        await DImpl.set_ext(ExternalAbstract);

        return { ExternalAbstract };
    }

    it("If an implementation of `D` which calls `f()` is used in the contract, when `g()` is called the value of `x` will change", async function () {
        const { ExternalAbstract } = await loadFixture(deployContract);

        const x_before = await ExternalAbstract.getX();
        await ExternalAbstract.g();

        expect(await ExternalAbstract.getX()).to.not.equal(x_before);
    })
})