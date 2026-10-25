# Lagrangian system

Lagrangian system

In mathematics, a Lagrangian system is a pair (Y, L), consisting of a smooth fiber bundle Y → X and a Lagrangian density L, which yields the Euler–Lagrange differential operator acting on sections of Y → X.
In classical mechanics, many dynamical systems are Lagrangian systems. The configuration space of such a Lagrangian system is a fiber bundle

        Q
        →

          R

    {\displaystyle Q\rightarrow \mathbb {R} }

 over the time axis

          R

    {\displaystyle \mathbb {R} }

. In particular,

        Q

          R

        ×
        M

    {\displaystyle Q=\mathbb {R} \times M}

 if a reference frame is fixed. In classical field theory, all field systems are the Lagrangian ones.

Lagrangians and Euler–Lagrange operators
A Lagrangian density L (or, simply, a Lagrangian) of order r is defined as an n-form, n = dim X, on the r-order jet manifold JrY of Y.
A Lagrangian L can be introduced as an element of the variational bicomplex of the differential graded algebra O∗∞(Y) of exterior forms on jet manifolds of Y → X. The coboundary operator of this bicomplex contains the variational operator δ which, acting on L, defines the associated Euler–Lagrange operator δL.

In coordinates
Given bundle coordinates xλ, yi on a fiber bundle Y and the adapted coordinates xλ, yi, yiΛ, (Λ = (λ1, ...,λk), |Λ| = k ≤ r) on jet manifolds JrY, a Lagrangian L and its Euler–Lagrange operator read:

        L

            L

        (

          x

            λ

        ,

          y

            i

        ,

          y

            Λ

            i

        )

          d

            n

        x
        ,

    {\displaystyle L={\mathcal {L}}(x^{\lambda },y^{i},y_{\Lambda }^{i})\,d^{n}x,}

        δ
        L

          δ

            i

            L

        d

          y

            i

        ∧

          d

            n

        x
        ,

          δ

            i

            L

          ∂

            i

            L

        +

          ∑

            Λ

        (
        −
        1

          )

            Λ

          d

            Λ

          ∂

            i

            Λ

            L

        ,

    {\displaystyle \delta L=\delta _{i}{\mathcal {L}}\,dy^{i}\wedge d^{n}x,\qquad \delta _{i}{\mathcal {L}}=\partial _{i}{\mathcal {L}}+\sum {|\Lambda |}(-1)^{|\Lambda |}\,d{\Lambda }\,\partial _{i}^{\Lambda }{\mathcal {L}},}

where

          d

            Λ

          d

              λ

                1

        ⋯

          d

              λ

                k

        ,

          d

            λ

          ∂

            λ

        +

          y

            λ

            i

          ∂

            i

        +
        ⋯
        ,

    {\displaystyle d_{\Lambda }=d_{\lambda {1}}\cdots d{\lambda {k}},\qquad d{\lambda }=\partial {\lambda }+y{\lambda }^{i}\partial _{i}+\cdots ,}

denote the total derivatives.
For instance, a first-order Lagrangian and its second-order Euler–Lagrange operator take the form

        L

            L

        (

          x

            λ

        ,

          y

            i

        ,

          y

            λ

            i

        )

          d

            n

        x
        ,

          δ

            i

        L

          ∂

            i

            L

        −

          d

            λ

          ∂

            i

            λ

            L

        .

    {\displaystyle L={\mathcal {L}}(x^{\lambda },y^{i},y_{\lambda }^{i})\,d^{n}x,\qquad \delta _{i}L=\partial {i}{\mathcal {L}}-d{\lambda }\partial _{i}^{\lambda }{\mathcal {L}}.}

Euler–Lagrange equations
The kernel of an Euler–Lagrange operator provides the Euler–Lagrange equations δL = 0.

Cohomology and Noether's theorems
Cohomology of the variational bicomplex leads to the so-called
variational formula

        d
        L

        δ
        L
        +

          d

            H

          Θ

            L

        ,

    {\displaystyle dL=\delta L+d_{H}\Theta _{L},}

where

          d

            H

          Θ

            L

        d

          x

            λ

        ∧

          d

            λ

        ϕ
        ,

        ϕ
        ∈

          O

            ∞

            ∗

        (
        Y
        )

    {\displaystyle d_{H}\Theta {L}=dx^{\lambda }\wedge d{\lambda }\phi ,\qquad \phi \in O_{\infty }^{*}(Y)}

is the total differential and θL is a Lepage equivalent of L. Noether's first theorem and Noether's second theorem are corollaries of this variational formula.

Graded manifolds
Extended to graded manifolds, the variational bicomplex provides description of graded Lagrangian systems of even and odd variables.

Alternative formulations
In a different way, Lagrangians, Euler–Lagrange operators and Euler–Lagrange equations are introduced in the framework of the calculus of variations.

Classical mechanics
In classical mechanics, equations of motion are first and second order differential equations on a manifold M or various fiber bundles Q over

          R

    {\displaystyle \mathbb {R} }

. A solution of the equations of motion is called a motion.
