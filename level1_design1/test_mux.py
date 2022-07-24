# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux12"""

    x=12
    A = 1
   
    dut.inp12.value = A
    dut.sel.value = x
    
    await Timer(2, units='ns')
    assert dut.out.value == L, f"Mux result is incorrect: {dut.X.value}!=1"


    @cocotb.test()
async def test_ran_mux(dut):
    """Test for mux30"""

     y=30
     B = 2

     dut.inp30.value = B
     dut.sel.value = y
    await Timer(2, units='ns')
    assert dut.out.value == e, f"Mux result is incorrect: {dut.X.value}!=2"
