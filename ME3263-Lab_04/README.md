# Lab 4 - Predicting Natural Frequencies with the Finite Element Method


## What is the Finite Element Method?

Many engineering problems present themselves as partial differential equations (PDEs). The fields of solid mechanics, electromagnetics,
fluid mechanics, and heat transfer often describe a spatially varying quantity using PDEs - imagine, for example, the strain or 
temperature distribution across an engine component. For simple geometries, these types of "boundary value problems" can be solved 
analytically. For complicated geometries, analytical solutions are at best prohibitively time consuming and at worst impossible. 
In such cases, Finite Element Analysis (FEA) is the standard solution method.

The Finite Element Method (FEM) involves taking a continuous representation of a physical system and breaking it up into a finite number 
of elements. In three dimensions, these elements would commonly be shapes like cubes (hexahedrons) or pyramids (tetrahedrons). They are 
connected to their neighbors via "nodes" at each corner. This method results in a set of simultaneous algebraic equations that, when 
solved together, satisfies the governing equations (e.g., displacement or stress) at every node. With an increasing number of elements, 
the solution found using FEA will approach the analytical solution.

## Modal analysis with the Finite Element Method

In this lab, you will develop a model of your cantilevered beam using Ansys, and conduct a modal analysis to discover its fundamental 
frequencies and mode shapes. You will be judging the accuracy of your model in three ways:

- Convergence - examining the tendency of the FEA to approach a final solution with decreasing element size
- Verification - comparing your results to an analytical model
- Validation - comparing your results to an experimental model

## Deliverables

For this assignment, you will have two weeks in the lab. You and your lab partner will submit a __joint report__ as a .pdf to your
HuskyCT section within __one week__ of your final lab date. It will only be necessary for one of you to submit the report. Please clearly 
mark, either in the body as footnotes or in the appendix as a separate section, what each of you contributed to the overall report.

You are limited to __5 pages__ (not including the title page, references, or appendix) and __4 figures__. Additional data, figures, and 
information can be put in an appendix. The appendix will not be graded, but you may refer to it to explain data, methods, or other 
relevant information.