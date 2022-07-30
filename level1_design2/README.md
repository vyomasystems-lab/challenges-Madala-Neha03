# 31:1 MUX Design Verification


![new](https://user-images.githubusercontent.com/99884583/181202916-699119c3-4dbf-45cc-80cb-b044b2f8663d.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (sequence detector module here) are input_bit, reset, clock. The seq_seen is taken as output which gives value 1 if the sequence is detected otherwise zero .

The values are assigned to the input port using 

```
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

```

```
dut.inp_bit.value = 1
dut.inp_bit.value = 0
dut.inp_bit.value = 1
dut.inp_bit.value = 1
dut.inp_bit.value = 1
```

The assert statement is used for comparing the adder's outut to the expected value.

The following error is seen:

```
assert dut.seq_seen == 0,f"Output is incorrect {dut.seq_seen}!=0"
                     AssertionError: Output is incorrect 1!=0
```

## Test Scenario **(Important)**
- Test Inputs: inp_bit = 1,0,1,1,1
- Expected Output: out=1
- Observed Output in the DUT dut.seq_seen=1

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
 assign seq_seen = current_state == SEQ_1011 ? 1 : 0;                   ====> BUG

  // state transition
  always @(posedge clk)
  begin
    if(reset)
    begin
      current_state <= IDLE;
    end
    else
    begin
      current_state <= next_state;
    end
  end

  // state transition based on the input and current state
  always @(inp_bit or current_state)
  begin
    case(current_state)
      IDLE:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1;
        else
          next_state = IDLE;
      end
      SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = IDLE;                                            ====> BUG
        else
          next_state = SEQ_10;
      end
      SEQ_10:
      begin
        if(inp_bit == 1)
          next_state = SEQ_101;
        else
          next_state = IDLE;
      end
      SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = IDLE;                                              ====> BUG
      end
      SEQ_1011:
      begin
        next_state = IDLE;                                                 ====> BUG
      end
    endcase
  end
```

The assign statement should be synchronized with the clock, so that it can detect the sequence and result is obtained at a synchronized time otherwise the output is obtained before the prescribed time.
In the overlapped moore sequence detector 
-> if the state is SEQ_1 and input_bit is 1 the next state should be SEQ_1.
-> if the state is SEQ_101 and input_bit is 0 the next state should be SEQ_10.
-> if the state is SEQ_1011 and input_bit is 1 the next state should be SEQ_1, input_bit is 0 the next state should be SEQ_10.

## Design Fix
Updating the design and re-running the test makes the test pass.

![level1design1debugged](https://user-images.githubusercontent.com/99884583/181204811-16d723c8-52d1-41e8-b932-1df9397656bf.png)

The updated design is checked in as level1_design1_debugged.v

## Verification Strategy

Writing a testbench with a desired sequence and detecting whether the output is synchronized with the clock or delayed or forward in time.

## Is the verification complete ?
 
