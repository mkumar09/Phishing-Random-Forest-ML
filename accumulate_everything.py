import csv
import numpy as np

class Data:
    def __init__(self):
        with open(r"C:\Users\Megha Agrawal\Desktop\project\codes\attributes\all_features\easy_ham.csv","r") as f:
            reader = csv.reader(f)

            data2 = np.array(list(reader))
            data2=data2.astype(np.float)

            with open(r"C:\Users\Megha Agrawal\Desktop\project\codes\attributes\all_features\easy_ham_2.csv","r") as f:
                reader = csv.reader(f)

                data1 = np.array(list(reader))
                data1=data1.astype(np.float)

            self.data = np.concatenate((data2,data1),axis=0)

            with open(r"C:\Users\Megha Agrawal\Desktop\project\codes\attributes\all_features\hard_ham.csv","r") as f:
                reader = csv.reader(f)

                data1 = np.array(list(reader))
                data1=data1.astype(np.float)

            self.data = np.concatenate((self.data,data1),axis=0)

            with open(r"C:\Users\Megha Agrawal\Desktop\project\codes\attributes\all_features\spam.csv","r") as f:
                reader = csv.reader(f)

                data1 = np.array(list(reader))
                data1=data1.astype(np.float)

            self.data = np.concatenate((self.data,data1),axis=0)

            with open(r"C:\Users\Megha Agrawal\Desktop\project\codes\attributes\all_features\spam_2.csv","r") as f:
                reader = csv.reader(f)

                data1 = np.array(list(reader))
                data1=data1.astype(np.float)

            self.data = np.concatenate((self.data,data1),axis=0)
