# Shift Register with different modes of operation

![level3bug](https://user-images.githubusercontent.com/99884583/182012581-f5e6d838-63be-41b2-b29d-6518c7693bd2.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (shift register module here) are input,load,select input, reset,clock. 
The register is having 3 bit input and output port, 2 bit select input to control the mode of operation including clk, reset and load signals. The rest signal resets the output to zero. The load signal loads the input parallely to the output. The control unit in this register is having four cases.
1. for case 00 it shifts the output to left
2. for case 01 it shifts the output to right
3. for case 10 it rotates the output to left
4. for case 11 it rotates the output to right

The values are assigned to the input port using 

```
     A = 11      #1011
     B = 6
    
    dut.ip.value = A
    dut.load.value = 1                         #load
    dut.sel.value = 0                          #left shift
    
    dut.load.value = 0                         #load
    dut.sel.value = 0                          #left shift
    
```

```
    C = 10
    D = 5

    dut.ip.value = C
    dut.load.value = 1                                 #load
    dut.sel.value = 1                                  #right shift

    dut.ip.value = C
    dut.load.value = 0                                  #load
    dut.sel.value = 1                                   #right shift
```

The assert statement is used for comparing the shift register output to the expected value.

The following error is seen:

```
assert dut.op.value == B,f"Output is incorrect {dut.op.value}!=0110"
                     AssertionError: Output is incorrect 0101!=0110
```

```
assert dut.op.value == D,f"Output is incorrect {dut.op.value}!=0101"
                     AssertionError: Output is incorrect 0100!=0101
```

## Test Scenario **(Important)**
- Test Inputs: ip = 1011, load = 1, sel = 0
-              ip = 1011, load = 0, sel = 0
- Expected Output: out = 0110
- Observed Output in the DUT dut.op.value=0101


- Test Inputs: ip = 1010, load = 1, sel = 1
-              ip = 1010, load = 0, sel = 1
- Expected Output: out = 0101
- Observed Output in the DUT dut.op.value=100

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
 begin
     if (rst)
       
       op = 0;
      
     else    
       case(load)
         1'b1: 
          begin                                 //Load Input
            op = ip;
          end
          
         1'b0:                                 //Operation 
           case (sel)
            2'b00:  op = op>>1;                //Left Shift                  ====> BUG
            2'b01:  op = op<<1;               //Right Shift                  ====> BUG
            2'b10:  op = {op[2:0],op[3]};    //Rotate Left
            2'b11:  op = {op[0], op[3:1]};  //Rotate Right
          endcase                                     
   end 
```

The Right shift operator is used for the left shift.
The left shift operator is used for the right shift.

## Design Fix
Updating the design and re-running the test makes the test pass.

![design2 debug](https://user-images.githubusercontent.com/99884583/181904485-365bd3f3-f62d-49b2-929d-b9f3f2e78361.png)

The updated design is checked in as level3_debugged.v

## Verification Strategy

Writing a testbench with variable inputs and comparing it with the desired output.

## Is the verification complete ?
 YES
