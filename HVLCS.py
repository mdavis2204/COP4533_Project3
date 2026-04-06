input_file = "example_input1.in"
output_file = "example_output1.out"

def read_inputs():
    with open("inputs/" + input_file, "r") as f:
        num_letters = int(f.readline())

        for i in range(num_letters):
            print(f.readline())



if __name__ == '__main__':
    read_inputs()

