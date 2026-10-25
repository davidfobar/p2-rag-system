# Engquist–Majda absorbing boundary condition

Engquist–Majda absorbing boundary condition

In numerical methods for partial differential equations, Engquist–Majda absorbing boundary conditions or Lindman–Engquist–Majda absorbing boundary conditions are a hierarchy of absorbing boundary conditions for the numerical solution of wave equations. Named after mathematicians Björn Engquist and Andrew Majda, they are designed to allow waves to exit a finite computational domain with minimal artificial reflection through the use of one-way wave equations, essentially making the boundaries transparent to outgoing radiation. Within the context of computational electromagnetics, they are known as Mur absorbing boundary condition after Gerrit Mur, who introduced a discretized version of the boundary conditions for finite-difference time-domain method in 1981.

Theory
A simple form of Engquist–Majda absorbing boundary condition can be formulated through one-dimensional scalar wave equation:

          (

              L

                x

                2

            −

              v

                −
                2

              L

                t

                2

          )

        U
        (
        x
        ,
        t
        )

        G
        U
        (
        x
        ,
        t
        )

        0

    {\displaystyle \left(L_{x}^{2}-v^{-2}L_{t}^{2}\right)U(x,t)=GU(x,t)=0}

where

          L

            {
            x
            ,
            t
            }

          ∂

            {
            x
            ,
            t
            }

    {\displaystyle L_{{x,t}}=\partial _{{x,t}}}

 are the partial differential operators and

        v

    {\displaystyle v}

 is the wave velocity;

        G

    {\displaystyle G}

 is the resultant wave function operator. This operator can be split into two one-way wave operators, resulting in advection equations:

        G
        U
        (
        x
        ,
        t
        )

          G

            +

          G

            −

        U
        (
        x
        ,
        t
        )

        0

    {\displaystyle GU(x,t)=G^{+}G^{-}U(x,t)=0}

          G

            +

          L

            x

        +

          v

            −
            1

          L

            t

    {\displaystyle G^{+}=L_{x}+v^{-1}L_{t}}

          G

            −

          L

            x

        −

          v

            −
            1

          L

            t

    {\displaystyle G^{-}=L_{x}-v^{-1}L_{t}}

Applying the following boundary conditions at a simulation region from

        x

        0

    {\displaystyle x=0}

 to

        x

        L

    {\displaystyle x=L}

 results in the cancellation of outgoing waves:

          G

            +

        U
        (
        x
        ,
        t
        )

            x

            0

          (

              L

                x

            +

              v

                −
                1

              L

                t

          )

        U
        (
        x
        ,
        t
        )

            x

            0

        0

    {\displaystyle G^{+}U(x,t)|{x=0}=\left(L{x}+v^{-1}L_{t}\right)U(x,t)|_{x=0}=0}

          G

            −

        U
        (
        x
        ,
        t
        )

            x

            L

          (

              L

                x

            −

              v

                −
                1

              L

                t

          )

        U
        (
        x
        ,
        t
        )

            x

            L

        0

    {\displaystyle G^{-}U(x,t)|{x=L}=\left(L{x}-v^{-1}L_{t}\right)U(x,t)|_{x=L}=0}

In the case of higher dimensions, i.e. the two-dimensional scalar wave equation, the operator form can be written as:

          (

              L

                x

                2

            +

              L

                y

                2

            −

              v

                −
                2

              L

                t

                2

          )

        U
        (
        x
        ,
        y
        ,
        t
        )

          G

            +

          G

            −

        U
        (
        x
        ,
        y
        ,
        t
        )

        0

    {\displaystyle \left(L_{x}^{2}+L_{y}^{2}-v^{-2}L_{t}^{2}\right)U(x,y,t)=G^{+}G^{-}U(x,y,t)=0}

For waves traveling along the

        x

    {\displaystyle x}

-axis, the operator splitting results in:

          G

            +

        U
        (
        x
        ,
        y
        ,
        t
        )

            x

            0

          (

              L

                x

            +

              v

                −
                1

              L

                t

                1
                −

                  v

                    2

                      L

                        y

                        2

                      L

                        t

                        2

          )

        U
        (
        x
        ,
        t
        )

            x

            0

        0

    {\displaystyle G^{+}U(x,y,t)|{x=0}=\left(L{x}+v^{-1}L_{t}{\sqrt {1-v^{2}{\frac {L_{y}^{2}}{L_{t}^{2}}}}}\right)U(x,t)|_{x=0}=0}

          G

            −

        U
        (
        x
        ,
        y
        ,
        t
        )

            x

            L

          (

              L

                x

            −

              v

                −
                1

              L

                t

                1
                −

                  v

                    2

                      L

                        y

                        2

                      L

                        t

                        2

          )

        U
        (
        x
        ,
        t
        )

            x

            L

        0

    {\displaystyle G^{-}U(x,y,t)|{x=L}=\left(L{x}-v^{-1}L_{t}{\sqrt {1-v^{2}{\frac {L_{y}^{2}}{L_{t}^{2}}}}}\right)U(x,t)|_{x=L}=0}

The terms in square brackets constitute pseudo-differential operators and their theoretical exact forms are nonlocal. In practice, they can be locally approximated with their Taylor series representations. First-order approximation

        (

            1
            −

              s

                2

        ≈
        1
        )

    {\displaystyle ({\sqrt {1-s^{2}}}\approx 1)}

 yields:

          G

            +

        ≈

          L

            x

        +

          v

            −
            1

          L

            t

    {\displaystyle G^{+}\approx L_{x}+v^{-1}L_{t}}

          G

            −

        ≈

          L

            x

        −

          v

            −
            1

          L

            t

    {\displaystyle G^{-}\approx L_{x}-v^{-1}L_{t}}

which is equivalent to the Engquist–Majda condition for one-dimensional wave equation: in the theoretical limit, it perfectly absorbs the normally incident waves while causing reflections for waves impinging on other angles. A second-order approximation

        (

            1
            −

              s

                2

        ≈
        1
        −

          s

            2

          /

        2
        )

    {\displaystyle ({\sqrt {1-s^{2}}}\approx 1-s^{2}/2)}

 yields a better performance:

          G

            +

        ≈

          L

            x

        +

          v

            −
            1

          L

            t

          [

            1
            −

              v

                2

                  L

                    y

                    2

                  2

                    L

                      t

                      2

          ]

          L

            x

        +

          v

            −
            1

          L

            t

        −

                v

                  2

                L

                  y

                  2

              2

                L

                  t

                  2

    {\displaystyle G^{+}\approx L_{x}+v^{-1}L_{t}\left[1-v^{2}{\frac {L_{y}^{2}}{2L_{t}^{2}}}\right]=L_{x}+v^{-1}L_{t}-{\frac {v^{2}L_{y}^{2}}{2L_{t}^{2}}}}

          G

            −

        ≈

          L

            x

        −

          v

            −
            1

          L

            t

          [

            1
            −

              v

                2

                  L

                    y

                    2

                  2

                    L

                      t

                      2

          ]

          L

            x

        −

          v

            −
            1

          L

            t

        +

                v

                  2

                L

                  y

                  2

              2

                L

                  t

                  2

    {\displaystyle G^{-}\approx L_{x}-v^{-1}L_{t}\left[1-v^{2}{\frac {L_{y}^{2}}{2L_{t}^{2}}}\right]=L_{x}-v^{-1}L_{t}+{\frac {v^{2}L_{y}^{2}}{2L_{t}^{2}}}}

Higher-order boundary conditions can also be obtained through Padé or Chebyshev approximation of the pseudo-differential operators; these are known as generalized Trefethen–Halpern absorbing boundary conditions.

History and applications
Engquist and Majda's seminal paper on the absorbing boundary conditions was published in 1977. An earlier form of the absorbing boundary conditions was previously reported in 1973 by physicist and Los Alamos National Laboratory staff member Erick L. Lindman, who first suggested the use of one-way equations to construct absorbing boundaries. Since their introduction, Engquist–Majda absorbing boundary conditions have been applied to numerical solutions of various different problems in areas ranging from acoustics to seismology, particularly within finite difference and finite element formulations. In computational electromagnetics, they are known as Mur boundary conditions, named after Gerrit Mur's extension of the Engquist–Majda operators to the finite-difference time-domain method (FDTD). While Mur boundary condition enjoyed popularity in the FDTD applications for a decade following its introduction, it was subsequently superseded by more efficient perfectly matched layers and more accurate exact absorbing conditions in the 1990s.
Engquist–Majda absorbing boundary conditions, alongside the Dirac equation, were instrumental in the development of an exact one-way wave equation in 2025.
