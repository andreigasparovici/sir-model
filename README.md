# SIR model

The SIR model computes the evolution of an infectious disease over time.

![](https://render.githubusercontent.com/render/math?math=N) - population

![](https://render.githubusercontent.com/render/math?math=S(t)) - number of susceptible people

![](https://render.githubusercontent.com/render/math?math=I(t)) - number of infected people

![](https://render.githubusercontent.com/render/math?math=S(t)) - number of recovered people

![](https://render.githubusercontent.com/render/math?math=D(t)) - number of deceased people

![](https://render.githubusercontent.com/render/math?math=\beta) - rate of infection

![](https://render.githubusercontent.com/render/math?math=\gamma) - rate of recovery

![](https://render.githubusercontent.com/render/math?math=\mu) - rate of mortality

The model consists of the following system of ODEs:

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/1211c5146940bacb8a0df97780330a2599eb4625)

The system is solved numerically using Euler's method.

## Visualization example

![](anim.gif)

## Article

[Using Mathematical Modeling to Simulate an Epidemic](https://medium.com/towards-artificial-intelligence/using-mathematical-modeling-to-simulate-an-epidemic-2ceaf0c8286d)
