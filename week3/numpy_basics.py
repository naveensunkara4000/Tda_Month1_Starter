import numpy as np

def main():
    a = np.array([1,2,3])
    b = np.array([10,20,30])
    print("a:", a)
    print("b:", b)
    print("a + b:", a + b)  # element-wise
    print("a * 2:", a * 2)  # broadcasting
    M = np.arange(1,10).reshape(3,3)
    print("Matrix M:\n", M)
    print("M.T (transpose):\n", M.T)
    print("Mean of M:", M.mean())

if __name__ == "__main__":
    main()