# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test here! ######')
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info(f"curr_state={dut.current_state.value}")
    dut._log.info(f"next_state={dut.next_state.value}")
    assert dut.current_state.value == dut.SEQ_1.value,f"Output is incorrect {dut.current_state}!={dut.SEQ_1.value}"
    
    

    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info(f"curr_state={dut.current_state.value}")
    dut._log.info(f"next_state={dut.next_state.value}")
    assert dut.current_state.value == dut.SEQ_1.value,f"Output is incorrect {dut.current_state}!={dut.SEQ_1.value}"
