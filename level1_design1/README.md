# 31:1 MUX Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![new](https://user-images.githubusercontent.com/99884583/181202916-699119c3-4dbf-45cc-80cb-b044b2f8663d.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (mux module here) which takes in 31 inputs of 2 bits each, with a 4 bit select input and gives 2-bit output.
The inputs in the module are defined as *inp0,inp1,inp2,....inp30*. selct line is defined as *sel* and output line as *out*.

The values are assigned to the input port using 

```
dut.inp12.value = 3
dut.sel.value = 12
```

```
dut.inp30.value = 2
dut.sel.value = 30
```

The assert statement is used for comparing the adder's outut to the expected value.

The following error is seen:

```
assert dut.out.value == A, "result is incorrect: {OUT} != {A}, expected value={EXP}".format(
                     AssertionError: result is incorrect: 0 != 3, expected value=3
```

```
   assert dut.out.value == A, "result is incorrect: {OUT} != {A}, expected value={EXP}".format(
                     AssertionError: result is incorrect: 0 != 2, expected value=2
```
## Test Scenario **(Important)**
- Test Inputs: inp12=3 sel=12
- Expected Output: out=3
- Observed Output in the DUT dut.out.vlaue=0


- Test Inputs: inp30=2 sel=30
- Expected Output: out=2
- Observed Output in the DUT dut.out.vlaue=0

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
 case(sel)
      5'b00000: out = inp0;  
      5'b00001: out = inp1;  
      5'b00010: out = inp2;  
      5'b00011: out = inp3;  
      5'b00100: out = inp4;  
      5'b00101: out = inp5;  
      5'b00110: out = inp6;  
      5'b00111: out = inp7;  
      5'b01000: out = inp8;  
      5'b01001: out = inp9;  
      5'b01010: out = inp10;
      5'b01011: out = inp11;
      5'b01101: out = inp12;                 ====> BUG
      5'b01101: out = inp13;
      5'b01110: out = inp14;
      5'b01111: out = inp15;
      5'b10000: out = inp16;
      5'b10001: out = inp17;
      5'b10010: out = inp18;
      5'b10011: out = inp19;
      5'b10100: out = inp20;
      5'b10101: out = inp21;
      5'b10110: out = inp22;
      5'b10111: out = inp23;
      5'b11000: out = inp24;
      5'b11001: out = inp25;
      5'b11010: out = inp26;
      5'b11011: out = inp27;
      5'b11100: out = inp28;
      5'b11101: out = inp29;
      default: out = 0;                       ====> BUG
    endcase
  end
```
For the MUX design, the logic for inp12 should be ``5'b01100`` instead of ``5'b01101`` as in the design code.
The logic unit for inp30 5'b11110 is not present. so, the default case is applied and output is obtained as 0.

## Design Fix
Updating the design and re-running the test makes the test pass.

![](https://i.imgur.com/5XbL1ZH.png)

The updated design is checked in as level1_design1_debugged.v


