# OpenLB

OpenLB

OpenLB is an object-oriented implementation of the lattice Boltzmann methods (LBM). It is the first implementation of a generic platform for LBM programming, which is shared with the open source community (GPLv2).
The code is written in C++ and is used by application programmers as well as developers, with the ability to implement custom models
OpenLB supports complex data structures that allow simulations in complex geometries and parallel execution using MPI, OpenMP and CUDA on high-performance computers.
The source code uses the concepts of interfaces and templates, so that efficient, direct and intuitive implementations of the LBM become possible.
The efficiency and scalability has been checked and proved by code reviews.
A user manual and a source code documentation by DoxyGen are available on the project page.

Functions
OpenLB is being constantly developed. By now the following features are implemented:

Computational fluid dynamics in complex geometry
Automatic generation of a grid
Turbulent flow
Multi-component flow
Thermal flow
Light radiation
Topology optimizing
Particle flow (Euler–Euler and Euler–Lagrange method)

Automated grid generation
Automated grid generation is one of the great advantages of OpenLB over other CFD software packages. The main advantages are listed below:

Use of geometries in the STL file format or geometrically primitive forms (e.g. ball, cylinder, cone) and their union, intersection and difference
Very fast voxelization: 6003 ~ 1 minute
Handling non-watertight surfaces
Memory-friendly using octrees
Load distribution for parallel execution with MPI, OpenMP and CUDA.
The automatic grid generation can assume both an STL file as well as primitive geometries. For the geometry, a uniform and rectangular grid is created which encloses the entire space of the geometry. The superfluous grid cells are then removed and the remaining cuboids are shrunk to fit the given geometry. Finally, the grid is distributed to different threads or processors for the parallel execution of the simulation. The boundary conditions and start values can be set using material numbers.

Literature
Krause, Mathias J. and Latt, Jonas and Heuveline, Vincent. "Towards a hybrid parallelization of lattice Boltzmann methods." Computers & Mathematics with Applications 58.5 (2009): 1071–1080.
Heuveline, Vincent, and Mathias J. Krause. "OpenLB: towards an efficient parallel open source library for lattice Boltzmann fluid flow simulations." International Workshop on State-of-the-Art in Scientific and Parallel Computing. PARA. Vol. 9. 2010.
Krause, Mathias J., Thomas Gengenbach, and Vincent Heuveline. "Hybrid parallel simulations of fluid flows in complex geometries: Application to the human lungs." European Conference on Parallel Processing. Springer Berlin Heidelberg, 2010.
Krause, Mathias J. "Fluid flow simulation and optimisation with lattice Boltzmann methods on high performance computers: application to the human respiratory system." Karlsruhe Institute of Technology, KIT (2010).
Trunk, Robin, et al. "Inertial dilute particulate fluid flow simulations with an Euler–Euler lattice Boltzmann method." Journal of Computational Science (2016).
Mink, Albert, et al. "A 3D Lattice Boltzmann method for light simulation in participating media." Journal of Computational Science (2016).

Awards
Winner Mimics Innovation Award (2011)
Honorary certificate in the Group Humanitarian Impact, "Itanium® Solutions Alliance Innovation Awards" (2009)
Finalist in the Group Humanitarian Impact Innovation, "Itanium® Solutions Alliance Innovation Awards" (2007)
