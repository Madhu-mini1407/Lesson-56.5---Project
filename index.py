def prints(n):
    if (n <= 1):
        return
    print("Codingal", end="\r")
    prints(n/2)
    prints(n/2)

def myfunction(n):
    print(f"--- Complexity Analysis for n = {n} ---")

    # 1. Linear Loop
    for i in range(0, n + 1):
        x = i

    # 2. Logarithmic Loop
    j = 1
    while j <= n + 1:
        j = j * 2

    # 3. Constant Loop
    for i in range(0, 100):
        y = i

    # 4. Recursive Part 
    print("Executing Recursive Calls...")
    prints(n)

    print("\nExecution Finished.")

myfunction(10)
print("="*30)
myfunction(100)