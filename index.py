def print_recurrence_relations():
    print("Function: myfunction1(n)")
    print("T(n) = T(n/2) + T(n/3) + n")
    print("Time Complexity: O(n)")
    
    print("-" * 30)
    
    print("Function: myfunction2(n)")
    print("T(n) = T(n-1) + 1")
    print("Time Complexity: O(n)")

if __name__ == "__main__":
    print_recurrence_relations()