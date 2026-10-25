# Hitchin system

Hitchin system

In mathematics, the Hitchin integrable system is an integrable system depending on the choice of a complex reductive group and a compact Riemann surface, introduced by Nigel Hitchin in 1987. It lies on the crossroads of algebraic geometry, the theory of Lie algebras and integrable system theory. It also plays an important role in the geometric Langlands correspondence over the field of complex numbers through conformal field theory.
A genus zero analogue of the Hitchin system, the Garnier system, was discovered by René Garnier somewhat earlier as a certain limit of the Schlesinger equations, and Garnier solved his system by defining spectral curves. (The Garnier system is the classical limit of the Gaudin model. In turn, the Schlesinger equations are the classical limit of the Knizhnik–Zamolodchikov equations).
Almost all integrable systems of classical mechanics can be obtained as particular cases of the Hitchin system or their common generalization defined by Bottacin and Markman in 1994.

Description
Using the language of algebraic geometry, the phase space of the system is a partial compactification of the cotangent bundle to the moduli space of stable G-bundles for some reductive group G, on some compact algebraic curve. This space is endowed with a canonical symplectic form. Suppose for simplicity that

        G

          G
          L

        (
        n
        ,

          C

        )

    {\displaystyle G=\mathrm {GL} (n,\mathbb {C} )}

, the general linear group; then the Hamiltonians can be described as follows: the tangent space to the moduli space of G-bundles at the bundle F is

          H

            1

        (
        End
        ⁡
        (
        F
        )
        )
        ,

    {\displaystyle H^{1}(\operatorname {End} (F)),}

which by Serre duality is dual to

        Φ
        ∈

          H

            0

        (
        End
        ⁡
        (
        F
        )
        ⊗
        K
        )
        ,

    {\displaystyle \Phi \in H^{0}(\operatorname {End} (F)\otimes K),}

where

        K

    {\displaystyle K}

 is the canonical bundle, so a pair

        (
        F
        ,
        Φ
        )

    {\displaystyle (F,\Phi )}

called a Hitchin pair or Higgs bundle, defines a point in the cotangent bundle. Taking

        Tr
        ⁡
        (

          Φ

            k

        )
        ,

        k

        1
        ,
        …
        ,
        rank
        ⁡
        (
        G
        )

    {\displaystyle \operatorname {Tr} (\Phi ^{k}),\qquad k=1,\ldots ,\operatorname {rank} (G)}

one obtains elements in

          H

            0

        (

          K

            ⊗
            k

        )
        ,

    {\displaystyle H^{0}(K^{\otimes k}),}

which is a vector space which does not depend on

        (
        F
        ,
        Φ
        )

    {\displaystyle (F,\Phi )}

. So taking any basis in these vector spaces we obtain functions Hi, which are Hitchin's hamiltonians. The construction for general reductive group is similar and uses invariant polynomials on the Lie algebra of G.
For trivial reasons these functions are algebraically independent, and some calculations show that their number is exactly half of the dimension of the phase space. The nontrivial part is a proof of Poisson commutativity of these functions. They therefore define an integrable system in the symplectic or Arnol'd–Liouville sense.

Hitchin fibration
The Hitchin fibration is the map from the moduli space of Hitchin pairs to characteristic polynomials, a higher genus analogue of the map Garnier used to define the spectral curves. Ngô (2006, 2010) used Hitchin fibrations over finite fields in his proof of the fundamental lemma.
To be more precise, the version of Hitchin fibration that is used by Ngô has source the moduli stack of Hitchin pairs, instead of the moduli space. Let

            g

    {\displaystyle {\mathfrak {g}}}

 be the Lie algebra of the reductive algebraic group

        G

    {\displaystyle G}

. We have the adjoint action of

        G

    {\displaystyle G}

 on

            g

    {\displaystyle {\mathfrak {g}}}

. We can then take the stack quotient

            g

          /

        G

    {\displaystyle {\mathfrak {g}}/G}

 and the GIT quotient

            g

          /

          /

        G

    {\displaystyle {\mathfrak {g}}/!/G}

, and there is a natural morphism

        χ
        :

            g

          /

        G
        →

            g

          /

          /

        G

    {\displaystyle \chi :{\mathfrak {g}}/G\to {\mathfrak {g}}/!/G}

. There is also the natural scaling action of the multiplicative group

            G

            m

    {\displaystyle \mathbb {G} _{m}}

 on

            g

    {\displaystyle {\mathfrak {g}}}

, which descends to the stack and GIT quotients. Furthermore, the morphism

        χ

    {\displaystyle \chi }

 is equivariant with respect to the

            G

            m

    {\displaystyle \mathbb {G} _{m}}

-actions. Therefore, given any line bundle

        L

    {\displaystyle L}

 on our curve

        C

    {\displaystyle C}

, we can twist the morphism

        χ

    {\displaystyle \chi }

 by the

            G

            m

    {\displaystyle \mathbb {G} _{m}}

-torsor, and obtain a morphism

          χ

            L

        :
        (

            g

          /

        G

          )

            L

        →
        (

            g

          /

          /

        G

          )

            L

    {\displaystyle \chi {L}:({\mathfrak {g}}/G){L}\to ({\mathfrak {g}}/!/G)_{L}}

 of stacks over

        C

    {\displaystyle C}

. Finally, the moduli stack of

        L

    {\displaystyle L}

-twisted Higgs bundles is recovered as the section stack

        H
        i
        g
        g
        s

        S
        e
        c
        t
        (
        C
        ,
        (

            g

          /

        G

          )

            L

        )

    {\displaystyle Higgs=Sect(C,({\mathfrak {g}}/G)_{L})}

; the corresponding Hitchin base is recovered as

        A
        (
        C
        ,
        L
        )
        :=
        S
        e
        c
        t
        (
        C
        ,
        (

            g

          /

          /

        G

          )

            L

        )

    {\displaystyle A(C,L):=Sect(C,({\mathfrak {g}}/!/G)_{L})}

, which is represented by a vector space; and the Hitchin morphism at the stack level

        h
        :
        H
        i
        g
        g
        s
        →
        A
        (
        C
        ,
        L
        )

    {\displaystyle h:Higgs\to A(C,L)}

 is simply the morphism induced by the morphism

          χ

            L

    {\displaystyle \chi _{L}}

 above. Note that this definition is not relevant to semistability. To obtain the Hitchin fibration mentioned above, we need to take

        L

    {\displaystyle L}

 to be the canonical bundle, restrict to the semistable part of

        H
        i
        g
        g
        s

    {\displaystyle Higgs}

, and then take the induced morphism on the moduli space. To be even more precise, the version of

        H
        i
        g
        g
        s

    {\displaystyle Higgs}

 that is used by Ngô often has the restriction that

        deg
        ⁡
        (
        L
        )
        ≥
        2
        g

    {\displaystyle \deg(L)\geq 2g}

, so that it cannot be the canonical bundle. This condition is added to guarantee that the topology of the Hitchin morphism is, in a precise sense, determined by its restriction to the smooth part, see (Chaudouard & Laumon 2016) for the vector bundle case.
