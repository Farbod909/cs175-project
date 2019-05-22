import numpy as np
import random
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.autograd import Variable

seed = 42
np.random.seed(seed)
#torch.manual_seed(seed)

classes = ("dirt", "wheat", "carrot", "potato", "beetroot")

#from torch.autograd import Variable
#import torch.nn.functional as F

#from the pytorch tutorial, it seems as that if we want to do a greedy approach to a problem, we let the neural network run throught the environment and save all the reward it gets for every action. Since the network will act random at first, it will help  us get a good pool of samples. Then we use those samples and train our network on it. For example, we'll give it some random state s and the label will be the r_j

class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.replay = []
        self.conv1 = nn.Conv2d(9,6, kernel_size = 2)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.fc1 = nn.Linear(50, 120)
        self.fc2 = nn.Linear(120,5)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.fc1(x)
        x = self.fc1(x)
        return F.log_softmax(x)

    def conv2d_size_out(size, kernel_size = 2, stride = 1):
        return (size - (kernel_size - 1) - 1) // stride  + 1

    def add_experience(self,exp):
        if len(self.replay) < 200:
            self.replay.append(exp)
        else:
            self.replay.pop(0)
            self.replay.append(exp)

    def print_replay(self):
        for tup in self.replay:
            print(tup)

    def train(self):
        print("replay len: ", len(self.replay))
        batch = random.sample(self.replay, 5)
        for exp in batch:
            s = torch.Tensor(np.array(exp[0]).astype(int))
            print("s: ", s)
            action = exp[1]
            reward = exp[2]
            s_prime = torch.Tensor(np.array(exp[3]).astype(int))

            self.forward(s)



        


def grab_farm(farm):
    farm = ["dirt"] * (farm**2)
    print("cnn farm: ", farm)
    print(translate_farm(farm))

def translate_farm(farm):
    cell_to_id = {"dirt":1, "wheat":2, "carrots":3, "potatoes":4, "beetroots":5}
    id_to_cell = {val:key for key,val in cell_to_id.items()}
    return [id_to_cell[ident] for ident in farm]

def train(s, Qout, reward, s1):
    #s <- cu
    pass

    
        


