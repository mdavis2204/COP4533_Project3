input_file = "examples/example1.in"
output_file = "examples/example1.out"

def read_inputs(read_input_file=input_file):
    with open("tests/" + read_input_file, "r") as f:
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

    # Fills in the DP Table
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

    optVal = OPT(lenA, lenB)    

    # Backtrack through DP array to get optimal subsequence
    def backtrack(i, j):
        if i == 0 or j == 0:
            return ''
        if A[i-1] == B[j-1] and dp[i][j] == values[A[i-1]] + dp[i-1][j-1]:
            return backtrack(i-1, j-1) + A[i-1]
        elif dp[i-1][j] >= dp[i][j-1]:
            return backtrack(i-1, j)
        else:
            return backtrack(i, j-1)
    
    optSubseq = backtrack(lenA, lenB)

    return optVal, optSubseq

def question1():
    times = []
    for i in range(1, 11):
        q1_file = "non_triv" + str(i) + "/" + "non_triv" + str(i) + ".in"
        num_letters, values, stringA, stringB = read_inputs(q1_file)

        from datetime import datetime

        time_before = datetime.now()
        HighestValLCS(stringA, stringB, values)
        time_after = datetime.now()

        times.append((time_after - time_before).total_seconds())

    return times;

if __name__ == '__main__':
    # print(question1())

    num_letters, values, stringA, stringB = read_inputs()
    optVal, optSubseq = HighestValLCS(stringA, stringB, values)
    print(optVal)
    print(optSubseq)
