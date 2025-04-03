# DESCRIPTION
Simulation of instruction fetch for a simple assembly line program that adds an already present array to memory


# TODO
Writes after reads
Read after write 
Random array access


.data
array:  .word 0:32
n:      .word 32

.text
.globl main

# WRITE TO ALL ELEMENTS OF ARRAYS IN FACTORS OF 2 ([0,2,4,6,8,...])
main:
  addi t0, t0, 0 # Current sum
  addi t1, t1, 2 # Base factor
  la t2, array # Array Address
  lw t3, n # Array Size

loopWrite:
  addi t0, t0, t1
  sw t0, 0(t2)
  
  add a0, t0, $zero
  jal print_register
  
  addi t2, t2, 4
  add t3, t3, -1
  bne t3, $zero, loopWrite

# READ ALL ELEMENTS AND GET SUM
## For each adress also write current sum to include a write operation right after read
redefineVariables:
  addi t0, t0, 0 # Total sum
  la t1, word # Address
  lw t2, n # Size

loopRead:
  lw t3, 0(a1)
  add t0, t0, t3
  
  sw t0, 0(t1) # WRITE AFTER MODIFY
  
  add a0, t0, $zero
  jal print_register

  addi t1, t1, 4
  add t2, t2, -1
  bne t2, $zero, loopRead


#Jump to end
  j .end


print_register:
  li a7, a0          
  ecall             # Custom system call for printing

  li a7, 11         # Print newline character            
  ecall

  ret               # Return to caller

end:

END ASSEMBLY

