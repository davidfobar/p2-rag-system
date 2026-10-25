# Appell's equation of motion

Appell's equation of motion

In classical mechanics, Appell's equation of motion (a.k.a. the Gibbs–Appell equation of motion) is an alternative general formulation of classical mechanics described by Josiah Willard Gibbs in 1879 and Paul Émile Appell in 1900.

Statement
The Gibbs-Appell equation reads

          Q

            r

              ∂
              S

              ∂

                α

                  r

        ,

    {\displaystyle Q_{r}={\frac {\partial S}{\partial \alpha _{r}}},}

where

          α

            r

                q
                ¨

            r

    {\displaystyle \alpha {r}={\ddot {q}}{r}}

 is an arbitrary generalized acceleration, or the second time derivative of the generalized coordinates

          q

            r

    {\displaystyle q_{r}}

, and

          Q

            r

    {\displaystyle Q_{r}}

 is its corresponding generalized force. The generalized force gives the work done

        d
        W

          ∑

            r

            1

            D

          Q

            r

        d

          q

            r

        ,

    {\displaystyle dW=\sum {r=1}^{D}Q{r}dq_{r},}

where the index

        r

    {\displaystyle r}

 runs over the

        D

    {\displaystyle D}

 generalized coordinates

          q

            r

    {\displaystyle q_{r}}

, which usually correspond to the degrees of freedom of the system. The function

        S

    {\displaystyle S}

 is defined as the mass-weighted sum of the particle accelerations squared,

        S

            1
            2

          ∑

            k

            1

            N

          m

            k

            a

            k

            2

        ,

    {\displaystyle S={\frac {1}{2}}\sum {k=1}^{N}m{k}\mathbf {a} _{k}^{2}\,,}

where the index

        k

    {\displaystyle k}

 runs over the

        K

    {\displaystyle K}

 particles, and

            a

            k

                  r

                ¨

            k

                d

                  2

                  r

                  k

              d

                t

                  2

    {\displaystyle \mathbf {a} {k}={\ddot {\mathbf {r} }}{k}={\frac {d^{2}\mathbf {r} _{k}}{dt^{2}}}}

is the acceleration of the

        k

    {\displaystyle k}

-th particle, the second time derivative of its position vector

            r

            k

    {\displaystyle \mathbf {r} _{k}}

. Each

            r

            k

    {\displaystyle \mathbf {r} _{k}}

 is expressed in terms of generalized coordinates, and

            a

            k

    {\displaystyle \mathbf {a} _{k}}

 is expressed in terms of the generalized accelerations.

Relations to other formulations of classical mechanics
Appell's formulation does not introduce any new physics to classical mechanics and as such is equivalent to other reformulations of classical mechanics, such as Lagrangian mechanics, and Hamiltonian mechanics. All classical mechanics is contained within Newton's laws of motion. In some cases, Appell's equation of motion may be more convenient than the commonly used Lagrangian mechanics, particularly when nonholonomic constraints are involved. In fact, Appell's equation leads directly to Lagrange's equations of motion. Moreover, it can be used to derive Kane's equations, which are particularly suited for describing the motion of complex spacecraft. Appell's formulation is an application of Gauss' principle of least constraint.

Derivation
The change in the particle positions rk for an infinitesimal change in the D generalized coordinates is

        d

            r

            k

          ∑

            r

            1

            D

        d

          q

            r

              ∂

                  r

                  k

              ∂

                q

                  r

    {\displaystyle d\mathbf {r} _{k}=\sum {r=1}^{D}dq{r}{\frac {\partial \mathbf {r} {k}}{\partial q{r}}}}

Taking two derivatives with respect to time yields an equivalent equation for the accelerations

              ∂

                  a

                  k

              ∂

                α

                  r

              ∂

                  r

                  k

              ∂

                q

                  r

    {\displaystyle {\frac {\partial \mathbf {a} _{k}}{\partial \alpha _{r}}}={\frac {\partial \mathbf {r} {k}}{\partial q{r}}}}

The work done by an infinitesimal change dqr in the generalized coordinates is

        d
        W

          ∑

            r

            1

            D

          Q

            r

        d

          q

            r

          ∑

            k

            1

            N

            F

            k

        ⋅
        d

            r

            k

          ∑

            k

            1

            N

          m

            k

            a

            k

        ⋅
        d

            r

            k

    {\displaystyle dW=\sum {r=1}^{D}Q{r}dq_{r}=\sum _{k=1}^{N}\mathbf {F} _{k}\cdot d\mathbf {r} _{k}=\sum {k=1}^{N}m{k}\mathbf {a} _{k}\cdot d\mathbf {r} _{k}}

where Newton's second law for the kth particle

            F

            k

          m

            k

            a

            k

    {\displaystyle \mathbf {F} {k}=m{k}\mathbf {a} _{k}}

has been used. Substituting the formula for drk and swapping the order of the two summations yields the formulae

        d
        W

          ∑

            r

            1

            D

          Q

            r

        d

          q

            r

          ∑

            k

            1

            N

          m

            k

            a

            k

        ⋅

          ∑

            r

            1

            D

        d

          q

            r

          (

                ∂

                    r

                    k

                ∂

                  q

                    r

          )

          ∑

            r

            1

            D

        d

          q

            r

          ∑

            k

            1

            N

          m

            k

            a

            k

        ⋅

          (

                ∂

                    r

                    k

                ∂

                  q

                    r

          )

    {\displaystyle dW=\sum {r=1}^{D}Q{r}dq_{r}=\sum {k=1}^{N}m{k}\mathbf {a} _{k}\cdot \sum {r=1}^{D}dq{r}\left({\frac {\partial \mathbf {r} {k}}{\partial q{r}}}\right)=\sum {r=1}^{D}dq{r}\sum {k=1}^{N}m{k}\mathbf {a} _{k}\cdot \left({\frac {\partial \mathbf {r} {k}}{\partial q{r}}}\right)}

Therefore, the generalized forces are

          Q

            r

          ∑

            k

            1

            N

          m

            k

            a

            k

        ⋅

          (

                ∂

                    r

                    k

                ∂

                  q

                    r

          )

          ∑

            k

            1

            N

          m

            k

            a

            k

        ⋅

          (

                ∂

                    a

                    k

                ∂

                  α

                    r

          )

    {\displaystyle Q_{r}=\sum {k=1}^{N}m{k}\mathbf {a} _{k}\cdot \left({\frac {\partial \mathbf {r} {k}}{\partial q{r}}}\right)=\sum {k=1}^{N}m{k}\mathbf {a} _{k}\cdot \left({\frac {\partial \mathbf {a} _{k}}{\partial \alpha _{r}}}\right)}

This equals the derivative of S with respect to the generalized accelerations

              ∂
              S

              ∂

                α

                  r

            ∂

              ∂

                α

                  r

            1
            2

          ∑

            k

            1

            N

          m

            k

                a

                k

            2

          ∑

            k

            1

            N

          m

            k

            a

            k

        ⋅

          (

                ∂

                    a

                    k

                ∂

                  α

                    r

          )

    {\displaystyle {\frac {\partial S}{\partial \alpha _{r}}}={\frac {\partial }{\partial \alpha _{r}}}{\frac {1}{2}}\sum {k=1}^{N}m{k}\left|\mathbf {a} _{k}\right|^{2}=\sum {k=1}^{N}m{k}\mathbf {a} _{k}\cdot \left({\frac {\partial \mathbf {a} _{k}}{\partial \alpha _{r}}}\right)}

yielding Appell's equation of motion

              ∂
              S

              ∂

                α

                  r

          Q

            r

        .

    {\displaystyle {\frac {\partial S}{\partial \alpha {r}}}=Q{r}.}

Examples

Euler's equations of rigid body dynamics
Euler's equations provide an excellent illustration of Appell's formulation.
Consider a rigid body of N particles joined by rigid rods. The rotation of the body may be described by an angular velocity vector

          ω

    {\displaystyle {\boldsymbol {\omega }}}

, and the corresponding angular acceleration vector

          α

              d

                ω

              d
              t

    {\displaystyle {\boldsymbol {\alpha }}={\frac {d{\boldsymbol {\omega }}}{dt}}}

The generalized force for a rotation is the torque

            N

    {\displaystyle {\textbf {N}}}

, since the work done for an infinitesimal rotation

        δ

          ϕ

    {\displaystyle \delta {\boldsymbol {\phi }}}

 is

        d
        W

          N

        ⋅
        δ

          ϕ

    {\displaystyle dW=\mathbf {N} \cdot \delta {\boldsymbol {\phi }}}

. The velocity of the

        k

    {\displaystyle k}

-th particle is given by

            v

            k

          ω

        ×

            r

            k

    {\displaystyle \mathbf {v} _{k}={\boldsymbol {\omega }}\times \mathbf {r} _{k}}

where

            r

            k

    {\displaystyle \mathbf {r} _{k}}

 is the particle's position in Cartesian coordinates; its corresponding acceleration is

            a

            k

              d

                  v

                  k

              d
              t

          α

        ×

            r

            k

        +

          ω

        ×

            v

            k

    {\displaystyle \mathbf {a} _{k}={\frac {d\mathbf {v} _{k}}{dt}}={\boldsymbol {\alpha }}\times \mathbf {r} _{k}+{\boldsymbol {\omega }}\times \mathbf {v} _{k}}

Therefore, the function

        S

    {\displaystyle S}

 may be written as

        S

            1
            2

          ∑

            k

            1

            N

          m

            k

          (

                a

                k

            ⋅

                a

                k

          )

            1
            2

          ∑

            k

            1

            N

          m

            k

          {

                (

                    α

                  ×

                      r

                      k

                )

                2

            +

                (

                    ω

                  ×

                      v

                      k

                )

                2

            +
            2

              (

                  α

                ×

                    r

                    k

              )

            ⋅

              (

                  ω

                ×

                    v

                    k

              )

          }

    {\displaystyle S={\frac {1}{2}}\sum {k=1}^{N}m{k}\left(\mathbf {a} _{k}\cdot \mathbf {a} _{k}\right)={\frac {1}{2}}\sum {k=1}^{N}m{k}\left{\left({\boldsymbol {\alpha }}\times \mathbf {r} _{k}\right)^{2}+\left({\boldsymbol {\omega }}\times \mathbf {v} _{k}\right)^{2}+2\left({\boldsymbol {\alpha }}\times \mathbf {r} _{k}\right)\cdot \left({\boldsymbol {\omega }}\times \mathbf {v} _{k}\right)\right}}

Setting the derivative of S with respect to

          α

    {\displaystyle {\boldsymbol {\alpha }}}

 equal to the torque yields Euler's equations

          I

            x
            x

          α

            x

        −

          (

              I

                y
                y

            −

              I

                z
                z

          )

          ω

            y

          ω

            z

          N

            x

    {\displaystyle I_{xx}\alpha {x}-\left(I{yy}-I_{zz}\right)\omega _{y}\omega {z}=N{x}}

          I

            y
            y

          α

            y

        −

          (

              I

                z
                z

            −

              I

                x
                x

          )

          ω

            z

          ω

            x

          N

            y

    {\displaystyle I_{yy}\alpha {y}-\left(I{zz}-I_{xx}\right)\omega _{z}\omega {x}=N{y}}

          I

            z
            z

          α

            z

        −

          (

              I

                x
                x

            −

              I

                y
                y

          )

          ω

            x

          ω

            y

          N

            z

    {\displaystyle I_{zz}\alpha {z}-\left(I{xx}-I_{yy}\right)\omega _{x}\omega {y}=N{z}}
