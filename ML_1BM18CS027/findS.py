
def findS(dataset, hypothesis, n, a):
   for i in range(len(dataset)):
      if dataset[i][-1] == 'yes':
         print('The tuple', i+1, 'is a positive instance.')
         for j in range(n):
            if hypothesis[j] == '0'  or dataset[i][j] == hypothesis[j]:
               hypothesis[j] = dataset[i][j]
            else:
               hypothesis[j] = '?'
            print('The hypothesis for traning tuple',i+1,'and instance',j+1, 'is:', hypothesis)
      elif dataset[i][-1] == 'no':
         print('The tuple', i+1, 'is a negative instance.')
         print('The hypothesis for traning tuple',i+1,'and instance',j+1, 'is:', hypothesis)
   return hypothesis



def main():
   n = int(input('Enter total no of attributes:'))
   a = int(input('Enter total no of training tuple:'))
   hypothesis = ['0']*n
   print('The Initial hypothesis:', hypothesis)
   dataset = []
   print('Enter {} training tuple:'.format(a))   
   for i in range(a):
      l = list(map(str, input().split()))
      dataset.append(l)
   hypothesis = findS(dataset, hypothesis, n, a)
   print('Final Hypothesis: ', hypothesis)

if __name__ == "__main__":
   main()



'''
OUTPUT:

bmsce@bmsce-Precision-T1700:~/1bm18cs027/ML$ python3 findS.py
Enter total no of attributes:6
Enter total no of training tuple:4
The Initial hypothesis: ['0', '0', '0', '0', '0', '0']
Enter 4 training tuple:
sunny   warm    normal  strong  warm    same    yes
sunny   warm    high    strong  warm    same    yes
rainy   cold    high    strong  warm    change  no
sunny   warm    high    strong  cool    change  yes
The instance 1 is a positive instance.
The hypothesis for traning tuple 1 and instance 1 is: ['sunny', '0', '0', '0', '0', '0']
The hypothesis for traning tuple 1 and instance 2 is: ['sunny', 'warm', '0', '0', '0', '0']
The hypothesis for traning tuple 1 and instance 3 is: ['sunny', 'warm', 'normal', '0', '0', '0']
The hypothesis for traning tuple 1 and instance 4 is: ['sunny', 'warm', 'normal', 'strong', '0', '0']
The hypothesis for traning tuple 1 and instance 5 is: ['sunny', 'warm', 'normal', 'strong', 'warm', '0']
The hypothesis for traning tuple 1 and instance 6 is: ['sunny', 'warm', 'normal', 'strong', 'warm', 'same']
The instance 2 is a positive instance.
The hypothesis for traning tuple 2 and instance 1 is: ['sunny', 'warm', 'normal', 'strong', 'warm', 'same']
The hypothesis for traning tuple 2 and instance 2 is: ['sunny', 'warm', 'normal', 'strong', 'warm', 'same']
The hypothesis for traning tuple 2 and instance 3 is: ['sunny', 'warm', '?', 'strong', 'warm', 'same']
The hypothesis for traning tuple 2 and instance 4 is: ['sunny', 'warm', '?', 'strong', 'warm', 'same']
The hypothesis for traning tuple 2 and instance 5 is: ['sunny', 'warm', '?', 'strong', 'warm', 'same']
The hypothesis for traning tuple 2 and instance 6 is: ['sunny', 'warm', '?', 'strong', 'warm', 'same']
The instance 3 is a negative instance.
The hypothesis for traning tuple 3 and instance 6 is: ['sunny', 'warm', '?', 'strong', 'warm', 'same']
The instance 4 is a positive instance.
The hypothesis for traning tuple 4 and instance 1 is: ['sunny', 'warm', '?', 'strong', 'warm', 'same']
The hypothesis for traning tuple 4 and instance 2 is: ['sunny', 'warm', '?', 'strong', 'warm', 'same']
The hypothesis for traning tuple 4 and instance 3 is: ['sunny', 'warm', '?', 'strong', 'warm', 'same']
The hypothesis for traning tuple 4 and instance 4 is: ['sunny', 'warm', '?', 'strong', 'warm', 'same']
The hypothesis for traning tuple 4 and instance 5 is: ['sunny', 'warm', '?', 'strong', '?', 'same']
The hypothesis for traning tuple 4 and instance 6 is: ['sunny', 'warm', '?', 'strong', '?', '?']
Final Hypothesis:  ['sunny', 'warm', '?', 'strong', '?', '?']
bmsce@bmsce-Precision-T1700:~/1bm18cs027/ML$ 

'''
