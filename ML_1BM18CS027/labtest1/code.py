#Consider the following dataset. How do you use the Candidate Elimination algorithm when the first example is negative?
#Implement the algorithm for the same.

from os import sep
import numpy as np 
import pandas as pd


#algo
def candidate_elimination(concepts, target):
    specific_h = concepts[1].copy()  
    general_h = [["?" for i in range(len(specific_h))] for i in range(len(specific_h))]        
    print("Initialization of Specific hypotheses and General hypotheses")     
    print("Specific hypotheses \n", specific_h)  
    print("General hypotheses \n", general_h)  
    print("\nCandidate Elimination Algorithm: \n")
    for i, h in enumerate(concepts):
        if target[i] == "yes":
            print("If instance is Positive ", end="")
            for x in range(len(specific_h)): 
                if h[x]!= specific_h[x]:                    
                    specific_h[x] ='?'                     
                    general_h[x][x] ='?'                   
        if target[i] == "no":            
            print("If instance is Negative ", end="")
            for x in range(len(specific_h)): 
                if h[x]!= specific_h[x]:                    
                    general_h[x][x] = specific_h[x]                
                else:                    
                    general_h[x][x] = '?'        
        print("steps of Candidate Elimination Algorithm(Step {})".format(i+1))        
        print("Specific hypotheses \n", specific_h)  
        print("General hypotheses \n", general_h)
        print("\n")

    indices = [i for i, val in enumerate(general_h) if val == ['?', '?', '?', '?', '?']]    
    for i in indices:   
        general_h.remove(['?', '?', '?', '?', '?']) 
    return specific_h, general_h 

#take input
def main():
    data = pd.read_csv('/home/dhanrz/Old Folder/6SEM/ML_1BM18CS027/labtest1/buys.csv')
    print("Data from Given csv File: ")
    concepts = np.array(data.iloc[:,0:-1])
    print('Concepts:',*concepts, sep='\n')
    target = np.array(data.iloc[:,-1])  
    print("Target \n",target,"\n\n")
    finalS, finalG = candidate_elimination(concepts, target)
    print("Final specific_h:", finalG, sep="\n")
    print("Final general_h:", finalG, sep="\n")

main()
