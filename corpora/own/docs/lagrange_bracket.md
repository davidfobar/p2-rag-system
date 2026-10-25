# Lagrange bracket

Lagrange bracket

Lagrange brackets are certain expressions closely related to Poisson brackets that were introduced by Joseph Louis Lagrange from 1808 to 1810 for the purposes of mathematical formulation of classical mechanics, but unlike the Poisson brackets, have fallen out of use.

Definition
Suppose that (q1, ..., qn, p1, ..., pn) is a system of canonical coordinates on a phase space. If each of them is expressed as a function of two variables, u and v, then the Lagrange bracket of u and v is defined by the formula

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

        .

    {\displaystyle [u,v]_{p,q}=\sum {i=1}^{n}\left({\frac {\partial q{i}}{\partial u}}{\frac {\partial p_{i}}{\partial v}}-{\frac {\partial p_{i}}{\partial u}}{\frac {\partial q_{i}}{\partial v}}\right).}

Properties
Lagrange brackets do not depend on the system of canonical coordinates (q, p). If (Q,P) = (Q1, ..., Qn, P1, ..., Pn) is another system of canonical coordinates, so that

        Q

        Q
        (
        q
        ,
        p
        )
        ,
        P

        P
        (
        q
        ,
        p
        )

    {\displaystyle Q=Q(q,p),P=P(q,p)}

 is a canonical transformation, then the Lagrange bracket is an invariant of the transformation, in the sense that

        [
        u
        ,
        v

          ]

            q
            ,
            p

        [
        u
        ,
        v

          ]

            Q
            ,
            P

    {\displaystyle [u,v]{q,p}=[u,v]{Q,P}}

 Therefore, the subscripts indicating the canonical coordinates are often omitted.
If Ω is the symplectic form on the 2n-dimensional phase space W and u1,...,u2n form a system of coordinates on W, the symplectic form can be written as

        Ω

            1
            2

          Ω

            i
            j

        d

          u

            i

        ∧
        d

          u

            j

    {\displaystyle \Omega ={\frac {1}{2}}\Omega _{ij}du^{i}\wedge du^{j}}

 where the matrix

          Ω

            i
            j

        [

          u

            i

        ,

          u

            j

          ]

            p
            ,
            q

        ,

        1
        ≤
        i
        ,
        j
        ≤
        2
        n

    {\displaystyle \Omega {ij}=[u{i},u_{j}]_{p,q},\quad 1\leq i,j\leq 2n}

 represents the components of Ω, viewed as a tensor, in the coordinates u. This matrix is the inverse of the matrix formed by the Poisson brackets

            (

              Ω

                −
                1

            )

            i
            j

        {

          u

            i

        ,

          u

            j

        }
        ,

        1
        ≤
        i
        ,
        j
        ≤
        2
        n

    {\displaystyle \left(\Omega ^{-1}\right){ij}={u{i},u_{j}},\quad 1\leq i,j\leq 2n}

 of the coordinates u.
As a corollary of the preceding properties, coordinates (Q1, ..., Qn, P1, ..., Pn) on a phase space are canonical if and only if the Lagrange brackets between them have the form

        [

          Q

            i

        ,

          Q

            j

          ]

            p
            ,
            q

        0
        ,

        [

          P

            i

        ,

          P

            j

          ]

            p
            ,
            q

        0
        ,

        [

          Q

            i

        ,

          P

            j

          ]

            p
            ,
            q

        −
        [

          P

            j

        ,

          Q

            i

          ]

            p
            ,
            q

          δ

            i
            j

        .

    {\displaystyle [Q_{i},Q_{j}]{p,q}=0,\quad [P{i},P_{j}]{p,q}=0,\quad [Q{i},P_{j}]{p,q}=-[P{j},Q_{i}]_{p,q}=\delta _{ij}.}

Lagrange matrix in canonical transformations

The concept of Lagrange brackets can be expanded to that of matrices by defining the Lagrange matrix.
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

, the Lagrange matrix is defined as

            L

        (
        η
        )

          M

            T

        J
        M

    {\textstyle {\mathcal {L}}(\eta )=M^{T}JM}

, where

        J

    {\displaystyle J}

 is the symplectic matrix under the same conventions used to order the set of coordinates. It follows from the definition that:

              L

            i
            j

        (
        η
        )

        [

          M

            T

        J
        M

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

                      k

                  ∂

                    η

                      i

                  ∂

                    ε

                      N
                      +
                      k

                  ∂

                    η

                      j

            −

                  ∂

                    ε

                      N
                      +
                      k

                  ∂

                    η

                      i

                  ∂

                    ε

                      k

                  ∂

                    η

                      j

          )

          ∑

            k

            1

            N

          (

                  ∂

                    Q

                      k

                  ∂

                    η

                      i

                  ∂

                    P

                      k

                  ∂

                    η

                      j

            −

                  ∂

                    P

                      k

                  ∂

                    η

                      i

                  ∂

                    Q

                      k

                  ∂

                    η

                      j

          )

        [

          η

            i

        ,

          η

            j

          ]

            ε

    {\displaystyle {\mathcal {L}}{ij}(\eta )=[M^{T}JM]{ij}=\sum _{k=1}^{N}\left({\frac {\partial \varepsilon _{k}}{\partial \eta _{i}}}{\frac {\partial \varepsilon _{N+k}}{\partial \eta _{j}}}-{\frac {\partial \varepsilon _{N+k}}{\partial \eta _{i}}}{\frac {\partial \varepsilon _{k}}{\partial \eta _{j}}}\right)=\sum {k=1}^{N}\left({\frac {\partial Q{k}}{\partial \eta {i}}}{\frac {\partial P{k}}{\partial \eta {j}}}-{\frac {\partial P{k}}{\partial \eta {i}}}{\frac {\partial Q{k}}{\partial \eta _{j}}}\right)=[\eta _{i},\eta {j}]{\varepsilon }}

The Lagrange matrix satisfies the following known properties:

                      L

                    T

                −

                    L

                    L

                  M

                      2

                      L

                    −
                    1

                (
                η
                )

                −

                  M

                    −
                    1

                J
                (

                  M

                    −
                    1

                  )

                    T

                −

                    P

                (
                η
                )

    {\displaystyle {\begin{aligned}{\mathcal {L}}^{T}&=-{\mathcal {L}}\|{\mathcal {L}}|&={|M|^{2}}\{\mathcal {L}}^{-1}(\eta )&=-M^{-1}J(M^{-1})^{T}=-{\mathcal {P}}(\eta )\\end{aligned}}}

where the

            P

        (
        η
        )

    {\textstyle {\mathcal {P}}(\eta )}

 is known as a Poisson matrix and whose elements correspond to Poisson brackets. The last identity can also be stated as the following:

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
The invariance of Lagrange bracket can be expressed as:

        [

          η

            i

        ,

          η

            j

          ]

            ε

        [

          η

            i

        ,

          η

            j

          ]

            η

          J

            i
            j

    {\textstyle [\eta _{i},\eta {j}]{\varepsilon }=[\eta _{i},\eta {j}]{\eta }=J_{ij}}

, which directly leads to the symplectic condition:

          M

            T

        J
        M

        J

    {\textstyle M^{T}JM=J}

.
