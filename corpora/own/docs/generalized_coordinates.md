# Generalized coordinates

Generalized coordinates

In analytical mechanics, generalized coordinates are a set of parameters used to represent the configuration of a system in a configuration space. These parameters must uniquely define the configuration of the system relative to a reference configuration. The generalized velocities are the time derivatives of the generalized coordinates of the system. The adjective "generalized" distinguishes these parameters from the traditional use of the term "coordinate" to refer to Cartesian coordinates.
An example of a generalized coordinate would be to describe the position of a pendulum using the angle of the pendulum relative to vertical, rather than by the x and y position of the pendulum.
Although there may be many possible choices for generalized coordinates for a physical system, they are generally selected to simplify calculations, such as the solution of the equations of motion for the system. If the coordinates are independent of one another, the number of independent generalized coordinates is defined by the number of degrees of freedom of the system.
Generalized coordinates are paired with generalized momenta to provide canonical coordinates on phase space.

Constraints and degrees of freedom

Generalized coordinates are usually selected to provide the minimum number of independent coordinates that define the configuration of a system, which simplifies the formulation of Lagrange's equations of motion. However, it can also occur that a useful set of generalized coordinates may be dependent, which means that they are related by one or more constraint equations.

Holonomic constraints

For a system of N particles in 3D real coordinate space, the position vector of each particle can be written as a 3-tuple in Cartesian coordinates:

                    r

                    1

                (

                  x

                    1

                ,

                  y

                    1

                ,

                  z

                    1

                )
                ,

                    r

                    2

                (

                  x

                    2

                ,

                  y

                    2

                ,

                  z

                    2

                )
                ,

                ⋮

                    r

                    N

                (

                  x

                    N

                ,

                  y

                    N

                ,

                  z

                    N

                )

    {\displaystyle {\begin{aligned}&\mathbf {r} {1}=(x{1},y_{1},z_{1}),\&\mathbf {r} {2}=(x{2},y_{2},z_{2}),\&\qquad \qquad \vdots \&\mathbf {r} {N}=(x{N},y_{N},z_{N})\end{aligned}}}

Any of the position vectors can be denoted rk where k = 1, 2, …, N labels the particles. A holonomic constraint is a constraint equation of the form for particle k

        f
        (

            r

            k

        ,
        t
        )

        0

    {\displaystyle f(\mathbf {r} _{k},t)=0}

which connects all the 3 spatial coordinates of that particle together, so they are not independent. The constraint may change with time, so time t will appear explicitly in the constraint equations. At any instant of time, any one coordinate will be determined from the other coordinates, e.g. if xk and zk are given, then so is yk. One constraint equation counts as one constraint. If there are C constraints, each has an equation, so there will be C constraint equations. There is not necessarily one constraint equation for each particle, and if there are no constraints on the system then there are no constraint equations.
So far, the configuration of the system is defined by 3N quantities, but C coordinates can be eliminated, one coordinate from each constraint equation. The number of independent coordinates is n = 3N − C. (In D dimensions, the original configuration would need ND coordinates, and the reduction by constraints means n = ND − C). It is ideal to use the minimum number of coordinates needed to define the configuration of the entire system, while taking advantage of the constraints on the system. These quantities are known as generalized coordinates in this context, denoted qj(t). It is convenient to collect them into an n-tuple

          q

        (
        t
        )

        (

          q

            1

        (
        t
        )
        ,

          q

            2

        (
        t
        )
        ,

        …
        ,

          q

            n

        (
        t
        )
        )

    {\displaystyle \mathbf {q} (t)=(q_{1}(t),\ q_{2}(t),\ \ldots ,\ q_{n}(t))}

which is a point in the configuration space of the system. They are all independent of one other, and each is a function of time. Geometrically they can be lengths along straight lines, or arc lengths along curves, or angles; not necessarily Cartesian coordinates or other standard orthogonal coordinates. There is one for each degree of freedom, so the number of generalized coordinates equals the number of degrees of freedom, n. A degree of freedom corresponds to one quantity that changes the configuration of the system, for example the angle of a pendulum, or the arc length traversed by a bead along a wire.
If it is possible to find from the constraints as many independent variables as there are degrees of freedom, these can be used as generalized coordinates. The position vector rk of particle k is a function of all the n generalized coordinates (and, through them, of time),

            r

            k

            r

            k

        (

          q

        (
        t
        )
        )

        ,

    {\displaystyle \mathbf {r} _{k}=\mathbf {r} _{k}(\mathbf {q} (t))\,,}

and the generalized coordinates can be thought of as parameters associated with the constraint.
The corresponding time derivatives of q are the generalized velocities,

                q

              ˙

              d

                q

              d
              t

        (

                q
                ˙

            1

        (
        t
        )
        ,

                q
                ˙

            2

        (
        t
        )
        ,

        …
        ,

                q
                ˙

            n

        (
        t
        )
        )

    {\displaystyle {\dot {\mathbf {q} }}={\frac {d\mathbf {q} }{dt}}=({\dot {q}}{1}(t),\ {\dot {q}}{2}(t),\ \ldots ,\ {\dot {q}}_{n}(t))}

(each dot over a quantity indicates one time derivative). The velocity vector vk is the total derivative of rk with respect to time

            v

            k

                  r

                ˙

            k

              d

                  r

                  k

              d
              t

          ∑

            j

            1

            n

              ∂

                  r

                  k

              ∂

                q

                  j

                q
                ˙

            j

        .

    {\displaystyle \mathbf {v} {k}={\dot {\mathbf {r} }}{k}={\frac {d\mathbf {r} _{k}}{dt}}=\sum _{j=1}^{n}{\frac {\partial \mathbf {r} {k}}{\partial q{j}}}{\dot {q}}_{j}\,.}

and so generally depends on the generalized velocities and coordinates. Since we are free to specify the initial values of the generalized coordinates and velocities separately, the generalized coordinates qj and velocities dqj/dt can be treated as independent variables.

Non-holonomic constraints
A mechanical system can involve constraints on both the generalized coordinates and their derivatives. Constraints of this type are known as non-holonomic. First-order non-holonomic constraints have the form

        g
        (

          q

        ,

                q

              ˙

        ,
        t
        )

        0

        ,

    {\displaystyle g(\mathbf {q} ,{\dot {\mathbf {q} }},t)=0\,,}

An example of such a constraint is a rolling wheel or knife-edge that constrains the direction of the velocity vector. Non-holonomic constraints can also involve next-order derivatives such as generalized accelerations.

Physical quantities in generalized coordinates

Kinetic energy
The total kinetic energy of the system is the energy of the system's motion, defined as

        T

            1
            2

          ∑

            k

            1

            N

          m

            k

                  r

                ˙

            k

        ⋅

                  r

                ˙

            k

        ,

    {\displaystyle T={\frac {1}{2}}\sum {k=1}^{N}m{k}{\dot {\mathbf {r} }}{k}\cdot {\dot {\mathbf {r} }}{k}\,,}

in which · is the dot product. The kinetic energy is a function only of the velocities vk, not the coordinates rk themselves. By contrast an important observation is

                  r

                ˙

            k

        ⋅

                  r

                ˙

            k

          ∑

            i
            ,
            j

            1

            n

          (

                  ∂

                      r

                      k

                  ∂

                    q

                      i

            ⋅

                  ∂

                      r

                      k

                  ∂

                    q

                      j

          )

                q
                ˙

            i

                q
                ˙

            j

        ,

    {\displaystyle {\dot {\mathbf {r} }}{k}\cdot {\dot {\mathbf {r} }}{k}=\sum _{i,j=1}^{n}\left({\frac {\partial \mathbf {r} {k}}{\partial q{i}}}\cdot {\frac {\partial \mathbf {r} {k}}{\partial q{j}}}\right){\dot {q}}{i}{\dot {q}}{j},}

which illustrates the kinetic energy is in general a function of the generalized velocities, coordinates, and time if the constraints also vary with time, so T = T(q, dq/dt, t).
In the case the constraints on the particles are time-independent, then all partial derivatives with respect to time are zero, and the kinetic energy is a homogeneous function of degree 2 in the generalized velocities.
Still for the time-independent case, this expression is equivalent to taking the line element squared of the trajectory for particle k,

        d

          s

            k

            2

        d

            r

            k

        ⋅
        d

            r

            k

          ∑

            i
            ,
            j

            1

            n

          (

                  ∂

                      r

                      k

                  ∂

                    q

                      i

            ⋅

                  ∂

                      r

                      k

                  ∂

                    q

                      j

          )

        d

          q

            i

        d

          q

            j

        ,

    {\displaystyle ds_{k}^{2}=d\mathbf {r} _{k}\cdot d\mathbf {r} _{k}=\sum _{i,j=1}^{n}\left({\frac {\partial \mathbf {r} {k}}{\partial q{i}}}\cdot {\frac {\partial \mathbf {r} {k}}{\partial q{j}}}\right)dq_{i}dq_{j}\,,}

and dividing by the square differential in time, dt2, to obtain the velocity squared of particle k. Thus for time-independent constraints it is sufficient to know the line element to quickly obtain the kinetic energy of particles and hence the Lagrangian.
It is instructive to see the various cases of polar coordinates in 2D and 3D, owing to their frequent appearance. In 2D polar coordinates (r, θ),

            (

                  d
                  s

                  d
                  t

            )

            2

                r
                ˙

            2

        +

          r

            2

                θ
                ˙

            2

        ,

    {\displaystyle \left({\frac {ds}{dt}}\right)^{2}={\dot {r}}^{2}+r^{2}{\dot {\theta }}^{2}\,,}

in 3D cylindrical coordinates (r, θ, z),

            (

                  d
                  s

                  d
                  t

            )

            2

                r
                ˙

            2

        +

          r

            2

                θ
                ˙

            2

        +

                z
                ˙

            2

        ,

    {\displaystyle \left({\frac {ds}{dt}}\right)^{2}={\dot {r}}^{2}+r^{2}{\dot {\theta }}^{2}+{\dot {z}}^{2}\,,}

in 3D spherical coordinates (r, θ, φ),

            (

                  d
                  s

                  d
                  t

            )

            2

                r
                ˙

            2

        +

          r

            2

                θ
                ˙

            2

        +

          r

            2

          sin

            2

        ⁡
        θ

                φ
                ˙

            2

        .

    {\displaystyle \left({\frac {ds}{dt}}\right)^{2}={\dot {r}}^{2}+r^{2}{\dot {\theta }}^{2}+r^{2}\sin ^{2}\theta \,{\dot {\varphi }}^{2}\,.}

Generalized momentum
The generalized momentum "canonically conjugate to" the coordinate qi is defined by

          p

            i

              ∂
              L

              ∂

                      q
                      ˙

                  i

        .

    {\displaystyle p_{i}={\frac {\partial L}{\partial {\dot {q}}_{i}}}.}

If the Lagrangian L does not depend on some coordinate qi, then it follows from the Euler–Lagrange equations that the corresponding generalized momentum will be a conserved quantity, because the time derivative is zero implying the momentum is a constant of the motion;

              ∂
              L

              ∂

                q

                  i

            d

              d
              t

              ∂
              L

              ∂

                      q
                      ˙

                  i

                p
                ˙

            i

        0

        .

    {\displaystyle {\frac {\partial L}{\partial q_{i}}}={\frac {d}{dt}}{\frac {\partial L}{\partial {\dot {q}}{i}}}={\dot {p}}{i}=0\,.}

Examples

Bead on a wire

For a bead sliding on a frictionless wire subject only to gravity in 2d space, the constraint on the bead can be stated in the form f (r) = 0, where the position of the bead can be written r = (x(s), y(s)), in which s is a parameter, the arc length s along the curve from some point on the wire. This is a suitable choice of generalized coordinate for the system. Only one coordinate is needed instead of two, because the position of the bead can be parameterized by one number, s, and the constraint equation connects the two coordinates x and y; either one is determined from the other. The constraint force is the reaction force the wire exerts on the bead to keep it on the wire, and the non-constraint applied force is gravity acting on the bead.
Suppose the wire changes its shape with time, by flexing. Then the constraint equation and position of the particle are respectively

        f
        (

          r

        ,
        t
        )

        0

        ,

          r

        (
        x
        (
        s
        ,
        t
        )
        ,
        y
        (
        s
        ,
        t
        )
        )

    {\displaystyle f(\mathbf {r} ,t)=0\,,\quad \mathbf {r} =(x(s,t),y(s,t))}

which now both depend on time t due to the changing coordinates as the wire changes its shape. Notice time appears implicitly via the coordinates and explicitly in the constraint equations.

Simple pendulum

The relationship between the use of generalized coordinates and Cartesian coordinates to characterize the movement of a mechanical system can be illustrated by considering the constrained dynamics of a simple pendulum.
A simple pendulum consists of a mass M hanging from a pivot point so that it is constrained to move on a circle of radius L. The position of the mass is defined by the coordinate vector r = (x, y) measured in the plane of the circle such that y is in the vertical direction. The coordinates x and y are related by the equation of the circle

        f
        (
        x
        ,
        y
        )

          x

            2

        +

          y

            2

        −

          L

            2

        0
        ,

    {\displaystyle f(x,y)=x^{2}+y^{2}-L^{2}=0,}

that constrains the movement of M. This equation also provides a constraint on the velocity components,

              f
              ˙

        (
        x
        ,
        y
        )

        2
        x

              x
              ˙

        +
        2
        y

              y
              ˙

        0.

    {\displaystyle {\dot {f}}(x,y)=2x{\dot {x}}+2y{\dot {y}}=0.}

Now introduce the parameter θ, that defines the angular position of M from the vertical direction. It can be used to define the coordinates x and y, such that

          r

        (
        x
        ,
        y
        )

        (
        L
        sin
        ⁡
        θ
        ,
        −
        L
        cos
        ⁡
        θ
        )
        .

    {\displaystyle \mathbf {r} =(x,y)=(L\sin \theta ,-L\cos \theta ).}

The use of θ to define the configuration of this system avoids the constraint provided by the equation of the circle.
Notice that the force of gravity acting on the mass m is formulated in the usual Cartesian coordinates,

          F

        (
        0
        ,
        −
        m
        g
        )
        ,

    {\displaystyle \mathbf {F} =(0,-mg),}

where g is the acceleration due to gravity.
The virtual work of gravity on the mass m as it follows the trajectory r is given by

        δ
        W

          F

        ⋅
        δ

          r

        .

    {\displaystyle \delta W=\mathbf {F} \cdot \delta \mathbf {r} .}

The variation δr can be computed in terms of the coordinates x and y, or in terms of the parameter θ,

        δ

          r

        (
        δ
        x
        ,
        δ
        y
        )

        (
        L
        cos
        ⁡
        θ
        ,
        L
        sin
        ⁡
        θ
        )
        δ
        θ
        .

    {\displaystyle \delta \mathbf {r} =(\delta x,\delta y)=(L\cos \theta ,L\sin \theta )\delta \theta .}

Thus, the virtual work is given by

        δ
        W

        −
        m
        g
        δ
        y

        −
        m
        g
        L
        sin
        ⁡
        (
        θ
        )
        δ
        θ
        .

    {\displaystyle \delta W=-mg\delta y=-mgL\sin(\theta )\delta \theta .}

Notice that the coefficient of δy is the y-component of the applied force. In the same way, the coefficient of δθ is known as the generalized force along generalized coordinate θ, given by

          F

            θ

        −
        m
        g
        L
        sin
        ⁡
        θ
        .

    {\displaystyle F_{\theta }=-mgL\sin \theta .}

To complete the analysis consider the kinetic energy T of the mass, using the velocity,

          v

        (

              x
              ˙

        ,

              y
              ˙

        )

        (
        L
        cos
        ⁡
        θ
        ,
        L
        sin
        ⁡
        θ
        )

              θ
              ˙

        ,

    {\displaystyle \mathbf {v} =({\dot {x}},{\dot {y}})=(L\cos \theta ,L\sin \theta ){\dot {\theta }},}

so,

        T

            1
            2

        m

          v

        ⋅

          v

            1
            2

        m
        (

                x
                ˙

            2

        +

                y
                ˙

            2

        )

            1
            2

        m

          L

            2

                θ
                ˙

            2

        .

    {\displaystyle T={\frac {1}{2}}m\mathbf {v} \cdot \mathbf {v} ={\frac {1}{2}}m({\dot {x}}^{2}+{\dot {y}}^{2})={\frac {1}{2}}mL^{2}{\dot {\theta }}^{2}.}

D'Alembert's form of the principle of virtual work for the pendulum in terms of the coordinates x and y are given by,

            d

              d
              t

              ∂
              T

              ∂

                    x
                    ˙

        −

              ∂
              T

              ∂
              x

          F

            x

        +
        λ

              ∂
              f

              ∂
              x

        ,

            d

              d
              t

              ∂
              T

              ∂

                    y
                    ˙

        −

              ∂
              T

              ∂
              y

          F

            y

        +
        λ

              ∂
              f

              ∂
              y

        .

    {\displaystyle {\frac {d}{dt}}{\frac {\partial T}{\partial {\dot {x}}}}-{\frac {\partial T}{\partial x}}=F_{x}+\lambda {\frac {\partial f}{\partial x}},\quad {\frac {d}{dt}}{\frac {\partial T}{\partial {\dot {y}}}}-{\frac {\partial T}{\partial y}}=F_{y}+\lambda {\frac {\partial f}{\partial y}}.}

This yields the three equations

        m

              x
              ¨

        λ
        (
        2
        x
        )
        ,

        m

              y
              ¨

        −
        m
        g
        +
        λ
        (
        2
        y
        )
        ,

          x

            2

        +

          y

            2

        −

          L

            2

        0
        ,

    {\displaystyle m{\ddot {x}}=\lambda (2x),\quad m{\ddot {y}}=-mg+\lambda (2y),\quad x^{2}+y^{2}-L^{2}=0,}

in the three unknowns, x, y and λ.
Using the parameter θ, those equations take the form

            d

              d
              t

              ∂
              T

              ∂

                    θ
                    ˙

        −

              ∂
              T

              ∂
              θ

          F

            θ

        ,

    {\displaystyle {\frac {d}{dt}}{\frac {\partial T}{\partial {\dot {\theta }}}}-{\frac {\partial T}{\partial \theta }}=F_{\theta },}

which becomes,

        m

          L

            2

              θ
              ¨

        −
        m
        g
        L
        sin
        ⁡
        θ
        ,

    {\displaystyle mL^{2}{\ddot {\theta }}=-mgL\sin \theta ,}

or

              θ
              ¨

        +

            g
            L

        sin
        ⁡
        θ

        0.

    {\displaystyle {\ddot {\theta }}+{\frac {g}{L}}\sin \theta =0.}

This formulation yields one equation because there is a single parameter and no constraint equation.
This shows that the parameter θ is a generalized coordinate that can be used in the same way as the Cartesian coordinates x and y to analyze the pendulum.

Double pendulum

The benefits of generalized coordinates become apparent with the analysis of a double pendulum.
For the two masses mi (i = 1, 2), let ri = (xi, yi), i = 1, 2 define their two trajectories. These vectors satisfy the two constraint equations,

          f

            1

        (

          x

            1

        ,

          y

            1

        ,

          x

            2

        ,

          y

            2

        )

            r

            1

        ⋅

            r

            1

        −

          L

            1

            2

        0

    {\displaystyle f_{1}(x_{1},y_{1},x_{2},y_{2})=\mathbf {r} _{1}\cdot \mathbf {r} {1}-L{1}^{2}=0}

and

          f

            2

        (

          x

            1

        ,

          y

            1

        ,

          x

            2

        ,

          y

            2

        )

        (

            r

            2

        −

            r

            1

        )
        ⋅
        (

            r

            2

        −

            r

            1

        )
        −

          L

            2

            2

        0.

    {\displaystyle f_{2}(x_{1},y_{1},x_{2},y_{2})=(\mathbf {r} _{2}-\mathbf {r} _{1})\cdot (\mathbf {r} _{2}-\mathbf {r} {1})-L{2}^{2}=0.}

The formulation of Lagrange's equations for this system yields six equations in the four Cartesian coordinates xi, yi (i = 1, 2) and the two Lagrange multipliers λi (i = 1, 2) that arise from the two constraint equations.
Now introduce the generalized coordinates θi (i = 1, 2) that define the angular position of each mass of the double pendulum from the vertical direction. In this case, we have

            r

            1

        (

          L

            1

        sin
        ⁡

          θ

            1

        ,
        −

          L

            1

        cos
        ⁡

          θ

            1

        )
        ,

            r

            2

        (

          L

            1

        sin
        ⁡

          θ

            1

        ,
        −

          L

            1

        cos
        ⁡

          θ

            1

        )
        +
        (

          L

            2

        sin
        ⁡

          θ

            2

        ,
        −

          L

            2

        cos
        ⁡

          θ

            2

        )
        .

    {\displaystyle \mathbf {r} {1}=(L{1}\sin \theta {1},-L{1}\cos \theta _{1}),\quad \mathbf {r} {2}=(L{1}\sin \theta {1},-L{1}\cos \theta {1})+(L{2}\sin \theta {2},-L{2}\cos \theta _{2}).}

The force of gravity acting on the masses is given by,

            F

            1

        (
        0
        ,
        −

          m

            1

        g
        )
        ,

            F

            2

        (
        0
        ,
        −

          m

            2

        g
        )

    {\displaystyle \mathbf {F} {1}=(0,-m{1}g),\quad \mathbf {F} {2}=(0,-m{2}g)}

where g is the acceleration due to gravity. Therefore, the virtual work of gravity on the two masses as they follow the trajectories ri (i = 1, 2) is given by

        δ
        W

            F

            1

        ⋅
        δ

            r

            1

        +

            F

            2

        ⋅
        δ

            r

            2

        .

    {\displaystyle \delta W=\mathbf {F} _{1}\cdot \delta \mathbf {r} _{1}+\mathbf {F} _{2}\cdot \delta \mathbf {r} _{2}.}

The variations δri (i = 1, 2) can be computed to be

        δ

            r

            1

        (

          L

            1

        cos
        ⁡

          θ

            1

        ,

          L

            1

        sin
        ⁡

          θ

            1

        )
        δ

          θ

            1

        ,

        δ

            r

            2

        (

          L

            1

        cos
        ⁡

          θ

            1

        ,

          L

            1

        sin
        ⁡

          θ

            1

        )
        δ

          θ

            1

        +
        (

          L

            2

        cos
        ⁡

          θ

            2

        ,

          L

            2

        sin
        ⁡

          θ

            2

        )
        δ

          θ

            2

    {\displaystyle \delta \mathbf {r} {1}=(L{1}\cos \theta {1},L{1}\sin \theta _{1})\delta \theta _{1},\quad \delta \mathbf {r} {2}=(L{1}\cos \theta {1},L{1}\sin \theta _{1})\delta \theta {1}+(L{2}\cos \theta {2},L{2}\sin \theta _{2})\delta \theta _{2}}

Thus, the virtual work is given by

        δ
        W

        −
        (

          m

            1

        +

          m

            2

        )
        g

          L

            1

        sin
        ⁡

          θ

            1

        δ

          θ

            1

        −

          m

            2

        g

          L

            2

        sin
        ⁡

          θ

            2

        δ

          θ

            2

        ,

    {\displaystyle \delta W=-(m_{1}+m_{2})gL_{1}\sin \theta _{1}\delta \theta {1}-m{2}gL_{2}\sin \theta _{2}\delta \theta _{2},}

and the generalized forces are

          F

              θ

                1

        −
        (

          m

            1

        +

          m

            2

        )
        g

          L

            1

        sin
        ⁡

          θ

            1

        ,

          F

              θ

                2

        −

          m

            2

        g

          L

            2

        sin
        ⁡

          θ

            2

        .

    {\displaystyle F_{\theta {1}}=-(m{1}+m_{2})gL_{1}\sin \theta {1},\quad F{\theta {2}}=-m{2}gL_{2}\sin \theta _{2}.}

Compute the kinetic energy of this system to be

        T

            1
            2

          m

            1

            v

            1

        ⋅

            v

            1

        +

            1
            2

          m

            2

            v

            2

        ⋅

            v

            2

            1
            2

        (

          m

            1

        +

          m

            2

        )

          L

            1

            2

                θ
                ˙

            1

            2

        +

            1
            2

          m

            2

          L

            2

            2

                θ
                ˙

            2

            2

        +

          m

            2

          L

            1

          L

            2

        cos
        ⁡
        (

          θ

            2

        −

          θ

            1

        )

                θ
                ˙

            1

                θ
                ˙

            2

        .

    {\displaystyle T={\frac {1}{2}}m_{1}\mathbf {v} _{1}\cdot \mathbf {v} {1}+{\frac {1}{2}}m{2}\mathbf {v} _{2}\cdot \mathbf {v} {2}={\frac {1}{2}}(m{1}+m_{2})L_{1}^{2}{\dot {\theta }}{1}^{2}+{\frac {1}{2}}m{2}L_{2}^{2}{\dot {\theta }}{2}^{2}+m{2}L_{1}L_{2}\cos(\theta _{2}-\theta {1}){\dot {\theta }}{1}{\dot {\theta }}_{2}.}

Euler–Lagrange equation yield two equations in the unknown generalized coordinates θi (i = 1, 2) given by

        (

          m

            1

        +

          m

            2

        )

          L

            1

            2

                θ
                ¨

            1

        +

          m

            2

          L

            1

          L

            2

                θ
                ¨

            2

        cos
        ⁡
        (

          θ

            2

        −

          θ

            1

        )
        +

          m

            2

          L

            1

          L

            2

                  θ

                    2

                ˙

            2

        sin
        ⁡
        (

          θ

            1

        −

          θ

            2

        )

        −
        (

          m

            1

        +

          m

            2

        )
        g

          L

            1

        sin
        ⁡

          θ

            1

        ,

    {\displaystyle (m_{1}+m_{2})L_{1}^{2}{\ddot {\theta }}{1}+m{2}L_{1}L_{2}{\ddot {\theta }}_{2}\cos(\theta _{2}-\theta {1})+m{2}L_{1}L_{2}{\dot {\theta _{2}}}^{2}\sin(\theta _{1}-\theta {2})=-(m{1}+m_{2})gL_{1}\sin \theta _{1},}

and

          m

            2

          L

            2

            2

                θ
                ¨

            2

        +

          m

            2

          L

            1

          L

            2

                θ
                ¨

            1

        cos
        ⁡
        (

          θ

            2

        −

          θ

            1

        )
        +

          m

            2

          L

            1

          L

            2

                  θ

                    1

                ˙

            2

        sin
        ⁡
        (

          θ

            2

        −

          θ

            1

        )

        −

          m

            2

        g

          L

            2

        sin
        ⁡

          θ

            2

        .

    {\displaystyle m_{2}L_{2}^{2}{\ddot {\theta }}{2}+m{2}L_{1}L_{2}{\ddot {\theta }}_{1}\cos(\theta _{2}-\theta {1})+m{2}L_{1}L_{2}{\dot {\theta _{1}}}^{2}\sin(\theta _{2}-\theta {1})=-m{2}gL_{2}\sin \theta _{2}.}

The use of the generalized coordinates θi (i = 1, 2) provides an alternative to the Cartesian formulation of the dynamics of the double pendulum.

Spherical pendulum

For a 3D example, a spherical pendulum with constant length l free to swing in any angular direction subject to gravity, the constraint on the pendulum bob can be stated in the form

        f
        (

          r

        )

          x

            2

        +

          y

            2

        +

          z

            2

        −

          l

            2

        0

        ,

    {\displaystyle f(\mathbf {r} )=x^{2}+y^{2}+z^{2}-l^{2}=0\,,}

where the position of the pendulum bob can be written

          r

        (
        x
        (
        θ
        ,
        ϕ
        )
        ,
        y
        (
        θ
        ,
        ϕ
        )
        ,
        z
        (
        θ
        ,
        ϕ
        )
        )

        ,

    {\displaystyle \mathbf {r} =(x(\theta ,\phi ),y(\theta ,\phi ),z(\theta ,\phi ))\,,}

in which (θ, φ) are the spherical polar angles because the bob moves in the surface of a sphere. The position r is measured along the suspension point to the bob, here treated as a point particle. A logical choice of generalized coordinates to describe the motion are the angles (θ, φ). Only two coordinates are needed instead of three, because the position of the bob can be parameterized by two numbers, and the constraint equation connects the three coordinates (x, y, z) so any one of them is determined from the other two.

Generalized coordinates and virtual work
The principle of virtual work states that if a system is in static equilibrium, the virtual work of the applied forces is zero for all virtual movements of the system from this state, that is, δW = 0 for any variation δr. When formulated in terms of generalized coordinates, this is equivalent to the requirement that the generalized forces for any virtual displacement are zero, that is Fi = 0.
Let the forces on the system be Fj (j = 1, 2, …, m) be applied to points with Cartesian coordinates rj (j = 1, 2, …, m), then the virtual work generated by a virtual displacement from the equilibrium position is given by

        δ
        W

          ∑

            j

            1

            m

            F

            j

        ⋅
        δ

            r

            j

        .

    {\displaystyle \delta W=\sum _{j=1}^{m}\mathbf {F} _{j}\cdot \delta \mathbf {r} _{j}.}

where δrj (j = 1, 2, …, m) denote the virtual displacements of each point in the body.
Now assume that each δrj depends on the generalized coordinates qi (i = 1, 2, …, n) then

        δ

            r

            j

              ∂

                  r

                  j

              ∂

                q

                  1

        δ

            q

            1

        +
        …
        +

              ∂

                  r

                  j

              ∂

                q

                  n

        δ

            q

            n

        ,

    {\displaystyle \delta \mathbf {r} _{j}={\frac {\partial \mathbf {r} {j}}{\partial q{1}}}\delta {q}_{1}+\ldots +{\frac {\partial \mathbf {r} {j}}{\partial q{n}}}\delta {q}_{n},}

and

        δ
        W

          (

              ∑

                j

                1

                m

                F

                j

            ⋅

                  ∂

                      r

                      j

                  ∂

                    q

                      1

          )

        δ

            q

            1

        +
        …
        +

          (

              ∑

                j

                1

                m

                F

                j

            ⋅

                  ∂

                      r

                      j

                  ∂

                    q

                      n

          )

        δ

            q

            n

        .

    {\displaystyle \delta W=\left(\sum _{j=1}^{m}\mathbf {F} _{j}\cdot {\frac {\partial \mathbf {r} {j}}{\partial q{1}}}\right)\delta {q}_{1}+\ldots +\left(\sum _{j=1}^{m}\mathbf {F} _{j}\cdot {\frac {\partial \mathbf {r} {j}}{\partial q{n}}}\right)\delta {q}_{n}.}

The n terms

          F

            i

          ∑

            j

            1

            m

            F

            j

        ⋅

              ∂

                  r

                  j

              ∂

                q

                  i

        ,

        i

        1
        ,
        …
        ,
        n
        ,

    {\displaystyle F_{i}=\sum _{j=1}^{m}\mathbf {F} _{j}\cdot {\frac {\partial \mathbf {r} {j}}{\partial q{i}}},\quad i=1,\ldots ,n,}

are the generalized forces acting on the system. Kane shows that these generalized forces can also be formulated in terms of the ratio of time derivatives,

          F

            i

          ∑

            j

            1

            m

            F

            j

        ⋅

              ∂

                  v

                  j

              ∂

                      q
                      ˙

                  i

        ,

        i

        1
        ,
        …
        ,
        n
        ,

    {\displaystyle F_{i}=\sum _{j=1}^{m}\mathbf {F} _{j}\cdot {\frac {\partial \mathbf {v} {j}}{\partial {\dot {q}}{i}}},\quad i=1,\ldots ,n,}

where vj is the velocity of the point of application of the force Fj.
In order for the virtual work to be zero for an arbitrary virtual displacement, each of the generalized forces must be zero, that is

        δ
        W

        0

        ⇒

          F

            i

        0
        ,
        i

        1
        ,
        …
        ,
        n
        .

    {\displaystyle \delta W=0\quad \Rightarrow \quad F_{i}=0,i=1,\ldots ,n.}

Bibliography of cited references
Ginsberg, Jerry H. (2008). Engineering dynamics (3rd ed.). Cambridge UK: Cambridge University Press. ISBN 978-0-521-88303-0.
Goldstein, Herbert; Poole, Charles; Safko, John (2002). Classical Mechanics (3rd ed.). San Francisco, CA: Addison Wesley. ISBN 0-201-65702-3.
Hand, Louis N.; Finch, Janet D. (1998). Analytical mechanics. Cambridge: Cambridge University Press. ISBN 978-0521575720.
Kibble, T.W.B; Berkshire, F.H. (2004). Classical Mechanics (5th ed.). River Edge NJ: Imperial College Press. ISBN 1860944248.
Landau, L. D.; Lifshitz, E.M. (1976). Mechanics (Third ed.). Oxford. ISBN 978-0750628969.{{cite book}}: CS1 maint: location missing publisher (link)
Torby, Bruce (1984). "Energy Methods". Advanced Dynamics for Engineers. HRW Series in Mechanical Engineering. United States of America: CBS College Publishing. ISBN 0-03-063366-4.
