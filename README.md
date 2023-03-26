# Applicability
Application that finds the electrical consumption of a specific process/application

## Design consideration
### Which platform to implement?
The 2 main platforms used by consumers are Windows and Mac 

<sup>Linux is also used but to a small extent. It is mainly used in servers</sup>

While there are currently many methods to get the power consumption on specific apps for linux and Windows, 
I have decided to find energy consumption for Mac systems instead
* Many programs implemented on Windows already (powercfg.exe -ENERGY)
* A large majority of programmers run their programs on Mac
* Linux systems already have many programs like PowerTop which does the equivalent

