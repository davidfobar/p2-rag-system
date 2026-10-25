# Elasticity tensor

Elasticity tensor

The elasticity tensor is a fourth-rank tensor describing the stress-strain relation in
a linear elastic material. Other names are elastic modulus tensor and stiffness tensor. Common symbols include

          C

    {\displaystyle \mathbf {C} }

 and

          Y

    {\displaystyle \mathbf {Y} }

.
The defining equation can be written as

          T

            i
            j

          C

            i
            j
            k
            l

          E

            k
            l

    {\displaystyle T^{ij}=C^{ijkl}E_{kl}}

where

          T

            i
            j

    {\displaystyle T^{ij}}

 and

          E

            k
            l

    {\displaystyle E_{kl}}

 are the components of the Cauchy stress tensor and infinitesimal strain tensor, and

          C

            i
            j
            k
            l

    {\displaystyle C^{ijkl}}

 are the components of the elasticity tensor. Summation over repeated indices is implied. This relationship can be interpreted as a generalization of Hooke's law to a 3D continuum.
A general fourth-rank tensor

          F

    {\displaystyle \mathbf {F} }

 in 3D has 34 = 81 independent components

          F

            i
            j
            k
            l

    {\displaystyle F_{ijkl}}

, but the elasticity tensor has at most 21 independent components. This fact follows from the symmetry of the stress and strain tensors, together with the requirement that the stress derives from an elastic energy potential. For isotropic materials, the elasticity tensor has just two independent components, which can be chosen to be the bulk modulus and shear modulus.

Definition
The most general linear relation between two second-rank tensors

          T

        ,

          E

    {\displaystyle \mathbf {T} ,\mathbf {E} }

 is

          T

            i
            j

          C

            i
            j
            k
            l

          E

            k
            l

    {\displaystyle T^{ij}=C^{ijkl}E_{kl}}

where

          C

            i
            j
            k
            l

    {\displaystyle C^{ijkl}}

 are the components of a fourth-rank tensor

          C

    {\displaystyle \mathbf {C} }

. The elasticity tensor is defined as

          C

    {\displaystyle \mathbf {C} }

 for the case where

          T

    {\displaystyle \mathbf {T} }

 and

          E

    {\displaystyle \mathbf {E} }

 are the stress and strain tensors, respectively.
The compliance tensor

          K

    {\displaystyle \mathbf {K} }

 is defined from the inverse stress-strain relation:

          E

            i
            j

          K

            i
            j
            k
            l

          T

            k
            l

    {\displaystyle E^{ij}=K^{ijkl}T_{kl}}

The two are related by

          K

            i
            j
            p
            q

          C

            p
            q
            k
            l

            1
            2

          (

              δ

                i

                k

              δ

                j

                l

            +

              δ

                i

                l

              δ

                j

                k

          )

    {\displaystyle K_{ijpq}C^{pqkl}={\frac {1}{2}}\left(\delta _{i}^{k}\delta _{j}^{l}+\delta _{i}^{l}\delta _{j}^{k}\right)}

where

          δ

            n

            m

    {\displaystyle \delta _{n}^{m}}

 is the Kronecker delta.
Unless otherwise noted, this article assumes

          C

    {\displaystyle \mathbf {C} }

 is defined from the stress-strain relation of a linear elastic material, in the limit of small strain.

Special cases

Isotropic
For an isotropic material,

          C

    {\displaystyle \mathbf {C} }

 simplifies to

          C

            i
            j
            k
            l

        λ

          (
          X
          )

          g

            i
            j

          g

            k
            l

        +
        μ

          (
          X
          )

          (

              g

                i
                k

              g

                j
                l

            +

              g

                i
                l

              g

                k
                j

          )

    {\displaystyle C^{ijkl}=\lambda !\left(X\right)g^{ij}g^{kl}+\mu !\left(X\right)\left(g^{ik}g^{jl}+g^{il}g^{kj}\right)}

where

        λ

    {\displaystyle \lambda }

 and

        μ

    {\displaystyle \mu }

 are scalar functions of the material coordinates

        X

    {\displaystyle X}

, and

          g

    {\displaystyle \mathbf {g} }

 is the metric tensor in the reference frame of the material. In an orthonormal Cartesian coordinate basis, there is no distinction between upper and lower indices, and the metric tensor can be replaced with the Kronecker delta:

          C

            i
            j
            k
            l

        λ

          (
          X
          )

          δ

            i
            j

          δ

            k
            l

        +
        μ

          (
          X
          )

          (

              δ

                i
                k

              δ

                j
                l

            +

              δ

                i
                l

              δ

                k
                j

          )

          [Cartesian coordinates]

    {\displaystyle C_{ijkl}=\lambda !\left(X\right)\delta _{ij}\delta _{kl}+\mu !\left(X\right)\left(\delta _{ik}\delta _{jl}+\delta _{il}\delta _{kj}\right)\quad {\text{[Cartesian coordinates]}}}

Substituting the first equation into the stress-strain relation and summing over repeated indices gives

          T

            i
            j

        λ

          (
          X
          )

        ⋅

          (

              T
              r

              E

          )

          g

            i
            j

        +
        2
        μ

          (
          X
          )

          E

            i
            j

    {\displaystyle T^{ij}=\lambda !\left(X\right)\cdot \left(\mathrm {Tr} \,\mathbf {E} \right)g^{ij}+2\mu !\left(X\right)E^{ij}}

where

          T
          r

          E

        ≡

          E

            i

            i

    {\displaystyle \mathrm {Tr} \,\mathbf {E} \equiv E_{\,i}^{i}}

 is the trace of

          E

    {\displaystyle \mathbf {E} }

.
In this form,

        μ

    {\displaystyle \mu }

 and

        λ

    {\displaystyle \lambda }

 can be identified with the first and second Lamé parameters.
An equivalent expression is

          T

            i
            j

        K

          (
          X
          )

        ⋅

          (

              T
              r

              E

          )

          g

            i
            j

        +
        2
        μ

          (
          X
          )

          Σ

            i
            j

    {\displaystyle T^{ij}=K!\left(X\right)\cdot \left(\mathrm {Tr} \,\mathbf {E} \right)g^{ij}+2\mu !\left(X\right)\Sigma ^{ij}}

where

        K

        λ
        +
        (
        2

          /

        3
        )
        μ

    {\displaystyle K=\lambda +(2/3)\mu }

 is the bulk modulus, and

          Σ

            i
            j

        ≡

          E

            i
            j

        −
        (
        1

          /

        3
        )

          (

              T
              r

              E

          )

          g

            i
            j

    {\displaystyle \Sigma ^{ij}\equiv E^{ij}-(1/3)\left(\mathrm {Tr} \,\mathbf {E} \right)g^{ij}}

are the components of the shear tensor

          Σ

    {\displaystyle \mathbf {\Sigma } }

.

Cubic crystals
The elasticity tensor of a cubic crystal has components

                  C

                    i
                    j
                    k
                    l

                λ

                  g

                    i
                    j

                  g

                    k
                    l

                +
                μ

                  (

                      g

                        i
                        k

                      g

                        j
                        l

                    +

                      g

                        i
                        l

                      g

                        k
                        j

                  )

                +
                α

                  (

                      a

                        i

                      a

                        j

                      a

                        k

                      a

                        l

                    +

                      b

                        i

                      b

                        j

                      b

                        k

                      b

                        l

                    +

                      c

                        i

                      c

                        j

                      c

                        k

                      c

                        l

                  )

    {\displaystyle {\begin{aligned}C^{ijkl}&=\lambda g^{ij}g^{kl}+\mu \left(g^{ik}g^{jl}+g^{il}g^{kj}\right)\&+\alpha \left(a^{i}a^{j}a^{k}a^{l}+b^{i}b^{j}b^{k}b^{l}+c^{i}c^{j}c^{k}c^{l}\right)\end{aligned}}}

where

          a

    {\displaystyle \mathbf {a} }

,

          b

    {\displaystyle \mathbf {b} }

, and

          c

    {\displaystyle \mathbf {c} }

 are unit vectors corresponding to the three mutually perpendicular axes of the crystal unit cell. The coefficients

        λ

    {\displaystyle \lambda }

,

        μ

    {\displaystyle \mu }

, and

        α

    {\displaystyle \alpha }

 are scalars; because they are coordinate-independent, they are intrinsic material constants. Thus, a crystal with cubic symmetry is described by three independent elastic constants.
In an orthonormal Cartesian coordinate basis, there is no distinction between upper and lower indices, and

          g

            i
            j

    {\displaystyle g^{ij}}

 is the Kronecker delta, so the expression simplifies to

                  C

                    i
                    j
                    k
                    l

                λ

                  δ

                    i
                    j

                  δ

                    k
                    l

                +
                μ

                  (

                      δ

                        i
                        k

                      δ

                        j
                        l

                    +

                      δ

                        i
                        l

                      δ

                        k
                        j

                  )

                +
                α

                  (

                      a

                        i

                      a

                        j

                      a

                        k

                      a

                        l

                    +

                      b

                        i

                      b

                        j

                      b

                        k

                      b

                        l

                    +

                      c

                        i

                      c

                        j

                      c

                        k

                      c

                        l

                  )

    {\displaystyle {\begin{aligned}C_{ijkl}&=\lambda \delta _{ij}\delta _{kl}+\mu \left(\delta _{ik}\delta _{jl}+\delta _{il}\delta {kj}\right)\&+\alpha \left(a{i}a_{j}a_{k}a_{l}+b_{i}b_{j}b_{k}b_{l}+c_{i}c_{j}c_{k}c_{l}\right)\end{aligned}}}

Other crystal classes
There are similar expressions for the components of

          C

    {\displaystyle \mathbf {C} }

 in other crystal symmetry classes. The number of independent elastic constants for several of these is given in table 1.

Properties

Symmetries
The elasticity tensor has several symmetries that follow directly from its defining equation

          T

            i
            j

          C

            i
            j
            k
            l

          E

            k
            l

    {\displaystyle T^{ij}=C^{ijkl}E_{kl}}

. The symmetry of the stress and strain tensors implies that

          C

            i
            j
            k
            l

          C

            j
            i
            k
            l

          and

          C

            i
            j
            k
            l

          C

            i
            j
            l
            k

        ,

    {\displaystyle C_{ijkl}=C_{jikl}\qquad {\text{and}}\qquad C_{ijkl}=C_{ijlk},}

Usually, one also assumes that the stress derives from an elastic energy potential

        U

    {\displaystyle U}

:

          T

            i
            j

              ∂
              U

              ∂

                E

                  i
                  j

    {\displaystyle T^{ij}={\frac {\partial U}{\partial E_{ij}}}}

which implies

          C

            i
            j
            k
            l

                ∂

                  2

              U

              ∂

                E

                  i
                  j

              ∂

                E

                  k
                  l

    {\displaystyle C_{ijkl}={\frac {\partial ^{2}U}{\partial E_{ij}\partial E_{kl}}}}

Hence,

          C

    {\displaystyle \mathbf {C} }

 must be symmetric under interchange of the first and second pairs of indices:

          C

            i
            j
            k
            l

          C

            k
            l
            i
            j

    {\displaystyle C_{ijkl}=C_{klij}}

The symmetries listed above reduce the number of independent components from 81 to 21. If a material has additional symmetries, then this number is further reduced.

Transformations
Under rotation, the components

          C

            i
            j
            k
            l

    {\displaystyle C^{ijkl}}

 transform as

          C

            i
            j
            k
            l

          ′

          R

            i
            p

          R

            j
            q

          R

            k
            r

          R

            l
            s

          C

            p
            q
            r
            s

    {\displaystyle C'{ijkl}=R{ip}R_{jq}R_{kr}R_{ls}C^{pqrs}}

where

          C

            i
            j
            k
            l

          ′

    {\displaystyle C'_{ijkl}}

 are the covariant components in the rotated basis, and

          R

            i
            j

    {\displaystyle R_{ij}}

are the elements of the corresponding rotation matrix. A similar transformation rule holds for other linear transformations.

Invariants
The components of

          C

    {\displaystyle \mathbf {C} }

 generally acquire different values under a change of basis. Nevertheless, for certain types of transformations,
there are specific combinations of components, called invariants, that remain unchanged. Invariants are defined with respect to a given set of transformations, formally known as a group operation. For example, an invariant with respect to the group of proper orthogonal transformations, called SO(3), is a quantity that remains constant under arbitrary 3D rotations.

          C

    {\displaystyle \mathbf {C} }

 possesses two linear invariants and seven quadratic invariants with respect to SO(3). The linear invariants are

                  L

                    1

                  C

                    i
                    j

                    i
                    j

                  L

                    2

                  C

                    j
                    j

                    i
                    i

    {\displaystyle {\begin{aligned}L_{1}&=C_{\,\,\,ij}^{ij}\L_{2}&=C_{\,\,\,jj}^{ii}\end{aligned}}}

and the quadratic invariants are

          {

              L

                1

                2

            ,

              L

                2

                2

            ,

              L

                1

              L

                2

            ,

              C

                i
                j
                k
                l

              C

                i
                j
                k
                l

            ,

              C

                i
                i
                k
                l

              C

                j
                j
                k
                l

            ,

              C

                i
                i
                k
                l

              C

                j
                k
                j
                l

            ,

              C

                k
                i
                i
                l

              C

                k
                j
                j
                l

          }

    {\displaystyle \left{L_{1}^{2},\,L_{2}^{2},\,L_{1}L_{2},\,C_{ijkl}C^{ijkl},\,C_{iikl}C^{jjkl},\,C_{iikl}C^{jkjl},\,C_{kiil}C^{kjjl}\right}}

These quantities are linearly independent, that is, none can be expressed as a linear combination of the others.
They are also complete, in the sense that there are no additional independent linear or quadratic invariants.

Decompositions

A common strategy in tensor analysis is to decompose a tensor into simpler components that can be analyzed separately. For example, the
displacement gradient tensor

          W

          ∇

          ξ

    {\displaystyle \mathbf {W} =\mathbf {\nabla } \mathbf {\xi } }

 can be decomposed as

          W

            1
            3

        Θ

          g

        +

          Σ

        +

          R

    {\displaystyle \mathbf {W} ={\frac {1}{3}}\Theta \mathbf {g} +\mathbf {\Sigma } +\mathbf {R} }

where

        Θ

    {\displaystyle \Theta }

 is a rank-0 tensor (a scalar), equal to the trace of

          W

    {\displaystyle \mathbf {W} }

;

          Σ

    {\displaystyle \mathbf {\Sigma } }

 is symmetric and trace-free; and

          R

    {\displaystyle \mathbf {R} }

 is antisymmetric. Component-wise,

                  Σ

                    i
                    j

                ≡

                  W

                    (
                    i
                    j
                    )

                    1
                    2

                  (

                      W

                        i
                        j

                    +

                      W

                        j
                        i

                  )

                −

                    1
                    3

                  (

                      T
                      r

                      W

                  )

                  g

                    i
                    j

                  R

                    i
                    j

                ≡

                  W

                    [
                    i
                    j
                    ]

                    1
                    2

                  (

                      W

                        i
                        j

                    −

                      W

                        j
                        i

                  )

    {\displaystyle {\begin{aligned}\Sigma ^{ij}\equiv W^{(ij)}&={\frac {1}{2}}\left(W^{ij}+W^{ji}\right)-{\frac {1}{3}}\left(\mathrm {Tr} \,\mathbf {W} \right)g^{ij}\R^{ij}\equiv W^{[ij]}&={\frac {1}{2}}\left(W^{ij}-W^{ji}\right)\end{aligned}}}

Here and later, symmetrization and antisymmetrization are denoted by

        (
        i
        j
        )

    {\displaystyle (ij)}

 and

        [
        i
        j
        ]

    {\displaystyle [ij]}

, respectively. This decomposition is irreducible, in the sense of being invariant under rotations, and is an important tool in the conceptual development of continuum mechanics.
The elasticity tensor has rank 4, and its decompositions are more complex and varied than those of a rank-2 tensor. A few examples are described below.

M and N tensors
This decomposition is obtained by symmeterization and antisymmeterization of the middle two indices:

          C

            i
            j
            k
            l

          M

            i
            j
            k
            l

        +

          N

            i
            j
            k
            l

    {\displaystyle C^{ijkl}=M^{ijkl}+N^{ijkl}}

where

                  M

                    i
                    j
                    k
                    l

                ≡

                  C

                    i
                    (
                    j
                    k
                    )
                    l

                    1
                    2

                  (

                      C

                        i
                        j
                        k
                        l

                    +

                      C

                        i
                        k
                        j
                        l

                  )

                  N

                    i
                    j
                    k
                    l

                ≡

                  C

                    i
                    [
                    j
                    k
                    ]
                    l

                    1
                    2

                  (

                      C

                        i
                        j
                        k
                        l

                    −

                      C

                        i
                        k
                        j
                        l

                  )

    {\displaystyle {\begin{aligned}M^{ijkl}\equiv C^{i(jk)l}={\frac {1}{2}}\left(C^{ijkl}+C^{ikjl}\right)\N^{ijkl}\equiv C^{i[jk]l}={\frac {1}{2}}\left(C^{ijkl}-C^{ikjl}\right)\end{aligned}}}

A disadvantage of this decomposition is that

          M

            i
            j
            k
            l

    {\displaystyle M^{ijkl}}

 and

          N

            i
            j
            k
            l

    {\displaystyle N^{ijkl}}

 do not
obey all original symmetries of

          C

            i
            j
            k
            l

    {\displaystyle C^{ijkl}}

, as they are not symmetric under interchange of the first two indices. In addition, it is not irreducible, so it is not invariant under linear transformations such as rotations.

Irreducible representations

An irreducible representation can be built by considering the notion of a totally symmetric tensor, which is invariant under the interchange of any two indices. A totally symmetric tensor

          S

    {\displaystyle \mathbf {S} }

 can be constructed from

          C

    {\displaystyle \mathbf {C} }

 by summing over all

        4
        !

        24

    {\displaystyle 4!=24}

 permutations of the indices

                  S

                    i
                    j
                    k
                    l

                    1

                      4
                      !

                  ∑

                    (
                    i
                    ,
                    j
                    ,
                    k
                    ,
                    l
                    )
                    ∈

                      S

                        4

                  C

                    i
                    j
                    k
                    l

                    1

                      4
                      !

                  (

                      C

                        i
                        j
                        k
                        l

                    +

                      C

                        j
                        i
                        k
                        l

                    +

                      C

                        i
                        k
                        j
                        l

                    +
                    …

                  )

    {\displaystyle {\begin{aligned}S^{ijkl}&={\frac {1}{4!}}\sum {(i,j,k,l)\in S{4}}C^{ijkl}\&={\frac {1}{4!}}\left(C^{ijkl}+C^{jikl}+C^{ikjl}+\ldots \right)\end{aligned}}}

where

            S

            4

    {\displaystyle \mathbb {S} _{4}}

 is the set of all permutations of the four indices. Owing to the symmetries of

          C

            i
            j
            k
            l

    {\displaystyle C^{ijkl}}

, this sum reduces to

          S

            i
            j
            k
            l

            1
            3

          (

              C

                i
                j
                k
                l

            +

              C

                i
                k
                l
                j

            +

              C

                i
                l
                j
                k

          )

    {\displaystyle S^{ijkl}={\frac {1}{3}}\left(C^{ijkl}+C^{iklj}+C^{iljk}\right)}

The difference

          A

            i
            j
            k
            l

        ≡

          C

            i
            j
            k
            l

        −

          S

            i
            j
            k
            l

            1
            3

          (

            2

              C

                i
                j
                k
                l

            −

              C

                i
                l
                k
                j

            −

              C

                i
                k
                l
                j

          )

    {\displaystyle A^{ijkl}\equiv C^{ijkl}-S^{ijkl}={\frac {1}{3}}\left(2C^{ijkl}-C^{ilkj}-C^{iklj}\right)}

is an asymmetric tensor (not antisymmetric). The decomposition

          C

            i
            j
            k
            l

          S

            i
            j
            k
            l

        +

          A

            i
            j
            k
            l

    {\displaystyle C^{ijkl}=S^{ijkl}+A^{ijkl}}

 can be shown to be unique and irreducible with respect to

            S

            4

    {\displaystyle \mathbb {S} _{4}}

. In other words, any additional symmetrization operations on

          S

    {\displaystyle \mathbf {S} }

 or

          A

    {\displaystyle \mathbf {A} }

 will either leave it unchanged or evaluate to zero. It is also irreducible with respect to arbitrary linear transformations, that is, the general linear group

        G
        (
        3
        ,

          R

        )

    {\displaystyle G(3,\mathbb {R} )}

.
However, this decomposition is not irreducible with respect to the group of rotations SO(3). Instead,

          S

    {\displaystyle \mathbf {S} }

 decomposes into three irreducible parts, and

          A

    {\displaystyle \mathbf {A} }

 into two:

                  C

                    i
                    j
                    k
                    l

                  S

                    i
                    j
                    k
                    l

                +

                  A

                    i
                    j
                    k
                    l

                  (

                        (
                        1
                        )

                      S

                        i
                        j
                        k
                        l

                    +

                        (
                        2
                        )

                      S

                        i
                        j
                        k
                        l

                    +

                        (
                        3
                        )

                      S

                        i
                        j
                        k
                        l

                  )

                +

                  (

                        (
                        1
                        )

                      A

                        i
                        j
                        k
                        l

                      +

                        (
                        2
                        )

                      A

                        i
                        j
                        k
                        l

                  )

    {\displaystyle {\begin{aligned}C^{ijkl}&=S^{ijkl}+A^{ijkl}\&=\left(^{(1)}!S^{ijkl}+\,^{(2)}!S^{ijkl}+\,^{(3)}!S^{ijkl}\right)+\,\left(^{(1)}!A^{ijkl}+^{(2)}!A^{ijkl}\right)\end{aligned}}}

See Itin (2020) for explicit expressions in terms of the components of

          C

    {\displaystyle \mathbf {C} }

.
This representation decomposes the space of elasticity tensors into a direct sum of subspaces:

            C

          (

                (
                1
                )

                C

            ⊕

                (
                2
                )

                C

            ⊕

                (
                3
                )

                C

          )

        ⊕

          (

                (
                4
                )

                C

            ⊕

                (
                5
                )

                C

          )

    {\displaystyle {\mathcal {C}}=\left(^{(1)}!{\mathcal {C}}\oplus \,^{(2)}!{\mathcal {C}}\oplus \,^{(3)}!{\mathcal {C}}\right)\oplus \,\left(^{(4)}!{\mathcal {C}}\oplus \,^{(5)}!{\mathcal {C}}\right)}

with dimensions

        21

        (
        1
        ⊕
        5
        ⊕
        9
        )
        ⊕
        (
        1
        ⊕
        5
        )

    {\displaystyle 21=(1\oplus 5\oplus 9)\oplus (1\oplus 5)}

These subspaces are each isomorphic to a harmonic tensor space

            H

            n

        (

            R

            3

        )

    {\displaystyle \mathbb {H} _{n}(\mathbb {R} ^{3})}

. Here,

            H

            n

        (

            R

            3

        )

    {\displaystyle \mathbb {H} _{n}(\mathbb {R} ^{3})}

 is the space of 3D, totally symmetric, traceless tensors of rank

        n

    {\displaystyle n}

. In particular,

            (
            1
            )

            C

    {\displaystyle ^{(1)}!{\mathcal {C}}}

 and

            (
            4
            )

            C

    {\displaystyle ^{(4)}!{\mathcal {C}}}

 correspond to

            H

            0

    {\displaystyle \mathbb {H} _{0}}

,

            (
            2
            )

            C

    {\displaystyle ^{(2)}!{\mathcal {C}}}

 and

            (
            5
            )

            C

    {\displaystyle ^{(5)}!{\mathcal {C}}}

 correspond to

            H

            2

    {\displaystyle \mathbb {H} _{2}}

, and

            (
            3
            )

            C

    {\displaystyle ^{(3)}!{\mathcal {C}}}

 corresponds to

            H

            4

    {\displaystyle \mathbb {H} _{4}}

.
