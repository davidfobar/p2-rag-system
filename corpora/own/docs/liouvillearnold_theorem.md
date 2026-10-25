# Liouville–Arnold theorem

Liouville–Arnold theorem

The Liouville–Arnold theorem is a result in classical mechanics which says, roughly speaking, that seemingly complicated systems can be described as combinations of simple systems if they satisfy certain conditions. The theorem is stated in the language of Hamiltonian mechanics, an approach to mechanics that focuses on the concept of energy. It is named after Joseph Liouville and Vladimir Arnold.

Background and overview
One of the simplest systems in mechanics is that of n independent ideal springs. This system belongs to a class of dynamical systems known as Hamiltonian, which means that the dynamics can be completely inferred from the total energy, which depends only on the position and momentum (of each spring). Independence of the springs is expressed mathematically using an algebraic construct known as the Poisson algebra, which is an algebra on all (smooth) functions of position and momentum, and in terms of which Hamilton's equations are formulated. The key ingredient is the Poisson bracket of two functions f and g, which produces another function denoted

        {
        f
        ,
        g
        }

    {\displaystyle {f,g}}

. This bracket is antisymmetric, like the familiar cross product from vector calculus, meaning that swapping the order of the arguments changes the sign of the result:

        {
        f
        ,
        g
        }

        −
        {
        g
        ,
        f
        }

    {\displaystyle {f,g}=-{g,f}}

. Two functions are said to Poisson-commute if

        {
        f
        ,
        g
        }

        0

    {\displaystyle {f,g}=0}

. Independence of the system of springs is formally the statement that the Hamiltonians (the energies) of each of the n springs Poisson-commute. Each Hamiltonian is known as a first integral of motion, meaning that it Poisson-commutes with the total energy governing the entire system. The Hamiltonian of the i-th spring is (kinetic + potential energy):

          H

            i

            1
            2

        (

          p

            i

            2

          /

          m

            i

        +

          k

            i

          x

            i

            2

        )

    {\displaystyle H_{i}={\frac {1}{2}}(p_{i}^{2}/m_{i}+k_{i}x_{i}^{2})}

 where

          k

            i

    {\displaystyle k_{i}}

 is the spring constant,

          m

            i

    {\displaystyle m_{i}}

 the mass,

          p

            i

    {\displaystyle p_{i}}

 is the momentum, and

          x

            i

    {\displaystyle x_{i}}

 the mass's displacement from equilibrium. The Hamiltonian of the full system is the sum of the Hamiltonians of the springs:

        H

          ∑

            i

            1

            n

          H

            i

    {\displaystyle H=\sum {i=1}^{n}H{i}}

, and the independence condition is

        {

          H

            i

        ,

          H

            j

        }

        0

    {\displaystyle {H_{i},H_{j}}=0}

. In the phase space

            R

            2
            n

    {\displaystyle \mathbb {R} ^{2n}}

, with coordinates

        (

          x

            1

        ,

          x

            2

        ,
        …
        ,

          x

            n

        ,

          p

            1

        ,

          p

            2

        ,
        …
        ,

          p

            n

        )

    {\displaystyle (x_{1},x_{2},\dots ,x_{n},p_{1},p_{2},\dots ,p_{n})}

, the (simultaneous) level surfaces of equal energy

          H

            i

          E

            i

    {\displaystyle H_{i}=E_{i}}

, with

          E

            i

    {\displaystyle E_{i}}

 constant, are tori. In particular, they are closed and bounded, i.e., compact.
The Liouville–Arnold theorem states that if, in a Hamiltonian system with n degrees of freedom (such as the n springs in the basic example), there are also n independent, Poisson commuting first integrals, and the (n-dimensional) simultaneous level sets of the first integrals are compact, then the dynamical system resolves completely into a system of n independent systems (such as the n independent harmonic oscillators in the example of the springs). More precisely, there exists a canonical transformation to action-angle coordinates in which the transformed Hamiltonian is dependent only upon the action coordinates and the angle coordinates evolve linearly in time. Thus the equations of motion for the system can be solved in quadratures if the level simultaneous set conditions can be separated.

History
The theorem was proven in its original form by Liouville in 1853 for functions on

            R

            2
            n

    {\displaystyle \mathbb {R} ^{2n}}

 with canonical symplectic structure. It was generalized to the setting of symplectic manifolds by Arnold, who gave a proof in his textbook Mathematical Methods of Classical Mechanics published in 1974.

Statement

Preliminary definitions
Let

        (

          M

            2
            n

        ,
        ω
        )

    {\displaystyle (M^{2n},\omega )}

 be a

        2
        n

    {\displaystyle 2n}

-dimensional symplectic manifold with symplectic structure

        ω

    {\displaystyle \omega }

.
An integrable system on

          M

            2
            n

    {\displaystyle M^{2n}}

 is a set of

        n

    {\displaystyle n}

 functions on

          M

            2
            n

    {\displaystyle M^{2n}}

, labelled

        F

        (

          F

            1

        ,
        ⋯
        ,

          F

            n

        )

    {\displaystyle F=(F_{1},\cdots ,F_{n})}

, satisfying

(Generic) linear independence:

        d

          F

            1

        ∧
        ⋯
        ∧
        d

          F

            n

        ≠
        0

    {\displaystyle dF_{1}\wedge \cdots \wedge dF_{n}\neq 0}

 on a dense set
Mutually Poisson commuting: the Poisson bracket

        {

          F

            i

        ,

          F

            j

        }

    {\displaystyle {F_{i},F_{j}}}

 vanishes for any pair of values

        i
        ,
        j

    {\displaystyle i,j}

.
The Poisson bracket

        {
        F
        ,
        G
        }

    {\displaystyle {F,G}}

 is the negative Hamiltonian function generating the Lie bracket of vector fields

        [

          X

            F

        ,

          X

            G

        ]

    {\displaystyle [X_{F},X_{G}]}

 of the Hamiltonian vector field corresponding to the two functions

        F
        ,
        G

    {\displaystyle F,G}

, but can easier be defined by evaluating the canonical 2-form

        ω

    {\displaystyle \omega }

 on the vector fields

          X

            F

        ,

          X

            G

    {\displaystyle X_{F},X_{G}}

.
In full, if

          X

            H

    {\displaystyle X_{H}}

 is the Hamiltonian vector field corresponding to a smooth function

        H
        :

          M

            2
            n

        →

          R

    {\displaystyle H:M^{2n}\rightarrow \mathbb {R} }

, then for two smooth functions

        F
        ,
        G

    {\displaystyle F,G}

, the Poisson bracket is

        {
        F
        ,
        G
        }
        :=
        ω
        (

          X

            F

        ,

          X

            G

        )

    {\displaystyle {F,G}:=\omega (X_{F},X_{G})}

 such that

          X

            {
            F
            ,
            G
            }

        −
        [

          X

            F

        ,

          X

            G

        ]
        .

    {\displaystyle X_{{F,G}}=-[X_{F},X_{G}].}

A point

        p

    {\displaystyle p}

 is a regular point if

        d

          F

            1

        ∧
        ⋯
        ∧
        d

          F

            n

        (
        p
        )
        ≠
        0

    {\displaystyle dF_{1}\wedge \cdots \wedge dF_{n}(p)\neq 0}

.
The integrable system defines a function

        F
        :

          M

            2
            n

        →

            R

            n

    {\displaystyle F:M^{2n}\rightarrow \mathbb {R} ^{n}}

. Denote by

          L

              c

    {\displaystyle L_{\mathbf {c} }}

 the level set of the functions

          F

            i

    {\displaystyle F_{i}}

,

          L

              c

        {
        x
        :

          F

            i

        (
        x
        )

          c

            i

        }
        ,

    {\displaystyle L_{\mathbf {c} }={x:F_{i}(x)=c_{i}},}

or alternatively,

          L

              c

          F

            −
            1

        (

          c

        )

    {\displaystyle L_{\mathbf {c} }=F^{-1}(\mathbf {c} )}

.
Now if

          M

            2
            n

    {\displaystyle M^{2n}}

 is given the additional structure of a distinguished function

        H

    {\displaystyle H}

, the Hamiltonian system

        (

          M

            2
            n

        ,
        ω
        ,
        H
        )

    {\displaystyle (M^{2n},\omega ,H)}

 is integrable if

        H

    {\displaystyle H}

 can be completed to an integrable system, that is, there exists an integrable system

        F

        (

          F

            1

        H
        ,

          F

            2

        ,
        ⋯
        ,

          F

            n

        )

    {\displaystyle F=(F_{1}=H,F_{2},\cdots ,F_{n})}

.

Theorem
If

        (

          M

            2
            n

        ,
        ω
        ,
        F
        )

    {\displaystyle (M^{2n},\omega ,F)}

 is an integrable Hamiltonian system, and

        p

    {\displaystyle p}

 is a regular point, the theorem characterizes the level set

          L

            c

    {\displaystyle L_{c}}

 of the image of the regular point

        c

        F
        (
        p
        )

    {\displaystyle c=F(p)}

:

          L

            c

    {\displaystyle L_{c}}

 is a smooth manifold which is invariant under the Hamiltonian flow induced by

        H

          F

            1

    {\displaystyle H=F_{1}}

 (and therefore under Hamiltonian flow induced by any element of the integrable system).
If

          L

            c

    {\displaystyle L_{c}}

 is furthermore compact and connected, it is diffeomorphic to the N-torus

            T

            n

    {\displaystyle \mathbb {T} ^{n}}

.
There exist (local) coordinates

        (

          θ

            1

        ,
        ⋯
        ,

          θ

            n

        ,

          ω

            1

        ,
        ⋯
        ,

          ω

            n

        )

    {\displaystyle (\theta _{1},\cdots ,\theta _{n},\omega _{1},\cdots ,\omega _{n})}

 on

          L

            c

    {\displaystyle L_{c}}

 such that the

          ω

            i

    {\displaystyle \omega _{i}}

 are constant on the level set while

                θ
                ˙

            i

        :=
        {

          θ

            i

        ,
        H
        }

          ω

            i

    {\displaystyle {\dot {\theta }}_{i}:={\theta _{i},H}=\omega _{i}}

. These coordinates are called action-angle coordinates.

Examples of Liouville-integrable systems
A Hamiltonian system which is integrable is referred to as 'integrable in the Liouville sense' or 'Liouville-integrable'. Famous examples are given in this section.
Some notation is standard in the literature. When the symplectic manifold under consideration is

            R

            2
            n

    {\displaystyle \mathbb {R} ^{2n}}

, its coordinates are often written

        (

          q

            1

        ,
        ⋯
        ,

          q

            n

        ,

          p

            1

        ,
        ⋯
        ,

          p

            n

        )

    {\displaystyle (q_{1},\cdots ,q_{n},p_{1},\cdots ,p_{n})}

 and the canonical symplectic form is

        ω

          ∑

            i

        d

          q

            i

        ∧
        d

          p

            i

    {\displaystyle \omega =\sum {i}dq{i}\wedge dp_{i}}

. Unless otherwise stated, these are assumed for this section.

Harmonic oscillator:

        (

            R

            2
            n

        ,
        ω
        ,
        H
        )

    {\displaystyle (\mathbb {R} ^{2n},\omega ,H)}

 with

        H
        (

          q

        ,

          p

        )

          ∑

            i

          (

                  p

                    i

                    2

                  2
                  m

            +

                1
                2

            m

              ω

                i

                2

              q

                i

                2

          )

    {\displaystyle H(\mathbf {q} ,\mathbf {p} )=\sum {i}\left({\frac {p{i}^{2}}{2m}}+{\frac {1}{2}}m\omega {i}^{2}q{i}^{2}\right)}

. Defining

          H

            i

              p

                i

                2

              2
              m

        +

            1
            2

        m

          ω

            i

            2

          q

            i

            2

    {\displaystyle H_{i}={\frac {p_{i}^{2}}{2m}}+{\frac {1}{2}}m\omega {i}^{2}q{i}^{2}}

, the integrable system is

        (
        H
        ,

          H

            1

        ,
        ⋯
        ,

          H

            n
            −
            1

        )

    {\displaystyle (H,H_{1},\cdots ,H_{n-1})}

.
Central force system:

        (

            R

            6

        ,
        ω
        ,
        H
        )

    {\displaystyle (\mathbb {R} ^{6},\omega ,H)}

 with

        H
        (

          q

        ,

          p

        )

                p

                2

              2
              m

        −
        U
        (

            q

            2

        )

    {\displaystyle H(\mathbf {q} ,\mathbf {p} )={\frac {\mathbf {p} ^{2}}{2m}}-U(\mathbf {q} ^{2})}

 with

        U

    {\displaystyle U}

 some potential function. Defining the angular momentum

          L

          p

        ×

          q

    {\displaystyle \mathbf {L} =\mathbf {p} \times \mathbf {q} }

, the integrable system is

        (
        H
        ,

            L

            2

        ,

          L

            3

        )

    {\displaystyle (H,\mathbf {L} ^{2},L_{3})}

.
Integrable tops: The Lagrange, Euler and Kovalevskaya tops are integrable in the Liouville sense.
