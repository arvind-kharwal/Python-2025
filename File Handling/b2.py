import pickle
with open('data.dat','rb') as f:
    d = pickle.load(f)
    print(d)