# Fradkin tensor

Fradkin tensor

The Fradkin tensor, or Jauch-Hill-Fradkin tensor, named after Josef-Maria Jauch and Edward Lee Hill and David M. Fradkin, is a conservation law used in the treatment of the isotropic multidimensional harmonic oscillator in classical mechanics. For the treatment of the quantum harmonic oscillator in quantum mechanics, it is replaced by the tensor-valued Fradkin operator.
The Fradkin tensor provides enough conserved quantities to make the oscillator's equations of motion maximally superintegrable. This implies that to determine the trajectory of the system, no differential equations need to be solved, only algebraic ones.
Similarly to the Laplace–Runge–Lenz vector in the Kepler problem, the Fradkin tensor arises from a hidden symmetry of the harmonic oscillator.

Definition
Suppose the Hamiltonian of a harmonic oscillator is given by

        H

                    p
                    →

                2

              2
              m

        +

            1
            2

        m

          ω

            2

                x
                →

            2

    {\displaystyle H={\frac {{\vec {p}}^{2}}{2m}}+{\frac {1}{2}}m\omega ^{2}{\vec {x}}^{2}}

with

momentum

              p
              →

    {\displaystyle {\vec {p}}}

,
mass

        m

    {\displaystyle m}

,
angular frequency

        ω

    {\displaystyle \omega }

, and
displacement

              x
              →

    {\displaystyle {\vec {x}}}

,
then the Fradkin tensor (up to an arbitrary normalisation) is defined as

          F

            i
            j

                p

                  i

                p

                  j

              2
              m

        +

            1
            2

        m

          ω

            2

          x

            i

          x

            j

        .

    {\displaystyle F_{ij}={\frac {p_{i}p_{j}}{2m}}+{\frac {1}{2}}m\omega ^{2}x_{i}x_{j}.}

In particular,

        H

    {\displaystyle H}

 is given by the trace:

        H

        Tr
        ⁡
        (
        F
        )

    {\displaystyle H=\operatorname {Tr} (F)}

. The Fradkin Tensor is a thus a symmetric matrix, and for an

        n

    {\displaystyle n}

-dimensional harmonic oscillator has

                n
                (
                n
                +
                1
                )

              2

        −
        1

    {\displaystyle {\tfrac {n(n+1)}{2}}-1}

 independent entries, for example 5 in 3 dimensions.

Properties
The Fradkin tensor is orthogonal to the angular momentum

              L
              →

              x
              →

        ×

              p
              →

    {\displaystyle {\vec {L}}={\vec {x}}\times {\vec {p}}}

:

          F

            i
            j

          L

            j

        0

    {\displaystyle F_{ij}L_{j}=0}

contracting the Fradkin tensor with the displacement vector gives the relationship

          x

            i

          F

            i
            j

          x

            j

        E

                x
                →

            2

        −

                    L
                    →

                2

              2
              m

    {\displaystyle x_{i}F_{ij}x_{j}=E{\vec {x}}^{2}-{\frac {{\vec {L}}^{2}}{2m}}}

.
The 5 independent components of the Fradkin tensor and the 3 components of angular momentum give the 8 generators of

        S
        U
        (
        3
        )

    {\displaystyle SU(3)}

, the three-dimensional special unitary group in 3 dimensions, with the relationships

                {

                  L

                    i

                ,

                  L

                    j

                }

                  ε

                    i
                    j
                    k

                  L

                    k

                {

                  L

                    i

                ,

                  F

                    j
                    k

                }

                  ε

                    i
                    j
                    n

                  F

                    n
                    k

                +

                  ε

                    i
                    k
                    n

                  F

                    j
                    n

                {

                  F

                    i
                    j

                ,

                  F

                    k
                    l

                }

                      ω

                        2

                    4

                  (

                      δ

                        i
                        k

                      ε

                        j
                        l
                        n

                    +

                      δ

                        i
                        l

                      ε

                        j
                        k
                        n

                    +

                      δ

                        j
                        k

                      ε

                        i
                        l
                        n

                    +

                      δ

                        j
                        l

                      ε

                        i
                        k
                        n

                  )

                  L

                    n

                ,

    {\displaystyle {\begin{aligned}{L_{i},L_{j}}&=\varepsilon {ijk}L{k}\{L_{i},F_{jk}}&=\varepsilon {ijn}F{nk}+\varepsilon {ikn}F{jn}\{F_{ij},F_{kl}}&={\frac {\omega ^{2}}{4}}\left(\delta _{ik}\varepsilon _{jln}+\delta _{il}\varepsilon _{jkn}+\delta _{jk}\varepsilon _{iln}+\delta _{jl}\varepsilon {ikn}\right)L{n}\,,\end{aligned}}}

where

        {
        ⋅
        ,
        ⋅
        }

    {\displaystyle {\cdot ,\cdot }}

 is the Poisson bracket,

        δ

    {\displaystyle \delta }

 is the Kronecker delta, and

        ε

    {\displaystyle \varepsilon }

 is the Levi-Civita symbol.

Proof of conservation
In Hamiltonian mechanics, the time evolution of any function

        A

    {\displaystyle A}

 defined on phase space is given by

                d

              A

                d

              t

        {
        A
        ,
        H
        }

          ∑

            k

          (

                  ∂
                  A

                  ∂

                    x

                      k

                  ∂
                  H

                  ∂

                    p

                      k

            −

                  ∂
                  A

                  ∂

                    p

                      k

                  ∂
                  H

                  ∂

                    x

                      k

          )

        +

              ∂
              A

              ∂
              t

    {\displaystyle {\frac {\mathrm {d} A}{\mathrm {d} t}}={A,H}=\sum {k}\left({\frac {\partial A}{\partial x{k}}}{\frac {\partial H}{\partial p_{k}}}-{\frac {\partial A}{\partial p_{k}}}{\frac {\partial H}{\partial x_{k}}}\right)+{\frac {\partial A}{\partial t}}}

,
so for the Fradkin tensor of the harmonic oscillator,

                d

                F

                  i
                  j

                d

              t

            1
            2

          ω

            2

          ∑

            k

            (

        (

          x

            j

          δ

            i
            k

        +

          x

            i

          δ

            j
            k

        )

          p

            k

        −
        (

          p

            j

          δ

            i
            k

        +

          p

            i

          δ

            j
            k

        )

          x

            k

            )

        0.

    {\displaystyle {\frac {\mathrm {d} F_{ij}}{\mathrm {d} t}}={\frac {1}{2}}\omega ^{2}\sum {k}{\Big (}(x{j}\delta {ik}+x{i}\delta {jk})p{k}-(p_{j}\delta {ik}+p{i}\delta {jk})x{k}{\Big )}=0.}

.
The Fradkin tensor is the conserved quantity associated to the transformation

          x

            i

        →

          x

            i

          ′

          x

            i

        +

            1
            2

          ω

            −
            1

          ε

            j
            k

          (

                    x
                    ˙

                j

              δ

                i
                k

            +

                    x
                    ˙

                k

              δ

                i
                j

          )

    {\displaystyle x_{i}\to x_{i}'=x_{i}+{\frac {1}{2}}\omega ^{-1}\varepsilon {jk}\left({\dot {x}}{j}\delta {ik}+{\dot {x}}{k}\delta _{ij}\right)}

by Noether's theorem.

Quantum mechanics
In quantum mechanics, position and momentum are replaced by the position- and momentum operators and the Poisson brackets by the commutator. As such the Hamiltonian becomes the Hamiltonian operator, angular momentum the angular momentum operator, and the Fradkin tensor the Fradkin operator. All of the above properties continue to hold after making these replacements.
