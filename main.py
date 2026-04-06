input_file = "example_input1.in"
output_file = "example_output1.out"

def read_inputs():
    with open("inputs/" + input_file, "r") as f:
        # Read the first line to get the number of letters
        num_letters = int(f.readline())

        # Read the next few lines to get the values of the letters
        values = {}
        for i in range(num_letters):
            # Split the line into the letter and value
            letter, value = f.readline().split()
            values[letter] = int(value)

        # Read the next 2 lines to get the strings
        string1 = f.readline().strip()
        string2 = f.readline().strip()

        return num_letters, values, string1, string2

if __name__ == '__main__':
    num_letters, values, string1, string2 = read_inputs()
    print(num_letters, values, string1, string2)
