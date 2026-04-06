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
        stringA = f.readline().strip()
        stringB = f.readline().strip()

        return num_letters, values, stringA, stringB

def HighestValLCS(A, B, values):
    lenA = len(A)
    lenB = len(B)

    dp = [[None]*(lenB+1) for _ in range(lenA+1)]

    def OPT(i, j):
        if i == 0 or j == 0:
            return 0
        if dp[i][j] is not None:
            return dp[i][j]
        # Use i-1 j-1 when accessing string because they are 0 indexed 
        # (our DP array is 1-indexed, dp[0] is a stand in for empty string)
        if A[i-1] != B[j-1]:
            dp[i][j] = max(OPT(i-1, j), OPT(i, j-1))
        elif A[i-1] == B[j-1]:
            dp[i][j] = max(OPT(i-1, j), OPT(i, j-1), values[A[i-1]] + OPT(i-1, j-1))
        return dp[i][j]

    return OPT(lenA, lenB)    

if __name__ == '__main__':
    num_letters, values, stringA, stringB = read_inputs()
    print(num_letters, values, stringA, stringB)
