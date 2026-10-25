# Contact dynamics

Contact dynamics

Contact dynamics deals with the motion of multibody systems subjected to unilateral contacts and friction. Such systems are omnipresent in many multibody dynamics applications. Consider for example

Contacts between wheels and ground in vehicle dynamics
Squealing of brakes due to friction induced oscillations
Motion of many particles, spheres which fall in a funnel, mixing processes (granular media)
Clockworks
Walking machines
Arbitrary machines with limit stops, friction.
Anatomic tissues (skin, iris/lens, eyelids/anterior ocular surface, joint cartilages, vascular endothelium/blood cells, muscles/tendons, et cetera)
In the following it is discussed how such mechanical systems with unilateral contacts and friction can be modeled and how the time evolution of such systems can be obtained by numerical integration. In addition, some examples are given.

Modeling
The two main approaches for modeling mechanical systems with unilateral contacts and friction are the regularized and the non-smooth approach. In the following, the two approaches are introduced using a simple example. Consider a block which can slide or stick on a table (see figure 1a). The motion of the block is described by the equation of motion, whereas the friction force is unknown (see figure 1b). In order to obtain the friction force, a separate force law must be specified which links the friction force to the associated velocity of the block.

Non-smooth approach
A more sophisticated approach is the non-smooth approach, which uses set-valued force laws to model mechanical systems with unilateral contacts and friction. Consider again the block which slides or sticks on the table. The associated set-valued friction law of type Sgn is depicted in figure 3. Regarding the sliding case, the friction force is given. Regarding the sticking case, the friction force is set-valued and determined according to an additional algebraic constraint.

To conclude, the non-smooth approach changes the underlying mathematical structure if required and leads to a proper description of mechanical systems with unilateral contacts and friction. As a consequence of the changing mathematical structure, impacts can occur, and the time evolutions of the positions and the velocities can not be assumed to be smooth anymore. As a consequence, additional impact equations and impact laws have to be defined. In order to handle the changing mathematical structure, the set-valued force laws are commonly written as inequality or inclusion problems. The evaluation of these inequalities/inclusions is commonly done by solving linear (or nonlinear) complementarity problems, by quadratic programming or by transforming the inequality/inclusion problems into projective equations which can be solved iteratively by Jacobi or Gauss–Seidel techniques.
The non-smooth approach provides a new modeling approach for mechanical systems with unilateral contacts and friction, which incorporates also the whole classical mechanics subjected to bilateral constraints. The approach is associated to the classical DAE theory and leads to robust integration schemes.

Numerical integration
The integration of regularized models can be done by standard stiff solvers for ordinary differential equations. However, oscillations induced by the regularization can occur. Considering non-smooth models of mechanical systems with unilateral contacts and friction, two main classes of integrators exist, the event-driven and the so-called time-stepping integrators.

Event-driven integrators
Event-driven integrators distinguish between smooth parts of the motion in which the underlying structure of the differential equations does not change, and in events or so-called switching points at which this structure changes, i.e. time instants at which a unilateral contact closes or a stick slip transition occurs. At these switching points, the set-valued force (and additional impact) laws are evaluated in order to obtain a new underlying mathematical structure on which the integration can be continued. Event-driven integrators are very accurate but are not suitable for systems with many contacts.

Time-stepping integrators
Time-stepping integrators are dedicated numerical schemes for mechanical systems with many contacts. The first time-stepping integrator was introduced by J.J. Moreau. The integrators do not aim at resolving switching points and are therefore very robust in application. As the integrators work with the integral of the contact forces and not with the forces itself, the methods can handle both motion and impulsive events like impacts. As a drawback, the accuracy of time-stepping integrators is low. This can be fixed by using a step-size refinement at switching points. Smooth parts of the motion are processed by larger step sizes, and higher order integration methods can be used to increase the integration order.

Examples
This section gives some examples of mechanical systems with unilateral contacts and friction. The results have been obtained by a non-smooth approach using time-stepping integrators.

Granular materials
Time-stepping methods are especially well suited for the simulation of granular materials. Figure 4 depicts the simulation of mixing 1000 disks.

Billiard
Consider two colliding spheres in a billiard play. Figure 5a shows some snapshots of two colliding spheres, figure 5b depicts the associated trajectories.

Wheelie of a motorbike
If the acceleration of a two-wheeled system such as a motorbike is enough to overcome the force of gravity keeping one of the wheels on the ground, it can perform a maneuver called a wheelie. Figure 6 shows some snapshots of a simulation.

Motion of the woodpecker toy
The woodpecker toy is a well known benchmark problem in contact dynamics. The toy consists of a pole, a sleeve with a hole that is slightly larger than the diameter of the pole, a spring and the woodpecker body. In operation, the woodpecker moves down the pole performing some kind of pitching motion, which is controlled by the sleeve. Figure 7 shows some snapshots of a simulation.

A simulation and visualization can be found at https://github.com/gabyx/Woodpecker.
