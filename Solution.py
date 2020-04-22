import sys 
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import pickle


class Solution:
    
           
    def __init__(self,df_TSP,filename):
        self.filename = filename
        self.df_TSP = df_TSP
        self.n = len(self.df_TSP) # nr of cities
        root = math.sqrt(self.n)
        if (int(root + 0.5)**2 != self.n):
            print("n=" + str(self.n) + " is not a perfect square!")
            sys.exit() 
        # distance from each city to the depot
        self.dist_depot = [((self.df_TSP.iloc[i,1]- 0)**2 + (self.df_TSP.iloc[i,2]-0)**2)**0.5 for i in range(self.n)]
        # symmetric nxn matrix with distances between each city
        self.dist = [[((self.df_TSP.iloc[i,1]-self.df_TSP.iloc[j,1])**2+(self.df_TSP.iloc[i,2]-self.df_TSP.iloc[j,2])**2)**0.5 for j in range(self.n)] for i in range(self.n)]
        self.dim = int(self.n**0.5) # nr of rows and columns
        self.sol = [[ (-1) for i in range(self.dim)] for j in range(self.dim)]  # solution
           
    # This function intialises the solution using the algorithm GREEDY
    # the first column of my solution is first filled with random cities (without replacement)
    # then each row is filled with the city that is closest in location to the previous city 
    # with respect to each row (without replacement)
    def InitialSolution(self):
        print("n",self.n)
        if (self.n == 1):
            self.sol = [0]
            print("sol",self.sol)
            print(self.dist)
            print(self.dist_depot)
            return 
        cities = list(range(self.n)) # this is a list I store my cities in in order to be able to fill in 
                                # unique cities in my solution
        li = np.random.choice(self.n,self.dim, replace = False) # dim random cities to fill first column of my solution
                                                                # here li stands for list but do not want to confuse this 
                                                                # variable with function list so called it li
        for i in range(self.dim):
            cities[li[i]] = -1 # when cities are allocated to my solution
                               # set these cities equal to -1 in cities array to be able to draw without permuation
        for i in range(self.dim):
            self.sol[i][0] = li[i] # filling in first column of my solution with cities
        city0 = 0 # this will be my first city of reference from cities 
        for c in cities:
            if c >= 0:
                city0 = c
                break 
        d0 = self.dist[self.sol[0][0]][city0] # this will be the corresponding distance with respect to city0
        count = self.n - self.dim # count nr of cities left that have not been allocated to solution
        while (count != 0): # as long as there are still cities to allocate
            for i in range(self.dim): # for each column
                for j in range(self.dim-1): # for each row
                    if (count == 2): # this is to check when there are only 2 cities left to allocate
                        count = 0
                        if (self.dim > 2): # if dimension of solution is greater than 2
                            city3 = 0 # this variable stores last city 
                            dist3 = 0 # this variable stores last distance
                            for c in cities: 
                                if ((c >= 0) and (c != city0)):
                                    city3 = c      
                                    dist3 = self.dist[self.sol[self.dim-1][-3]][city3]
                                    break 
                            # compare the distances of the last 2 cities and allocate these to solution        
                            if dist3 < d0:
                                self.sol[self.dim-1][-2] = city3 
                                self.sol[self.dim-1][-1] = city0 
                            else:
                                self.sol[self.dim-1][-2] = city0 
                                self.sol[self.dim-1][-1] = city3              
                        elif (self.dim == 2): # if dimension of solution is 2x2 matrix 
                            city3 = 0
                            for c in cities: 
                                if (c>= 0 and c!= city0):
                                    city3 = c  
                                    break 
                            dist3 = self.dist[self.sol[0][0]][city3]
                            d0 = self.dist[self.sol[0][0]][city0]
                            # compare distances of last 2 cities and allocate these to solution
                            if (dist3 < d0):
                                self.sol[0][1] = city3 
                                self.sol[1][1] = city0 
                            else: 
                                self.sol[0][1] = city0 
                                self.sol[1][1] = city3  
                        # else: # if dimension of solution is 1
                            # p = 0    
                    if count > 2: # if there are more than 2 cities to allocate
                        # find smallest distance and allocate city to solution
                        for c in cities:
                            if (c >= 0): 
                                dist1 = self.dist[self.sol[i][j]][c]  
                                if dist1 < d0:
                                    city0 = c  
                                    d0 = dist1
                        cities[city0] = -1 
                        self.sol[i][j+1] = city0 
                        count = count - 1
                        for c in cities: 
                            if c >= 0:
                                city0 = c
                                d0 = self.dist[self.sol[i][j+1]][c] 
                                break 
                        if (j+1 == self.dim-1): 
                            for c in cities: 
                                if c >= 0:
                                    city0 = c
                                    d0 = self.dist[self.sol[i+1][0]][c]  
                                    break 
                        else: 
                            for c in cities: 
                                if c >= 0:
                                    city0 = c          
                                    d0 = self.dist[self.sol[i][j+1]][c]                            
        print("\nSolution initialised according to greedy algorithm")
        test = self.Test()
        if (test == True):
            print("Initial solution is unique!")    
                                      
           
    # swap operation over rows and columns
    def Swap(self,x1, y1, x2, y2): 
        temp = self.sol[x1][y1]
        self.sol[x1][y1] = self.sol[x2][y2]
        self.sol[x2][y2] = temp
    
    # insert operation over rows only
    def Insert(self,x,y1,y2): 
        # y2 will be inserted    
        # if cities are adjacent or equal    
        if (y2 == y1 or abs(y2 -y1) == 1):
            self.Swap(x,y1,x,y2)
        # if y1 is to the left of y2 
        elif y1 > y2: # elements of solution will have to be shifted left when y2 is inserted at y1
            temp = self.sol[x][y2]
            for i in range(abs(y2-y1)): 
                self.sol[x][y2+i] = self.sol[x][y2+1+i]
            self.sol[x][y1] = temp
        else: # y1 is to the right of y2 so elements in solution will have to be shifted to the right
              # when y2 is inserted at y1
            temp = self.sol[x][y2] 
            for i in range(abs(y2-y1)): 
                self.sol[x][y2-i] = self.sol[x][y2-1-i]
            self.sol[x][y1] = temp

    # reverse operation
    def Reverse(self,y1,y2,x):
        if( abs(y2 - y1) == 1 or abs(y2-y1) == 2 or abs(y2 - y1) == 0): # 1 or no elements in between y1 and y2
            # normal swap 
            self.Swap(x,y1,x,y2)
        else: 
            if (abs(y2 -y1)%2 != 0): # nr of elements between y1 and y2 is even
                for i in range(abs(y2-y1)-2):
                    if y1 < y2:
                        self.Swap(x,y1+i,x,y2-i)
                    else: 
                        self.Swap(x,y1-i,x,y2+i)
            else: # nr of elements between y1 and y2 is uneven 
                for i in range(abs(y2-y1)-3):
                    if y1 < y2:
                        self.Swap(x,y1+i,x,y2-i)
                    else:  
                        self.Swap(x,y1-i,x,y2+i) 

    # calculate cost
    def Cost(self):
        cost = 0 # total cost 
        if (self.n == 1):
            cost = self.dist_depot[0] + self.dist_depot[0]
        else:     
            TotalCost = [0 for x in range(len(self.sol[0]))] # to stor sums of distances of each column
            count = 0 # to retrieve index to store sums of costs for each row of solution
            for j in range(len(self.sol[0])): # for each row of solution
                cost = cost +self.dist_depot[self.sol[j][0]] # add distance from depot to first city
                for i in range(len(self.sol[0])-1): 
                    cost = cost + self.dist[self.sol[j][i]][self.sol[j][i+1]] # then add distances between cities
                cost = cost + self.dist_depot[self.sol[j][-1]] # distance from last city to depot
                TotalCost[count] = cost
                count = count + 1
                cost = 0
            cost = sum(TotalCost) + max(TotalCost) - min(TotalCost) 
        return cost

    # Calculate feasibility
    def Feasibility(self):
        f = 0 # feasibility
        if (self.n == 1):
            f = 1    
        else:     
            for i in range(len(self.sol)): # i = 0,1
                if (self.sol[i][0]%2 == 0):
                    f = f + 1
                if (self.sol[i][-1]%2 != 0):
                    f = f + 1             
        return f

    # Method 1: Hill Climbing method
    def HC(self):
        x = int(100000/100)
        X = list(range(1,(x+1)))   
        Y = [0 for i in range(x)] 
        count = 0
        cost = self.Cost()
        if (self.n == 1):
            test = True
            Y = [cost for i in range(x)]
        else:     
            x = int(100000/100)
            X = list(range(1,(x+1)))   
            Y = [0 for i in range(x)] 
            count = 0
            cost = self.Cost()
            for i in range(100000):
                x1 = np.random.randint(0,self.dim)
                y1 = np.random.randint(0,self.dim)
                x2 = np.random.randint(0,self.dim)
                y2 = np.random.randint(0,self.dim)
                self.Swap(x1, y1, x2, y2)
                new_cost = self.Cost()
                if new_cost <= cost:
                    cost = new_cost
                else:
                    self.Swap(x2, y2, x1, y1)
                if ((i+1)%100 == 0):
                    Y[count] =cost
                    count = count + 1
            test = self.Test() 
        print("\n HILL CLIMBING METHOD: ")
        print("Is solution correct: ",test)
        print("Cost: ",cost)
        f = self.Feasibility()
        print("Feasibility: ",f)
        answer1 = self.Write()
        if (answer1 == 1): 
            self.WriteToFile(cost,f)
        elif (answer1 == 2):    
            self.WB_to_file(cost,f)
        elif (answer1 == 3): 
            self.WriteToFile(cost,f) 
            self.WB_to_file(cost,f)      
        answer2 = self.GraphSol()
        if (answer2 == 1):
            self.Graph_Fig1(" hill climbing method") 
        if (answer2 == 2):
            self.Graph_Fig2(X,Y," hill climbing method") 
        if (answer2 == 3): 
            self.Graph_Fig1(" hill climbing method")
            self.Graph_Fig2(X,Y," hill climbing method")         
        return cost, self.sol,test

    # User input/output for graphing solution
    def GraphSol(self):
        print("\nWould you like see graphs of solution ? ")
        print("Input <0>: NO")
        print("Input <1>: Fig (1): Visual representation of solution")
        print("Input <2>: Fig (2): Iterations vs Cost line graph")
        print("Input <3>: Fig (1) and Fig (2) ")
        try: 
            answer = input("INPUT: ") 
            answer = int(answer)
        except ValueError:
            print("Wrong input given!")
            exit()    
        return answer

    # User input/output for writing solution to csv/bs files
    def Write(self):
        print("\nWould you like to save solution? ")
        print("Input <0>: No saving of file")
        print("Input <1>: Save file as csv file")
        print("Input <2>: Save file as binary file")
        print("Input <3>: Save both binary and csv file")
        try: 
            answer = input("INPUT: ") 
            answer = int(answer)
        except ValueError:
            print("Wrong input given!")
            sys.exit()    
        return answer
           

    # Method 2: HC by using swap, insert and revert operations at random
    def HC_Swap_Insert_Reverse(self): 
        x = int(100000/100)
        X = list(range(1,(x+1)))   
        Y = [0 for i in range(x)] 
        count = 0
        cost = self.Cost()
        if (self.n == 1):
            test = True
            Y = [cost for i in range(x)]
        else:     
            for i in range(100000):
                operation = np.random.randint(0,4)
                # 1: swap 
                # 2: insert 
                # 3: reverse
                x1 = np.random.randint(0,self.dim)
                y1 = np.random.randint(0,self.dim)
                x2 = np.random.randint(0,self.dim)
                y2 = np.random.randint(0,self.dim)
                x = np.random.randint(0,self.dim)
                if (operation == 1):
                    self.Swap(x1, y1, x2, y2)
                elif (operation == 2):
                    self.Insert(x,y1,y2)
                else: 
                    self.Reverse(y1,y2,x)        
                new_cost = self.Cost()
                if new_cost <= cost:
                    cost = new_cost
                else:
                    if (operation == 1):
                        self.Swap(x2, y2, x1, y1)
                    elif (operation == 2):
                        self.Reverse(y2,y1,x)
                    else: 
                        self.Insert(x,y2,y1) 
                if ((i+1)%100 == 0):
                    Y[count] =cost
                    count = count + 1    
            test = self.Test()
        print("\n HILL CLIMBING METHOD USING SWAP INSERT REVERT ")
        print("Is solution correct: ",test)
        print("Cost: ",cost)
        f = self.Feasibility()
        print("Feasibility: ",f)
        answer1 = self.Write()
        if (answer1 == 1): 
            self.WriteToFile(cost,f)
        elif (answer1 == 2):    
            self.WB_to_file(cost,f)
        elif (answer1 == 3): 
            self.WriteToFile(cost,f) 
            self.WB_to_file(cost,f)      
        answer2 = self.GraphSol()
        if (answer2 == 1):
            self.Graph_Fig1(" hill climbing with swap insert revert") 
        if (answer2 == 2):
            self.Graph_Fig2(X,Y," hill climbing with swap insert revert") 
        if (answer2 == 3): 
            self.Graph_Fig1(" hill climbing with swap insert revert")
            self.Graph_Fig2(X,Y," hill climbing with swap insert revert")         
        return cost,self.sol,test    

    # Method 3: HC by implementing simulated annealing
    def SimulatedAnnealing(self):
        X = list(0 for i in range(1037))   
        for i in range(1037):
            X[i] = (i*2002 + 1)
        Y = [0 for i in range(1037)] # cost
        T0 = 10000
        coolingRate = 0.99999
        index = 0 # index to insert cost in Y 
        value = 0 # variable to help store cost at index t
        NrIter = 0 # nr of iterations 
        absoluteTemp = 0.00001
        cost0 = self.Cost() # initial cost
        if (self.n == 1):
            test = True
            Y = [cost0 for i in range(1037)]
        else:     
            while (T0 > absoluteTemp):
                # count = count + 1
                x1 = np.random.randint(0,self.dim)
                y1 = np.random.randint(0,self.dim)
                x2 = np.random.randint(0,self.dim)
                y2 = np.random.randint(0,self.dim)
                self.Swap(x1, y1, x2, y2)
                cost1 = self.Cost() # new cost
                if cost1 < cost0:
                    cost0 = cost1 #accept new solution
                else: 
                    q = np.random.randint(0,2)
                    if q < math.exp(-(cost1-cost0)/T0): # accept solution if relation holds
                        cost0 = cost1  
                    else:
                        self.Swap(x2,y2,x1,y1) 
                T0  = T0*coolingRate  # cool temperature
                if (NrIter == value):
                    value = value + 2001 
                    Y[index] = cost0
                    index = index + 1
                NrIter = NrIter + 1    
            test = self.Test() 
        X[-1] = NrIter
        Y[-1] = cost0
        print("\n HILL CLIMBING METHOD USING SIMULATED ANNEALING ")
        print("Is solution correct ",test)
        print("Cost: ",cost0)
        f = self.Feasibility()
        print("Feasibility: ",f)
        answer1 = self.Write()
        if (answer1 == 1): 
            self.WriteToFile(cost0,f)
        elif (answer1 == 2):    
            self.WB_to_file(cost0,f)
        elif (answer1 == 3): 
            self.WriteToFile(cost0,f) 
            self.WB_to_file(cost0,f)      
        answer2 = self.GraphSol()
        if (answer2 == 1):
            self.Graph_Fig1( " simulated annealing") 
        if (answer2 == 2):
            self.Graph_Fig2(X,Y," simulated annealing") 
        if (answer2 == 3): 
            self.Graph_Fig1(" simulated annealing")
            self.Graph_Fig2(X,Y," simulated annealing")   
        return cost0,self.sol,test 

    # To test whether the solution has unique elements
    def Test(self):
        test = True 
        cities = list(range(self.n))
        count = [0 for i in range(self.n)]
        for i in range(self.dim):
            for j in range(self.dim):
                for c in cities:
                    if c == self.sol[i][j]:
                        count[c] = count[c] + 1
                    if count[c] > 1: 
                        test = False
        return test
    
    # Fig 2: Iterations Vs Cost line-graph 
    def Graph_Fig2(self,X,Y,title):
        fig2 = plt.figure()
        plt.grid(b = "True",axis = "both",color="lightgrey",linestyle = "-", linewidth = 0.5)
        plt.plot(X,Y,linestyle="-",linewidth = 1)
        plt.title("Iterations Vs Cost line-graph for" + title)
        plt.xlabel("Nr of iterations")
        plt.ylabel("Cost") 
        print("\nFig (2): Iterations Vs Cost line-graph for" + title)
        filename = input("Save file as: <filename.pdf> ")
        plt.savefig(filename)

    # Fig 1: Visual representation of solution
    def Graph_Fig1(self,title):   
        fig1 = plt.figure()
        colors = []
        for i in range(self.dim):
            colors.append('#%06X' % np.random.randint(0, 0xFFFFFF))
        x = [[0 for i in range(self.dim + 2)] for j in range(self.dim)]
        y = [[0 for i in range(self.dim + 2)] for j in range(self.dim)]
        if (self.n == 1):
            x[0][1] = self.df_TSP.iloc[self.sol[0],1] 
            y[0][1] = self.df_TSP.iloc[self.sol[0],2]   
        else:              
            for i in range(self.dim):
                for j in range(self.dim):    
                    x[i][j+1] = self.df_TSP.iloc[self.sol[i][j],1]
                    y[i][j+1] = self.df_TSP.iloc[self.sol[i][j],2] 
        plt.grid(b = "True",axis = "both",color="lightgrey",linestyle = "-", linewidth = 0.5)
        plt.axhline(y=0,color = "grey", linewidth = 1)
        plt.axvline(x = 0, color = "grey", linewidth = 1)
        trucks = ["" for i in range(self.dim)]
        for i in range(self.dim):
            trucks[i] = "Truck " + str(i+1)
        for i in range(self.dim):    
            plt.plot(x[i][:],y[i][:], linestyle ="-", marker = "o", color = colors[i], linewidth = 1,label = trucks[i])        
        plt.legend(loc = "upper left")
        plt.title("Visual representation of solution for" + title)
        print("\nFig (1): Visual representation of solution" + title)
        filename = input("Save file as: <filename.pdf> ")
        plt.savefig(filename)
        
        
    # write to csv file 
    def WriteToFile(self,cost,f):
        filename = input("\nSave file as < filename.csv >")
        with open(filename,'w') as writeFile:
            if (self.n == 1):
                writeFile.write(str(0) + "\n")
            else: 
                for i in range(self.dim):
                    writeFile.write(','.join(str(s) for s in self.sol[i]))
                    writeFile.write("\n")         
            writeFile.write(str(cost) +"\n" + str(f))  

    # write to binary file
    def WB_to_file(self,cost,f):
        filename = input("\nSave file as <filename.bs> ")
        found = False
        try :
            file = open(filename,"rb")
            prev_run = pickle.load(file)
            found = True
        except FileNotFoundError :
            print("New file with name " + filename + " is created!")
        file = open(filename,"wb")
        if (found == True):
            pickle.dump(prev_run,file)
        pickle.dump(self.sol,file)
        pickle.dump(f,file)
        pickle.dump(cost,file)
        file.close()
      


        