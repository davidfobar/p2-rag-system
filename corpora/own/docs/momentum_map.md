# Momentum map

Momentum map

In mathematics, specifically in symplectic geometry, the momentum map (or, by false etymology, moment map) is a tool associated with a Hamiltonian action of a Lie group on a symplectic manifold, used to construct conserved quantities for the action. The momentum map generalizes the classical notions of linear and angular momentum. It is an essential ingredient in various constructions of symplectic manifolds, including symplectic (Marsden–Weinstein) quotients, discussed below, and symplectic cuts and sums.

Formal definition
Let

        M

    {\displaystyle M}

 be a manifold with symplectic form

        ω

    {\displaystyle \omega }

. Suppose that a Lie group

        G

    {\displaystyle G}

 acts on

        M

    {\displaystyle M}

 via symplectomorphisms (that is, the action of each

        g

    {\displaystyle g}

 in

        G

    {\displaystyle G}

 preserves

        ω

    {\displaystyle \omega }

). Let

            g

    {\displaystyle {\mathfrak {g}}}

 be the Lie algebra of

        G

    {\displaystyle G}

,

              g

            ∗

    {\displaystyle {\mathfrak {g}}^{*}}

 its dual, and

        ⟨

        ⋅
        ,
        ⋅
        ⟩
        :

              g

            ∗

        ×

            g

        →

          R

    {\displaystyle \langle \,\cdot ,\cdot \rangle :{\mathfrak {g}}^{*}\times {\mathfrak {g}}\to \mathbb {R} }

the pairing between the two. Any

        ξ

    {\displaystyle \xi }

 in

            g

    {\displaystyle {\mathfrak {g}}}

 induces a vector field

        ρ
        (
        ξ
        )

    {\displaystyle \rho (\xi )}

 on

        M

    {\displaystyle M}

 describing the infinitesimal action of

        ξ

    {\displaystyle \xi }

. To be precise, at a point

        x

    {\displaystyle x}

 in

        M

    {\displaystyle M}

 the vector

        ρ
        (
        ξ

          )

            x

    {\displaystyle \rho (\xi )_{x}}

 is

                  d

                    d

                  t

            t

            0

        exp
        ⁡
        (
        t
        ξ
        )
        ⋅
        x
        ,

    {\displaystyle \left.{\frac {\mathrm {d} }{\mathrm {d} t}}\right|_{t=0}\exp(t\xi )\cdot x,}

where

        exp
        :

            g

        →
        G

    {\displaystyle \exp :{\mathfrak {g}}\to G}

 is the exponential map and

        ⋅

    {\displaystyle \cdot }

 denotes the

        G

    {\displaystyle G}

-action on

        M

    {\displaystyle M}

. Let

          ι

            ρ
            (
            ξ
            )

        ω

    {\displaystyle \iota _{\rho (\xi )}\omega \,}

 denote the contraction of this vector field with

        ω

    {\displaystyle \omega }

. Because

        G

    {\displaystyle G}

 acts by symplectomorphisms, it follows, by Cartan’s Magic Formula, that

          ι

            ρ
            (
            ξ
            )

        ω

    {\displaystyle \iota _{\rho (\xi )}\omega \,}

 is closed (for all

        ξ

    {\displaystyle \xi }

 in

            g

    {\displaystyle {\mathfrak {g}}}

).
Suppose that

          ι

            ρ
            (
            ξ
            )

        ω

    {\displaystyle \iota _{\rho (\xi )}\omega \,}

 is not just closed but also exact, so that

          ι

            ρ
            (
            ξ
            )

        ω

          d

          H

            ξ

    {\displaystyle \iota {\rho (\xi )}\omega =\mathrm {d} H{\xi }}

 for some function

          H

            ξ

        :
        M
        →

          R

    {\displaystyle H_{\xi }:M\to \mathbb {R} }

. If this holds, then one may choose the

          H

            ξ

    {\displaystyle H_{\xi }}

 to make the map

        ξ
        ↦

          H

            ξ

    {\displaystyle \xi \mapsto H_{\xi }}

 linear. A momentum map for the

        G

    {\displaystyle G}

-action on

        (
        M
        ,
        ω
        )

    {\displaystyle (M,\omega )}

 is a map

        μ
        :
        M
        →

              g

            ∗

    {\displaystyle \mu :M\to {\mathfrak {g}}^{*}}

 such that

          d

        (
        ⟨
        μ
        ,
        ξ
        ⟩
        )

          ι

            ρ
            (
            ξ
            )

        ω

    {\displaystyle \mathrm {d} (\langle \mu ,\xi \rangle )=\iota _{\rho (\xi )}\omega }

for all

        ξ

    {\displaystyle \xi }

 in

            g

    {\displaystyle {\mathfrak {g}}}

. Here

        ⟨
        μ
        ,
        ξ
        ⟩

    {\displaystyle \langle \mu ,\xi \rangle }

 is the function from

        M

    {\displaystyle M}

 to

          R

    {\displaystyle \mathbb {R} }

 defined by

        ⟨
        μ
        ,
        ξ
        ⟩
        (
        x
        )

        ⟨
        μ
        (
        x
        )
        ,
        ξ
        ⟩

    {\displaystyle \langle \mu ,\xi \rangle (x)=\langle \mu (x),\xi \rangle }

. The momentum map is uniquely defined up to an additive constant of integration (on each connected component).
A

        G

    {\displaystyle G}

-action on a symplectic manifold

        (
        M
        ,
        ω
        )

    {\displaystyle (M,\omega )}

 is called Hamiltonian if it is symplectic and admits a momentum map.
A momentum map is often also required to be

        G

    {\displaystyle G}

-equivariant, where

        G

    {\displaystyle G}

 acts on

              g

            ∗

    {\displaystyle {\mathfrak {g}}^{*}}

 via the coadjoint action, and sometimes this requirement is included in the definition of a Hamiltonian group action. If the group is compact or semisimple, then the constant of integration can always be chosen to make the momentum map coadjoint equivariant. However, in general the coadjoint action must be modified to make the map equivariant (this is the case for example for the Euclidean group). The modification is by a 1-cocycle on the group with values in

              g

            ∗

    {\displaystyle {\mathfrak {g}}^{*}}

, as first described by Souriau (1970).

Examples of momentum maps
In the case of a Hamiltonian action of the circle

        G

        U
        (
        1
        )

    {\displaystyle G=U(1)}

, the Lie algebra dual

              g

            ∗

    {\displaystyle {\mathfrak {g}}^{*}}

 is naturally identified with

          R

    {\displaystyle \mathbb {R} }

, and the momentum map is simply the Hamiltonian function that generates the circle action.
Another classical case occurs when

        M

    {\displaystyle M}

 is the cotangent bundle of

            R

            3

    {\displaystyle \mathbb {R} ^{3}}

 and

        G

    {\displaystyle G}

 is the Euclidean group generated by rotations and translations. That is,

        G

    {\displaystyle G}

 is a six-dimensional group, the semidirect product of

        SO
        ⁡
        (
        3
        )

    {\displaystyle \operatorname {SO} (3)}

 and

            R

            3

    {\displaystyle \mathbb {R} ^{3}}

. The six components of the momentum map are then the three angular momenta and the three linear momenta.
Let

        N

    {\displaystyle N}

 be a smooth manifold and let

          T

            ∗

        N

    {\displaystyle T^{*}N}

 be its cotangent bundle, with projection map

        π
        :

          T

            ∗

        N
        →
        N

    {\displaystyle \pi :T^{*}N\rightarrow N}

. Let

        τ

    {\displaystyle \tau }

 denote the tautological 1-form on

          T

            ∗

        N

    {\displaystyle T^{*}N}

. Suppose

        G

    {\displaystyle G}

 acts on

        N

    {\displaystyle N}

. The induced action of

        G

    {\displaystyle G}

 on the symplectic manifold

        (

          T

            ∗

        N
        ,

          d

        τ
        )

    {\displaystyle (T^{*}N,\mathrm {d} \tau )}

, given by

        g
        ⋅
        η
        :=
        (

          T

            π
            (
            η
            )

          g

            −
            1

          )

            ∗

        η

    {\displaystyle g\cdot \eta :=(T_{\pi (\eta )}g^{-1})^{*}\eta }

 for

        g
        ∈
        G
        ,
        η
        ∈

          T

            ∗

        N

    {\displaystyle g\in G,\eta \in T^{*}N}

 is Hamiltonian with momentum map

        −

          ι

            ρ
            (
            ξ
            )

        τ

    {\displaystyle -\iota _{\rho (\xi )}\tau }

 for all

        ξ
        ∈

            g

    {\displaystyle \xi \in {\mathfrak {g}}}

. Here

          ι

            ρ
            (
            ξ
            )

        τ

    {\displaystyle \iota _{\rho (\xi )}\tau }

 denotes the contraction of the vector field

        ρ
        (
        ξ
        )

    {\displaystyle \rho (\xi )}

, the infinitesimal action of

        ξ

    {\displaystyle \xi }

, with the 1-form

        τ

    {\displaystyle \tau }

.
The facts mentioned below may be used to generate more examples of momentum maps.

Some facts about momentum maps
Let

        G
        ,
        H

    {\displaystyle G,H}

 be Lie groups with Lie algebras

            g

        ,

            h

    {\displaystyle {\mathfrak {g}},{\mathfrak {h}}}

, respectively.

Let

            O

        (
        F
        )
        ,
        F
        ∈

              g

            ∗

    {\displaystyle {\mathcal {O}}(F),F\in {\mathfrak {g}}^{*}}

 be a coadjoint orbit. Then there exists a unique symplectic structure on

            O

        (
        F
        )

    {\displaystyle {\mathcal {O}}(F)}

 such that inclusion map

            O

        (
        F
        )
        ↪

              g

            ∗

    {\displaystyle {\mathcal {O}}(F)\hookrightarrow {\mathfrak {g}}^{*}}

 is a momentum map.
Let

        G

    {\displaystyle G}

 act on a symplectic manifold

        (
        M
        ,
        ω
        )

    {\displaystyle (M,\omega )}

 with

          Φ

            G

        :
        M
        →

              g

            ∗

    {\displaystyle \Phi _{G}:M\rightarrow {\mathfrak {g}}^{*}}

 a momentum map for the action, and

        ψ
        :
        H
        →
        G

    {\displaystyle \psi :H\rightarrow G}

 be a Lie group homomorphism, inducing an action of

        H

    {\displaystyle H}

 on

        M

    {\displaystyle M}

. Then the action of

        H

    {\displaystyle H}

 on

        M

    {\displaystyle M}

 is also Hamiltonian, with momentum map given by

        (

          d

        ψ

          )

            e

            ∗

        ∘

          Φ

            G

    {\displaystyle (\mathrm {d} \psi )_{e}^{*}\circ \Phi _{G}}

, where

        (

          d

        ψ

          )

            e

            ∗

        :

              g

            ∗

        →

              h

            ∗

    {\displaystyle (\mathrm {d} \psi )_{e}^{}:{\mathfrak {g}}^{}\rightarrow {\mathfrak {h}}^{*}}

 is the dual map to

        (

          d

        ψ

          )

            e

        :

            h

        →

            g

    {\displaystyle (\mathrm {d} \psi )_{e}:{\mathfrak {h}}\rightarrow {\mathfrak {g}}}

 (

        e

    {\displaystyle e}

 denotes the identity element of

        H

    {\displaystyle H}

). A case of special interest is when

        H

    {\displaystyle H}

 is a Lie subgroup of

        G

    {\displaystyle G}

 and

        ψ

    {\displaystyle \psi }

 is the inclusion map.
Let

        (

          M

            1

        ,

          ω

            1

        )

    {\displaystyle (M_{1},\omega _{1})}

 be a Hamiltonian

        G

    {\displaystyle G}

-manifold and

        (

          M

            2

        ,

          ω

            2

        )

    {\displaystyle (M_{2},\omega _{2})}

 a Hamiltonian

        H

    {\displaystyle H}

-manifold. Then the natural action of

        G
        ×
        H

    {\displaystyle G\times H}

 on

        (

          M

            1

        ×

          M

            2

        ,

          ω

            1

        ×

          ω

            2

        )

    {\displaystyle (M_{1}\times M_{2},\omega _{1}\times \omega _{2})}

 is Hamiltonian, with momentum map the direct sum of the two momentum maps

          Φ

            G

    {\displaystyle \Phi _{G}}

 and

          Φ

            H

    {\displaystyle \Phi _{H}}

. Here

          ω

            1

        ×

          ω

            2

        :=

          π

            1

            ∗

          ω

            1

        +

          π

            2

            ∗

          ω

            2

    {\displaystyle \omega _{1}\times \omega _{2}:=\pi _{1}^{}\omega _{1}+\pi _{2}^{}\omega _{2}}

, where

          π

            i

        :

          M

            1

        ×

          M

            2

        →

          M

            i

    {\displaystyle \pi {i}:M{1}\times M_{2}\rightarrow M_{i}}

 denotes the projection map.
Let

        M

    {\displaystyle M}

 be a Hamiltonian

        G

    {\displaystyle G}

-manifold, and

        N

    {\displaystyle N}

 a submanifold of

        M

    {\displaystyle M}

 invariant under

        G

    {\displaystyle G}

 such that the restriction of the symplectic form on

        M

    {\displaystyle M}

 to

        N

    {\displaystyle N}

 is non-degenerate. This imparts a symplectic structure to

        N

    {\displaystyle N}

 in a natural way. Then the action of

        G

    {\displaystyle G}

 on

        N

    {\displaystyle N}

 is also Hamiltonian, with momentum map the composition of the inclusion map with

        M

    {\displaystyle M}

's momentum map.

Connection to Noether's Theorem
Noether's theorem admits a particularly elegant formulation in terms of momentum maps. A brief summary of the relevant objects in this section: let symplectic manifold

        (
        M
        ,
        ω
        )

    {\displaystyle (M,\omega )}

 be the phase space of a Hamiltonian system with Hamiltonian

        H
        :
        M
        →

          R

    {\displaystyle H:M\rightarrow \mathbb {R} }

. Each point

        z

    {\displaystyle z}

 in

        M

    {\displaystyle M}

 represents a state of the system, and its time evolution is governed by

              z
              ˙

          X

            H

    {\displaystyle {\dot {z}}=X_{H}}

 where

          X

            H

    {\displaystyle X_{H}}

 is the Hamiltonian vector field corresponding to the Hamiltonian

        H

    {\displaystyle H}

; that is,

          ι

              X

                H

        ω

        d
        H

    {\displaystyle \iota {X{H}}\omega =dH}

. Time evolution of functions

        F
        :
        M
        →

          R

    {\displaystyle F:M\rightarrow \mathbb {R} }

 can be readily shown to be given by the Poisson bracket

        {
        F
        ,
        H
        }

        ω
        (

          X

            F

        ,

          X

            H

        )

    {\displaystyle {F,H}=\omega (X_{F},X_{H})}

.
Now, Noether's theorem states that if the Hamiltonian is invariant under the (symplectomorphic) group action

        Φ
        (
        g
        ,
        z
        )
        :
        G
        ×
        M
        →
        M

    {\displaystyle \Phi (g,z):G\times M\rightarrow M}

 with infinitesimal generator

        ρ
        (
        ξ
        )

    {\displaystyle \rho (\xi )}

 as defined above, the corresponding momentum map

        J
        (
        ξ
        )

    {\displaystyle J(\xi )}

 will be a constant of motion. Proving this is simple: one simply differentiates the invariance condition

        H
        (
        z
        )

        H
        (
        Φ
        (
        g
        ,
        z
        )
        )

    {\displaystyle H(z)=H(\Phi (g,z))}

 with respect to

        g

    {\displaystyle g}

 to get

                0

                d
                H
                ⋅
                ρ
                (
                ξ
                )

                →

                0

                  ι

                    ρ
                    (
                    ξ
                    )

                  ι

                      X

                        H

                ω

                →

                0

                {
                H
                ,
                J
                (
                ξ
                )
                )
                }

                →

                0

                      J
                      ˙

                (
                ξ
                )

    {\displaystyle {\begin{aligned}0&=dH\cdot \rho (\xi )&\\rightarrow \quad 0&=\iota _{\rho (\xi )}\iota {X{H}}\omega \\rightarrow \quad 0&={H,J(\xi ))}\\rightarrow \quad 0&={\dot {J}}(\xi )\end{aligned}}}

Example: Conservation of Angular Momentum
Consider the classical Kepler problem. Here, the phase is the cotangent bundle of the plane. In Cartesian coordinates,

        H

            1
            2

        (

          p

            1

            2

        +

          p

            2

            2

        )
        −

            1

                q

                  1

                  2

              +

                q

                  2

                  2

    {\displaystyle H={\frac {1}{2}}(p_{1}^{2}+p_{2}^{2})-{\frac {1}{\sqrt {q_{1}^{2}+q_{2}^{2}}}}}

It is easy to see that the Hamiltonian is invariant under circular rotations of the plane. As mentioned earlier, the momentum map for the action on a cotangent bundle induced by an action on the base manifold is

          ι

            ρ
            (
            ξ
            )

        τ

    {\displaystyle \iota _{\rho (\xi )}\tau }

. To compute this, we first note that

        τ

    {\displaystyle \tau }

 is given in coordinates by

          p

            1

        d

          q

            1

        +

          p

            2

        d

          q

            2

    {\displaystyle p_{1}dq_{1}+p_{2}dq_{2}}

. Since there are no

        d

          p

            1

    {\displaystyle dp_{1}}

 or

        d

          p

            2

    {\displaystyle dp_{2}}

 terms in

        τ

    {\displaystyle \tau }

, we actually only need to compute the part of

        ρ
        (
        ξ
        )

    {\displaystyle \rho (\xi )}

 lying in the base manifold

            R

            2

    {\displaystyle \mathbb {R} ^{2}}

, which is:

            d

              d
              g

            [

                  cos
                  ⁡
                  g

                  sin
                  ⁡
                  g

                  −
                  sin
                  ⁡
                  g

                  cos
                  ⁡
                  g

            ]

            [

                    q

                      1

                    q

                      2

            ]

            g

            0

            [

                    q

                      2

                  −

                    q

                      1

            ]

    {\displaystyle {\frac {d}{dg}}{\begin{bmatrix}\cos g&\sin g\-\sin g&\cos g\end{bmatrix}}{\begin{bmatrix}q_{1}\q_{2}\end{bmatrix}}{\Big |}{g=0}={\begin{bmatrix}q{2}\-q_{1}\end{bmatrix}}}

Contracting this with

        τ

    {\displaystyle \tau }

 yields

        J

          p

            1

          q

            2

        −

          p

            2

          q

            1

    {\displaystyle J=p_{1}q_{2}-p_{2}q_{1}}

, and applying Noether's theorem tells us that this quantity, the angular momentum, is conserved throughout the course of the motion. This is equivalent to Kepler's second law.

Symplectic quotients
Suppose that the action of a Lie group

        G

    {\displaystyle G}

 on the symplectic manifold

        (
        M
        ,
        ω
        )

    {\displaystyle (M,\omega )}

 is Hamiltonian, as defined above, with equivariant momentum map

        μ
        :
        M
        →

              g

            ∗

    {\displaystyle \mu :M\to {\mathfrak {g}}^{*}}

. From the Hamiltonian condition, it follows that

          μ

            −
            1

        (
        0
        )

    {\displaystyle \mu ^{-1}(0)}

 is invariant under

        G

    {\displaystyle G}

.
Assume now that

        G

    {\displaystyle G}

 acts freely and properly on

          μ

            −
            1

        (
        0
        )

    {\displaystyle \mu ^{-1}(0)}

. It follows that

        0

    {\displaystyle 0}

 is a regular value of

        μ

    {\displaystyle \mu }

, so

          μ

            −
            1

        (
        0
        )

    {\displaystyle \mu ^{-1}(0)}

 and its quotient

          μ

            −
            1

        (
        0
        )

          /

        G

    {\displaystyle \mu ^{-1}(0)/G}

 are both smooth manifolds. The quotient inherits a symplectic form from

        M

    {\displaystyle M}

; that is, there is a unique symplectic form on the quotient whose pullback to

          μ

            −
            1

        (
        0
        )

    {\displaystyle \mu ^{-1}(0)}

 equals the restriction of

        ω

    {\displaystyle \omega }

 to

          μ

            −
            1

        (
        0
        )

    {\displaystyle \mu ^{-1}(0)}

. Thus, the quotient is a symplectic manifold, called the Marsden–Weinstein quotient, after (Marsden & Weinstein 1974), symplectic quotient, or symplectic reduction of

        M

    {\displaystyle M}

 by

        G

    {\displaystyle G}

 and is denoted

        M

          /

          /

        G

    {\displaystyle M/!!/G}

. Its dimension equals the dimension of

        M

    {\displaystyle M}

 minus twice the dimension of

        G

    {\displaystyle G}

.
More generally, if G does not act freely (but still properly), then (Sjamaar & Lerman 1991) showed that

        M

          /

          /

        G

          μ

            −
            1

        (
        0
        )

          /

        G

    {\displaystyle M/!!/G=\mu ^{-1}(0)/G}

 is a stratified symplectic space, i.e. a stratified space with compatible symplectic structures on the strata.

Flat connections on a surface
The space

          Ω

            1

        (
        Σ
        ,

            g

        )

    {\displaystyle \Omega ^{1}(\Sigma ,{\mathfrak {g}})}

 of connections on the trivial bundle

        Σ
        ×
        G

    {\displaystyle \Sigma \times G}

 on a surface carries an infinite dimensional symplectic form

        ⟨
        α
        ,
        β
        ⟩
        :=

          ∫

            Σ

          tr

        (
        α
        ∧
        β
        )
        .

    {\displaystyle \langle \alpha ,\beta \rangle :=\int _{\Sigma }{\text{tr}}(\alpha \wedge \beta ).}

The gauge group

            G

          Map

        (
        Σ
        ,
        G
        )

    {\displaystyle {\mathcal {G}}={\text{Map}}(\Sigma ,G)}

 acts on connections by conjugation

        g
        ⋅
        A
        :=

          g

            −
            1

        (

          d

        g
        )
        +

          g

            −
            1

        A
        g

    {\displaystyle g\cdot A:=g^{-1}(\mathrm {d} g)+g^{-1}Ag}

. Identify

          Lie

        (

            G

        )

          Ω

            0

        (
        Σ
        ,

            g

        )

          Ω

            2

        (
        Σ
        ,

            g

          )

            ∗

    {\displaystyle {\text{Lie}}({\mathcal {G}})=\Omega ^{0}(\Sigma ,{\mathfrak {g}})=\Omega ^{2}(\Sigma ,{\mathfrak {g}})^{*}}

 via the integration pairing. Then the map

        μ
        :

          Ω

            1

        (
        Σ
        ,

            g

        )
        →

          Ω

            2

        (
        Σ
        ,

            g

        )
        ,

        A

        ↦

        F
        :=

          d

        A
        +

            1
            2

        [
        A
        ∧
        A
        ]

    {\displaystyle \mu :\Omega ^{1}(\Sigma ,{\mathfrak {g}})\rightarrow \Omega ^{2}(\Sigma ,{\mathfrak {g}}),\qquad A\;\mapsto \;F:=\mathrm {d} A+{\frac {1}{2}}[A\wedge A]}

that sends a connection to its curvature is a moment map for the action of the gauge group on connections. In particular the moduli space of flat connections modulo gauge equivalence

          μ

            −
            1

        (
        0
        )

          /

            G

          Ω

            1

        (
        Σ
        ,

            g

        )

          /

          /

            G

    {\displaystyle \mu ^{-1}(0)/{\mathcal {G}}=\Omega ^{1}(\Sigma ,{\mathfrak {g}})/!!/{\mathcal {G}}}

 is given by symplectic reduction.
