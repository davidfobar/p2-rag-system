# Symplectic manifold

Symplectic manifold

In differential geometry, a symplectic manifold is a smooth manifold,

        M

    {\displaystyle M}

, equipped with a closed nondegenerate differential 2-form,

        ω

    {\displaystyle \omega }

, called the symplectic form. The study of symplectic manifolds is called symplectic geometry or symplectic topology. Symplectic manifolds arise naturally in abstract formulations of classical mechanics and analytical mechanics as the cotangent bundles of manifolds. For example, in the Hamiltonian formulation of classical mechanics, which provides one of the major motivations for the field, the set of all possible configurations of a system is modeled as a manifold, and this manifold's cotangent bundle describes the phase space of the system.

Motivation
Symplectic manifolds arise from classical mechanics; in particular, they are a generalization of the phase space of a closed system. In the same way the Hamilton equations allow one to derive the time evolution of a system from a set of differential equations, the symplectic form should allow one to obtain a vector field describing the flow of the system from the differential

        d
        H

    {\displaystyle dH}

 of a Hamiltonian function

        H

    {\displaystyle H}

. So we require a linear map

        T
        M
        →

          T

            ∗

        M

    {\displaystyle TM\rightarrow T^{*}M}

 from the tangent manifold

        T
        M

    {\displaystyle TM}

 to the cotangent manifold

          T

            ∗

        M

    {\displaystyle T^{*}M}

, or equivalently, an element of

          T

            ∗

        M
        ⊗

          T

            ∗

        M

    {\displaystyle T^{}M\otimes T^{}M}

. Letting

        ω

    {\displaystyle \omega }

 denote a section of

          T

            ∗

        M
        ⊗

          T

            ∗

        M

    {\displaystyle T^{}M\otimes T^{}M}

, the requirement that

        ω

    {\displaystyle \omega }

 be non-degenerate ensures that for every differential

        d
        H

    {\displaystyle dH}

 there is a unique corresponding vector field

          V

            H

    {\displaystyle V_{H}}

 such that

        d
        H

        ω
        (

          V

            H

        ,
        ⋅
        )

    {\displaystyle dH=\omega (V_{H},\cdot )}

. Since one desires the Hamiltonian to be constant along flow lines, one should have

        ω
        (

          V

            H

        ,

          V

            H

        )

        d
        H
        (

          V

            H

        )

        0

    {\displaystyle \omega (V_{H},V_{H})=dH(V_{H})=0}

, which implies that

        ω

    {\displaystyle \omega }

 is alternating and hence a 2-form. Finally, one makes the requirement that

        ω

    {\displaystyle \omega }

 should not change under flow lines, i.e. that the Lie derivative of

        ω

    {\displaystyle \omega }

 along

          V

            H

    {\displaystyle V_{H}}

 vanishes. Applying Cartan's formula, this amounts to (here

          ι

            X

    {\displaystyle \iota _{X}}

 is the interior product):

              L

              V

                H

        (
        ω
        )

        0

        ⇔

          d

        (

          ι

              V

                H

        ω
        )
        +

          ι

              V

                H

          d

        ω

          d

        (

          d

        H
        )
        +

          d

        ω
        (

          V

            H

        )

          d

        ω
        (

          V

            H

        )

        0

    {\displaystyle {\mathcal {L}}{V{H}}(\omega )=0\;\Leftrightarrow \;\mathrm {d} (\iota {V{H}}\omega )+\iota {V{H}}\mathrm {d} \omega =\mathrm {d} (\mathrm {d} \,H)+\mathrm {d} \omega (V_{H})=\mathrm {d} \omega (V_{H})=0}

so that, on repeating this argument for different smooth functions

        H

    {\displaystyle H}

 such that the corresponding

          V

            H

    {\displaystyle V_{H}}

 span the tangent space at each point the argument is applied at, we see that the requirement for the vanishing Lie derivative along flows of

          V

            H

    {\displaystyle V_{H}}

 corresponding to arbitrary smooth

        H

    {\displaystyle H}

 is equivalent to the requirement that ω should be closed.

Definition
Let

        M

    {\displaystyle M}

 be a smooth manifold. A symplectic form on

        M

    {\displaystyle M}

 is a closed non-degenerate differential 2-form

        ω

    {\displaystyle \omega }

. Here, non-degenerate means that for every point

        p
        ∈
        M

    {\displaystyle p\in M}

, the skew-symmetric pairing on the tangent space

          T

            p

        M

    {\displaystyle T_{p}M}

 defined by

        ω

    {\displaystyle \omega }

 is non-degenerate. That is to say, if there exists an

        X
        ∈

          T

            p

        M

    {\displaystyle X\in T_{p}M}

 such that

        ω
        (
        X
        ,
        Y
        )

        0

    {\displaystyle \omega (X,Y)=0}

 for all

        Y
        ∈

          T

            p

        M

    {\displaystyle Y\in T_{p}M}

, then

        X

        0

    {\displaystyle X=0}

. The closed condition means that the exterior derivative of

        ω

    {\displaystyle \omega }

 vanishes.
A symplectic manifold is a pair

        (
        M
        ,
        ω
        )

    {\displaystyle (M,\omega )}

 where

        M

    {\displaystyle M}

 is a smooth manifold and

        ω

    {\displaystyle \omega }

 is a symplectic form. Assigning a symplectic form to

        M

    {\displaystyle M}

 is referred to as giving

        M

    {\displaystyle M}

 a symplectic structure. Since in odd dimensions, skew-symmetric matrices are always singular, nondegeneracy implies that

        dim
        ⁡
        M

    {\displaystyle \dim M}

 is even.
By nondegeneracy,

        ω

    {\displaystyle \omega }

 can be used to define a pair of musical isomorphisms

          ω

            ♭

        :
        T
        M
        →

          T

            ∗

        M
        ,

          ω

            ♯

        :

          T

            ∗

        M
        →
        T
        M

    {\displaystyle \omega ^{\flat }:TM\rightarrow T^{}M,\omega ^{\sharp }:T^{}M\rightarrow TM}

, such that

        ω
        (
        X
        ,
        Y
        )

          ω

            ♭

        (
        X
        )
        (
        Y
        )

    {\displaystyle \omega (X,Y)=\omega ^{\flat }(X)(Y)}

 for any two vector fields

        X
        ,
        Y

    {\displaystyle X,Y}

, and

          ω

            ♯

        ∘

          ω

            ♭

        Id

    {\displaystyle \omega ^{\sharp }\circ \omega ^{\flat }=\operatorname {Id} }

.
A symplectic manifold

        (
        M
        ,
        ω
        )

    {\displaystyle (M,\omega )}

 is exact iff the symplectic form

        ω

    {\displaystyle \omega }

 is exact, i.e. equal to

        ω

        −
        d
        θ

    {\displaystyle \omega =-d\theta }

 for some 1-form

        θ

    {\displaystyle \theta }

. The symplectic form on any compact symplectic manifold without boundary is inexact, by Stokes' theorem.
By Darboux's theorem, around any point

        p

    {\displaystyle p}

 there exists a local coordinate system, in which

        ω

          Σ

            i

        d

          p

            i

        ∧
        d

          q

            i

    {\displaystyle \omega =\Sigma {i}dp{i}\wedge dq^{i}}

, where d denotes the exterior derivative and ∧ denotes the exterior product. This form is called the Poincaré two-form or the canonical two-form. Thus, we can locally think of M as being the cotangent bundle

          T

            ∗

            R

            n

    {\displaystyle T^{*}\mathbb {R} ^{n}}

 and generated by the corresponding tautological 1-form

        θ

          Σ

            i

          p

            i

        d

          q

            i

        ,

        ω

        d
        θ

    {\displaystyle \theta =\Sigma {i}p{i}dq^{i},\;\omega =d\theta }

.
A (local) Liouville form is any (locally defined)

        λ

    {\displaystyle \lambda }

 such that

        ω

        d
        λ

    {\displaystyle \omega =d\lambda }

. A vector field

        X

    {\displaystyle X}

 is (locally) Liouville iff

              L

            X

        ω

        ω

    {\displaystyle {\mathcal {L}}_{X}\omega =\omega }

. By Cartan's magic formula, this is equivalent to

        d
        (
        ω
        (
        X
        ,
        ⋅
        )
        )

        ω

    {\displaystyle d(\omega (X,\cdot ))=\omega }

. A Liouville vector field can thus be interpreted as a way to recover a (local) Liouville form. By Darboux's theorem, around any point there exists a local Liouville form, though it might not exist globally.
On a symplectic manifold, every smooth function

        H
        :
        M
        →

          R

    {\displaystyle H:M\to \mathbb {R} }

 determines a Hamiltonian vector field

          X

            H

    {\displaystyle X_{H}}

 by

          ι

              X

                H

        ω

        d
        H

    {\displaystyle \iota {X{H}}\omega =dH}

, up to sign convention. The integral curves of

          X

            H

    {\displaystyle X_{H}}

 are the Hamiltonian flow of

        H

    {\displaystyle H}

. In classical mechanics,

        H

    {\displaystyle H}

 is the energy function and the symplectic form encodes Hamilton's equations. The set of all Hamiltonian vector fields make up a Lie algebra, and is written as

        (
        Ham
        ⁡
        (
        M
        )
        ,
        [
        ⋅
        ,
        ⋅
        ]
        )

    {\displaystyle (\operatorname {Ham} (M),[\cdot ,\cdot ])}

 where

        [
        ⋅
        ,
        ⋅
        ]

    {\displaystyle [\cdot ,\cdot ]}

 is the Lie bracket.
Given any two smooth functions

        f
        ,
        g
        :
        M
        →

          R

    {\displaystyle f,g:M\to \mathbb {R} }

, their Poisson bracket is defined by

        {
        f
        ,
        g
        }

        ω
        (

          X

            g

        ,

          X

            f

        )

    {\displaystyle {f,g}=\omega (X_{g},X_{f})}

. This makes any symplectic manifold into a Poisson manifold. The Poisson bivector is a bivector field

        π

    {\displaystyle \pi }

 defined by

        {
        f
        ,
        g
        }

        π
        (
        d
        f
        ∧
        d
        g
        )

    {\displaystyle {f,g}=\pi (df\wedge dg)}

, or equivalently, by

        π
        :=

          ω

            −
            1

    {\displaystyle \pi :=\omega ^{-1}}

. The Poisson bracket and Lie bracket are related by

          X

            {
            f
            ,
            g
            }

        [

          X

            f

        ,

          X

            g

        ]

    {\textstyle X_{{f,g}}=[X_{f},X_{g}]}

.

Basic properties
If

        (
        M
        ,
        ω
        )

    {\displaystyle (M,\omega )}

 is a symplectic manifold of dimension

        2
        n

    {\displaystyle 2n}

, then

          ω

            n

    {\displaystyle \omega ^{n}}

 is a nowhere-vanishing top-degree form. Thus every symplectic manifold is orientable and has a natural volume form, called the symplectic volume form.
Unlike a Riemannian metric, a symplectic form does not define lengths or angles. By Darboux's theorem, all symplectic manifolds of the same dimension are locally symplectomorphic. Consequently, symplectic geometry has no local curvature invariant analogous to the Riemannian curvature tensor; many of its main questions are global.

Submanifolds
There are several natural geometric notions of submanifold of a symplectic manifold

        (
        M
        ,
        ω
        )

    {\displaystyle (M,\omega )}

. Let

        N
        ⊂
        M

    {\displaystyle N\subset M}

 be a submanifold. It is

symplectic iff

        ω

            N

    {\displaystyle \omega |_{N}}

 is a symplectic form on

        N

    {\displaystyle N}

;
isotropic iff

        ω

            N

        0

    {\displaystyle \omega |_{N}=0}

, equivalently, iff

          T

            p

        N
        ⊂

          T

            p

          N

            ⊥

    {\displaystyle T_{p}N\subset T_{p}N^{\perp }}

 for any

        p
        ∈
        N

    {\displaystyle p\in N}

, where

          T

            p

          N

            ⊥

    {\displaystyle T_{p}N^{\perp }}

 is the annihilator of

        ω
        (

          T

            p

        N
        )

    {\displaystyle \omega (T_{p}N)}

 in

          T

            p

        M

    {\displaystyle T_{p}M}

;
coisotropic iff

          T

            p

          N

            ⊥

        ⊂

          T

            p

        N

    {\displaystyle T_{p}N^{\perp }\subset T_{p}N}

 for any

        p
        ∈
        N

    {\displaystyle p\in N}

;
Lagrangian iff it is both isotropic and coisotropic, i.e.

        ω

            N

        0

    {\displaystyle \omega |_{N}=0}

 and

          dim

        N

              1
              2

        dim
        ⁡
        M

    {\displaystyle {\text{dim }}N={\tfrac {1}{2}}\dim M}

. By the nondegeneracy of

        ω

    {\displaystyle \omega }

, Lagrangian submanifolds are the maximal isotropic submanifolds and minimal coisotropic submanifolds.

Lagrangian submanifolds
Lagrangian submanifolds are the most important submanifolds. Weinstein proposed the "symplectic creed": Everything is a Lagrangian submanifold. By that, he means that everything in symplectic geometry is most naturally expressed in terms of Lagrangian submanifolds.
A Lagrangian fibration of a symplectic manifold M is a fibration where all of the fibers are Lagrangian submanifolds.
Given a submanifold

        N
        ⊂
        M

    {\displaystyle N\subset M}

 of codimension 1, the characteristic line distribution on it is the duals to its tangent spaces:

          T

            p

          N

            ω

    {\displaystyle T_{p}N^{\omega }}

. If there also exists a Liouville vector field

        X

    {\displaystyle X}

 in a neighborhood of it that is transverse to it. In this case, let

        α
        :=
        ω
        (
        X
        ,
        ⋅
        )

            N

    {\displaystyle \alpha :=\omega (X,\cdot )|_{N}}

, then

        (
        N
        ,
        α
        )

    {\displaystyle (N,\alpha )}

 is a contact manifold, and we say it is a contact type submanifold. In this case, the Reeb vector field is tangent to the characteristic line distribution.
An n-submanifold is locally specified by a smooth function

        u
        :

            R

            n

        →
        M

    {\displaystyle u:\mathbb {R} ^{n}\to M}

. It is a Lagrangian submanifold if

        ω
        (

          ∂

            i

        ,

          ∂

            j

        )

        0

    {\displaystyle \omega (\partial _{i},\partial _{j})=0}

 for all

        i
        ,
        j
        ∈
        1
        :
        n

    {\displaystyle i,j\in 1:n}

. If locally there is a canonical coordinate system

        (
        q
        ,
        p
        )

    {\displaystyle (q,p)}

, then the condition is equivalent to

        [
        u
        ,
        v

          ]

            p
            ,
            q

          ∑

            i

            1

            n

          (

                  ∂

                    q

                      i

                  ∂
                  u

                  ∂

                    p

                      i

                  ∂
                  v

            −

                  ∂

                    p

                      i

                  ∂
                  u

                  ∂

                    q

                      i

                  ∂
                  v

          )

        0
        ,

        ∀
        i
        ,
        j
        ∈
        1
        :
        n

    {\displaystyle [u,v]_{p,q}=\sum {i=1}^{n}\left({\frac {\partial q{i}}{\partial u}}{\frac {\partial p_{i}}{\partial v}}-{\frac {\partial p_{i}}{\partial u}}{\frac {\partial q_{i}}{\partial v}}\right)=0,\quad \forall i,j\in 1:n}

where

        [
        ⋅
        ,
        ⋅

          ]

            p
            ,
            q

    {\displaystyle [\cdot ,\cdot ]_{p,q}}

 is the Lagrange bracket in this coordinate system.
The graph of a closed 1-form on

        M

    {\displaystyle M}

 is a Lagrangian submanifold of

          T

            ∗

        M

    {\displaystyle T^{*}M}

. In particular, the graph of

        d
        f

    {\displaystyle df}

 is Lagrangian. Conversely, if a Lagrangian submanifold

        L
        ⊂

          T

            ∗

        M

    {\displaystyle L\subset T^{*}M}

 projects diffeomorphically to

        M

    {\displaystyle M}

, then it is the graph of a closed 1-form. It is globally the graph of

        d
        f

    {\displaystyle df}

 only when that closed 1-form is exact.

Lagrangian mapping

Let L be a Lagrangian submanifold of a symplectic manifold (K,ω) given by an immersion i : L ↪ K (i is called a Lagrangian immersion). Let π : K ↠ B give a Lagrangian fibration of K. The composite (π ∘ i) : L ↪ K ↠ B is a Lagrangian mapping. The critical value set of π ∘ i is called a caustic.
Two Lagrangian maps (π1 ∘ i1) : L1 ↪ K1 ↠ B1 and (π2 ∘ i2) : L2 ↪ K2 ↠ B2 are called Lagrangian equivalent if there exist diffeomorphisms σ, τ and ν such that both sides of the diagram given on the right commute, and τ preserves the symplectic form. Symbolically:

        τ
        ∘

          i

            1

          i

            2

        ∘
        σ
        ,

        ν
        ∘

          π

            1

          π

            2

        ∘
        τ
        ,

          τ

            ∗

          ω

            2

          ω

            1

        ,

    {\displaystyle \tau \circ i_{1}=i_{2}\circ \sigma ,\ \nu \circ \pi _{1}=\pi _{2}\circ \tau ,\ \tau ^{*}\omega _{2}=\omega _{1}\,,}

where τ∗ω2 denotes the pull back of ω2 by τ.

Symmetries

A map

        f
        :
        (
        M
        ,
        ω
        )
        →
        (

          M
          ′

        ,

          ω
          ′

        )

    {\displaystyle f:(M,\omega )\to (M',\omega ')}

 between symplectic manifolds is a symplectomorphism when it preserves the symplectic structure, i.e. the pullback is the same

          f

            ∗

          ω
          ′

        ω

    {\displaystyle f^{*}\omega '=\omega }

. The most important symplectomorphisms are symplectic flows, i.e. ones generated by integrating a vector field on

        (
        M
        ,
        ω
        )

    {\displaystyle (M,\omega )}

.
Given a vector field

        X

    {\displaystyle X}

 on

        (
        M
        ,
        ω
        )

    {\displaystyle (M,\omega )}

, it generates a symplectic flow iff

              L

            X

        ω

        0

    {\displaystyle {\mathcal {L}}_{X}\omega =0}

. Such vector fields are called symplectic. Any Hamiltonian vector field is symplectic, and conversely, any symplectic vector field is locally Hamiltonian.
A property that is preserved under all symplectomorphisms is a symplectic invariant. In the spirit of Erlangen program, symplectic geometry is the study of symplectic invariants.

Examples

The standard symplectic structure

Let

        {

          v

            1

        ,
        …
        ,

          v

            2
            n

        }

    {\displaystyle {v_{1},\ldots ,v_{2n}}}

 be a basis for

            R

            2
            n

        .

    {\displaystyle \mathbb {R} ^{2n}.}

 We define our symplectic form

        ω

    {\displaystyle \omega }

 on this basis as follows:

        ω
        (

          v

            i

        ,

          v

            j

        )

            {

                  1

                  j
                  −
                  i

                  n

                     with

                  1
                  ⩽
                  i
                  ⩽
                  n

                  −
                  1

                  i
                  −
                  j

                  n

                     with

                  1
                  ⩽
                  j
                  ⩽
                  n

                  0

                    otherwise

    {\displaystyle \omega (v_{i},v_{j})={\begin{cases}1&j-i=n{\text{ with }}1\leqslant i\leqslant n\-1&i-j=n{\text{ with }}1\leqslant j\leqslant n\0&{\text{otherwise}}\end{cases}}}

In this case the symplectic form reduces to a simple bilinear form. If

          I

            n

    {\displaystyle I_{n}}

 denotes the

        n
        ×
        n

    {\displaystyle n\times n}

 identity matrix then the matrix,

        Ω

    {\displaystyle \Omega }

, of this bilinear form is given by the

        2
        n
        ×
        2
        n

    {\displaystyle 2n\times 2n}

 block matrix:

        Ω

            (

                  0

                    I

                      n

                  −

                    I

                      n

                  0

            )

        .

    {\displaystyle \Omega ={\begin{pmatrix}0&I_{n}\-I_{n}&0\end{pmatrix}}.}

That is,

        ω

          d

          x

            1

        ∧

          d

          y

            1

        +
        ⋯
        +

          d

          x

            n

        ∧

          d

          y

            n

        .

    {\displaystyle \omega =\mathrm {d} x_{1}\wedge \mathrm {d} y_{1}+\dotsb +\mathrm {d} x_{n}\wedge \mathrm {d} y_{n}.}

It has a fibration by Lagrangian submanifolds with fixed value of

        y

    {\displaystyle y}

, i.e.

        {

            R

            n

        ×
        {
        y
        }
        :
        y
        ∈

            R

            n

        }

    {\displaystyle {\mathbb {R} ^{n}\times {y}:y\in \mathbb {R} ^{n}}}

.
A Liouville form for this is

        λ

            1
            2

          ∑

            i

          (

              x

                i

            d

              y

                i

            −

              y

                i

            d

              x

                i

          )

    {\textstyle \lambda ={\frac {1}{2}}\sum {i}\left(x{i}dy_{i}-y_{i}dx_{i}\right)}

 and

        ω

        d
        λ

    {\textstyle \omega =d\lambda }

, the Liouville vector field is

        Y

            1
            2

          ∑

            i

          (

              x

                i

              ∂

                  x

                    i

            +

              y

                i

              ∂

                  y

                    i

          )

        ,

    {\displaystyle Y={\frac {1}{2}}\sum {i}\left(x{i}\partial {x{i}}+y_{i}\partial {y{i}}\right),}

the radial field. Another Liouville form is

          Σ

            i

          x

            i

        d

          y

            i

    {\displaystyle \Sigma {i}x{i}dy_{i}}

, with Liouville vector field

        Y

          ∑

            i

          x

            i

          ∂

              x

                i

    {\textstyle Y=\sum {i}x{i}\partial {x{i}}}

.

Surfaces
Every oriented smooth surface with an area form is a symplectic manifold. In dimension two, the closedness condition is automatic for any 2-form.

Cotangent bundles
If

        Q

    {\displaystyle Q}

 is a smooth manifold, its cotangent bundle

          T

            ∗

        Q

    {\displaystyle T^{*}Q}

 carries a canonical 1-form

        λ

    {\displaystyle \lambda }

, also called the tautological or Liouville 1-form. The exterior derivative

        ω

        d
        λ

    {\displaystyle \omega =d\lambda }

, up to sign convention, is the canonical symplectic form on

          T

            ∗

        Q

    {\displaystyle T^{*}Q}

, also called the Poincaré two-form.
The canonical 1-form is defined by the property that, for any

        v
        ∈

          T

            x
            ,
            α

          T

            ∗

        Q

    {\displaystyle v\in T_{x,\alpha }T^{*}Q}

,

        λ
        (
        v
        )

        α
        (

          π

            ∗

        v
        )

    {\displaystyle \lambda (v)=\alpha (\pi _{*}v)}

 where

        π
        :

          T

            ∗

        Q
        →
        Q

    {\displaystyle \pi :T^{*}Q\to Q}

 is the bundle projection. In local coordinates

          q

            i

    {\displaystyle q^{i}}

 on

        Q

    {\displaystyle Q}

, the canonical 1-form is

        λ

          ∑

            i

            1

            n

          p

            i

        d

          q

            i

    {\displaystyle \lambda =\sum {i=1}^{n}p{i}dq^{i}}

 where

          p

            i

    {\displaystyle p_{i}}

 are fiber coordinates on the cotangent bundle such that

        α

          ∑

            i

            1

            n

          p

            i

        (
        α
        )
        d

          q

            i

    {\displaystyle \alpha =\sum {i=1}^{n}p{i}(\alpha )dq^{i}}

. In these coordinates, the canonical symplectic form is

        ω

          ∑

            i

            1

            n

        d

          p

            i

        ∧
        d

          q

            i

    {\displaystyle \omega =\sum {i=1}^{n}dp{i}\wedge dq^{i}}

The tautological 1-form

        λ

          ∑

            i

          p

            i

        d

          q

            i

    {\displaystyle \lambda =\sum {i}p{i}dq^{i}}

 has Liouville vector field

        Y

          ∑

            i

          p

            i

          ∂

              p

                i

    {\displaystyle Y=\sum {i}p{i}\partial {p{i}}}

, the fiberwise radial field. Its flow dilates covectors:

        (
        q
        ,
        p
        )
        ↦

          (

            q
            ,

              e

                t

            p

          )

    {\textstyle (q,p)\mapsto \left(q,e^{t}p\right)}

.
The zero section of the cotangent bundle is Lagrangian.

Kähler manifolds
A Kähler manifold is a symplectic manifold equipped with a compatible integrable complex structure. They form a particular class of complex manifolds. A large class of examples come from complex algebraic geometry. Any smooth complex projective variety

        V
        ⊂

            C
            P

            n

    {\displaystyle V\subset \mathbb {CP} ^{n}}

 has a symplectic form which is the restriction of the Fubini—Study form on the projective space

            C
            P

            n

    {\displaystyle \mathbb {CP} ^{n}}

.
A symplectic manifold endowed with a metric that is compatible with the symplectic form is an almost Kähler manifold in the sense that the tangent bundle has an almost complex structure, but this need not be integrable. A compatible almost-complex structure is an endomorphism

        J

    {\displaystyle J}

 of the tangent space such that

          J

            2

        −
        I

    {\displaystyle J^{2}=-I}

,

        ω
        (
        X
        ,
        J
        Y
        )

        −
        ω
        (
        J
        X
        ,
        Y
        )

    {\displaystyle \omega (X,JY)=-\omega (JX,Y)}

, and

        ω
        (
        X
        ,
        J
        X
        )
        ≥
        0

    {\displaystyle \omega (X,JX)\geq 0}

 for all

        X

    {\displaystyle X}

. For such a compatible almost complex structure,

        g
        (
        X
        ,
        Y
        )

        ω
        (
        X
        ,
        J
        Y
        )

    {\displaystyle g(X,Y)=\omega (X,JY)}

 defines a Riemannian metric. When

        J

    {\displaystyle J}

 is integrable, the resulting symplectic manifold is Kähler.

Coadjoint orbits
Coadjoint orbits of Lie groups carry natural symplectic forms. If

            O

        ⊂

              g

            ∗

    {\displaystyle {\mathcal {O}}\subset {\mathfrak {g}}^{*}}

 is the coadjoint orbit through

        ξ

    {\displaystyle \xi }

, then tangent vectors at

        ξ

    {\displaystyle \xi }

 have the form

          ad

            X

            ∗

        ⁡
        ξ

    {\displaystyle \operatorname {ad} _{X}^{*}\xi }

, and the symplectic form is given, up to sign convention, by

          ω

            ξ

        (

          ad

            X

            ∗

        ⁡
        ξ
        ,

          ad

            Y

            ∗

        ⁡
        ξ
        )

        ⟨
        ξ
        ,
        [
        X
        ,
        Y
        ]
        ⟩
        .

    {\displaystyle \omega _{\xi }(\operatorname {ad} _{X}^{}\xi ,\operatorname {ad} _{Y}^{}\xi )=\langle \xi ,[X,Y]\rangle .}

Coadjoint orbits also arise naturally in moment map theory and symplectic reduction.

Lagrangian correspondences
A symplectomorphism can be described as a Lagrangian submanifold. If

        ϕ
        :
        (
        M
        ,

          ω

            M

        )
        →
        (
        N
        ,

          ω

            N

        )

    {\displaystyle \phi :(M,\omega _{M})\to (N,\omega _{N})}

 is a symplectomorphism, then its graph is a Lagrangian submanifold of

            M
            ¯

        ×
        N

    {\displaystyle {\overline {M}}\times N}

, where

            M
            ¯

    {\displaystyle {\overline {M}}}

 denotes

        M

    {\displaystyle M}

 equipped with the symplectic form

        −

          ω

            M

    {\displaystyle -\omega _{M}}

.
More generally, a Lagrangian correspondence from

        M

    {\displaystyle M}

 to

        N

    {\displaystyle N}

 is a Lagrangian submanifold of

            M
            ¯

        ×
        N

    {\displaystyle {\overline {M}}\times N}

. Lagrangian correspondences are used in formulations of the symplectic category and in Floer homology.

Generalizations
Presymplectic manifolds generalize the symplectic manifolds by only requiring

        ω

    {\displaystyle \omega }

 to be closed, but possibly degenerate. Any submanifold of a symplectic manifold inherits a presymplectic structure.
Poisson manifolds generalize the symplectic manifolds by preserving only the differential-algebraic structures of a symplectic manifold.
Dirac manifolds generalize Poisson manifolds and presymplectic manifolds by preserving even less structure. The definition is designed so that any submanifold of a Poisson manifold induces a Dirac manifold. They can be called "pre-Poisson" manifolds.
A multisymplectic manifold of degree k is a manifold equipped with a closed nondegenerate k-form.
A polysymplectic manifold is a Legendre bundle provided with a polysymplectic tangent-valued

        (
        n
        +
        2
        )

    {\displaystyle (n+2)}

-form; it is utilized in Hamiltonian field theory.

General and cited references
McDuff, Dusa; Salamon, D. (1998). Introduction to Symplectic Topology. Oxford Mathematical Monographs. ISBN 0-19-850451-9.
Hofer, Helmut; Zehnder, Eduard (2011). Symplectic Invariants and Hamiltonian Dynamics. Modern Birkhäuser Classics. Basel: Springer Basel AG Springer e-books. ISBN 978-3-0348-0104-1.
Auroux, Denis. "Seminar on Mirror Symmetry".
Meinrenken, Eckhard. "Symplectic Geometry" (PDF).
Abraham, Ralph; Marsden, Jerrold E. (1978). Foundations of Mechanics. London: Benjamin-Cummings. See Section 3.2. ISBN 0-8053-0102-X.
de Gosson, Maurice A. (2006). Symplectic Geometry and Quantum Mechanics. Basel: Birkhäuser Verlag. ISBN 3-7643-7574-4.
Alan Weinstein (1971). "Symplectic manifolds and their lagrangian submanifolds". Advances in Mathematics. 6 (3): 329–46. doi:10.1016/0001-8708(71)90020-X.
Arnold, V. I. (1990). "Ch.1, Symplectic geometry". Singularities of Caustics and Wave Fronts. Mathematics and Its Applications. Vol. 62. Dordrecht: Springer Netherlands. doi:10.1007/978-94-011-3330-2. ISBN 978-1-4020-0333-2. OCLC 22509804.
