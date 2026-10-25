# Control volume

Control volume

In continuum mechanics and thermodynamics, a control volume (CV) is a mathematical abstraction employed in the process of creating mathematical models of physical processes. In an inertial frame of reference, it is a fictitious region of a given volume fixed in space or moving with constant flow velocity through which the continuuum (a continuous medium such as gas, liquid or solid) flows. The closed surface enclosing the region is referred to as the control surface.
At steady state, a control volume can be thought of as an arbitrary volume in which the mass of the continuum remains constant. As a continuum moves through the control volume, the mass entering the control volume is equal to the mass leaving the control volume. At steady state, and in the absence of work and heat transfer, the energy within the control volume remains constant. It is analogous to the classical mechanics concept of the free body diagram.

Overview
Typically, to understand how a given physical law applies to the system under consideration, one first begins by considering how it applies to a small, control volume, or "representative volume". There is nothing special about a particular control volume, it simply represents a small part of the system to which physical laws can be easily applied. This gives rise to what is termed a volumetric, or volume-wise formulation of the mathematical model.
One can then argue that since the physical laws behave in a certain way on a particular control volume, they behave the same way on all such volumes, since that particular control volume was not special in any way. In this way, the corresponding point-wise formulation of the mathematical model can be developed so it can describe the physical behaviour of an entire (and maybe more complex) system.
In continuum mechanics the conservation equations (for instance, the Navier-Stokes equations) are in integral form. They therefore apply on volumes. Finding forms of the equation that are independent of the control volumes allows simplification of the integral signs. The control volumes can be stationary or they can move with an arbitrary velocity.

Substantive derivative

Computations in continuum mechanics often require that the regular time derivation operator

        d

          /

        d
        t

    {\displaystyle d/dt\;}

is replaced by the substantive derivative operator

        D

          /

        D
        t

    {\displaystyle D/Dt}

.
This can be seen as follows.
Consider a bug that is moving through a volume where there is some scalar,
e.g. pressure, that varies with time and position:

        p

        p
        (
        t
        ,
        x
        ,
        y
        ,
        z
        )

    {\displaystyle p=p(t,x,y,z)\;}

.
If the bug during the time interval from

        t

    {\displaystyle t\;}

to

        t
        +
        d
        t

    {\displaystyle t+dt\;}

moves from

        (
        x
        ,
        y
        ,
        z
        )

    {\displaystyle (x,y,z)\;}

to

        (
        x
        +
        d
        x
        ,
        y
        +
        d
        y
        ,
        z
        +
        d
        z
        )
        ,

    {\displaystyle (x+dx,y+dy,z+dz),\;}

then the bug experiences a change

        d
        p

    {\displaystyle dp\;}

 in the scalar value,

        d
        p

              ∂
              p

              ∂
              t

        d
        t
        +

              ∂
              p

              ∂
              x

        d
        x
        +

              ∂
              p

              ∂
              y

        d
        y
        +

              ∂
              p

              ∂
              z

        d
        z

    {\displaystyle dp={\frac {\partial p}{\partial t}}dt+{\frac {\partial p}{\partial x}}dx+{\frac {\partial p}{\partial y}}dy+{\frac {\partial p}{\partial z}}dz}

(the total differential). If the bug is moving with a velocity

          v

        (

          v

            x

        ,

          v

            y

        ,

          v

            z

        )
        ,

    {\displaystyle \mathbf {v} =(v_{x},v_{y},v_{z}),}

the change in particle position is

          v

        d
        t

        (

          v

            x

        d
        t
        ,

          v

            y

        d
        t
        ,

          v

            z

        d
        t
        )
        ,

    {\displaystyle \mathbf {v} dt=(v_{x}dt,v_{y}dt,v_{z}dt),}

and we may write

                d
                p

                      ∂
                      p

                      ∂
                      t

                d
                t
                +

                      ∂
                      p

                      ∂
                      x

                  v

                    x

                d
                t
                +

                      ∂
                      p

                      ∂
                      y

                  v

                    y

                d
                t
                +

                      ∂
                      p

                      ∂
                      z

                  v

                    z

                d
                t

                  (

                          ∂
                          p

                          ∂
                          t

                    +

                          ∂
                          p

                          ∂
                          x

                      v

                        x

                    +

                          ∂
                          p

                          ∂
                          y

                      v

                        y

                    +

                          ∂
                          p

                          ∂
                          z

                      v

                        z

                  )

                d
                t

                  (

                          ∂
                          p

                          ∂
                          t

                    +

                      v

                    ⋅
                    ∇
                    p

                  )

                d
                t
                .

    {\displaystyle {\begin{alignedat}{2}dp&={\frac {\partial p}{\partial t}}dt+{\frac {\partial p}{\partial x}}v_{x}dt+{\frac {\partial p}{\partial y}}v_{y}dt+{\frac {\partial p}{\partial z}}v_{z}dt\&=\left({\frac {\partial p}{\partial t}}+{\frac {\partial p}{\partial x}}v_{x}+{\frac {\partial p}{\partial y}}v_{y}+{\frac {\partial p}{\partial z}}v_{z}\right)dt\&=\left({\frac {\partial p}{\partial t}}+\mathbf {v} \cdot \nabla p\right)dt.\\end{alignedat}}}

where

        ∇
        p

    {\displaystyle \nabla p}

 is the gradient of the scalar field p. So:

            d

              d
              t

            ∂

              ∂
              t

        +

          v

        ⋅
        ∇
        .

    {\displaystyle {\frac {d}{dt}}={\frac {\partial }{\partial t}}+\mathbf {v} \cdot \nabla .}

If the bug is just moving with the flow, the same formula applies, but now the velocity vector,v, is that of the flow, u.
The last parenthesized expression is the substantive derivative of the scalar pressure.
Since the pressure p in this computation is an arbitrary scalar field, we may abstract it and write the substantive derivative operator as

            D

              D
              t

            ∂

              ∂
              t

        +

          u

        ⋅
        ∇
        .

    {\displaystyle {\frac {D}{Dt}}={\frac {\partial }{\partial t}}+\mathbf {u} \cdot \nabla .}
