import sys
import io  # Import StringIO

# Ensure correct usage
if len(sys.argv) != 3:
    print("Usage: python script.py <template_file> <output_file>")
    sys.exit(1)

template_file = sys.argv[1]
output_filename = sys.argv[2]

# Read the template from the provided file
with open(template_file, "r") as file:
    lines = file.readlines()

i = 0
n = 32

with open(output_filename, "w") as output_file:
    while i < len(lines):
        if lines[i].strip() == "loop:":
            i += 1
            loop_builder = io.StringIO()

            while i < len(lines) and lines[i].strip() != "endloop":
                loop_builder.write(lines[i])
                i += 1

            if i < len(lines) and lines[i] == "endloop":
                i += 1  # Move past "endloop"

            loop = loop_builder.getvalue()
            for j in range(0, n):
                modified_trace = loop.replace("[I]", f"{j}").replace("IF", "2").replace("DF", "0").replace("DW", "1") 
                output_file.write(modified_trace)  # Add spacing between traces


        elif lines[i].strip() != "": 
            modified_trace = lines[i].replace("[N]", f"{n}").replace("IF", "2").replace("DF", "0").replace("DW", "1")  # Convert IF, DF, DW
            output_file.write(modified_trace)  # Add spacing between traces
        
        i += 1
        
print(f"Generated: {output_filename}")



