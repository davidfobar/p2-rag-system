# Dirac structure

Dirac structure

In mathematics a Dirac structure is a geometric structure generalizing both symplectic structures and Poisson structures, and having several applications to mechanics. It is based on the notion of the Dirac bracket constraint introduced by Paul Dirac and was first introduced by Ted Courant and Alan Weinstein.

Linear Dirac structures
Let

        V

    {\displaystyle V}

 be a real vector space, and

          V

            ∗

    {\displaystyle V^{*}}

 its dual. A (linear) Dirac structure on

        V

    {\displaystyle V}

 is a linear subspace

        D

    {\displaystyle D}

 of

        V
        ×

          V

            ∗

    {\displaystyle V\times V^{*}}

 satisfying

for all

        (
        v
        ,
        α
        )
        ∈
        D

    {\displaystyle (v,\alpha )\in D}

 one has

          ⟨

            α
            ,

            v

          ⟩

        0

    {\displaystyle \left\langle \alpha ,\,v\right\rangle =0}

,

        D

    {\displaystyle D}

 is maximal with respect to this property.
In particular, if

        V

    {\displaystyle V}

 is finite dimensional, then the second criterion is satisfied if

        dim
        ⁡
        D

        dim
        ⁡
        V

    {\displaystyle \dim D=\dim V}

. Similar definitions can be made for vector spaces over other fields.
An alternative (equivalent) definition often used is that

        D

    {\displaystyle D}

 satisfies

        D

          D

            ⊥

    {\displaystyle D=D^{\perp }}

, where orthogonality is with respect to the symmetric bilinear form on

        V
        ×

          V

            ∗

    {\displaystyle V\times V^{*}}

 given by

            ⟨

        (
        v
        ,
        α
        )
        ,

        (
        u
        ,
        β
        )

            ⟩

          ⟨

            α
            ,
            u

          ⟩

        +

          ⟨

            β
            ,
            v

          ⟩

    {\displaystyle {\bigl \langle }(v,\alpha ),\,(u,\beta ){\bigr \rangle }=\left\langle \alpha ,u\right\rangle +\left\langle \beta ,v\right\rangle }

.

Examples
If

        U
        ⊂
        V

    {\displaystyle U\subset V}

 is a vector subspace, then

        D

        U
        ×

          U

            ∘

    {\displaystyle D=U\times U^{\circ }}

 is a Dirac structure on

        V

    {\displaystyle V}

, where

          U

            ∘

    {\displaystyle U^{\circ }}

 is the annihilator of

        U

    {\displaystyle U}

; that is,

          U

            ∘

          {

            α
            ∈

              V

                ∗

            ∣

              α

                U

            0

          }

    {\displaystyle U^{\circ }=\left{\alpha \in V^{*}\mid \alpha _{\vert U}=0\right}}

.

Let

        ω
        :
        V
        →

          V

            ∗

    {\displaystyle \omega :V\to V^{*}}

 be a skew-symmetric linear map, then the graph of

        ω

    {\displaystyle \omega }

 is a Dirac structure.
Similarly, if

        Π
        :

          V

            ∗

        →
        V

    {\displaystyle \Pi :V^{*}\to V}

 is a skew-symmetric linear map, then its graph is a Dirac structure.

Dirac structures on manifolds
A Dirac structure

            D

    {\displaystyle {\mathfrak {D}}}

 on a smooth manifold

        M

    {\displaystyle M}

 is an assignment of a (linear) Dirac structure on the tangent space to

        M

    {\displaystyle M}

 at

        m

    {\displaystyle m}

, for each

        m
        ∈
        M

    {\displaystyle m\in M}

. That is,

for each

        m
        ∈
        M

    {\displaystyle m\in M}

, a Dirac subspace

          D

            m

    {\displaystyle D_{m}}

 of the space

          T

            m

        M
        ×

          T

            m

            ∗

        M

    {\displaystyle T_{m}M\times T_{m}^{*}M}

.
Many authors, in particular in geometry rather than the mechanics applications, require a Dirac structure to satisfy an extra integrability condition as follows:

suppose

        (

          X

            i

        ,

          α

            i

        )

    {\displaystyle (X_{i},\alpha _{i})}

 are sections of the Dirac bundle

            D

        →
        M

    {\displaystyle {\mathfrak {D}}\to M}

 (

        i

        1
        ,
        2
        ,
        3

    {\displaystyle i=1,2,3}

) then

          ⟨

              L

                  X

                    1

            (

              α

                2

            )
            ,

              X

                3

          ⟩

        +

          ⟨

              L

                  X

                    2

            (

              α

                3

            )
            ,

              X

                1

          ⟩

        +

          ⟨

              L

                  X

                    3

            (

              α

                1

            )
            ,

              X

                2

          ⟩

        0.

    {\displaystyle \left\langle L_{X_{1}}(\alpha {2}),\,X{3}\right\rangle +\left\langle L_{X_{2}}(\alpha {3}),\,X{1}\right\rangle +\left\langle L_{X_{3}}(\alpha {1}),\,X{2}\right\rangle =0.}

In the mechanics literature this would be called a closed or integrable Dirac structure.

Examples

Let

        Δ

    {\displaystyle \Delta }

 be a smooth distribution of constant rank on a manifold

        M

    {\displaystyle M}

, and for each

        m
        ∈
        M

    {\displaystyle m\in M}

 let

          D

            m

        {
        (
        u
        ,
        α
        )
        ∈

          T

            m

        M
        ×

          T

            m

            ∗

        M
        ∣
        u
        ∈
        Δ
        (
        m
        )
        ,

        α
        ∈
        Δ
        (
        m

          )

            ∘

        }

    {\displaystyle D_{m}={(u,\alpha )\in T_{m}M\times T_{m}^{*}M\mid u\in \Delta (m),\,\alpha \in \Delta (m)^{\circ }}}

, then the union of these subspaces over

        m

    {\displaystyle m}

 forms a Dirac structure on

        M

    {\displaystyle M}

.

Let

        ω

    {\displaystyle \omega }

 be a symplectic form on a manifold

        M

    {\displaystyle M}

, then its graph is a (closed) Dirac structure. More generally, this is true for any closed 2-form. If the 2-form is not closed, then the resulting Dirac structure is not closed.

Let

        Π

    {\displaystyle \Pi }

 be a Poisson structure on a manifold

        M

    {\displaystyle M}

, then its graph is a (closed) Dirac structure.

Any submanifold of a Poisson manifold induces a Dirac structure.

Applications

Port-Hamiltonian systems

Nonholonomic constraints

Thermodynamics
