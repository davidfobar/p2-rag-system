# Deformation (physics)

Deformation (physics)

In physics and continuum mechanics, deformation is the change in the shape or size of an object. It has dimension of length with SI unit of metre (m). It is quantified as the residual displacement of particles in a non-rigid body, from an initial configuration to a final configuration, excluding the body's average translation and rotation (its rigid transformation). A configuration is a set containing the positions of all particles of the body.
A deformation can occur because of external loads, intrinsic activity (e.g. muscle contraction), body forces (such as gravity or electromagnetic forces), or changes in temperature, moisture content, or chemical reactions, etc.
In a continuous body, a deformation field results from a stress field due to applied forces or because of some changes in the conditions of the body. The relation between stress and strain (relative deformation) is expressed by constitutive equations, e.g., Hooke's law for linear elastic materials.
Deformations which cease to exist after the stress field is removed are termed as elastic deformation. In this case, the continuum completely recovers its original configuration. On the other hand, irreversible deformations may remain, and these exist even after stresses have been removed. One type of irreversible deformation is plastic deformation, which occurs in material bodies after stresses have attained a certain threshold value known as the elastic limit or yield stress, and are the result of slip, or dislocation mechanisms at the atomic level. Another type of irreversible deformation is viscous deformation, which is the irreversible part of viscoelastic deformation.
In the case of elastic deformations, the response function linking strain to the deforming stress is the compliance tensor of the material.

Definition and formulation
Deformation is the change in the metric properties of a continuous body, meaning that a curve drawn in the initial body placement changes its length when displaced to a curve in the final placement. If none of the curves changes length, it is said that a rigid body displacement occurred.
It is convenient to identify a reference configuration or initial geometric state of the continuum body which all subsequent configurations are referenced from. The reference configuration need not be one the body actually will ever occupy. Often, the configuration at t = 0 is considered the reference configuration, κ0(B). The configuration at the current time t is the current configuration.
For deformation analysis, the reference configuration is identified as undeformed configuration, and the current configuration as deformed configuration. Additionally, time is not considered when analyzing deformation, thus the sequence of configurations between the undeformed and deformed configurations are of no interest.
The components Xi of the position vector X of a particle in the reference configuration, taken with respect to the reference coordinate system, are called the material or reference coordinates. On the other hand, the components xi of the position vector x of a particle in the deformed configuration, taken with respect to the spatial coordinate system of reference, are called the spatial coordinates
There are two methods for analysing the deformation of a continuum. One description is made in terms of the material or referential coordinates, called material description or Lagrangian description. A second description of deformation is made in terms of the spatial coordinates it is called the spatial description or Eulerian description.
There is continuity during deformation of a continuum body in the sense that:

The material points forming a closed curve at any instant will always form a closed curve at any subsequent time.
The material points forming a closed surface at any instant will always form a closed surface at any subsequent time and the matter within the closed surface will always remain within.

Affine deformation
An affine deformation is a deformation that can be completely described by an affine transformation. Such a transformation is composed of a linear transformation (such as rotation, shear, extension and compression) and a rigid body translation. Affine deformations are also called homogeneous deformations.
Therefore, an affine deformation has the form

          x

        (

          X

        ,
        t
        )

          F

        (
        t
        )
        ⋅

          X

        +

          c

        (
        t
        )

    {\displaystyle \mathbf {x} (\mathbf {X} ,t)={\boldsymbol {F}}(t)\cdot \mathbf {X} +\mathbf {c} (t)}

where x is the position of a point in the deformed configuration, X is the position in a reference configuration, t is a time-like parameter, F is the linear transformer and c is the translation. In matrix form, where the components are with respect to an orthonormal basis,

            [

                    x

                      1

                  (

                    X

                      1

                  ,

                    X

                      2

                  ,

                    X

                      3

                  ,
                  t
                  )

                    x

                      2

                  (

                    X

                      1

                  ,

                    X

                      2

                  ,

                    X

                      3

                  ,
                  t
                  )

                    x

                      3

                  (

                    X

                      1

                  ,

                    X

                      2

                  ,

                    X

                      3

                  ,
                  t
                  )

            ]

            [

                    F

                      11

                  (
                  t
                  )

                    F

                      12

                  (
                  t
                  )

                    F

                      13

                  (
                  t
                  )

                    F

                      21

                  (
                  t
                  )

                    F

                      22

                  (
                  t
                  )

                    F

                      23

                  (
                  t
                  )

                    F

                      31

                  (
                  t
                  )

                    F

                      32

                  (
                  t
                  )

                    F

                      33

                  (
                  t
                  )

            ]

            [

                    X

                      1

                    X

                      2

                    X

                      3

            ]

        +

            [

                    c

                      1

                  (
                  t
                  )

                    c

                      2

                  (
                  t
                  )

                    c

                      3

                  (
                  t
                  )

            ]

    {\displaystyle {\begin{bmatrix}x_{1}(X_{1},X_{2},X_{3},t)\x_{2}(X_{1},X_{2},X_{3},t)\x_{3}(X_{1},X_{2},X_{3},t)\end{bmatrix}}={\begin{bmatrix}F_{11}(t)&F_{12}(t)&F_{13}(t)\F_{21}(t)&F_{22}(t)&F_{23}(t)\F_{31}(t)&F_{32}(t)&F_{33}(t)\end{bmatrix}}{\begin{bmatrix}X_{1}\X_{2}\X_{3}\end{bmatrix}}+{\begin{bmatrix}c_{1}(t)\c_{2}(t)\c_{3}(t)\end{bmatrix}}}

The above deformation becomes non-affine or inhomogeneous if F = F(X,t) or c = c(X,t).

Rigid body motion
A rigid body motion is a special affine deformation that does not involve any shear, extension or compression. The transformation matrix F is proper orthogonal in order to allow rotations but no reflections.
A rigid body motion can be described by

          x

        (

          X

        ,
        t
        )

          Q

        (
        t
        )
        ⋅

          X

        +

          c

        (
        t
        )

    {\displaystyle \mathbf {x} (\mathbf {X} ,t)={\boldsymbol {Q}}(t)\cdot \mathbf {X} +\mathbf {c} (t)}

where

          Q

        ⋅

            Q

            T

            Q

            T

        ⋅

          Q

            1

    {\displaystyle {\boldsymbol {Q}}\cdot {\boldsymbol {Q}}^{T}={\boldsymbol {Q}}^{T}\cdot {\boldsymbol {Q}}={\boldsymbol {\mathit {1}}}}

In matrix form,

            [

                    x

                      1

                  (

                    X

                      1

                  ,

                    X

                      2

                  ,

                    X

                      3

                  ,
                  t
                  )

                    x

                      2

                  (

                    X

                      1

                  ,

                    X

                      2

                  ,

                    X

                      3

                  ,
                  t
                  )

                    x

                      3

                  (

                    X

                      1

                  ,

                    X

                      2

                  ,

                    X

                      3

                  ,
                  t
                  )

            ]

            [

                    Q

                      11

                  (
                  t
                  )

                    Q

                      12

                  (
                  t
                  )

                    Q

                      13

                  (
                  t
                  )

                    Q

                      21

                  (
                  t
                  )

                    Q

                      22

                  (
                  t
                  )

                    Q

                      23

                  (
                  t
                  )

                    Q

                      31

                  (
                  t
                  )

                    Q

                      32

                  (
                  t
                  )

                    Q

                      33

                  (
                  t
                  )

            ]

            [

                    X

                      1

                    X

                      2

                    X

                      3

            ]

        +

            [

                    c

                      1

                  (
                  t
                  )

                    c

                      2

                  (
                  t
                  )

                    c

                      3

                  (
                  t
                  )

            ]

    {\displaystyle {\begin{bmatrix}x_{1}(X_{1},X_{2},X_{3},t)\x_{2}(X_{1},X_{2},X_{3},t)\x_{3}(X_{1},X_{2},X_{3},t)\end{bmatrix}}={\begin{bmatrix}Q_{11}(t)&Q_{12}(t)&Q_{13}(t)\Q_{21}(t)&Q_{22}(t)&Q_{23}(t)\Q_{31}(t)&Q_{32}(t)&Q_{33}(t)\end{bmatrix}}{\begin{bmatrix}X_{1}\X_{2}\X_{3}\end{bmatrix}}+{\begin{bmatrix}c_{1}(t)\c_{2}(t)\c_{3}(t)\end{bmatrix}}}

Background: displacement

A change in the configuration of a continuum body results in a displacement. The displacement of a body has two components: a rigid-body displacement and a deformation. A rigid-body displacement consists of a simultaneous translation and rotation of the body without changing its shape or size. Deformation implies the change in shape and/or size of the body from an initial or undeformed configuration κ0(B) to a current or deformed configuration κt(B) (Figure 1).
If after a displacement of the continuum there is a relative displacement between particles, a deformation has occurred. On the other hand, if after displacement of the continuum the relative displacement between particles in the current configuration is zero, then there is no deformation and a rigid-body displacement is said to have occurred.
The vector joining the positions of a particle P in the undeformed configuration and deformed configuration is called the displacement vector u(X,t) = uiei in the Lagrangian description, or U(x,t) = UJEJ in the Eulerian description.
A displacement field is a vector field of all displacement vectors for all particles in the body, which relates the deformed configuration with the undeformed configuration. It is convenient to do the analysis of deformation or motion of a continuum body in terms of the displacement field. In general, the displacement field is expressed in terms of the material coordinates as

          u

        (

          X

        ,
        t
        )

          b

        (

          X

        ,
        t
        )
        +

          x

        (

          X

        ,
        t
        )
        −

          X

          or

          u

            i

          α

            i
            J

          b

            J

        +

          x

            i

        −

          α

            i
            J

          X

            J

    {\displaystyle \mathbf {u} (\mathbf {X} ,t)=\mathbf {b} (\mathbf {X} ,t)+\mathbf {x} (\mathbf {X} ,t)-\mathbf {X} \qquad {\text{or}}\qquad u_{i}=\alpha {iJ}b{J}+x_{i}-\alpha {iJ}X{J}}

or in terms of the spatial coordinates as

          U

        (

          x

        ,
        t
        )

          b

        (

          x

        ,
        t
        )
        +

          x

        −

          X

        (

          x

        ,
        t
        )

          or

          U

            J

          b

            J

        +

          α

            J
            i

          x

            i

        −

          X

            J

    {\displaystyle \mathbf {U} (\mathbf {x} ,t)=\mathbf {b} (\mathbf {x} ,t)+\mathbf {x} -\mathbf {X} (\mathbf {x} ,t)\qquad {\text{or}}\qquad U_{J}=b_{J}+\alpha {Ji}x{i}-X_{J}}

where αJi are the direction cosines between the material and spatial coordinate systems with unit vectors EJ and ei, respectively. Thus

            E

            J

        ⋅

            e

            i

          α

            J
            i

          α

            i
            J

    {\displaystyle \mathbf {E} _{J}\cdot \mathbf {e} _{i}=\alpha _{Ji}=\alpha _{iJ}}

and the relationship between ui and UJ is then given by

          u

            i

          α

            i
            J

          U

            J

          or

          U

            J

          α

            J
            i

          u

            i

    {\displaystyle u_{i}=\alpha {iJ}U{J}\qquad {\text{or}}\qquad U_{J}=\alpha {Ji}u{i}}

Knowing that

            e

            i

          α

            i
            J

            E

            J

    {\displaystyle \mathbf {e} _{i}=\alpha _{iJ}\mathbf {E} _{J}}

then

          u

        (

          X

        ,
        t
        )

          u

            i

            e

            i

          u

            i

        (

          α

            i
            J

            E

            J

        )

          U

            J

            E

            J

          U

        (

          x

        ,
        t
        )

    {\displaystyle \mathbf {u} (\mathbf {X} ,t)=u_{i}\mathbf {e} {i}=u{i}(\alpha _{iJ}\mathbf {E} {J})=U{J}\mathbf {E} _{J}=\mathbf {U} (\mathbf {x} ,t)}

It is common to superimpose the coordinate systems for the undeformed and deformed configurations, which results in b = 0, and the direction cosines become Kronecker deltas:

            E

            J

        ⋅

            e

            i

          δ

            J
            i

          δ

            i
            J

    {\displaystyle \mathbf {E} _{J}\cdot \mathbf {e} _{i}=\delta _{Ji}=\delta _{iJ}}

Thus, we have

          u

        (

          X

        ,
        t
        )

          x

        (

          X

        ,
        t
        )
        −

          X

          or

          u

            i

          x

            i

        −

          δ

            i
            J

          X

            J

          x

            i

        −

          X

            i

    {\displaystyle \mathbf {u} (\mathbf {X} ,t)=\mathbf {x} (\mathbf {X} ,t)-\mathbf {X} \qquad {\text{or}}\qquad u_{i}=x_{i}-\delta {iJ}X{J}=x_{i}-X_{i}}

or in terms of the spatial coordinates as

          U

        (

          x

        ,
        t
        )

          x

        −

          X

        (

          x

        ,
        t
        )

          or

          U

            J

          δ

            J
            i

          x

            i

        −

          X

            J

          x

            J

        −

          X

            J

    {\displaystyle \mathbf {U} (\mathbf {x} ,t)=\mathbf {x} -\mathbf {X} (\mathbf {x} ,t)\qquad {\text{or}}\qquad U_{J}=\delta {Ji}x{i}-X_{J}=x_{J}-X_{J}}

Displacement gradient tensor

The partial differentiation of the displacement vector with respect to the material coordinates yields the material displacement gradient tensor ∇Xu. Thus we have:

                  u

                (

                  X

                ,
                t
                )

                  x

                (

                  X

                ,
                t
                )
                −

                  X

                  ∇

                      X

                  u

                  ∇

                      X

                  x

                −

                  I

                  ∇

                      X

                  u

                  F

                −

                  I

    {\displaystyle {\begin{aligned}\mathbf {u} (\mathbf {X} ,t)&=\mathbf {x} (\mathbf {X} ,t)-\mathbf {X} \\nabla _{\mathbf {X} }\mathbf {u} &=\nabla _{\mathbf {X} }\mathbf {x} -\mathbf {I} \\nabla _{\mathbf {X} }\mathbf {u} &=\mathbf {F} -\mathbf {I} \end{aligned}}}

or

                  u

                    i

                  x

                    i

                −

                  δ

                    i
                    J

                  X

                    J

                  x

                    i

                −

                  X

                    i

                      ∂

                        u

                          i

                      ∂

                        X

                          K

                      ∂

                        x

                          i

                      ∂

                        X

                          K

                −

                  δ

                    i
                    K

    {\displaystyle {\begin{aligned}u_{i}&=x_{i}-\delta {iJ}X{J}=x_{i}-X_{i}\{\frac {\partial u_{i}}{\partial X_{K}}}&={\frac {\partial x_{i}}{\partial X_{K}}}-\delta _{iK}\end{aligned}}}

where F is the deformation gradient tensor.
Similarly, the partial differentiation of the displacement vector with respect to the spatial coordinates yields the spatial displacement gradient tensor ∇xU. Thus we have,

                  U

                (

                  x

                ,
                t
                )

                  x

                −

                  X

                (

                  x

                ,
                t
                )

                  ∇

                      x

                  U

                  I

                −

                  ∇

                      x

                  X

                  ∇

                      x

                  U

                  I

                −

                    F

                    −
                    1

    {\displaystyle {\begin{aligned}\mathbf {U} (\mathbf {x} ,t)&=\mathbf {x} -\mathbf {X} (\mathbf {x} ,t)\\nabla _{\mathbf {x} }\mathbf {U} &=\mathbf {I} -\nabla _{\mathbf {x} }\mathbf {X} \\nabla _{\mathbf {x} }\mathbf {U} &=\mathbf {I} -\mathbf {F} ^{-1}\end{aligned}}}

or

                  U

                    J

                  δ

                    J
                    i

                  x

                    i

                −

                  X

                    J

                  x

                    J

                −

                  X

                    J

                      ∂

                        U

                          J

                      ∂

                        x

                          k

                  δ

                    J
                    k

                −

                      ∂

                        X

                          J

                      ∂

                        x

                          k

    {\displaystyle {\begin{aligned}U_{J}&=\delta {Ji}x{i}-X_{J}=x_{J}-X_{J}\{\frac {\partial U_{J}}{\partial x_{k}}}&=\delta {Jk}-{\frac {\partial X{J}}{\partial x_{k}}}\end{aligned}}}

Examples
Homogeneous (or affine) deformations are useful in elucidating the behavior of materials. Some homogeneous deformations of interest are

uniform extension
pure dilation
equibiaxial tension
simple shear
pure shear
Linear or longitudinal deformations of long objects, such as beams and fibers, are called elongation or shortening; derived quantities are the relative elongation and the stretch ratio.
Plane deformations are also of interest, particularly in the experimental context.
Volume deformation is a uniform scaling due to isotropic compression; the relative volume deformation is called volumetric strain.

Plane deformation
A plane deformation, also called plane strain, is one where the deformation is restricted to one of the planes in the reference configuration. If the deformation is restricted to the plane described by the basis vectors e1, e2, the deformation gradient has the form

          F

          F

            11

            e

            1

        ⊗

            e

            1

        +

          F

            12

            e

            1

        ⊗

            e

            2

        +

          F

            21

            e

            2

        ⊗

            e

            1

        +

          F

            22

            e

            2

        ⊗

            e

            2

        +

            e

            3

        ⊗

            e

            3

    {\displaystyle {\boldsymbol {F}}=F_{11}\mathbf {e} _{1}\otimes \mathbf {e} {1}+F{12}\mathbf {e} _{1}\otimes \mathbf {e} {2}+F{21}\mathbf {e} _{2}\otimes \mathbf {e} {1}+F{22}\mathbf {e} _{2}\otimes \mathbf {e} _{2}+\mathbf {e} _{3}\otimes \mathbf {e} _{3}}

In matrix form,

          F

            [

                    F

                      11

                    F

                      12

                  0

                    F

                      21

                    F

                      22

                  0

                  0

                  0

                  1

            ]

    {\displaystyle {\boldsymbol {F}}={\begin{bmatrix}F_{11}&F_{12}&0\F_{21}&F_{22}&0\0&0&1\end{bmatrix}}}

From the polar decomposition theorem, the deformation gradient, up to a change of coordinates, can be decomposed into a stretch and a rotation. Since all the deformation is in a plane, we can write

          F

          R

        ⋅

          U

            [

                  cos
                  ⁡
                  θ

                  sin
                  ⁡
                  θ

                  0

                  −
                  sin
                  ⁡
                  θ

                  cos
                  ⁡
                  θ

                  0

                  0

                  0

                  1

            ]

            [

                    λ

                      1

                  0

                  0

                  0

                    λ

                      2

                  0

                  0

                  0

                  1

            ]

    {\displaystyle {\boldsymbol {F}}={\boldsymbol {R}}\cdot {\boldsymbol {U}}={\begin{bmatrix}\cos \theta &\sin \theta &0\-\sin \theta &\cos \theta &0\0&0&1\end{bmatrix}}{\begin{bmatrix}\lambda _{1}&0&0\0&\lambda _{2}&0\0&0&1\end{bmatrix}}}

where θ is the angle of rotation and λ1, λ2 are the principal stretches.

Isochoric plane deformation
If the deformation is isochoric (volume preserving) then det(F) = 1 and we have

          F

            11

          F

            22

        −

          F

            12

          F

            21

        1

    {\displaystyle F_{11}F_{22}-F_{12}F_{21}=1}

Alternatively,

          λ

            1

          λ

            2

        1

    {\displaystyle \lambda _{1}\lambda _{2}=1}

Simple shear
A simple shear deformation is defined as an isochoric plane deformation in which there is a set of line elements with a given reference orientation that do not change length and orientation during the deformation.
If e1 is the fixed reference orientation in which line elements do not deform during the deformation then λ1 = 1 and F·e1 = e1.
Therefore,

          F

            11

            e

            1

        +

          F

            21

            e

            2

            e

            1

        ⟹

          F

            11

        1

        ;

          F

            21

        0

    {\displaystyle F_{11}\mathbf {e} {1}+F{21}\mathbf {e} _{2}=\mathbf {e} {1}\quad \implies \quad F{11}=1~;~~F_{21}=0}

Since the deformation is isochoric,

          F

            11

          F

            22

        −

          F

            12

          F

            21

        1

        ⟹

          F

            22

        1

    {\displaystyle F_{11}F_{22}-F_{12}F_{21}=1\quad \implies \quad F_{22}=1}

Define

        γ
        :=

          F

            12

    {\displaystyle \gamma :=F_{12}}

Then, the deformation gradient in simple shear can be expressed as

          F

            [

                  1

                  γ

                  0

                  0

                  1

                  0

                  0

                  0

                  1

            ]

    {\displaystyle {\boldsymbol {F}}={\begin{bmatrix}1&\gamma &0\0&1&0\0&0&1\end{bmatrix}}}

Now,

          F

        ⋅

            e

            2

          F

            12

            e

            1

        +

          F

            22

            e

            2

        γ

            e

            1

        +

            e

            2

        ⟹

          F

        ⋅
        (

            e

            2

        ⊗

            e

            2

        )

        γ

            e

            1

        ⊗

            e

            2

        +

            e

            2

        ⊗

            e

            2

    {\displaystyle {\boldsymbol {F}}\cdot \mathbf {e} {2}=F{12}\mathbf {e} {1}+F{22}\mathbf {e} _{2}=\gamma \mathbf {e} _{1}+\mathbf {e} _{2}\quad \implies \quad {\boldsymbol {F}}\cdot (\mathbf {e} _{2}\otimes \mathbf {e} _{2})=\gamma \mathbf {e} _{1}\otimes \mathbf {e} _{2}+\mathbf {e} _{2}\otimes \mathbf {e} _{2}}

Since

            e

            i

        ⊗

            e

            i

            1

    {\displaystyle \mathbf {e} _{i}\otimes \mathbf {e} _{i}={\boldsymbol {\mathit {1}}}}

we can also write the deformation gradient as

          F

            1

        +
        γ

            e

            1

        ⊗

            e

            2

    {\displaystyle {\boldsymbol {F}}={\boldsymbol {\mathit {1}}}+\gamma \mathbf {e} _{1}\otimes \mathbf {e} _{2}}
