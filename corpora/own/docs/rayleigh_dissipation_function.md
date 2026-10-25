# Rayleigh dissipation function

Rayleigh dissipation function

In physics, the Rayleigh dissipation function, named after Lord Rayleigh, is a function used to handle the effects of velocity-proportional frictional forces in Lagrangian mechanics.
It was first introduced by him in 1873.
If the frictional force on a particle with velocity

              v
              →

    {\displaystyle {\vec {v}}}

 can be written as

                F
                →

            f

        −
        k

              v
              →

    {\displaystyle {\vec {F}}_{f}=-k{\vec {v}}}

, where

        k

    {\displaystyle k}

 is a diagonal matrix, then the Rayleigh dissipation function can be defined for a system of

        N

    {\displaystyle N}

 particles as

        R
        (
        v
        )

            1
            2

          ∑

            i

            1

            N

        (

          k

            x

          v

            i
            ,
            x

            2

        +

          k

            y

          v

            i
            ,
            y

            2

        +

          k

            z

          v

            i
            ,
            z

            2

        )
        .

    {\displaystyle R(v)={\frac {1}{2}}\sum {i=1}^{N}(k{x}v_{i,x}^{2}+k_{y}v_{i,y}^{2}+k_{z}v_{i,z}^{2}).}

This function represents half of the rate of energy dissipation of the system through friction. The force of friction is negative the velocity gradient of the dissipation function,

                F
                →

            f

        −

          ∇

            v

        R
        (
        v
        )

    {\displaystyle {\vec {F}}_{f}=-\nabla _{v}R(v)}

, analogous to a force being equal to the negative position gradient of a potential. This relationship is represented in terms of the set of generalized coordinates

          q

            i

          {

              q

                1

            ,

              q

                2

            ,
            …

              q

                n

          }

    {\displaystyle q_{i}=\left{q_{1},q_{2},\ldots q_{n}\right}}

 as

          F

            f
            ,
            i

        −

              ∂
              R

              ∂

                      q
                      ˙

                  i

    {\displaystyle F_{f,i}=-{\frac {\partial R}{\partial {\dot {q}}_{i}}}}

.
As friction is not conservative, it is included in the

          Q

            i

    {\displaystyle Q_{i}}

 term of Lagrange's equations,

            d

              d
              t

              ∂
              L

              ∂

                      q

                        i

                    ˙

        −

              ∂
              L

              ∂

                q

                  i

          Q

            i

    {\displaystyle {\frac {d}{dt}}{\frac {\partial L}{\partial {\dot {q_{i}}}}}-{\frac {\partial L}{\partial q_{i}}}=Q_{i}}

.
Applying of the value of the frictional force described by generalized coordinates into the Euler-Lagrange equations gives

            d

              d
              t

          (

                ∂
                L

                ∂

                        q

                          i

                      ˙

          )

        −

              ∂
              L

              ∂

                q

                  i

        −

              ∂
              R

              ∂

                      q
                      ˙

                  i

    {\displaystyle {\frac {d}{dt}}\left({\frac {\partial L}{\partial {\dot {q_{i}}}}}\right)-{\frac {\partial L}{\partial q_{i}}}=-{\frac {\partial R}{\partial {\dot {q}}_{i}}}}

.
Rayleigh writes the Lagrangian

        L

    {\displaystyle L}

 as kinetic energy

        T

    {\displaystyle T}

 minus potential energy

        V

    {\displaystyle V}

, which yields Rayleigh's equation from 1873.

            d

              d
              t

          (

                ∂
                T

                ∂

                        q

                          i

                      ˙

          )

        −

              ∂
              T

              ∂

                q

                  i

        +

              ∂
              R

              ∂

                      q
                      ˙

                  i

        +

              ∂
              V

              ∂

                q

                  i

        0

    {\displaystyle {\frac {d}{dt}}\left({\frac {\partial T}{\partial {\dot {q_{i}}}}}\right)-{\frac {\partial T}{\partial q_{i}}}+{\frac {\partial R}{\partial {\dot {q}}{i}}}+{\frac {\partial V}{\partial q{i}}}=0}

.
Since the 1970s the name Rayleigh dissipation potential for

        R

    {\displaystyle R}

 is more common. Moreover, the original theory is generalized from quadratic functions

        q
        ↦
        R
        (

              q
              ˙

        )

            1
            2

              q
              ˙

        ⋅

          V

              q
              ˙

    {\displaystyle q\mapsto R({\dot {q}})={\frac {1}{2}}{\dot {q}}\cdot \mathbb {V} {\dot {q}}}

 to
dissipation potentials that are depending on

        q

    {\displaystyle q}

 (then called state dependence) and are non-quadratic, which leads to nonlinear friction laws like in Coulomb friction or in plasticity. The main assumption is then, that the mapping

              q
              ˙

        ↦
        R
        (
        q
        ,

              q
              ˙

        )

    {\displaystyle {\dot {q}}\mapsto R(q,{\dot {q}})}

 is convex and satisfies

        0

        R
        (
        q
        ,
        0
        )
        ≤
        R
        (
        q
        ,

              q
              ˙

        )

    {\displaystyle 0=R(q,0)\leq R(q,{\dot {q}})}

.
