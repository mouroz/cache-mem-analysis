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
 