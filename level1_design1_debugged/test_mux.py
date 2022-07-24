# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux_inp12(dut):
    """Test for mux12"""

    A = 3
    B = 12
   
    dut.inp12.value = A
    dut.sel.value = B
    
    await Timer(2, units='ns')
    assert dut.out.value == A, "result is incorrect: {OUT} != {A}, expected value={EXP}".format(
        OUT=int(dut.out.value), A=int(dut.inp12.value), EXP=A)


@cocotb.test()
async def test_mux_inp30(dut):
    """Test for mux30"""

    A = 2
    B = 30
   
    dut.inp30.value = A
    dut.sel.value = B
    
    await Timer(2, units='ns')
    assert dut.out.value == A, "result is incorrect: {OUT} != {A}, expected value={EXP}".format(
        OUT=int(dut.out.value), A=int(dut.inp30.value), EXP=A)
