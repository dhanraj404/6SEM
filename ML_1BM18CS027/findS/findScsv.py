
import csv

def findS(dataset, hypothesis):
   for i in range(len(dataset)):
      if dataset[i][-1] == 'yes':
         print('The tuple', i+1, 'is a positive instance.')
         for j in range(len(hypothesis)):
            if hypothesis[j] == '0'  or dataset[i][j] == hypothesis[j]:
               hypothesis[j] = dataset[i][j]
            else:
               hypothesis[j] = '?'
            print('The hypothesis for traning tuple',i+1,'and instance',j+1, 'is:', hypothesis)
      elif dataset[i][-1] == 'no':
         print('The tuple', i+1, 'is a negative instance.')
         print('The hypothesis for traning tuple',i+1, 'is:', hypothesis)
   return hypothesis



def main():

    dataset = []
    with open('enojysport.csv', 'r') as csvfile:
        next(csvfile)
        for row in csv.reader(csvfile):
            dataset.append(row)
        print(dataset)
    hypothesis = ['0']*len(dataset[0])
    print('The Initial hypothesis:', hypothesis)
    hypothesis = findS(dataset, hypothesis)
    print('Final Hypothesis: ', hypothesis)

if __name__ == "__main__":
   main()



'''
OUTPUT:

bmsce@bmsce-Precision-T1700:~/1bm18cs027/6SEM/ML_1BM18CS027$ python3 findScsv.py
[['sunny', 'warm', 'normal', 'strong', 'warm', 'same', 'yes'], ['sunny', 'warm', 'high', 'strong', 'warm', 'same', 'yes'], ['rainy', 'cold', 'high', 'strong', 'warm', 'change', 'no'], ['sunny', 'warm', 'high', 'strong', 'cool', 'change', 'yes']]
The Initial hypothesis: ['0', '0', '0', '0', '0', '0', '0']
The tuple 1 is a positive instance.
The hypothesis for traning tuple 1 and instance 1 is: ['sunny', '0', '0', '0', '0', '0', '0']
The hypothesis for traning tuple 1 and instance 2 is: ['sunny', 'warm', '0', '0', '0', '0', '0']
The hypothesis for traning tuple 1 and instance 3 is: ['sunny', 'warm', 'normal', '0', '0', '0', '0']
The hypothesis for traning tuple 1 and instance 4 is: ['sunny', 'warm', 'normal', 'strong', '0', '0', '0']
The hypothesis for traning tuple 1 and instance 5 is: ['sunny', 'warm', 'normal', 'strong', 'warm', '0', '0']
The hypothesis for traning tuple 1 and instance 6 is: ['sunny', 'warm', 'normal', 'strong', 'warm', 'same', '0']
The hypothesis for traning tuple 1 and instance 7 is: ['sunny', 'warm', 'normal', 'strong', 'warm', 'same', 'yes']
The tuple 2 is a positive instance.
The hypothesis for traning tuple 2 and instance 1 is: ['sunny', 'warm', 'normal', 'strong', 'warm', 'same', 'yes']
The hypothesis for traning tuple 2 and instance 2 is: ['sunny', 'warm', 'normal', 'strong', 'warm', 'same', 'yes']
The hypothesis for traning tuple 2 and instance 3 is: ['sunny', 'warm', '?', 'strong', 'warm', 'same', 'yes']
The hypothesis for traning tuple 2 and instance 4 is: ['sunny', 'warm', '?', 'strong', 'warm', 'same', 'yes']
The hypothesis for traning tuple 2 and instance 5 is: ['sunny', 'warm', '?', 'strong', 'warm', 'same', 'yes']
The hypothesis for traning tuple 2 and instance 6 is: ['sunny', 'warm', '?', 'strong', 'warm', 'same', 'yes']
The hypothesis for traning tuple 2 and instance 7 is: ['sunny', 'warm', '?', 'strong', 'warm', 'same', 'yes']
The tuple 3 is a negative instance.
The hypothesis for traning tuple 3 is: ['sunny', 'warm', '?', 'strong', 'warm', 'same', 'yes']
The tuple 4 is a positive instance.
The hypothesis for traning tuple 4 and instance 1 is: ['sunny', 'warm', '?', 'strong', 'warm', 'same', 'yes']
The hypothesis for traning tuple 4 and instance 2 is: ['sunny', 'warm', '?', 'strong', 'warm', 'same', 'yes']
The hypothesis for traning tuple 4 and instance 3 is: ['sunny', 'warm', '?', 'strong', 'warm', 'same', 'yes']
The hypothesis for traning tuple 4 and instance 4 is: ['sunny', 'warm', '?', 'strong', 'warm', 'same', 'yes']
The hypothesis for traning tuple 4 and instance 5 is: ['sunny', 'warm', '?', 'strong', '?', 'same', 'yes']
The hypothesis for traning tuple 4 and instance 6 is: ['sunny', 'warm', '?', 'strong', '?', '?', 'yes']
The hypothesis for traning tuple 4 and instance 7 is: ['sunny', 'warm', '?', 'strong', '?', '?', 'yes']
Final Hypothesis:  ['sunny', 'warm', '?', 'strong', '?', '?', 'yes']
bmsce@bmsce-Precision-T1700:~/1bm18cs027/6SEM/ML_1BM18CS027$ ^C
bmsce@bmsce-Precision-T1700:~/1bm18cs027/6SEM/ML_1BM18CS027$ 

'''