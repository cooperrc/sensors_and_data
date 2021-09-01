# ME3263 Introduction to Sensors and Data Analysis (Fall 2018)

## Lab #4 Predicting Natural Frequencies with the Finite Element Method


### What is the Finite Element Method?

The Euler-Lagrange dynamic beam equation is an example of a partial differential
equation (PDE). These equations are common in many engineering applications e.g.
solid mechanics, electromagnetics, fluid mechanics, and quantum mechanics. The
finite element method solves PDEs. The FEM process involves two steps to create
matrices for a computer algorithm solution. First, the PDE is integrated from
the strong form to the weak form. Second, an approximation of the variable
"shapes" within each "element" is created to convert the integrals and
derivatives into matrices
[(1)](http://bcs.wiley.com/he-bcs/Books?action=index&bcsId=3625&itemId=0470035803).
For elements with nodes only at vertices, such as cubes (hexahedrons) or
pyramids (tetrahedrals), the "shape" function is linear for displacement. 
