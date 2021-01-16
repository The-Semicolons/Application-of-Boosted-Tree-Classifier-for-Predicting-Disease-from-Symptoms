# Application of Boosted Tree Classifier for Predicting Disease from Symptoms
 Research based testing Boosted Tree Classifier for Predicting Disease from Symptoms

## Dependencies
1. python 64 bit (Strictly) (32 bit will raise errors) `If you have 32 bit version. Uninstall it first then install 64 bit version.`
2. tensorflow 2.4
3. pandas

> Note: Ignore 10000 Warnings. Warnings are because we are using a version of tensorflow which can run without GPU. If you have GPU update cuda toolkit and cuDNN to run model faster.

> If you encounter an error named `Value out of range` that is because you put a value of variable that is way too large.

## Variables that needs to be tweaked
***Edit these variables in main.py file only***
- noOfTree
- maxTreeDepth
- learningRate
- noOfBatchesPerLayer

***Note your observation in the observation.xlsx file under the sheet of YOUR NAME***

> This algorithm uses plenty of randomness to create first trees so everytime you run the model even with same variable values you might get different values.

## Videos I referred to understand Boosted Tree Classifier
**In Sequence**
1. https://youtu.be/3CC4N4z3GJc
2. https://youtu.be/2xudPOBz-vs
3. https://youtu.be/jxuNLH5dXCs
4. https://youtu.be/StWY5QWMXCw

> You can choose not to watch these videos and find your own tutorials.

## Reading content
- Tensorflow Documentation: https://www.tensorflow.org/api_docs/python/tf/estimator/BoostedTreesClassifier
- Example of Boosted Tree: https://medium.com/tensorflow/how-to-train-boosted-trees-models-in-tensorflow-ca8466a53127