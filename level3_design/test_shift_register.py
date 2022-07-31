# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_shift_register(dut):
    """Test for shift register"""

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.rst.value = 1
    await FallingEdge(dut.clk)  
    dut.rst.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test here! ######')

    
    A = 11      #1011
    B = 6
    
  
    dut.ip.value = A
    dut.load.value = 1                         #load
    dut.sel.value = 0                          #left shift
    await FallingEdge(dut.clk)
    dut._log.info(f"ip={dut.ip.value}")
    dut._log.info(f"op={dut.op.value}")
    dut._log.info(f"load={dut.load.value}")
    dut._log.info(f"sel={dut.sel.value}")
    assert dut.op.value == A,f"Output is incorrect {dut.op.value}!=1011"

    
    dut.load.value = 0                         #load
    dut.sel.value = 0                          #left shift
    await FallingEdge(dut.clk)
    dut._log.info(f"ip={dut.ip.value}")
    dut._log.info(f"op={dut.op.value}")
    dut._log.info(f"load={dut.load.value}")
    dut._log.info(f"sel={dut.sel.value}")
    assert dut.op.value == B,f"Output is incorrect {dut.op.value}!=0110"



@cocotb.test()
async def test_shift_register_1(dut):
    """Test for shift register"""

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.rst.value = 1
    await FallingEdge(dut.clk)  
    dut.rst.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test here! ######')

    C = 10
    D = 5

    dut.ip.value = C
    dut.load.value = 1                                 #load
    dut.sel.value = 1                                  #right shift
    await FallingEdge(dut.clk)
    dut._log.info(f"ip={dut.ip.value}")
    dut._log.info(f"op={dut.op.value}")
    dut._log.info(f"load={dut.load.value}")
    dut._log.info(f"sel={dut.sel.value}")
    assert dut.op.value == C,f"Output is incorrect {dut.op.value}!=1010"

    dut.ip.value = C
    dut.load.value = 0                                  #load
    dut.sel.value = 1                                   #right shift
    await FallingEdge(dut.clk)
    dut._log.info(f"ip={dut.ip.value}")
    dut._log.info(f"op={dut.op.value}")
    dut._log.info(f"load={dut.load.value}")
    dut._log.info(f"sel={dut.sel.value}")
    assert dut.op.value == D,f"Output is incorrect {dut.op.value}!=0101"
