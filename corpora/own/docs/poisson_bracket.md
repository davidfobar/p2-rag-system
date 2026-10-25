# Poisson bracket

Poisson bracket

In mathematics and classical mechanics, the Poisson bracket is an important binary operation in Hamiltonian mechanics, playing a central role in Hamilton's equations of motion, which govern the time evolution of a Hamiltonian dynamical system. The Poisson bracket also distinguishes a certain class of coordinate transformations, called canonical transformations, which map canonical coordinate systems into other canonical coordinate systems. A "canonical coordinate system" consists of canonical position and momentum variables (below symbolized by

          q

            i

    {\displaystyle q_{i}}

 and

          p

            i

    {\displaystyle p_{i}}

, respectively) that satisfy canonical Poisson bracket relations. The set of possible canonical transformations is always very rich. For instance, it is often possible to choose the Hamiltonian itself

            H

            H

        (
        q
        ,
        p
        ,
        t
        )

    {\displaystyle {\mathcal {H}}={\mathcal {H}}(q,p,t)}

 as one of the new canonical momentum coordinates.
In a more general sense, the Poisson bracket is used to define a Poisson algebra, of which the algebra of functions on a Poisson manifold is a special case. There are other general examples, as well: it occurs in the theory of Lie algebras, where the tensor algebra of a Lie algebra forms a Poisson algebra; a detailed construction of how this comes about is given in the universal enveloping algebra article. Quantum deformations of the universal enveloping algebra lead to the notion of quantum groups.
All of these objects are named in honor of French mathematician Siméon Denis Poisson. He introduced the Poisson bracket in his 1809 treatise on mechanics.

Definition
Let

        V

    {\displaystyle V}

 be an associative algebra over the real numbers. A Poisson bracket is a function

        {
        ⋅
        ,
        ⋅
        }
        :
        V
        ×
        V
        →
        V

    {\displaystyle {\cdot ,\cdot }:V\times V\to V}

 that satisfies the following conditions:

Anticommutativity

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

Bilinearity

        {
        a
        f
        +
        b
        g
        ,
        h
        }

        a
        {
        f
        ,
        h
        }
        +
        b
        {
        g
        ,
        h
        }
        ,

    {\displaystyle {af+bg,h}=a{f,h}+b{g,h},}

        {
        h
        ,
        a
        f
        +
        b
        g
        }

        a
        {
        h
        ,
        f
        }
        +
        b
        {
        h
        ,
        g
        }
        ,

        a
        ,
        b
        ∈

          R

    {\displaystyle {h,af+bg}=a{h,f}+b{h,g},\quad a,b\in \mathbb {R} }

Leibniz's rule

        {
        f
        g
        ,
        h
        }

        {
        f
        ,
        h
        }
        g
        +
        f
        {
        g
        ,
        h
        }

    {\displaystyle {fg,h}={f,h}g+f{g,h}}

Jacobi identity

        {
        f
        ,
        {
        g
        ,
        h
        }
        }
        +
        {
        g
        ,
        {
        h
        ,
        f
        }
        }
        +
        {
        h
        ,
        {
        f
        ,
        g
        }
        }

        0

    {\displaystyle {f,{g,h}}+{g,{h,f}}+{h,{f,g}}=0}

If

        V

    {\displaystyle V}

 is a set of smooth functions defined on the extended phase space, it is sometimes assumed that

        {
        f
        ,

        k
        }

        0

    {\displaystyle {f,\,k}=0}

 for any

        f

    {\displaystyle f}

, as long as

        k

    {\displaystyle k}

 does not depend on coordinates other than time.

Canonical Poisson bracket in coordinates
In canonical coordinates (also known as Darboux coordinates)

        (
        q
        ,
        p
        ,
        t
        )

        (

          q

            1

        ,
        .
        .
        .
        ,

          q

            N

        ,

          p

            1

        ,
        .
        .
        .
        ,

          p

            N

        ,
        t
        )

    {\displaystyle (q,p,t)=(q_{1},...,q_{N},p_{1},...,p_{N},t)}

 on the (extended) phase space, given two functions

        f
        (
        q
        ,
        p
        ,
        t
        )

    {\displaystyle f(q,p,t)}

 and

        g
        (
        q
        ,
        p
        ,
        t
        )

    {\displaystyle g(q,p,t)}

, the (canonical) Poisson bracket takes the form

        {
        f
        ,
        g
        }

          ∑

            i

            1

            N

          (

                  ∂
                  f

                  ∂

                    q

                      i

                  ∂
                  g

                  ∂

                    p

                      i

            −

                  ∂
                  f

                  ∂

                    p

                      i

                  ∂
                  g

                  ∂

                    q

                      i

          )

        .

    {\displaystyle {f,g}=\sum {i=1}^{N}\left({\frac {\partial f}{\partial q{i}}}{\frac {\partial g}{\partial p_{i}}}-{\frac {\partial f}{\partial p_{i}}}{\frac {\partial g}{\partial q_{i}}}\right).}

The Poisson brackets of the canonical coordinates are

                {

                  q

                    k

                ,

                  q

                    l

                }

                  ∑

                    i

                    1

                    N

                  (

                          ∂

                            q

                              k

                          ∂

                            q

                              i

                          ∂

                            q

                              l

                          ∂

                            p

                              i

                    −

                          ∂

                            q

                              k

                          ∂

                            p

                              i

                          ∂

                            q

                              l

                          ∂

                            q

                              i

                  )

                  ∑

                    i

                    1

                    N

                  (

                      δ

                        k
                        i

                    ⋅
                    0
                    −
                    0
                    ⋅

                      δ

                        l
                        i

                  )

                0
                ,

                {

                  p

                    k

                ,

                  p

                    l

                }

                  ∑

                    i

                    1

                    N

                  (

                          ∂

                            p

                              k

                          ∂

                            q

                              i

                          ∂

                            p

                              l

                          ∂

                            p

                              i

                    −

                          ∂

                            p

                              k

                          ∂

                            p

                              i

                          ∂

                            p

                              l

                          ∂

                            q

                              i

                  )

                  ∑

                    i

                    1

                    N

                  (

                    0
                    ⋅

                      δ

                        l
                        i

                    −

                      δ

                        k
                        i

                    ⋅
                    0

                  )

                0
                ,

                {

                  q

                    k

                ,

                  p

                    l

                }

                  ∑

                    i

                    1

                    N

                  (

                          ∂

                            q

                              k

                          ∂

                            q

                              i

                          ∂

                            p

                              l

                          ∂

                            p

                              i

                    −

                          ∂

                            q

                              k

                          ∂

                            p

                              i

                          ∂

                            p

                              l

                          ∂

                            q

                              i

                  )

                  ∑

                    i

                    1

                    N

                  (

                      δ

                        k
                        i

                    ⋅

                      δ

                        l
                        i

                    −
                    0
                    ⋅
                    0

                  )

                  δ

                    k
                    l

                ,

    {\displaystyle {\begin{aligned}{q_{k},q_{l}}&=\sum {i=1}^{N}\left({\frac {\partial q{k}}{\partial q_{i}}}{\frac {\partial q_{l}}{\partial p_{i}}}-{\frac {\partial q_{k}}{\partial p_{i}}}{\frac {\partial q_{l}}{\partial q_{i}}}\right)=\sum _{i=1}^{N}\left(\delta _{ki}\cdot 0-0\cdot \delta {li}\right)=0,\{p{k},p_{l}}&=\sum {i=1}^{N}\left({\frac {\partial p{k}}{\partial q_{i}}}{\frac {\partial p_{l}}{\partial p_{i}}}-{\frac {\partial p_{k}}{\partial p_{i}}}{\frac {\partial p_{l}}{\partial q_{i}}}\right)=\sum _{i=1}^{N}\left(0\cdot \delta _{li}-\delta {ki}\cdot 0\right)=0,\{q{k},p_{l}}&=\sum {i=1}^{N}\left({\frac {\partial q{k}}{\partial q_{i}}}{\frac {\partial p_{l}}{\partial p_{i}}}-{\frac {\partial q_{k}}{\partial p_{i}}}{\frac {\partial p_{l}}{\partial q_{i}}}\right)=\sum _{i=1}^{N}\left(\delta _{ki}\cdot \delta _{li}-0\cdot 0\right)=\delta _{kl},\end{aligned}}}

where

          δ

            i
            j

    {\displaystyle \delta _{ij}}

 is the Kronecker delta.

Hamilton's equations of motion
Hamilton's equations of motion in canonical coordinates may be expressed in terms of the (canonical) Poisson bracket as follows:

                      d

                        q

                          i

                      d
                      t

                      ∂

                          H

                      ∂

                        p

                          i

                {

                  q

                    i

                ,

                    H

                }
                ,

                      d

                        p

                          i

                      d
                      t

                −

                      ∂

                          H

                      ∂

                        q

                          i

                {

                  p

                    i

                ,

                    H

                }
                .

    {\displaystyle {\begin{aligned}{\frac {dq_{i}}{dt}}&={\frac {\partial {\mathcal {H}}}{\partial p_{i}}}={q_{i},{\mathcal {H}}},\{\frac {dp_{i}}{dt}}&=-{\frac {\partial {\mathcal {H}}}{\partial q_{i}}}={p_{i},{\mathcal {H}}}.\end{aligned}}}

Suppose that

        f

        f
        (
        q
        ,
        p
        ,
        t
        )

    {\displaystyle f=f(q,p,t)}

 and let

        q
        (
        t
        )
        ,
        p
        (
        t
        )

    {\displaystyle q(t),p(t)}

 be the solutions to Hamilton's equations;. Then from the multivariable chain rule,

                    d

                      d
                      t

                f
                (
                q
                (
                t
                )
                ,
                p
                (
                t
                )
                ,
                t
                )

                      ∂
                      f

                      ∂
                      t

                +

                  ∑

                    i

                    1

                    N

                      ∂
                      f

                      ∂

                        q

                          i

                      d

                        q

                          i

                      d
                      t

                +

                      ∂
                      f

                      ∂

                        p

                          i

                      d

                        p

                          i

                      d
                      t

                      ∂
                      f

                      ∂
                      t

                +

                  ∑

                    i

                    1

                    N

                      ∂
                      f

                      ∂

                        q

                          i

                      ∂

                          H

                      ∂

                        p

                          i

                −

                      ∂
                      f

                      ∂

                        p

                          i

                      ∂

                          H

                      ∂

                        q

                          i

                      ∂
                      f

                      ∂
                      t

                +
                {
                f
                ,

                    H

                }

                .

    {\displaystyle {\begin{aligned}{\frac {d}{dt}}f(q(t),p(t),t)&={\frac {\partial f}{\partial t}}+\sum {i=1}^{N}{\frac {\partial f}{\partial q{i}}}{\frac {dq_{i}}{dt}}+{\frac {\partial f}{\partial p_{i}}}{\frac {dp_{i}}{dt}}\&={\frac {\partial f}{\partial t}}+\sum {i=1}^{N}{\frac {\partial f}{\partial q{i}}}{\frac {\partial {\mathcal {H}}}{\partial p_{i}}}-{\frac {\partial f}{\partial p_{i}}}{\frac {\partial {\mathcal {H}}}{\partial q_{i}}}\&={\frac {\partial f}{\partial t}}+{f,{\mathcal {H}}}~.\end{aligned}}}

In particular,

        u

        u
        (
        q
        ,
        p
        ,
        t
        )

    {\displaystyle u=u(q,p,t)}

 is a constant of motion if and only if

              ∂
              u

              ∂
              t

        {

            H

        ,
        u
        }

    {\displaystyle {\frac {\partial u}{\partial t}}={{\mathcal {H}},u}}

and the time evolution of a function

        f

    {\displaystyle f}

 on a symplectic manifold can be given as a one-parameter family of symplectomorphisms (i.e., canonical transformations, area-preserving diffeomorphisms), with the time

        t

    {\displaystyle t}

 being the parameter: Hamiltonian motion is a canonical transformation generated by the Hamiltonian. That is, Poisson brackets are preserved in it, so that any time

        t

    {\displaystyle t}

 in the solution to Hamilton's equations,

        q
        (
        t
        )

        exp
        ⁡
        (
        −
        t
        {

            H

        ,
        ⋅
        }
        )
        q
        (
        0
        )
        ,

        p
        (
        t
        )

        exp
        ⁡
        (
        −
        t
        {

            H

        ,
        ⋅
        }
        )
        p
        (
        0
        )
        ,

    {\displaystyle q(t)=\exp(-t{{\mathcal {H}},\cdot })q(0),\quad p(t)=\exp(-t{{\mathcal {H}},\cdot })p(0),}

can serve as the bracket coordinates. Poisson brackets are canonical invariants.
Dropping the coordinates,

            d

              d
              t

        f

          (

                ∂

                  ∂
                  t

            −
            {

                H

            ,
            ⋅
            }

          )

        f
        .

    {\displaystyle {\frac {d}{dt}}f=\left({\frac {\partial }{\partial t}}-{{\mathcal {H}},\cdot }\right)f.}

The operator in the convective part of the derivative,

        i

              L
              ^

        −
        {

            H

        ,
        ⋅
        }

    {\displaystyle i{\hat {L}}=-{{\mathcal {H}},\cdot }}

, is sometimes referred to as the Liouvillian (see Liouville's theorem (Hamiltonian)).

Poisson matrix in canonical transformations

The concept of Poisson brackets can be expanded to that of matrices by defining the Poisson matrix.
Consider the following canonical transformation:

        η

            [

                    q

                      1

                  ⋮

                    q

                      N

                    p

                      1

                  ⋮

                    p

                      N

            ]

        →

        ε

            [

                    Q

                      1

                  ⋮

                    Q

                      N

                    P

                      1

                  ⋮

                    P

                      N

            ]

    {\displaystyle \eta ={\begin{bmatrix}q_{1}\\vdots \q_{N}\p_{1}\\vdots \p_{N}\\end{bmatrix}}\quad \rightarrow \quad \varepsilon ={\begin{bmatrix}Q_{1}\\vdots \Q_{N}\P_{1}\\vdots \P_{N}\\end{bmatrix}}}

Defining

        M
        :=

              ∂
              (

                Q

              ,

                P

              )

              ∂
              (

                q

              ,

                p

              )

    {\textstyle M:={\frac {\partial (\mathbf {Q} ,\mathbf {P} )}{\partial (\mathbf {q} ,\mathbf {p} )}}}

, the Poisson matrix is defined as

            P

        (
        ε
        )

        M
        J

          M

            T

    {\textstyle {\mathcal {P}}(\varepsilon )=MJM^{T}}

, where

        J

    {\displaystyle J}

 is the symplectic matrix under the same conventions used to order the set of coordinates. It follows from the definition that:

              P

            i
            j

        (
        ε
        )

        [
        M
        J

          M

            T

          ]

            i
            j

          ∑

            k

            1

            N

          (

                  ∂

                    ε

                      i

                  ∂

                    η

                      k

                  ∂

                    ε

                      j

                  ∂

                    η

                      N
                      +
                      k

            −

                  ∂

                    ε

                      i

                  ∂

                    η

                      N
                      +
                      k

                  ∂

                    ε

                      j

                  ∂

                    η

                      k

          )

          ∑

            k

            1

            N

          (

                  ∂

                    ε

                      i

                  ∂

                    q

                      k

                  ∂

                    ε

                      j

                  ∂

                    p

                      k

            −

                  ∂

                    ε

                      i

                  ∂

                    p

                      k

                  ∂

                    ε

                      j

                  ∂

                    q

                      k

          )

        {

          ε

            i

        ,

          ε

            j

          }

            η

        .

    {\displaystyle {\mathcal {P}}{ij}(\varepsilon )=[MJM^{T}]{ij}=\sum _{k=1}^{N}\left({\frac {\partial \varepsilon _{i}}{\partial \eta _{k}}}{\frac {\partial \varepsilon _{j}}{\partial \eta _{N+k}}}-{\frac {\partial \varepsilon _{i}}{\partial \eta _{N+k}}}{\frac {\partial \varepsilon _{j}}{\partial \eta _{k}}}\right)=\sum _{k=1}^{N}\left({\frac {\partial \varepsilon {i}}{\partial q{k}}}{\frac {\partial \varepsilon {j}}{\partial p{k}}}-{\frac {\partial \varepsilon {i}}{\partial p{k}}}{\frac {\partial \varepsilon {j}}{\partial q{k}}}\right)={\varepsilon _{i},\varepsilon {j}}{\eta }.}

The Poisson matrix satisfies the following known properties:

                      P

                    T

                −

                    P

                    P

                    1

                      M

                          2

                      P

                    −
                    1

                (
                ε
                )

                −
                (

                  M

                    −
                    1

                  )

                    T

                J

                  M

                    −
                    1

                −

                    L

                (
                ε
                )

    {\displaystyle {\begin{aligned}{\mathcal {P}}^{T}&=-{\mathcal {P}}\|{\mathcal {P}}|&={\frac {1}{|M|^{2}}}\{\mathcal {P}}^{-1}(\varepsilon )&=-(M^{-1})^{T}JM^{-1}=-{\mathcal {L}}(\varepsilon )\\end{aligned}}}

where the

            L

        (
        ε
        )

    {\textstyle {\mathcal {L}}(\varepsilon )}

 is known as a Lagrange matrix and whose elements correspond to Lagrange brackets. The last identity can also be stated as the following:

          ∑

            k

            1

            2
            N

        {

          η

            i

        ,

          η

            k

        }
        [

          η

            k

        ,

          η

            j

        ]

        −

          δ

            i
            j

    {\displaystyle \sum _{k=1}^{2N}{\eta _{i},\eta _{k}}[\eta _{k},\eta _{j}]=-\delta _{ij}}

Note that the summation here involves generalized coordinates as well as generalized momentum.
The invariance of Poisson bracket can be expressed as:

        {

          ε

            i

        ,

          ε

            j

          }

            η

        {

          ε

            i

        ,

          ε

            j

          }

            ε

          J

            i
            j

    {\textstyle {\varepsilon _{i},\varepsilon {j}}{\eta }={\varepsilon _{i},\varepsilon {j}}{\varepsilon }=J_{ij}}

, which directly leads to the symplectic condition:

        M
        J

          M

            T

        J

    {\textstyle MJM^{T}=J}

.

Constants of motion
An integrable system will have constants of motion in addition to the energy. Such constants of motion will commute with the Hamiltonian under the Poisson bracket. Suppose some function

        f
        (
        p
        ,
        q
        )

    {\displaystyle f(p,q)}

 is a constant of motion. This implies that if

        p
        (
        t
        )
        ,
        q
        (
        t
        )

    {\displaystyle p(t),q(t)}

 is a trajectory or solution to Hamilton's equations of motion, then along that trajectory:

        0

              d
              f

              d
              t

    {\displaystyle 0={\frac {df}{dt}}}

Where, as above, the intermediate step follows by applying the equations of motion and we assume that

        f

    {\displaystyle f}

 does not explicitly depend on time. This equation is known as the Liouville equation. The content of Liouville's theorem is that the time evolution of a measure given by a distribution function

        f

    {\displaystyle f}

 is given by the above equation.
If the Poisson bracket of

        f

    {\displaystyle f}

 and

        g

    {\displaystyle g}

 vanishes (

        {
        f
        ,
        g
        }

        0

    {\displaystyle {f,g}=0}

), then

        f

    {\displaystyle f}

 and

        g

    {\displaystyle g}

 are said to be in involution. In order for a Hamiltonian system to be completely integrable,

        n

    {\displaystyle n}

 independent constants of motion must be in mutual involution, where

        n

    {\displaystyle n}

 is the number of degrees of freedom.
Furthermore, according to Poisson's Theorem, if two quantities

        A

    {\displaystyle A}

 and

        B

    {\displaystyle B}

 are explicitly time independent (

        A
        (
        p
        ,
        q
        )
        ,
        B
        (
        p
        ,
        q
        )

    {\displaystyle A(p,q),B(p,q)}

) constants of motion, so is their Poisson bracket

        {
        A
        ,

        B
        }

    {\displaystyle {A,\,B}}

. This follows from the Jacobi identity (see section below). Poisson's Theorem does not always supply a useful result, however, since the number of possible constants of motion is limited (

        2
        n
        −
        1

    {\displaystyle 2n-1}

 for a system with

        n

    {\displaystyle n}

 degrees of freedom), and so the result may be trivial (a constant, or a function of

        A

    {\displaystyle A}

 and

        B

    {\displaystyle B}

.)

The Poisson bracket in coordinate-free language
Let

        M

    {\displaystyle M}

 be a symplectic manifold, that is, a manifold equipped with a symplectic form: a 2-form

        ω

    {\displaystyle \omega }

 which is both closed (i.e., its exterior derivative

        d
        ω

    {\displaystyle d\omega }

 vanishes) and non-degenerate. For example, in the treatment above, take

        M

    {\displaystyle M}

 to be

            R

            2
            n

    {\displaystyle \mathbb {R} ^{2n}}

 and take

        ω

          ∑

            i

            1

            n

        d

          q

            i

        ∧
        d

          p

            i

        .

    {\displaystyle \omega =\sum {i=1}^{n}dq{i}\wedge dp_{i}.}

If

          ι

            v

        ω

    {\displaystyle \iota _{v}\omega }

 is the interior product or contraction operation defined by

        (

          ι

            v

        ω
        )
        (
        u
        )

        ω
        (
        v
        ,

        u
        )

    {\displaystyle (\iota _{v}\omega )(u)=\omega (v,\,u)}

, then non-degeneracy is equivalent to saying that for every one-form

        α

    {\displaystyle \alpha }

 there is a unique vector field

          Ω

            α

    {\displaystyle \Omega _{\alpha }}

 such that

          ι

              Ω

                α

        ω

        α

    {\displaystyle \iota _{\Omega _{\alpha }}\omega =\alpha }

. Alternatively,

          Ω

            d
            H

          ω

            −
            1

        (
        d
        H
        )

    {\displaystyle \Omega _{dH}=\omega ^{-1}(dH)}

. Then if

        H

    {\displaystyle H}

 is a smooth function on

        M

    {\displaystyle M}

, the Hamiltonian vector field

          X

            H

    {\displaystyle X_{H}}

 can be defined to be

          Ω

            d
            H

    {\displaystyle \Omega _{dH}}

. It is easy to see that

                  X

                      p

                        i

                    ∂

                      ∂

                        q

                          i

                  X

                      q

                        i

                −

                    ∂

                      ∂

                        p

                          i

                .

    {\displaystyle {\begin{aligned}X_{p_{i}}&={\frac {\partial }{\partial q_{i}}}\X_{q_{i}}&=-{\frac {\partial }{\partial p_{i}}}.\end{aligned}}}

The Poisson bracket

        {
        ⋅
        ,

        ⋅
        }

    {\displaystyle \ {\cdot ,\,\cdot }}

 on (M, ω) is a bilinear operation on differentiable functions, defined by

        {
        f
        ,

        g
        }

        ω
        (

          X

            f

        ,

          X

            g

        )

    {\displaystyle {f,\,g}\;=\;\omega (X_{f},\,X_{g})}

; the Poisson bracket of two functions on M is itself a function on M. The Poisson bracket is antisymmetric because:

        {
        f
        ,
        g
        }

        ω
        (

          X

            f

        ,

          X

            g

        )

        −
        ω
        (

          X

            g

        ,

          X

            f

        )

        −
        {
        g
        ,
        f
        }
        .

    {\displaystyle {f,g}=\omega (X_{f},X_{g})=-\omega (X_{g},X_{f})=-{g,f}.}

Furthermore,

Here Xgf denotes the vector field Xg applied to the function f as a directional derivative, and

              L

              X

                g

        f

    {\displaystyle {\mathcal {L}}{X{g}}f}

 denotes the (entirely equivalent) Lie derivative of the function f.
If α is an arbitrary one-form on M, the vector field Ωα generates (at least locally) a flow

          ϕ

            x

        (
        t
        )

    {\displaystyle \phi _{x}(t)}

 satisfying the boundary condition

          ϕ

            x

        (
        0
        )

        x

    {\displaystyle \phi _{x}(0)=x}

 and the first-order differential equation

              d

                ϕ

                  x

              d
              t

              Ω

                α

              ϕ

                x

            (
            t
            )

        .

    {\displaystyle {\frac {d\phi _{x}}{dt}}=\left.\Omega {\alpha }\right|{\phi _{x}(t)}.}

The

          ϕ

            x

        (
        t
        )

    {\displaystyle \phi _{x}(t)}

 will be symplectomorphisms (canonical transformations) for every t as a function of x if and only if

              L

              Ω

                α

        ω

        0

    {\displaystyle {\mathcal {L}}_{\Omega _{\alpha }}\omega \;=\;0}

; when this is true, Ωα is called a symplectic vector field. Recalling Cartan's identity

              L

            X

        ω

        d
        (

          ι

            X

        ω
        )

        +

          ι

            X

        d
        ω

    {\displaystyle {\mathcal {L}}_{X}\omega \;=\;d(\iota _{X}\omega )\,+\,\iota _{X}d\omega }

 and dω = 0, it follows that

              L

              Ω

                α

        ω

        d

          (

              ι

                  Ω

                    α

            ω

          )

        d
        α

    {\displaystyle {\mathcal {L}}_{\Omega _{\alpha }}\omega \;=\;d\left(\iota _{\Omega _{\alpha }}\omega \right)\;=\;d\alpha }

. Therefore, Ωα is a symplectic vector field if and only if α is a closed form. Since

        d
        (
        d
        f
        )

          d

            2

        f

        0

    {\displaystyle d(df)\;=\;d^{2}f\;=\;0}

, it follows that every Hamiltonian vector field Xf is a symplectic vector field, and that the Hamiltonian flow consists of canonical transformations. From (1) above, under the Hamiltonian flow

          X

              H

    {\displaystyle X_{\mathcal {H}}}

,

            d

              d
              t

        f
        (

          ϕ

            x

        (
        t
        )
        )

          X

              H

        f

        {
        f
        ,

            H

        }
        .

    {\displaystyle {\frac {d}{dt}}f(\phi {x}(t))=X{\mathcal {H}}f={f,{\mathcal {H}}}.}

This is a fundamental result in Hamiltonian mechanics, governing the time evolution of functions defined on phase space. As noted above, when

        {
        f
        ,

            H

        }

        0

    {\displaystyle {f,{\mathcal {H}}}=0}

, f is a constant of motion of the system. In addition, in canonical coordinates (with

        {

          p

            i

        ,

          p

            j

        }

        {

          q

            i

        ,

          q

            j

        }

        0

    {\displaystyle {p_{i},\,p_{j}}\;=\;{q_{i},q_{j}}\;=\;0}

 and

        {

          q

            i

        ,

          p

            j

        }

          δ

            i
            j

    {\displaystyle {q_{i},\,p_{j}}\;=\;\delta _{ij}}

), Hamilton's equations for the time evolution of the system follow immediately from this formula.
It also follows from (1) that the Poisson bracket is a derivation; that is, it satisfies a non-commutative version of Leibniz's product rule:

The Poisson bracket is intimately connected to the Lie bracket of the Hamiltonian vector fields. Because the Lie derivative is a derivation,

              L

            v

          ι

            u

        ω

          ι

                  L

                v

            u

        ω
        +

          ι

            u

              L

            v

        ω

          ι

            [
            v
            ,
            u
            ]

        ω
        +

          ι

            u

              L

            v

        ω
        .

    {\displaystyle {\mathcal {L}}_{v}\iota _{u}\omega =\iota {{\mathcal {L}}{v}u}\omega +\iota {u}{\mathcal {L}}{v}\omega =\iota _{[v,u]}\omega +\iota {u}{\mathcal {L}}{v}\omega .}

Thus if v and u are symplectic, using

              L

            v

        ω

        0

              L

            u

        ω

    {\displaystyle {\mathcal {L}}{v}\omega =0={\mathcal {L}}{u}\omega }

, Cartan's identity, and the fact that

          ι

            u

        ω

    {\displaystyle \iota _{u}\omega }

 is a closed form,

          ι

            [
            v
            ,
            u
            ]

        ω

              L

            v

          ι

            u

        ω

        d
        (

          ι

            v

          ι

            u

        ω
        )
        +

          ι

            v

        d
        (

          ι

            u

        ω
        )

        d
        (

          ι

            v

          ι

            u

        ω
        )

        d
        (
        ω
        (
        u
        ,
        v
        )
        )
        .

    {\displaystyle \iota {[v,u]}\omega ={\mathcal {L}}{v}\iota _{u}\omega =d(\iota _{v}\iota _{u}\omega )+\iota _{v}d(\iota _{u}\omega )=d(\iota _{v}\iota _{u}\omega )=d(\omega (u,v)).}

It follows that

        [
        v
        ,
        u
        ]

          X

            ω
            (
            u
            ,
            v
            )

    {\displaystyle [v,u]=X_{\omega (u,v)}}

, so that

Thus, the Poisson bracket on functions corresponds to the Lie bracket of the associated Hamiltonian vector fields. We have also shown that the Lie bracket of two symplectic vector fields is a Hamiltonian vector field and hence is also symplectic. In the language of abstract algebra, the symplectic vector fields form a subalgebra of the Lie algebra of smooth vector fields on M, and the Hamiltonian vector fields form an ideal of this subalgebra. The symplectic vector fields are the Lie algebra of the (infinite-dimensional) Lie group of symplectomorphisms of M.
It is widely asserted that the Jacobi identity for the Poisson bracket,

        {
        f
        ,
        {
        g
        ,
        h
        }
        }
        +
        {
        g
        ,
        {
        h
        ,
        f
        }
        }
        +
        {
        h
        ,
        {
        f
        ,
        g
        }
        }

        0

    {\displaystyle {f,{g,h}}+{g,{h,f}}+{h,{f,g}}=0}

follows from the corresponding identity for the Lie bracket of vector fields, but this is true only up to a locally constant function. However, to prove the Jacobi identity for the Poisson bracket, it is sufficient to show that:

          ad

            {
            g
            ,
            f
            }

          ad

            −
            {
            f
            ,
            g
            }

        [

          ad

            f

        ,

          ad

            g

        ]

    {\displaystyle \operatorname {ad} _{{g,f}}=\operatorname {ad} _{-{f,g}}=[\operatorname {ad} _{f},\operatorname {ad} _{g}]}

where the operator

          ad

            g

    {\displaystyle \operatorname {ad} _{g}}

 on smooth functions on M is defined by

          ad

            g

        ⁡
        (
        ⋅
        )

        {
        ⋅
        ,

        g
        }

    {\displaystyle \operatorname {ad} _{g}(\cdot )\;=\;{\cdot ,\,g}}

 and the bracket on the right-hand side is the commutator of operators,

        [
        A
        ,

        B
        ]

        A
        ⁡
        B
        −
        B
        ⁡
        A

    {\displaystyle [\operatorname {A} ,\,\operatorname {B} ]\;=\;\operatorname {A} \operatorname {B} -\operatorname {B} \operatorname {A} }

. By (1), the operator

          ad

            g

    {\displaystyle \operatorname {ad} _{g}}

 is equal to the operator Xg. The proof of the Jacobi identity follows from (3) because, up to the factor of -1, the Lie bracket of vector fields is just their commutator as differential operators.
The algebra of smooth functions on M, together with the Poisson bracket forms a Poisson algebra, because it is a Lie algebra under the Poisson bracket, which additionally satisfies Leibniz's rule (2). We have shown that every symplectic manifold is a Poisson manifold, that is a manifold with a "curly-bracket" operator on smooth functions such that the smooth functions form a Poisson algebra. However, not every Poisson manifold arises in this way, because Poisson manifolds allow for degeneracy which cannot arise in the symplectic case.

A result on conjugate momenta
Given a smooth vector field

        X

    {\displaystyle X}

 on the configuration space, let

          P

            X

    {\displaystyle P_{X}}

 be its conjugate momentum. The conjugate momentum mapping is a Lie algebra anti-homomorphism from the Lie bracket to the Poisson bracket:

        {

          P

            X

        ,

          P

            Y

        }

        −

          P

            [
            X
            ,
            Y
            ]

        .

    {\displaystyle {P_{X},P_{Y}}=-P_{[X,Y]}.}

This important result is worth a short proof. Write a vector field

        X

    {\displaystyle X}

 at point

        q

    {\displaystyle q}

 in the configuration space as

          X

            q

          ∑

            i

          X

            i

        (
        q
        )

            ∂

              ∂

                q

                  i

    {\displaystyle X_{q}=\sum _{i}X^{i}(q){\frac {\partial }{\partial q^{i}}}}

where

            ∂

              ∂

                q

                  i

    {\textstyle {\frac {\partial }{\partial q^{i}}}}

 is the local coordinate frame. The conjugate momentum to

        X

    {\displaystyle X}

 has the expression

          P

            X

        (
        q
        ,
        p
        )

          ∑

            i

          X

            i

        (
        q
        )

          p

            i

    {\displaystyle P_{X}(q,p)=\sum {i}X^{i}(q)\;p{i}}

where the

          p

            i

    {\displaystyle p_{i}}

 are the momentum functions conjugate to the coordinates. One then has, for a point

        (
        q
        ,
        p
        )

    {\displaystyle (q,p)}

 in the phase space,

                {

                  P

                    X

                ,

                  P

                    Y

                }
                (
                q
                ,
                p
                )

                  ∑

                    i

                  ∑

                    j

                  {

                      X

                        i

                    (
                    q
                    )

                      p

                        i

                    ,

                      Y

                        j

                    (
                    q
                    )

                      p

                        j

                  }

                  ∑

                    i
                    j

                  p

                    i

                  Y

                    j

                (
                q
                )

                      ∂

                        X

                          i

                      ∂

                        q

                          j

                −

                  p

                    j

                  X

                    i

                (
                q
                )

                      ∂

                        Y

                          j

                      ∂

                        q

                          i

                −

                  ∑

                    i

                  p

                    i

                [
                X
                ,
                Y

                  ]

                    i

                (
                q
                )

                −

                  P

                    [
                    X
                    ,
                    Y
                    ]

                (
                q
                ,
                p
                )
                .

    {\displaystyle {\begin{aligned}{P_{X},P_{Y}}(q,p)&=\sum _{i}\sum {j}\left{X^{i}(q)\;p{i},Y^{j}(q)\;p_{j}\right}\&=\sum {ij}p{i}Y^{j}(q){\frac {\partial X^{i}}{\partial q^{j}}}-p_{j}X^{i}(q){\frac {\partial Y^{j}}{\partial q^{i}}}\&=-\sum {i}p{i}\;[X,Y]^{i}(q)\&=-P_{[X,Y]}(q,p).\end{aligned}}}

The above holds for all

        (
        q
        ,
        p
        )

    {\displaystyle (q,p)}

, giving the desired result.

Quantization
Poisson brackets deform to Moyal brackets upon quantization, that is, they generalize to a different Lie algebra, the Moyal algebra, or, equivalently in Hilbert space, quantum commutators. The Wigner-İnönü group contraction of these (the classical limit, ħ → 0) yields the above Lie algebra.
To state this more explicitly and precisely, the universal enveloping algebra of the Heisenberg algebra is the Weyl algebra (modulo the relation that the center be the unit). The Moyal product is then a special case of the star product on the algebra of symbols. An explicit definition of the algebra of symbols, and the star product is given in the article on the universal enveloping algebra.

Remarks
