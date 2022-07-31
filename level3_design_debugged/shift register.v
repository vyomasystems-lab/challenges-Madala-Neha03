// See LICENSE.vyoma for more details
// Verilog module for Shift register


module shift_register(op,clk,rst, load,sel,ip);
  output reg [3:0] op;
  input load;
  input [1:0] sel;
  input [3:0] ip;
  input clk, rst;
  
  always @(posedge clk or rst)
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
            2'b00:  op = op<<1;                //Left Shift
            2'b01:  op = op>>1;               //Right Shift
            2'b10:  op = {op[2:0],op[3]};    //Rotate Left
            2'b11:  op = {op[0], op[3:1]};  //Rotate Right
          endcase                                     
       endcase
   
   end 
    
  endmodule
