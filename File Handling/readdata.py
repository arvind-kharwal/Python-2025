import pickle
with open('db.dat','rb') as f:
    text = pickle.load(f)
    print(text)