# Strain-rate tensor

Strain-rate tensor

In continuum mechanics, the strain-rate tensor or rate-of-strain tensor is a physical quantity that describes the rate of change of the strain (i.e., the relative deformation) of a material in the neighborhood of a certain point, at a certain moment of time. It can be defined as the derivative of the strain tensor with respect to time, or as the symmetric component of the Jacobian matrix (derivative with respect to position) of the flow velocity. In fluid mechanics it also can be described as the velocity gradient, a measure of how the velocity of a fluid changes between different points within the fluid. Though the term can refer to a velocity profile (variation in velocity across layers of flow in a pipe), it is often used to mean the gradient of a flow's velocity with respect to its coordinates. The concept has implications in a variety of areas of physics and engineering, including magnetohydrodynamics, mining and water treatment.
The strain rate tensor is a purely kinematic concept that describes the macroscopic motion of the material. Therefore, it does not depend on the nature of the material, or on the forces and stresses that may be acting on it; and it applies to any continuous medium, whether solid, liquid or gas.
On the other hand, for any fluid except superfluids, any gradual change in its deformation (i.e. a non-zero strain rate tensor) gives rise to viscous forces in its interior, due to friction between adjacent fluid elements, that tend to oppose that change. At any point in the fluid, these stresses can be described by a viscous stress tensor that is, almost always, completely determined by the strain rate tensor and by certain intrinsic properties of the fluid at that point. Viscous stress also occur in solids, in addition to the elastic stress observed in static deformation; when it is too large to be ignored, the material is said to be viscoelastic.

Dimensional analysis
By performing dimensional analysis, the dimensions of velocity gradient can be determined. The dimensions of velocity are

              L

                1

              T

                −
                1

    {\displaystyle {\mathsf {L^{1}T^{-1}}}}

, and the dimensions of distance are

              L

                1

    {\displaystyle {\mathsf {L^{1}}}}

. Since the velocity gradient can be expressed as

              Δ

                velocity

              Δ

                distance

    {\displaystyle {\frac {\Delta {\text{velocity}}}{\Delta {\text{distance}}}}}

. Therefore, the velocity gradient has the same dimensions as this ratio, i.e.,

              T

                −
                1

    {\displaystyle {\mathsf {T^{-1}}}}

.

In continuum mechanics
In 3 dimensions, the gradient

        ∇

          v

    {\displaystyle \nabla \mathbf {v} }

 of the velocity

          v

    {\displaystyle \mathbf {v} }

 is a second-order tensor which can be expressed as the matrix

          L

    {\displaystyle \mathbf {L} }

:

          L

        ∇

          v

            [

                        ∂

                          v

                            x

                        ∂
                        x

                        ∂

                          v

                            y

                        ∂
                        x

                        ∂

                          v

                            z

                        ∂
                        x

                        ∂

                          v

                            x

                        ∂
                        y

                        ∂

                          v

                            y

                        ∂
                        y

                          ∂

                            v

                              z

                          ∂
                          y

                        ∂

                          v

                            x

                        ∂
                        z

                        ∂

                          v

                            y

                        ∂
                        z

                        ∂

                          v

                            z

                        ∂
                        z

            ]

    {\displaystyle \mathbf {L} =\nabla \mathbf {v} ={\begin{bmatrix}{\frac {\partial v_{x}}{\partial x}}&{\frac {\partial v_{y}}{\partial x}}&{\frac {\partial v_{z}}{\partial x}}\{\frac {\partial v_{x}}{\partial y}}&{\frac {\partial v_{y}}{\partial y}}&{{\frac {\partial v_{z}}{\partial y}}\ }\{\frac {\partial v_{x}}{\partial z}}&{\frac {\partial v_{y}}{\partial z}}&{\frac {\partial v_{z}}{\partial z}}\end{bmatrix}}}

          L

    {\displaystyle \mathbf {L} }

 can be decomposed into the sum of a symmetric matrix

            E

    {\displaystyle {\textbf {E}}}

 and a skew-symmetric matrix

            W

    {\displaystyle {\textbf {W}}}

 as follows

                  E

                    1
                    2

                  (

                      L

                    +

                        L

                          T

                  )

                  W

                    1
                    2

                  (

                      L

                    −

                        L

                          T

                  )

    {\displaystyle {\begin{aligned}\mathbf {E} &={\frac {1}{2}}\left(\mathbf {L} +\mathbf {L} ^{\textsf {T}}\right)\\mathbf {W} &={\frac {1}{2}}\left(\mathbf {L} -\mathbf {L} ^{\textsf {T}}\right)\end{aligned}}}

            E

    {\displaystyle {\textbf {E}}}

 is called the strain rate tensor and describes the rate of stretching and shearing.

            W

    {\displaystyle {\textbf {W}}}

 is called the spin tensor and describes the rate of rotation.

Relationship between shear stress and the velocity field
Sir Isaac Newton proposed that shear stress is directly proportional to the velocity gradient:

        τ

        μ

              ∂
              u

              ∂
              y

        .

    {\displaystyle \tau =\mu {\frac {\partial u}{\partial y}}.}

The constant of proportionality,

        μ

    {\displaystyle \mu }

, is called the dynamic viscosity.

Formal definition
Consider a material body, solid or fluid, that is flowing and/or moving in space. Let v be the velocity field within the body; that is, a smooth function from R3 × R such that v(p, t) is the macroscopic velocity of the material that is passing through the point p at time t.
The velocity v(p + r, t) at a point displaced from p by a small vector r can be written as a Taylor series:

          v

        (

          p

        +

          r

        ,
        t
        )

          v

        (

          p

        ,
        t
        )
        +
        (
        ∇

          v

        )
        (

          p

        ,
        t
        )
        (

          r

        )
        +

          higher order terms

        ,

    {\displaystyle \mathbf {v} (\mathbf {p} +\mathbf {r} ,t)=\mathbf {v} (\mathbf {p} ,t)+(\nabla \mathbf {v} )(\mathbf {p} ,t)(\mathbf {r} )+{\text{higher order terms}},}

where ∇v the gradient of the velocity field, understood as a linear map that takes a displacement vector r to the corresponding change in the velocity.

In an arbitrary reference frame, ∇v is related to the Jacobian matrix of the field, namely in 3 dimensions it is the 3 × 3 matrix

            (

              ∇

                v

            )

              T

            [

                    ∂

                      1

                    v

                      1

                    ∂

                      2

                    v

                      1

                    ∂

                      3

                    v

                      1

                    ∂

                      1

                    v

                      2

                    ∂

                      2

                    v

                      2

                    ∂

                      3

                    v

                      2

                    ∂

                      1

                    v

                      3

                    ∂

                      2

                    v

                      3

                    ∂

                      3

                    v

                      3

            ]

          J

        .

    {\displaystyle \left(\nabla \mathbf {v} \right)^{\mathrm {T} }={\begin{bmatrix}\partial {1}v{1}&\partial {2}v{1}&\partial {3}v{1}\\partial {1}v{2}&\partial {2}v{2}&\partial {3}v{2}\\partial {1}v{3}&\partial {2}v{3}&\partial {3}v{3}\end{bmatrix}}=\mathbf {J} .}

where vi is the component of v parallel to axis i and ∂jf denotes the partial derivative of a function f with respect to the space coordinate xj. Note that J is a function of p and t.
In this coordinate system, the Taylor approximation for the velocity near p is

          v

            i

        (

          p

        +

          r

        ,
        t
        )

          v

            i

        (

          p

        ,
        t
        )
        +

          ∑

            j

          J

            i
            j

        (

          p

        ,
        t
        )

          r

            j

          v

            i

        (

          p

        ,
        t
        )
        +

          ∑

            j

          ∂

            j

          v

            i

        (

          p

        ,
        t
        )

          r

            j

        ;

    {\displaystyle v_{i}(\mathbf {p} +\mathbf {r} ,t)=v_{i}(\mathbf {p} ,t)+\sum {j}J{ij}(\mathbf {p} ,t)r_{j}=v_{i}(\mathbf {p} ,t)+\sum _{j}\partial {j}v{i}(\mathbf {p} ,t)r_{j};}

or simply

          v

        (

          p

        +

          r

        ,
        t
        )

          v

        (

          p

        ,
        t
        )
        +

          J

        (

          p

        ,
        t
        )

          r

    {\displaystyle \mathbf {v} (\mathbf {p} +\mathbf {r} ,t)=\mathbf {v} (\mathbf {p} ,t)+\mathbf {J} (\mathbf {p} ,t)\mathbf {r} }

if v and r are viewed as 3 × 1 matrices.

Symmetric and antisymmetric parts

Any matrix can be decomposed into the sum of a symmetric matrix and an antisymmetric matrix. Applying this to the Jacobian matrix with symmetric and antisymmetric components E and R respectively:

                  E

                    1
                    2

                  (

                      J

                    +

                        J

                          T

                  )

                  R

                    1
                    2

                  (

                      J

                    −

                        J

                          T

                  )

                  E

                    i
                    j

                    1
                    2

                  (

                      ∂

                        j

                      v

                        i

                    +

                      ∂

                        i

                      v

                        j

                  )

                  R

                    i
                    j

                    1
                    2

                  (

                      ∂

                        j

                      v

                        i

                    −

                      ∂

                        i

                      v

                        j

                  )

    {\displaystyle {\begin{aligned}\mathbf {E} &={\frac {1}{2}}\left(\mathbf {J} +\mathbf {J} ^{\textsf {T}}\right)&\mathbf {R} &={\frac {1}{2}}\left(\mathbf {J} -\mathbf {J} ^{\textsf {T}}\right)\E_{ij}&={\frac {1}{2}}\left(\partial {j}v{i}+\partial {i}v{j}\right)&R_{ij}&={\frac {1}{2}}\left(\partial {j}v{i}-\partial {i}v{j}\right)\end{aligned}}}

This decomposition is independent of coordinate system, and so has physical significance. Then the velocity field may be approximated as

          v

        (

          p

        +

          r

        ,
        t
        )
        ≈

          v

        (

          p

        ,
        t
        )
        +

          E

        (

          p

        ,
        t
        )
        (

          r

        )
        +

          R

        (

          p

        ,
        t
        )
        (

          r

        )
        ,

    {\displaystyle \mathbf {v} (\mathbf {p} +\mathbf {r} ,t)\approx \mathbf {v} (\mathbf {p} ,t)+\mathbf {E} (\mathbf {p} ,t)(\mathbf {r} )+\mathbf {R} (\mathbf {p} ,t)(\mathbf {r} ),}

that is,

                  v

                    i

                (

                  p

                +

                  r

                ,
                t
                )

                  v

                    i

                (

                  p

                ,
                t
                )
                +

                  ∑

                    j

                  E

                    i
                    j

                (

                  p

                ,
                t
                )

                  r

                    j

                +

                  ∑

                    j

                  R

                    i
                    j

                (

                  p

                ,
                t
                )

                  r

                    j

                  v

                    i

                (

                  p

                ,
                t
                )
                +

                    1
                    2

                  ∑

                    j

                  (

                      ∂

                        j

                      v

                        i

                    (

                      p

                    ,
                    t
                    )
                    +

                      ∂

                        i

                      v

                        j

                    (

                      p

                    ,
                    t
                    )

                  )

                  r

                    j

                +

                    1
                    2

                  ∑

                    j

                  (

                      ∂

                        j

                      v

                        i

                    (

                      p

                    ,
                    t
                    )
                    −

                      ∂

                        i

                      v

                        j

                    (

                      p

                    ,
                    t
                    )

                  )

                  r

                    j

    {\displaystyle {\begin{aligned}v_{i}(\mathbf {p} +\mathbf {r} ,t)&=v_{i}(\mathbf {p} ,t)+\sum {j}E{ij}(\mathbf {p} ,t)r_{j}+\sum {j}R{ij}(\mathbf {p} ,t)r_{j}\&=v_{i}(\mathbf {p} ,t)+{\frac {1}{2}}\sum _{j}\left(\partial {j}v{i}(\mathbf {p} ,t)+\partial {i}v{j}(\mathbf {p} ,t)\right)r_{j}+{\frac {1}{2}}\sum _{j}\left(\partial {j}v{i}(\mathbf {p} ,t)-\partial {i}v{j}(\mathbf {p} ,t)\right)r_{j}\end{aligned}}}

The antisymmetric term R represents a rigid-like rotation of the fluid about the point p. Its angular velocity

              ω
              →

    {\displaystyle {\vec {\omega }}}

 is

              ω
              →

            1
            2

        ∇
        ×

          v

            1
            2

            [

                    ∂

                      2

                    v

                      3

                  −

                    ∂

                      3

                    v

                      2

                    ∂

                      3

                    v

                      1

                  −

                    ∂

                      1

                    v

                      3

                    ∂

                      1

                    v

                      2

                  −

                    ∂

                      2

                    v

                      1

            ]

        .

    {\displaystyle {\vec {\omega }}={\frac {1}{2}}\nabla \times \mathbf {v} ={\frac {1}{2}}{\begin{bmatrix}\partial {2}v{3}-\partial {3}v{2}\\partial {3}v{1}-\partial {1}v{3}\\partial {1}v{2}-\partial {2}v{1}\end{bmatrix}}.}

The product ∇ × v is called the vorticity of the vector field. A rigid rotation does not change the relative positions of the fluid elements, so the antisymmetric term R of the velocity gradient does not contribute to the rate of change of the deformation. The actual strain rate is therefore described by the symmetric E term, which is the strain rate tensor.

Shear rate and compression rate

The symmetric term E (the rate-of-strain tensor) can be broken down further as the sum of a scalar times the unit tensor, that represents a gradual isotropic expansion or contraction; and a traceless symmetric tensor which represents a gradual shearing deformation, with no change in volume:

          E

        (

          p

        ,
        t
        )
        (

          r

        )

          S

        (

          p

        ,
        t
        )
        (

          r

        )
        +

          D

        (

          p

        ,
        t
        )
        (

          r

        )
        .

    {\displaystyle \mathbf {E} (\mathbf {p} ,t)(\mathbf {r} )=\mathbf {S} (\mathbf {p} ,t)(\mathbf {r} )+\mathbf {D} (\mathbf {p} ,t)(\mathbf {r} ).}

That is,

          E

            i
            j

                    1
                    3

                  (

                      ∑

                        k

                      ∂

                        k

                      v

                        k

                  )

                  δ

                    i
                    j

              ⏟

              rate-of-expansion tensor

              S

                i
                j

        +

                            1
                            2

                          (

                              ∂

                                i

                              v

                                j

                            +

                              ∂

                                j

                              v

                                i

                          )

                      ⏞

                      E

                        i
                        j

                −

                  S

                    i
                    j

              ⏟

              rate-of-shear tensor

              D

                i
                j

        ,

    {\displaystyle E_{ij}=\underbrace {{\frac {1}{3}}\left(\sum _{k}\partial {k}v{k}\right)\delta _{ij}} {{\text{rate-of-expansion tensor }}S{ij}}+\underbrace {\overbrace {{\frac {1}{2}}\left(\partial {i}v{j}+\partial {j}v{i}\right)} ^{E_{ij}}-S_{ij}} {{\text{rate-of-shear tensor }}D{ij}},}

Here δ is the unit tensor, such that δij is 1 if i = j and 0 if i ≠ j. This decomposition is independent of the choice of coordinate system, and is therefore physically significant.
The trace of the expansion rate tensor is the divergence of the velocity field:

        ∇
        ⋅

          v

          ∂

            1

          v

            1

        +

          ∂

            2

          v

            2

        +

          ∂

            3

          v

            3

        ;

    {\displaystyle \nabla \cdot \mathbf {v} =\partial {1}v{1}+\partial {2}v{2}+\partial {3}v{3};}

which is the rate at which the volume of a fixed amount of fluid increases at that point.
The shear rate tensor is represented by a symmetric 3 × 3 matrix, and describes a flow that combines compression and expansion flows along three orthogonal axes, such that there is no change in volume. This type of flow occurs, for example, when a rubber strip is stretched by pulling at the ends, or when honey falls from a spoon as a smooth unbroken stream.
For a two-dimensional flow, the divergence of v has only two terms and quantifies the change in area rather than volume. The factor 1/3 in the expansion rate term should be replaced by 1/2 in that case.

Examples
The study of velocity gradients is useful in analysing path dependent materials and in the subsequent study of stresses and strains; e.g., Plastic deformation of metals. The near-wall velocity gradient of the unburned reactants flowing from a tube is a key parameter for characterising flame stability. The velocity gradient of a plasma can define conditions for the solutions to fundamental equations in magnetohydrodynamics.

Fluid in a pipe
Consider the velocity field of a fluid flowing through a pipe. The layer of fluid in contact with the pipe tends to be at rest with respect to the pipe. This is called the no slip condition. If the velocity difference between fluid layers at the centre of the pipe and at the sides of the pipe is sufficiently small, then the fluid flow is observed in the form of continuous layers. This type of flow is called laminar flow.
The flow velocity difference between adjacent layers can be measured in terms of a velocity gradient, given by

        Δ
        u

          /

        Δ
        y

    {\displaystyle \Delta u/\Delta y}

. Where

        Δ
        u

    {\displaystyle \Delta u}

 is the difference in flow velocity between the two layers and

        Δ
        y

    {\displaystyle \Delta y}

 is the distance between the layers.
