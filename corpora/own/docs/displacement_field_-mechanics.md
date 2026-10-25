# Displacement field (mechanics)

Displacement field (mechanics)

In mechanics, a displacement field is the assignment of displacement vectors for all points in a region or body that are displaced from one state to another. A displacement vector specifies the position of a point or a particle in reference to an origin or to a previous position. For example, a displacement field may be used to describe the effects of deformation on a solid body.

Formulation
Before considering displacement, the state before deformation must be defined. It is a state in which the coordinates of all points are known and described by the function:

                R
                →

            0

        :
        Ω
        →
        P

    {\displaystyle {\vec {R}}_{0}:\Omega \to P}

where

                R
                →

            0

    {\displaystyle {\vec {R}}_{0}}

 is a placement vector

        Ω

    {\displaystyle \Omega }

 are all the points of the body

        P

    {\displaystyle P}

 are all the points in the space in which the body is present
Most often it is a state of the body in which no forces are applied.
Then given any other state of this body in which coordinates of all its points are described as

                R
                →

            1

    {\displaystyle {\vec {R}}_{1}}

 the displacement field is the difference between two body states:

              u
              →

                R
                →

            1

        −

                R
                →

            0

    {\displaystyle {\vec {u}}={\vec {R}}{1}-{\vec {R}}{0}}

where

              u
              →

    {\displaystyle {\vec {u}}}

 is a displacement field, which for each point of the body specifies a displacement vector.

Decomposition

The displacement of a body has two components: a rigid-body displacement and a deformation.

A rigid-body displacement consists of a translation and rotation of the body without changing its shape or size.
Deformation implies the change in shape and/or size of the body from an initial or undeformed configuration

          κ

            0

        (

            B

        )

    {\displaystyle \kappa _{0}({\mathcal {B}})}

 to a current or deformed configuration

          κ

            t

        (

            B

        )

    {\displaystyle \kappa _{t}({\mathcal {B}})}

 (Figure 1).
A change in the configuration of a continuum body can be described by a displacement field. A displacement field is a vector field of all displacement vectors for all particles in the body, which relates the deformed configuration with the undeformed configuration. The distance between any two particles changes if and only if deformation has occurred. If displacement occurs without deformation, then it is a rigid-body displacement.

Displacement gradient tensor

Two types of displacement gradient tensor may be defined, following the Lagrangian and Eulerian specifications.
The displacement of particles indexed by variable i may be expressed as follows. The vector joining the positions of a particle in the undeformed configuration

          P

            i

    {\displaystyle P_{i}}

 and deformed configuration

          p

            i

    {\displaystyle p_{i}}

 is called the displacement vector,

          p

            i

        −

          P

            i

    {\displaystyle p_{i}-P_{i}}

, denoted

          u

            i

    {\displaystyle u_{i}}

 or

          U

            i

    {\displaystyle U_{i}}

 below.

Material coordinates (Lagrangian description)
Using

          X

    {\displaystyle \mathbf {X} }

 in place of

          P

            i

    {\displaystyle P_{i}}

 and

          x

    {\displaystyle \mathbf {x} }

 in place of

          p

            i

    {\displaystyle p_{i}\,!}

, both of which are vectors from the origin of the coordinate system to each respective point, we have the Lagrangian description of the displacement vector:

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

    {\displaystyle \mathbf {u} (\mathbf {X} ,t)=u_{i}\mathbf {e} _{i}}

where

            e

            i

    {\displaystyle \mathbf {e} _{i}}

 are the unit vectors that define the basis of the material (body-frame) coordinate system.
Expressed in terms of the material coordinates, i.e.

          u

    {\displaystyle \mathbf {u} }

 as a function of

          X

    {\displaystyle \mathbf {X} }

, the displacement field is:

          u

        (

          X

        ,
        t
        )

          b

        (
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

    {\displaystyle \mathbf {u} (\mathbf {X} ,t)=\mathbf {b} (t)+\mathbf {x} (\mathbf {X} ,t)-\mathbf {X} \qquad {\text{or}}\qquad u_{i}=\alpha {iJ}b{J}+x_{i}-\alpha {iJ}X{J}}

where

          b

        (
        t
        )

    {\displaystyle \mathbf {b} (t)}

 is the displacement vector representing rigid-body translation.
The partial derivative of the displacement vector with respect to the material coordinates yields the material displacement gradient tensor

          ∇

              X

          u

    {\displaystyle \nabla _{\mathbf {X} }\mathbf {u} \,!}

. Thus we have,

          ∇

              X

          u

          ∇

              X

          x

        −

          R

          F

        −

          R

          or

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

          α

            i
            K

          F

            i
            K

        −

          α

            i
            K

    {\displaystyle \nabla _{\mathbf {X} }\mathbf {u} =\nabla {\mathbf {X} }\mathbf {x} -\mathbf {R} =\mathbf {F} -\mathbf {R} \qquad {\text{or}}\qquad {\frac {\partial u{i}}{\partial X_{K}}}={\frac {\partial x_{i}}{\partial X_{K}}}-\alpha {iK}=F{iK}-\alpha _{iK}}

where

          F

    {\displaystyle \mathbf {F} }

 is the material deformation gradient tensor and

          R

    {\displaystyle \mathbf {R} }

 is a rotation.

Spatial coordinates (Eulerian description)
In the Eulerian description, the vector extending from a particle

        P

    {\displaystyle P}

 in the undeformed configuration to its location in the deformed configuration is called the displacement vector:

          U

        (

          x

        ,
        t
        )

          U

            J

            E

            J

    {\displaystyle \mathbf {U} (\mathbf {x} ,t)=U_{J}\mathbf {E} _{J}}

where

            E

            i

    {\displaystyle \mathbf {E} _{i}}

 are the orthonormal unit vectors that define the basis of the spatial (lab frame) coordinate system.
Expressed in terms of spatial coordinates, i.e.

          U

    {\displaystyle \mathbf {U} }

 as a function of

          x

    {\displaystyle \mathbf {x} }

, the displacement field is:

          U

        (

          x

        ,
        t
        )

          b

        (
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

    {\displaystyle \mathbf {U} (\mathbf {x} ,t)=\mathbf {b} (t)+\mathbf {x} -\mathbf {X} (\mathbf {x} ,t)\qquad {\text{or}}\qquad U_{J}=b_{J}+\alpha {Ji}x{i}-X_{J}}

The spatial derivative, i.e., the partial derivative of the displacement vector with respect to the spatial coordinates, yields the spatial displacement gradient tensor

          ∇

              x

          U

    {\displaystyle \nabla _{\mathbf {x} }\mathbf {U} \,!}

. Thus we have,

          ∇

              x

          U

            R

            T

        −

          ∇

              x

          X

            R

            T

        −

            F

            −
            1

          or

              ∂

                U

                  J

              ∂

                x

                  k

          α

            J
            k

        −

              ∂

                X

                  J

              ∂

                x

                  k

          α

            J
            k

        −

          F

            J
            k

            −
            1

        ,

    {\displaystyle \nabla _{\mathbf {x} }\mathbf {U} =\mathbf {R} ^{T}-\nabla {\mathbf {x} }\mathbf {X} =\mathbf {R} ^{T}-\mathbf {F} ^{-1}\qquad {\text{or}}\qquad {\frac {\partial U{J}}{\partial x_{k}}}=\alpha {Jk}-{\frac {\partial X{J}}{\partial x_{k}}}=\alpha {Jk}-F{Jk}^{-1}\,,}

where

            F

            −
            1

          H

    {\displaystyle \mathbf {F} ^{-1}=\mathbf {H} }

 is the spatial deformation gradient tensor.

Relationship between the material and spatial coordinate systems

          α

            J
            i

    {\displaystyle \alpha _{Ji}}

 are the direction cosines between the material and spatial coordinate systems with unit vectors

            E

            J

    {\displaystyle \mathbf {E} _{J}}

 and

            e

            i

    {\displaystyle \mathbf {e} _{i}\,!}

, respectively. Thus

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

The relationship between

          u

            i

    {\displaystyle u_{i}}

 and

          U

            J

    {\displaystyle U_{J}}

 is then given by

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

Combining the coordinate systems of deformed and undeformed configurations
It is common to superimpose the coordinate systems for the deformed and undeformed configurations, which results in

          b

        0

    {\displaystyle \mathbf {b} =0\,!}

, and the direction cosines become Kronecker deltas, i.e.,

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

Thus in material (undeformed) coordinates, the displacement may be expressed as:

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

    {\displaystyle \mathbf {u} (\mathbf {X} ,t)=\mathbf {x} (\mathbf {X} ,t)-\mathbf {X} \qquad {\text{or}}\qquad u_{i}=x_{i}-\delta {iJ}X{J}}

And in spatial (deformed) coordinates, the displacement may be expressed as:

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

    {\displaystyle \mathbf {U} (\mathbf {x} ,t)=\mathbf {x} -\mathbf {X} (\mathbf {x} ,t)\qquad {\text{or}}\qquad U_{J}=\delta {Ji}x{i}-X_{J}}
