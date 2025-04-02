import sys

# Ensure correct usage
if len(sys.argv) != 3:
    print("Usage: python script.py <template_file>")
    sys.exit(1)

template_file = sys.argv[1]
output_filename = sys.argv[2]

# Read the template from the provided file
with open(template_file, "r") as file:
    template = file.read()


template_file = sys.argv[1]

with open(output_filename, "w") as output_file:
    for i in range(31, 64):
        modified_trace = template.replace("[I]", f"{i}")
        modified_trace = modified_trace.replace("IF", "2").replace("DF", "0").replace("DW", "1")  # Convert IF, DF, DW
        output_file.write(modified_trace)  # Add spacing between traces
print(f"Generated: {output_filename}")

