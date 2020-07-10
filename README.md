# SIR model

The SIR model computes the evolution of an infectious disease over time.

![](https://render.githubusercontent.com/render/math?math=S(t)) - number of susceptible people

![](https://render.githubusercontent.com/render/math?math=I(t)) - number of infected people

![](https://render.githubusercontent.com/render/math?math=S(t)) - number of recovered people

The model consists of the following system of ODEs:

![](https://render.githubusercontent.com/render/math?math=%5Cfrac%7Bd%7D%7Bdt%7D%5Cbegin%7Bpmatrix%7D%0D%0AS+%5C%5C+I+%5C%5C+R%0D%0A%5Cend%7Bpmatrix%7D+%3D+%5Cbegin%7Bpmatrix%7D%0D%0A-%5Cbeta+S+I+%5C%5C+%0D%0A%5Cbeta+S+I+-+%5Cgamma+I+%5C%5C%0D%0A%5Cgamma+I%0D%0A%5Cend%7Bpmatrix%7D)

## Visualization example

![](sir.png)
