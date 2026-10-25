# Dynamical simulation

Dynamical simulation

Dynamical simulation, in computational physics, is the simulation of systems of objects that are free to move, usually in three dimensions according to Newton's laws of classical dynamics, or approximations thereof. Dynamical simulation is used in computer animation to assist animators to produce realistic motion, in industrial design (for example to simulate crashes as an early step in crash testing), and in video games. Body movement is calculated using time integration methods.

Physics engines

In computer science, a program called a physics engine is used to model the behaviors of objects in space. These engines allow simulation of the way bodies of many types are affected by a variety of physical stimuli. They are also used to create dynamical simulations without having to know anything about physics. Physics engines are used throughout the video game and movie industry, but not all physics engines are alike. They are generally broken into real-time and the high precision, but these are not the only options. Most real-time physics engines are inaccurate and yield only the barest approximation of the real world, whereas most high-precision engines are far too slow for use in everyday applications.
To understand how these Physics engines are built, a basic understanding of physics is required. Physics engines are based on the actual behaviors of the world as described by classical mechanics. Engines do not typically account for non-classical mechanics (see theory of relativity and quantum mechanics) because most visualization deals with large bodies moving relatively slowly. The models used in dynamical simulations determine how accurate these simulations are.

Formulation

Particle model

The first model which may be used in physics engines governs the motion of infinitesimal objects with finite mass called “particles.” This equation, called Newton’s Second law (see Newton's laws) or the definition of force, is the fundamental behavior governing all motion:

              F
              →

        m

              a
              →

    {\displaystyle {\vec {F}}=m{\vec {a}}}

This equation allows us to fully model the behavior of particles, but it is not sufficient for most simulations because it does not account for the rotational motion of rigid bodies. This is the simplest model that can be used in a physics engine and was extensively used in early video games.

Inertial model

Bodies in the real world deform as forces are applied to them, so we call them “soft,” but often the deformation is negligibly small compared to the motion, and it is very complicated to model, so most physics engines ignore deformation. A body that is assumed to be non-deformable is called a rigid body. Rigid body dynamics deals with the motion of objects that cannot change shape, size, or mass but can change orientation and position.
To account for rotational energy and momentum, we must describe how force is applied to the object using a moment, and account for the mass distribution of the object using an inertia tensor. We describe these complex interactions with an equation somewhat similar to the definition of force above:

                d

              (

                I

                ω

              )

                d

              t

          ∑

            j

            1

            N

          τ

            j

    {\displaystyle {\frac {\mathrm {d} (\mathbf {I} {\boldsymbol {\omega }})}{\mathrm {d} t}}=\sum _{j=1}^{N}\tau _{j}}

where

          I

    {\displaystyle \mathbf {I} }

 is the central inertia tensor,

              ω
              →

    {\displaystyle {\vec {\omega }}}

 is the angular velocity vector, and

          τ

            j

    {\displaystyle \tau _{j}}

 is the moment of the jth external force about the mass center.
The inertia tensor describes the location of each particle of mass in a given object in relation to the object's center of mass. This allows us to determine how an object will rotate dependent on the forces applied to it. This angular motion is quantified by the angular velocity vector.
As long as we stay below relativistic speeds (see Relativistic dynamics), this model will accurately simulate all relevant behavior. This method requires the Physics engine to solve six ordinary differential equations at every instant we want to render, which is a simple task for modern computers.

Euler model

The inertial model is much more complex than we typically need but it is the most simple to use. In this model, we do not need to change our forces or constrain our system. However, if we make a few intelligent changes to our system, simulation will become much easier, and our calculation time will decrease. The first constraint will be to put each torque in terms of the principal axes. This makes each torque much more difficult to program, but it simplifies our equations significantly. When we apply this constraint, we diagonalize the moment of inertia tensor, which simplifies our three equations into a special set of equations called Euler's equations. These equations describe all rotational momentum in terms of the principal axes:

                  I

                    1

                        ω
                        ˙

                    1

                +
                (

                  I

                    3

                −

                  I

                    2

                )

                  ω

                    2

                  ω

                    3

                  N

                    1

                  I

                    2

                        ω
                        ˙

                    2

                +
                (

                  I

                    1

                −

                  I

                    3

                )

                  ω

                    3

                  ω

                    1

                  N

                    2

                  I

                    3

                        ω
                        ˙

                    3

                +
                (

                  I

                    2

                −

                  I

                    1

                )

                  ω

                    1

                  ω

                    2

                  N

                    3

    {\displaystyle {\begin{matrix}I_{1}{\dot {\omega }}{1}+(I{3}-I_{2})\omega _{2}\omega {3}&=&N{1}\I_{2}{\dot {\omega }}{2}+(I{1}-I_{3})\omega _{3}\omega {1}&=&N{2}\I_{3}{\dot {\omega }}{3}+(I{2}-I_{1})\omega _{1}\omega {2}&=&N{3}\end{matrix}}}

The N terms are applied torques about the principal axes
The I terms are the principal moments of inertia
The

          ω

    {\displaystyle {\omega }}

 terms are angular velocities about the principal axes
The drawback to this model is that all the computation is on the front end, so it is still slower than we would like. The real usefulness is not apparent because it still relies on a system of non-linear differential equations. To alleviate this problem, we have to find a method that can remove the second term from the equation. This will allow us to integrate much more easily. The easiest way to do this is to assume a certain amount of symmetry.

Symmetric/torque model
The two types of symmetric objects that will simplify Euler's equations are “symmetric tops” and “symmetric spheres.” The first assumes one degree of symmetry, this makes two of the I terms equal. These objects, like cylinders and tops, can be expressed with one very simple equation and two slightly simpler equations. This does not do us much good, because with one more symmetry we can get a large jump in speed with almost no change in appearance. The symmetric sphere makes all of the I terms equal (the Moment of inertia scalar), which makes all of these equations simple:

                I

                        ω
                        ˙

                    1

                  N

                    1

                I

                        ω
                        ˙

                    2

                  N

                    2

                I

                        ω
                        ˙

                    3

                  N

                    3

    {\displaystyle {\begin{matrix}I{\dot {\omega }}{1}&=&N{1}\I{\dot {\omega }}{2}&=&N{2}\I{\dot {\omega }}{3}&=&N{3}\end{matrix}}}

The N terms are applied torques about the principal axes
The

          ω

    {\displaystyle {\omega }}

 terms are angular velocities about the principal axes
The I term is the scalar Moment of inertia:

        I

                  d
                  e
                  f

          ∫

            V

          l

            2

        (
        m
        )

        d
        m

          ∭

            V

          l

            2

        (
        v
        )

        ρ
        (
        v
        )

        d
        v

          ∭

            V

          l

            2

        (
        x
        ,
        y
        ,
        z
        )

        ρ
        (
        x
        ,
        y
        ,
        z
        )

        d
        x

        d
        y

        d
        z

    {\displaystyle I\ {\stackrel {\mathrm {def} }{=}}\ \int _{V}l^{2}(m)\,dm=\iiint _{V}l^{2}(v)\,\rho (v)\,dv=\iiint _{V}l^{2}(x,y,z)\,\rho (x,y,z)\,dx\,dy\,dz!}

where
V is the volume region of the object,
r is the distance from the axis of rotation,
m is mass,
v is volume,
ρ is the pointwise density function of the object,
x, y, z are the Cartesian coordinates.
These equations allow us to simulate the behavior of an object that can spin in a way very close to the method simulate motion without spin. This is a simple model but it is accurate enough to produce realistic output in real-time Dynamical simulations. It also allows a Physics engine to focus on the changing forces and torques rather than varying inertia.

Multiple bodies
Multibody simulation (MBS) is a method of numerical simulation in which multibody systems are composed of various rigid or elastic bodies. Connections between the bodies can be modeled with kinematic constraints (such as joints) or force elements (such as spring dampers). Unilateral constraints and Coulomb-friction can also be used to model frictional contacts between bodies.
Multibody simulation is a useful tool for conducting motion analysis. It is often used during product development to evaluate characteristics of comfort, safety, and performance. For example, multibody simulation has been widely used since the 1990s as a component of automotive suspension design. It can also be used to study issues of biomechanics, with applications including sports medicine, osteopathy, and human-machine interaction.
The heart of any multibody simulation software program is the solver. The solver is a set of computation algorithms that solve equations of motion. Types of components that can be studied through multibody simulation range from electronic control systems to noise, vibration and harshness. Complex models such as engines are composed of individually designed components, e.g. pistons and crankshafts.
The MBS process often can be divided in 5 main activities. The first activity of the MBS process chain is the "3D CAD master model", in which product developers, designers and engineers are using the CAD system to generate a CAD model and its assembly structure related to given specifications. This 3D CAD master model is converted during the activity "Data transfer" to the MBS input data formats i.e. STEP. The "MBS Modeling" is the most complex activity in the process chain. Following rules and experiences, the 3D model in MBS format, multiple boundaries, kinematics, forces, moments or degrees of freedom are used as input to generate the MBS model. Engineers have to use MBS software and their knowledge and skills in the field of engineering mechanics and machine dynamics to build the MBS model including joints and links. The generated MBS model is used during the next activity "Simulation". Simulations, which are specified by time increments and boundaries like starting conditions are run by MBS Software. It is also possible to perform MBS simulations using free and open source packages. The last activity is the "Analysis and evaluation". Engineers use case-dependent directives to analyze and evaluate moving paths, speeds, accelerations, forces or moments. The results are used to enable releases or to improve the MBS model, in case the results are insufficient. One of the most important benefits of the MBS process chain is the usability of the results to optimize the 3D CAD master model components. Due to the fact that the process chain enables the optimization of component design, the resulting loops can be used to achieve a high level of design and MBS model optimization in an iterative process.
