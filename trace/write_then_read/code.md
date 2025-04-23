# ALGORITHM DESCRIPTION
Write sequence on a unknown array of size N. With a given factor, the sequence is a arithmetic progression 
Then read all elements of the array from left to right:
- Obtain current sum that starts at 0 and adds to each element read
- The current sum overwrites the array element, describing a new sequence of partial sum to the array

Jump function calls are called on each loop to further strain memory





# DESCRIPTION OF FILE FORMATTING

## Words
[N] is where the size will be stored (0)
[I] is adress of array (1-32)


## Data
The original data defintions sections is divided by <DATA></DATA>


## Code
The original code sections are divided by <CODE></CODE>


## Memory instructions
Memory instructions converted from the code are inside <INST></INSTR>

Loops defined with beq for all elements of the array are marked by <arr-loop></arr-loop>
loops are also repeated by the converter, and [I] is used to iterate the adresses 

Additional jal function jumps on <INST></INST> are separated by <jal-LABEL></jal-LABEL>
where LABEL is the name of the label
  

## Memory adress:
Instructions and Data is already mapped by the simulator
Therefore instructions start at 0 and data also starts at 0


## Python converter template
Manual conversion is required for a less readable file used by the python converter 
where only a few simple indicators are used
(If needed, it would not be difficult to implement direct conversion later, but its
not the focus of this project)

The file organization goes as follows:
- [N] can be used anywhere to signal the extraction of "n" word adress
- "loop:" is used to initiate the array loop, and must end with linebreak
- "endloop" is used to end a array loop and must end with linebreak
- Inside the loops [I] are used to extract following array indexes
 
 


<DATA>
  .data
  n:      .word 0   
  array:  .word 1:N #Any array size


  .text
  .globl main
</DATA>


<CODE>
  # READ ALL ELEMENTS AND GET SUM
  ## For each adress also write current sum to include a write operation right after read

  
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
    # NO INSTRUCTIONS - FORCED END

<CODE>



<MEM>
  IF 0
  IF 1
  IF 2
  IF 3
  DF [N]
  <arr-loop>
    IF 4
    IF 5
    DW [I] 
    IF 6
    IF 7
    <jal-print>
      IF 23
      IF 24
      IF 25
      IF 26
      IF 27
    </jal-print>
    IF 8 
    IF 9
    IF 10
  </arr-loop>
  IF 11
  IF 12
  IF 13
  DF [N]
  <arr-loop>
    IF 14
    DF [I] 
    IF 15
    IF 16
    DW [I] 
    IF 17
    <jal-print>
      IF 23
      IF 24
      IF 25
      IF 26
      IF 27
    </jal-print>
    IF 19 
    IF 20
    IF 21
  </arr-loop>
  IF 22
  IF 28

</MEM>


