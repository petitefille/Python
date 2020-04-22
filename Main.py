import sys 
import pandas as pd
import Solution
from Solution import Solution

import numpy as np
import math
import matplotlib.pyplot as plt

 


def read_file():
    try: 
        print("\n * * * * * * * TSP Program * * * * * * * ")
        print("\nPlease input name of file containing city locations ")
        filename = input("Format: <filename.csv> ")
        df_TSP =pd.read_csv(filename)
        print("File with name " + filename + " found!")
    except FileNotFoundError :
        print("The file with name " + filename + " does not exist!")
        sys.exit()
    return df_TSP,filename 


df_TSP,filename = read_file() # to see comparison of optimisation methods I have used I2.csv

Solution1 = Solution(df_TSP,filename)
Solution1.InitialSolution()
cost = Solution1.Cost()
cost1, sol1,test1 = Solution1.HC() # Method 1
Solution2 = Solution(df_TSP,filename) 
Solution2.InitialSolution()
cost2, sol2,test2 = Solution2.HC_Swap_Insert_Reverse() # Method 2
# simulated annealing method yields the lowest cost 
# but takes a lot of computation time 
Solution3 = Solution(df_TSP,filename)
Solution3.InitialSolution()
cost3, sol3,test3 = Solution3.SimulatedAnnealing() # Method 3



# CONCLUSION:

# Method 2 (Hill Climbing method with swap/insert/revert at random ) gives worse solution because
# it cannot produce a better solution than my initial solution obtained using GREEDY algorithm
# Method 1 (Hill Climbing method) obtains 2nd best solution but it is more efficient optimising solution
# Method 3 (Simulated Annealing) obtains the lowest final cost but uses a lot of time optimising the solution.
# These conclusions are also illustrated in the different figures and csv file produced with the respect
# to applied method (1,2 or 3).






