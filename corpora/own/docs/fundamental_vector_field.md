# Fundamental vector field

Fundamental vector field

In the study of mathematics, and especially of differential geometry, fundamental vector fields are instruments that describe the infinitesimal behaviour of a smooth Lie group action on a smooth manifold. Such vector fields find important applications in the study of Lie theory, symplectic geometry, and the study of Hamiltonian group actions.

Motivation
Important to applications in mathematics and physics is the notion of a flow on a manifold. In particular, if

        M

    {\displaystyle M}

 is a smooth manifold and

        X

    {\displaystyle X}

 is a smooth vector field, one is interested in finding integral curves to

        X

    {\displaystyle X}

. More precisely, given

        p
        ∈
        M

    {\displaystyle p\in M}

 one is interested in curves

          γ

            p

        :

          R

        →
        M

    {\displaystyle \gamma _{p}:\mathbb {R} \to M}

 such that:

          γ

            p

          ′

        (
        t
        )

          X

              γ

                p

            (
            t
            )

        ,

          γ

            p

        (
        0
        )

        p
        ,

    {\displaystyle \gamma {p}'(t)=X{\gamma _{p}(t)},\qquad \gamma _{p}(0)=p,}

for which local solutions are guaranteed by the Existence and Uniqueness Theorem of Ordinary Differential Equations. If

        X

    {\displaystyle X}

 is furthermore a complete vector field, then the flow of

        X

    {\displaystyle X}

, defined as the collection of all integral curves for

        X

    {\displaystyle X}

, is a diffeomorphism of

        M

    {\displaystyle M}

. The flow

          ϕ

            X

        :

          R

        ×
        M
        →
        M

    {\displaystyle \phi _{X}:\mathbb {R} \times M\to M}

 given by

          ϕ

            X

        (
        t
        ,
        p
        )

          γ

            p

        (
        t
        )

    {\displaystyle \phi _{X}(t,p)=\gamma _{p}(t)}

 is in fact an action of the additive Lie group

        (

          R

        ,
        +
        )

    {\displaystyle (\mathbb {R} ,+)}

 on

        M

    {\displaystyle M}

.
Conversely, every smooth action

        A
        :

          R

        ×
        M
        →
        M

    {\displaystyle A:\mathbb {R} \times M\to M}

 defines a complete vector field

        X

    {\displaystyle X}

 via the equation:

          X

            p

                d

                  d
                  t

            t

            0

        A
        (
        t
        ,
        p
        )
        .

    {\displaystyle X_{p}=\left.{\frac {d}{dt}}\right|_{t=0}A(t,p).}

It is then a simple result that there is a bijective correspondence between

          R

    {\displaystyle \mathbb {R} }

-actions on

        M

    {\displaystyle M}

 and complete vector fields on

        M

    {\displaystyle M}

.
In the language of flow theory, the vector field

        X

    {\displaystyle X}

 is called the infinitesimal generator. Intuitively, the behaviour of the flow at each point corresponds to the "direction" indicated by the vector field. It is a natural question to ask whether one may establish a similar correspondence between vector fields and more arbitrary Lie group actions on

        M

    {\displaystyle M}

.

Definition
Let

        G

    {\displaystyle G}

 be a Lie group with corresponding Lie algebra

            g

    {\displaystyle {\mathfrak {g}}}

. Furthermore, let

        M

    {\displaystyle M}

 be a smooth manifold endowed with a smooth action

        A
        :
        G
        ×
        M
        →
        M

    {\displaystyle A:G\times M\to M}

. Denote the map

          A

            p

        :
        G
        →
        M

    {\displaystyle A_{p}:G\to M}

 such that

          A

            p

        (
        g
        )

        A
        (
        g
        ,
        p
        )

    {\displaystyle A_{p}(g)=A(g,p)}

, called the orbit map of

        A

    {\displaystyle A}

 corresponding to

        p

    {\displaystyle p}

. For

        X
        ∈

            g

    {\displaystyle X\in {\mathfrak {g}}}

, the fundamental vector field

          X

            #

    {\displaystyle X^{#}}

 corresponding to

        X

    {\displaystyle X}

 is given by any of the following equivalent definitions:

          X

            p

            #

          d

            e

          A

            p

        (
        X
        )

    {\displaystyle X_{p}^{#}=d_{e}A_{p}(X)}

          X

            p

            #

          d

            (
            e
            ,
            p
            )

        A

          (

            X
            ,

              0

                  T

                    p

                M

          )

    {\displaystyle X_{p}^{#}=d_{(e,p)}A\left(X,0_{T_{p}M}\right)}

          X

            p

            #

                d

                  d
                  t

            t

            0

        A

          (

            exp
            ⁡
            (
            t
            X
            )
            ,
            p

          )

    {\displaystyle X_{p}^{#}=\left.{\frac {d}{dt}}\right|_{t=0}A\left(\exp(tX),p\right)}

where

        d

    {\displaystyle d}

 is the differential of a smooth map and

          0

              T

                p

            M

    {\displaystyle 0_{T_{p}M}}

 is the zero vector in the vector space

          T

            p

        M

    {\displaystyle T_{p}M}

.
The map

            g

        →
        Γ
        (
        T
        M
        )
        ,
        X
        ↦
        −

          X

            #

    {\displaystyle {\mathfrak {g}}\to \Gamma (TM),X\mapsto -X^{#}}

 can then be shown to be a Lie algebra homomorphism.

Applications

Lie groups
The Lie algebra of a Lie group

        G

    {\displaystyle G}

 may be identified with either the left- or right-invariant vector fields on

        G

    {\displaystyle G}

. It is a well-known result that such vector fields are isomorphic to

          T

            e

        G

    {\displaystyle T_{e}G}

, the tangent space at identity. In fact, if we let

        G

    {\displaystyle G}

 act on itself via right-multiplication, the corresponding fundamental vector fields are precisely the left-invariant vector fields.

Hamiltonian group actions
In the motivation, it was shown that there is a bijective correspondence between smooth

          R

    {\displaystyle \mathbb {R} }

-actions and complete vector fields. Similarly, given a symplectic manifold

        (
        M
        ,
        ω
        )

    {\displaystyle (M,\omega )}

, there is a bijective correspondence between symplectic actions (the induced diffeomorphisms are all symplectomorphisms) and complete symplectic vector fields.
A closely related idea is that of Hamiltonian vector fields. Given a symplectic manifold

        (
        M
        ,
        ω
        )

    {\displaystyle (M,\omega )}

, we say that

          X

            H

    {\displaystyle X_{H}}

 is a Hamiltonian vector field if there exists a smooth function

        H
        :
        M
        →

          R

    {\displaystyle H:M\to \mathbb {R} }

 satisfying

        d
        H

          ι

              X

                H

        ω

    {\displaystyle dH=\iota {X{H}}\omega }

where the map

        ι

    {\displaystyle \iota }

 is the interior product. This motivates the definition of a Hamiltonian group action as follows: If

        G

    {\displaystyle G}

 is a Lie group with Lie algebra

            g

    {\displaystyle {\mathfrak {g}}}

 and

        A
        :
        G
        ×
        M
        →
        M

    {\displaystyle A:G\times M\to M}

 is a group action of

        G

    {\displaystyle G}

 on a smooth manifold

        M

    {\displaystyle M}

, then we say that

        A

    {\displaystyle A}

 is a Hamiltonian group action if there exists a moment map

        μ
        :
        M
        →

              g

            ∗

    {\displaystyle \mu :M\to {\mathfrak {g}}^{*}}

 such that for each:

        X
        ∈

            g

    {\displaystyle X\in {\mathfrak {g}}}

,

        d

          μ

            X

          ι

              X

                #

        ω
        ,

    {\displaystyle d\mu ^{X}=\iota _{X^{#}}\omega ,}

where

          μ

            X

        :
        M
        →

          R

        ,
        p
        ↦
        ⟨
        μ
        (
        p
        )
        ,
        X
        ⟩

    {\displaystyle \mu ^{X}:M\to \mathbb {R} ,p\mapsto \langle \mu (p),X\rangle }

 and

          X

            #

    {\displaystyle X^{#}}

 is the fundamental vector field of

        X

    {\displaystyle X}

.
