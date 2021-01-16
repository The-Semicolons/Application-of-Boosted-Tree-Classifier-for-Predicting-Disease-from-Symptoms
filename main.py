# File created by Utkarsh Gupta
# Dated 15/1/2020

# Touched on 17/1/2020 by Utkarsh Gupta

# Main function : Program execution starts and ends here.

from TreeClassifier import treeClassifier
from time import time


def runModel():
    tree = treeClassifier()
    # Change these variables for testing.
    tree.getParameterList(noOfTree=100,
                          maxTreeDepth=5,
                          learningRate=0.1,
                          noOfBatchesPerLayer=2)

    tree.loadFiles()
    tree.generateFeatureColumn()
    t1 = time()
    tree.constructTree()
    tree.trainTree()
    t2 = time()
    tree.evaluateTree()
    t3 = time()
    print("Tree construction time:", t2 - t1)
    print("Tree evaluation time:", t3 - t2)


if __name__ == '__main__':
    runModel()
