# Hopfield

The problem consists of creating a Hopfield network with 25 fully connected neurons and using it as an associative memory to store and retrieve letter patterns. In this case the letter patterns are A, B and C represented as binary arrays. The goal is for the network to store these patterns, and when presented with an incomplete or noisy pattern, it can retrieve the closest stored pattern.

Three functions are implemented: hopfield_update, which updates the network synchronously, hopfield_weights, which calculates the Hopfield weight matrix, and plot_patterns_as_letters, which visualizes the patterns as matrices of letters. The letter patterns A, B and C are plotted as binary matrices, where + 1 represents an activated pixel part (of the letter) and -1 represents an inactive pixel (empty space).

It is important to point out that Python version 3.10.5 under Windows 10 was used to solve the problem, and the NumPy library was also enabled to generate data, manipulate matrices and perform numerical operations related to the Hopfield network; in addition, the Matplotlib library was incorporated to better appreciate the results through graphs.

![image](https://github.com/YakoViTo/Hopfield/assets/135473233/765c8975-b599-44b9-81e1-9542be8f40b9)
![image](https://github.com/YakoViTo/Hopfield/assets/135473233/51dcb018-251b-4a20-8664-22c5f8a442e7)
