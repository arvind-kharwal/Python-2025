import pickle
with open('data.dat','wb') as f:
    l = ['Python',10,3.5]
    pickle.dump(l,f)