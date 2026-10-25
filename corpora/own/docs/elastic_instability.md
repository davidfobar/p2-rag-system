# Elastic instability

Elastic instability

Elastic instability is a form of instability occurring in elastic systems, such as buckling of beams and plates subject to large compressive loads.
There are a lot of ways to study this kind of instability. One of them is to use the method of incremental deformations based on superposing a small perturbation on an equilibrium solution.

Single degree of freedom-systems
Consider as a simple example a rigid beam of length L, hinged in one end and free in the other, and having an angular spring attached to the hinged end. The beam is loaded in the free end by a force F acting in the compressive axial direction of the beam, see the figure to the right.

Moment equilibrium condition
Assuming a clockwise angular deflection

        θ

    {\displaystyle \theta }

, the clockwise moment exerted by the force becomes

          M

            F

        F
        L
        sin
        ⁡
        θ

    {\displaystyle M_{F}=FL\sin \theta }

. The moment equilibrium equation is given by

        F
        L
        sin
        ⁡
        θ

          k

            θ

        θ

    {\displaystyle FL\sin \theta =k_{\theta }\theta }

where

          k

            θ

    {\displaystyle k_{\theta }}

 is the spring constant of the angular spring (Nm/radian). Assuming

        θ

    {\displaystyle \theta }

 is small enough, implementing the Taylor expansion of the sine function and keeping the two first terms yields

        F
        L

            (

        θ
        −

            1
            6

          θ

            3

            )

        ≈

          k

            θ

        θ

    {\displaystyle FL{\Bigg (}\theta -{\frac {1}{6}}\theta ^{3}{\Bigg )}\approx k_{\theta }\theta }

which has three solutions, the trivial

        θ

        0

    {\displaystyle \theta =0}

, and

        θ
        ≈
        ±

            6

                (

            1
            −

                  k

                    θ

                  F
                  L

                )

    {\displaystyle \theta \approx \pm {\sqrt {6{\Bigg (}1-{\frac {k_{\theta }}{FL}}{\Bigg )}}}}

which is imaginary (i.e. not physical) for

        F
        L
        <

          k

            θ

    {\displaystyle FL<k_{\theta }}

 and real otherwise. This implies that for small compressive forces, the only equilibrium state is given by

        θ

        0

    {\displaystyle \theta =0}

, while if the force exceeds the value

          k

            θ

          /

        L

    {\displaystyle k_{\theta }/L}

 there is suddenly another mode of deformation possible.

Energy method
The same result can be obtained by considering energy relations. The energy stored in the angular spring is

          E

              s
              p
              r
              i
              n
              g

        ∫

          k

            θ

        θ

          d

        θ

            1
            2

          k

            θ

          θ

            2

    {\displaystyle E_{\mathrm {spring} }=\int k_{\theta }\theta \mathrm {d} \theta ={\frac {1}{2}}k_{\theta }\theta ^{2}}

and the work done by the force is simply the force multiplied by the vertical displacement of the beam end, which is

        L
        (
        1
        −
        cos
        ⁡
        θ
        )

    {\displaystyle L(1-\cos \theta )}

. Thus,

          E

              f
              o
              r
              c
              e

        ∫

          F

            d

          x

          F
          L
          (
          1
          −
          cos
          ⁡
          θ
          )

    {\displaystyle E_{\mathrm {force} }=\int {F\mathrm {d} x=FL(1-\cos \theta )}}

The energy equilibrium condition

          E

              s
              p
              r
              i
              n
              g

          E

              f
              o
              r
              c
              e

    {\displaystyle E_{\mathrm {spring} }=E_{\mathrm {force} }}

 now yields

        F

          k

            θ

          /

        L

    {\displaystyle F=k_{\theta }/L}

 as before (besides from the trivial

        θ

        0

    {\displaystyle \theta =0}

).

Stability of the solutions
Any solution

        θ

    {\displaystyle \theta }

 is stable iff a small change in the deformation angle

        Δ
        θ

    {\displaystyle \Delta \theta }

 results in a reaction moment trying to restore the original angle of deformation. The net clockwise moment acting on the beam is

        M
        (
        θ
        )

        F
        L
        sin
        ⁡
        θ
        −

          k

            θ

        θ

    {\displaystyle M(\theta )=FL\sin \theta -k_{\theta }\theta }

An infinitesimal clockwise change of the deformation angle

        θ

    {\displaystyle \theta }

 results in a moment

        M
        (
        θ
        +
        Δ
        θ
        )

        M
        +
        Δ
        M

        F
        L
        (
        sin
        ⁡
        θ
        +
        Δ
        θ
        cos
        ⁡
        θ
        )
        −

          k

            θ

        (
        θ
        +
        Δ
        θ
        )

    {\displaystyle M(\theta +\Delta \theta )=M+\Delta M=FL(\sin \theta +\Delta \theta \cos \theta )-k_{\theta }(\theta +\Delta \theta )}

which can be rewritten as

        Δ
        M

        Δ
        θ
        (
        F
        L
        cos
        ⁡
        θ
        −

          k

            θ

        )

    {\displaystyle \Delta M=\Delta \theta (FL\cos \theta -k_{\theta })}

since

        F
        L
        sin
        ⁡
        θ

          k

            θ

        θ

    {\displaystyle FL\sin \theta =k_{\theta }\theta }

 due to the moment equilibrium condition. Now, a solution

        θ

    {\displaystyle \theta }

 is stable iff a clockwise change

        Δ
        θ

        0

    {\displaystyle \Delta \theta >0}

 results in a negative change of moment

        Δ
        M
        <
        0

    {\displaystyle \Delta M<0}

 and vice versa. Thus, the condition for stability becomes

              Δ
              M

              Δ
              θ

                d

              M

                d

              θ

        F
        L
        cos
        ⁡
        θ
        −

          k

            θ

        <
        0

    {\displaystyle {\frac {\Delta M}{\Delta \theta }}={\frac {\mathrm {d} M}{\mathrm {d} \theta }}=FL\cos \theta -k_{\theta }<0}

The solution

        θ

        0

    {\displaystyle \theta =0}

 is stable only for

        F
        L
        <

          k

            θ

    {\displaystyle FL<k_{\theta }}

, which is expected. By expanding the cosine term in the equation, the approximate stability condition is obtained:

        θ

            2

                (

            1
            −

                  k

                    θ

                  F
                  L

                )

    {\displaystyle |\theta |>{\sqrt {2{\Bigg (}1-{\frac {k_{\theta }}{FL}}{\Bigg )}}}}

for

        F
        L

          k

            θ

    {\displaystyle FL>k_{\theta }}

, which the two other solutions satisfy. Hence, these solutions are stable.

Multiple degrees of freedom-systems

By attaching another rigid beam to the original system by means of an angular spring a two degrees of freedom-system is obtained. Assume for simplicity that the beam lengths and angular springs are equal. The equilibrium conditions become

        F
        L
        (
        sin
        ⁡

          θ

            1

        +
        sin
        ⁡

          θ

            2

        )

          k

            θ

          θ

            1

    {\displaystyle FL(\sin \theta _{1}+\sin \theta {2})=k{\theta }\theta _{1}}

        F
        L
        sin
        ⁡

          θ

            2

          k

            θ

        (

          θ

            2

        −

          θ

            1

        )

    {\displaystyle FL\sin \theta {2}=k{\theta }(\theta _{2}-\theta _{1})}

where

          θ

            1

    {\displaystyle \theta _{1}}

 and

          θ

            2

    {\displaystyle \theta _{2}}

 are the angles of the two beams. Linearizing by assuming these angles are small yields

            (

                  F
                  L
                  −

                    k

                      θ

                  F
                  L

                    k

                      θ

                  F
                  L
                  −

                    k

                      θ

            )

            (

                    θ

                      1

                    θ

                      2

            )

            (

                  0

                  0

            )

    {\displaystyle {\begin{pmatrix}FL-k_{\theta }&FL\k_{\theta }&FL-k_{\theta }\end{pmatrix}}{\begin{pmatrix}\theta _{1}\\theta _{2}\end{pmatrix}}={\begin{pmatrix}0\0\end{pmatrix}}}

The non-trivial solutions to the system is obtained by finding the roots of the determinant of the system matrix, i.e. for

              F
              L

              k

                θ

            3
            2

        ∓

              5

            2

        ≈

          {

                  0.382

                  2.618

    {\displaystyle {\frac {FL}{k_{\theta }}}={\frac {3}{2}}\mp {\frac {\sqrt {5}}{2}}\approx \left{{\begin{matrix}0.382\2.618\end{matrix}}\right.}

Thus, for the two degrees of freedom-system there are two critical values for the applied force F. These correspond to two different modes of deformation which can be computed from the nullspace of the system matrix. Dividing the equations by

          θ

            1

    {\displaystyle \theta _{1}}

 yields

              θ

                2

              θ

                1

              θ

                1

            ≠
            0

              k

                θ

              F
              L

        −
        1
        ≈

          {

                  1.618

                    for

                  F
                  L

                    /

                    k

                      θ

                  ≈
                  0.382

                  −
                  0.618

                    for

                  F
                  L

                    /

                    k

                      θ

                  ≈
                  2.618

    {\displaystyle {\frac {\theta _{2}}{\theta {1}}}{\Big |}{\theta {1}\neq 0}={\frac {k{\theta }}{FL}}-1\approx \left{{\begin{matrix}1.618&{\text{for }}FL/k_{\theta }\approx 0.382\-0.618&{\text{for }}FL/k_{\theta }\approx 2.618\end{matrix}}\right.}

For the lower critical force the ratio is positive and the two beams deflect in the same direction while for the higher force they form a "banana" shape. These two states of deformation represent the buckling mode shapes of the system.
