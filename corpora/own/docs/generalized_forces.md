# Generalized forces

Generalized forces

In analytical mechanics (particularly Lagrangian mechanics), generalized forces are conjugate to generalized coordinates. They are obtained from the applied forces Fi, i = 1, …, n, acting on a system that has its configuration defined in terms of generalized coordinates. In the formulation of virtual work, each generalized force is the coefficient of the variation of a generalized coordinate.

Virtual work
Generalized forces can be obtained from the computation of the virtual work, δW, of the applied forces.
The virtual work of the forces, Fi, acting on the particles Pi, i = 1, ..., n, is given by

        δ
        W

          ∑

            i

            1

            n

            F

            i

        ⋅
        δ

            r

            i

    {\displaystyle \delta W=\sum _{i=1}^{n}\mathbf {F} _{i}\cdot \delta \mathbf {r} _{i}}

where δri is the virtual displacement of the particle Pi.

Generalized coordinates
Let the position vectors of each of the particles, ri, be a function of the generalized coordinates, qj, j = 1, ..., m. Then the virtual displacements δri are given by

        δ

            r

            i

          ∑

            j

            1

            m

              ∂

                  r

                  i

              ∂

                q

                  j

        δ

          q

            j

        ,

        i

        1
        ,
        …
        ,
        n
        ,

    {\displaystyle \delta \mathbf {r} _{i}=\sum _{j=1}^{m}{\frac {\partial \mathbf {r} {i}}{\partial q{j}}}\delta q_{j},\quad i=1,\ldots ,n,}

where δqj is the virtual displacement of the generalized coordinate qj.
The virtual work for the system of particles becomes

        δ
        W

            F

            1

        ⋅

          ∑

            j

            1

            m

              ∂

                  r

                  1

              ∂

                q

                  j

        δ

          q

            j

        +
        ⋯
        +

            F

            n

        ⋅

          ∑

            j

            1

            m

              ∂

                  r

                  n

              ∂

                q

                  j

        δ

          q

            j

        .

    {\displaystyle \delta W=\mathbf {F} _{1}\cdot \sum _{j=1}^{m}{\frac {\partial \mathbf {r} {1}}{\partial q{j}}}\delta q_{j}+\dots +\mathbf {F} _{n}\cdot \sum _{j=1}^{m}{\frac {\partial \mathbf {r} {n}}{\partial q{j}}}\delta q_{j}.}

Collect the coefficients of δqj so that

        δ
        W

          ∑

            i

            1

            n

            F

            i

        ⋅

              ∂

                  r

                  i

              ∂

                q

                  1

        δ

          q

            1

        +
        ⋯
        +

          ∑

            i

            1

            n

            F

            i

        ⋅

              ∂

                  r

                  i

              ∂

                q

                  m

        δ

          q

            m

        .

    {\displaystyle \delta W=\sum _{i=1}^{n}\mathbf {F} _{i}\cdot {\frac {\partial \mathbf {r} {i}}{\partial q{1}}}\delta q_{1}+\dots +\sum _{i=1}^{n}\mathbf {F} _{i}\cdot {\frac {\partial \mathbf {r} {i}}{\partial q{m}}}\delta q_{m}.}

Generalized forces
The virtual work of a system of particles can be written in the form

        δ
        W

          Q

            1

        δ

          q

            1

        +
        ⋯
        +

          Q

            m

        δ

          q

            m

        ,

    {\displaystyle \delta W=Q_{1}\delta q_{1}+\dots +Q_{m}\delta q_{m},}

where

          Q

            j

          ∑

            i

            1

            n

            F

            i

        ⋅

              ∂

                  r

                  i

              ∂

                q

                  j

        ,

        j

        1
        ,
        …
        ,
        m
        ,

    {\displaystyle Q_{j}=\sum _{i=1}^{n}\mathbf {F} _{i}\cdot {\frac {\partial \mathbf {r} {i}}{\partial q{j}}},\quad j=1,\ldots ,m,}

are called the generalized forces associated with the generalized coordinates qj, j = 1, ..., m.

Velocity formulation
In the application of the principle of virtual work it is often convenient to obtain virtual displacements from the velocities of the system. For the n particle system, let the velocity of each particle Pi be Vi, then the virtual displacement δri can also be written in the form

        δ

            r

            i

          ∑

            j

            1

            m

              ∂

                  V

                  i

              ∂

                      q
                      ˙

                  j

        δ

          q

            j

        ,

        i

        1
        ,
        …
        ,
        n
        .

    {\displaystyle \delta \mathbf {r} _{i}=\sum _{j=1}^{m}{\frac {\partial \mathbf {V} {i}}{\partial {\dot {q}}{j}}}\delta q_{j},\quad i=1,\ldots ,n.}

This means that the generalized force, Qj, can also be determined as

          Q

            j

          ∑

            i

            1

            n

            F

            i

        ⋅

              ∂

                  V

                  i

              ∂

                      q
                      ˙

                  j

        ,

        j

        1
        ,
        …
        ,
        m
        .

    {\displaystyle Q_{j}=\sum _{i=1}^{n}\mathbf {F} _{i}\cdot {\frac {\partial \mathbf {V} {i}}{\partial {\dot {q}}{j}}},\quad j=1,\ldots ,m.}

D'Alembert's principle
D'Alembert formulated the dynamics of a particle as the equilibrium of the applied forces with an inertia force (apparent force), called D'Alembert's principle. The inertia force of a particle, Pi, of mass mi is

            F

            i

            ∗

        −

          m

            i

            A

            i

        ,

        i

        1
        ,
        …
        ,
        n
        ,

    {\displaystyle \mathbf {F} {i}^{*}=-m{i}\mathbf {A} _{i},\quad i=1,\ldots ,n,}

where Ai is the acceleration of the particle.
If the configuration of the particle system depends on the generalized coordinates qj, j = 1, ..., m, then the generalized inertia force is given by

          Q

            j

            ∗

          ∑

            i

            1

            n

            F

            i

            ∗

        ⋅

              ∂

                  V

                  i

              ∂

                      q
                      ˙

                  j

        ,

        j

        1
        ,
        …
        ,
        m
        .

    {\displaystyle Q_{j}^{}=\sum _{i=1}^{n}\mathbf {F} _{i}^{}\cdot {\frac {\partial \mathbf {V} {i}}{\partial {\dot {q}}{j}}},\quad j=1,\ldots ,m.}

D'Alembert's form of the principle of virtual work yields

        δ
        W

        (

          Q

            1

        +

          Q

            1

            ∗

        )
        δ

          q

            1

        +
        ⋯
        +
        (

          Q

            m

        +

          Q

            m

            ∗

        )
        δ

          q

            m

        .

    {\displaystyle \delta W=(Q_{1}+Q_{1}^{})\delta q_{1}+\dots +(Q_{m}+Q_{m}^{})\delta q_{m}.}
