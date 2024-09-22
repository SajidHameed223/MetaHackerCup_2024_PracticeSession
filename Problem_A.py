def solve():
    T = int(input())  # number of test cases
    for t in range(1, T + 1):
        # Read the values of N and K
        N, K = map(int, input().split())
        S = [int(input()) for _ in range(N)]
        
        # Sorting the times for optimal crossings
        S.sort()

        # Simulate the crossing strategy and calculate the total time
        total_time = 0
        if len(S) > 2:
            total_time = 2*(S[0]*(len(S)-2)) + S[0]
        else:
            total_time = S[0]
            

        # Print the result for this test case
        if total_time <= K:
            print(f"Case #{t}: YES")
        else:
            print(f"Case #{t}: NO")

# Example usage
solve()