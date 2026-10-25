# Peridynamics

Peridynamics

Peridynamics is a non-local formulation of continuum mechanics that is oriented toward deformations with discontinuities, especially fractures. Originally, bond-based peridynamic was introduced, wherein, internal interaction forces between a material point and all the other ones with which it can interact, are modeled as a central force field. This type of force field can be imagined as a mesh of bonds connecting each point of the body with every other interacting point within a certain distance which depends on a material property, called the peridynamic horizon. Later, to overcome bond-based framework limitations for the material Poisson's ratio (

        1

          /

        3

    {\displaystyle 1/3}

 for plane stress and

        1

          /

        4

    {\displaystyle 1/4}

 for plane strain in two-dimensional configurations;

        1

          /

        4

    {\displaystyle 1/4}

 for three-dimensional ones), state-base peridynamics, has been formulated. Its characteristic feature is that the force exchanged between a point and another one is influenced by the deformation state of all other bonds relative to its interaction zone.
The characteristic feature of peridynamics, which makes it different from classical local mechanics, is the presence of finite-range bonds between any two points of the material body: it is a feature that approaches such formulations as discrete meso-scale theories of matter.

Etymology
The term peridynamic, as an adjective, was proposed in the year 2000 and comes from the prefix peri-, which means all around, near, or surrounding; and the root dyna, which means force or power. The term peridynamics, as a noun, is a shortened form of the phrase peridynamic model of solid mechanics.

Purpose
A fracture is a mathematical singularity to which the classical equations of continuum mechanics cannot be applied directly. The peridynamic theory has been proposed with the purpose of mathematically models fractures formation and dynamic in elastic materials. It is founded on integral equations, in contrast with classical continuum mechanics, which is based on partial differential equations. Since partial derivatives do not exist on crack surfaces and other geometric singularities, the classical equations of continuum mechanics cannot be applied directly when such features are present in a deformation. The integral equations of the peridynamic theory hold true also on singularities and can be applied directly, because they do not require partial derivatives. The ability to apply the same equations directly at all points in a mathematical model of a deforming structure helps the peridynamic approach to avoid the need for the special techniques of fracture mechanics like xFEM. For example, in peridynamics, there is no need for a separate crack growth law based on a stress intensity factor.

Definition and basic terminology

In the context of peridynamic theory, physical bodies are treated as constituted by a continuous points mesh which can exchange long-range mutual interaction forces, within a maximum and well established distance

        δ

        0

    {\displaystyle \delta >0}

: the peridynamic horizon radius. This perspective approaches much more to molecular dynamics than macroscopic bodies, and as a consequence, is not based on the concept of stress tensor (which is a local concept) and drift toward the notion of pairwise force that a material point

            x

    {\displaystyle {\bf {x}}}

 exchanges within its peridynamic horizon. With a Lagrangian point of view, suited for small displacements, the peridynamic horizon is considered fixed in the reference configuration and, then, deforms with the body. Consider a material body represented by

        Ω
        ⊂

            R

            n

    {\displaystyle \Omega \subset \mathbb {R} ^{n}}

, where

        n

    {\displaystyle n}

 can be either 1, 2 or 3. The body has a positive density

        ρ

    {\displaystyle \rho }

. Its reference configuration at the initial time is denoted by

          Ω

            0

        ⊂

            R

            n

    {\displaystyle \Omega _{0}\subset \mathbb {R} ^{n}}

. The reference configuration can either be the stress-free configuration or a specific configuration of the body chosen as a reference. In the context of peridynamics, every point in

        Ω

    {\displaystyle \Omega }

 interacts with all the points

              x

          ′

    {\displaystyle {\bf {x}}'}

 within a certain neighborhood defined by

        d
        (

            x

        ,

              x

          ′

        )
        ≤
        δ

    {\displaystyle d({\bf {x}},{\bf {x}}')\leq \delta }

, where

        δ

        0

    {\displaystyle \delta >0}

 and

        d
        (
        ⋅
        ,
        ⋅
        )

    {\displaystyle d(\cdot ,\cdot )}

 represents a suitable distance function on

          Ω

            0

    {\displaystyle \Omega _{0}}

. This neighborhood is often referred to as

          B

            δ

        (

            x

        )

    {\displaystyle B_{\delta }({\bf {x}})}

 in the literature. It is commonly known as the horizon or the family of

            x

    {\displaystyle {\bf {x}}}

.
The kinematics of

            x

    {\displaystyle {\bf {x}}}

 is described in terms of its displacement from the reference position, denoted as

            u

        (

            x

        ,
        t
        )
        :

          Ω

            0

        ×

            R

            +

        →

            R

            n

    {\displaystyle {\bf {u}}({\bf {x}},t):\Omega _{0}\times \mathbb {R} ^{+}\rightarrow \mathbb {R} ^{n}}

. Consequently, the position of

            x

    {\displaystyle {\bf {x}}}

 at a specific time

        t

    {\displaystyle t}

 is determined by

            y

        (

            x

        ,
        t
        )
        :=

            x

        +

            u

        (

            x

        ,
        t
        )

    {\displaystyle {\bf {y}}({\bf {x}},t):={\bf {x}}+{\bf {u}}({\bf {x}},t)}

. Furthermore, for each pair of interacting points, the change in the length of the bond relative to the initial configuration is tracked over time through the relative strain

        s
        (

            x

        ,

              x

          ′

        ,
        t
        )

    {\displaystyle s({\bf {x}},{\bf {x}}',t)}

, which can be expressed as:

        s

          (

                x

            ,

                  x

              ′

            ,
            t

          )

                    u

                  (

                          x

                        ′

                    ,
                    t

                  )

                −

                    u

                (

                    x

                ,
                t
                )

                      x

                    ′

                −

                    x

        ,

    {\displaystyle s\left({\bf {x}},{\bf {x}}',t\right)={\frac {\left|{\bf {u}}\left({\bf {x}}^{\prime },t\right)-{\bf {u}}({\bf {x}},t)\right|}{\left|{\bf {x}}^{\prime }-{\bf {x}}\right|}},}

where

        ⋅

    {\displaystyle |\cdot |}

 denotes the Euclidean norm and

              x

          ′

        ∈

          B

            δ

        (

            x

        )
        ∩

          Ω

            0

    {\displaystyle {\bf {x}}'\in B_{\delta }({\bf {x}})\cap \Omega _{0}}

.
The interaction between any

            x

    {\displaystyle {\bf {x}}}

 and

              x
              ′

    {\displaystyle {\bf {x'}}}

 is referred to as a bond. These pairwise bonds have varying lengths over time in response to the force per unit volume squared, denoted as

            f

        ≡

            f

        (

              x

          ′

        ,

            x

        ,

            u

        (

              x

          ′

        )
        ,

            u

        (

            x

        )
        ,
        t
        )

    {\displaystyle {\bf {f}}\equiv {\bf {f}}({\bf {x}}',{\bf {x}},{\bf {u}}({\bf {x}}'),{\bf {u}}({\bf {x}}),t)}

.
This force is commonly known as the pairwise force function or peridynamic kernel, and it encompasses all the constitutive (material-dependent) properties. It describes how the internal forces depend on the deformation. It's worth noting that the dependence of

            u

    {\displaystyle {\bf {u}}}

 on

        t

    {\displaystyle t}

 has been omitted here for the sake of simplicity in notation. Additionally, an external forcing term,

          b

        (

            x

        ,
        t
        )

    {\displaystyle \mathbf {b} ({\bf {x}},t)}

, is introduced, which results in the following equation of motion, representing the fundamental equation of peridynamics:

          ρ

                u

              t
              t

          (

              x

          ,
          t
          )

              F

          (

              x

          ,
          t
          )

        .

    {\displaystyle {\rho {\bf {u}}_{tt}({\bf {x}},t)={\bf {F}}({\bf {x}},t)}\,.}

where the integral term

            F

        (

            x

        ,
        t
        )

    {\displaystyle {\bf {F}}({\bf {x}},t)}

 is the sum of all of the internal and external per-unit-volume forces acting on

            x

    {\displaystyle {\bf {x}}}

:

              F

          (

              x

          ,
          t
          )
          :=

            ∫

                Ω

                  0

              ∩

                B

                  δ

              (

                  x

              )

              f

            (

                    x

                ′

              ,

                  x

              ,

                  u

                (

                      x

                  ′

                )

              ,

                  u

              (

                  x

              )

            )

          d

            V

                    x

                ′

          +

              b

          (

              x

          ,
          t
          )

        .

    {\displaystyle {{\bf {F}}({\bf {x}},t):=\int _{\Omega {0}\cap B{\delta }({\bf {x}})}{\bf {f}}\left({\bf {x}}',{\bf {x}},{\bf {u}}\left({\bf {x}}'\right),{\bf {u}}({\bf {x}})\right)dV_{{\bf {x}}'}+{\bf {b}}({\bf {x}},t)}\,.}

The vector valued function

            f

    {\displaystyle {\bf {f}}}

 is the force density that

              x
              ′

    {\displaystyle {\bf {x'}}}

 exerts on

            x

    {\displaystyle {\bf {x}}}

. This force density depends on the relative displacement and relative position vectors between

              x
              ′

    {\displaystyle {\bf {x'}}}

 and

            x

    {\displaystyle {\bf {x}}}

. The dimension of

            f

    {\displaystyle {\bf {f}}}

 is

        [
        N

          /

          m

            6

        ]

    {\displaystyle [N/m^{6}]}

.

Bond-based peridynamics
In this formulation of peridynamics, the kernel is determined by the nature of internal forces and physical constraints that governs the interaction between only two material points. For the sake of brevity, the following quantities are defined

              ξ

        :=

              x

          ′

        −

            x

    {\displaystyle {\bf {\bf {\xi }}}:={\bf {x}}'-{\bf {x}}}

 and

            η

        :=

            u

        (

              x

          ′

        )
        −

            u

        (

            x

        )

    {\displaystyle {\bf {\eta }}:={\bf {u}}({\bf {x}}')-{\bf {u}}({\bf {x}})}

 so that

            f

        (

              x

          ′

        −

            x

        ,

            u

        (

              x

          ′

        )
        −

            u

        (

            x

        )
        )
        ≡

              f

            (

                ξ

            ,

                η

            )

    {\displaystyle {\bf {f}}({\bf {x}}'-{\bf {x}},{\bf {u}}({\bf {x}}')-{\bf {u}}({\bf {x}}))\equiv {\bf {{f}({\bf {\xi }},{\bf {\eta }})}}}

Action and reaction principle
For any

            x

    {\displaystyle {\bf {x}}}

   and

              x
              ′

    {\displaystyle {\bf {x'}}}

   belonging to the neighborhood

          B

            δ

        (

            x

        )

    {\displaystyle B_{\delta }({\bf {x}})}

, the following relationship holds:

            f

        (
        −
        η
        ,
        −
        ξ
        )

        −

            f

        (
        η
        ,
        ξ
        )

    {\displaystyle {\bf {f}}(-\eta ,-\xi )=-{\bf {f}}(\eta ,\xi )}

  . This expression reflects the principle of action and reaction, commonly known as Newton's third law. It guarantees the conservation of linear momentum in a system composed of mutually interacting particles.

Angular momentum conservation
For any

            x

    {\displaystyle {\bf {x}}}

  and

                x

              ′

    {\displaystyle {\bf {{x}'}}}

  belonging to the neighborhood

          B

            δ

        (

            x

        )

    {\displaystyle B_{\delta }({\bf {x}})}

, the following condition holds:

        (
        ξ
        +
        η
        )
        ×

            f

        (
        ξ
        ,
        η
        )

        0

    {\displaystyle (\xi +\eta )\times {\bf {f}}(\xi ,\eta )=0}

 . This condition arises from considering the relative deformed ray-vector connecting

            x

    {\displaystyle {\bf {x}}}

  and

                x

              ′

    {\displaystyle {\bf {{x}'}}}

 as

        ξ
        +
        η

    {\displaystyle \xi +\eta }

 . The condition is satisfied if and only if the pairwise force density vector has the same direction as the relative deformed ray-vector. In other words,

            f

        (
        ξ
        ,
        η
        )

        f
        (
        ξ
        ,
        η
        )
        (
        ξ
        +
        η
        )

    {\displaystyle {\bf {f}}(\xi ,\eta )=f(\xi ,\eta )(\xi +\eta )}

  for all

        ξ

    {\displaystyle \xi }

  and

        η

    {\displaystyle \eta }

 , where

        f
        (
        ξ
        ,
        η
        )

    {\displaystyle f(\xi ,\eta )}

  is a scalar-valued function.

Hyperelastic material
An hyperelastic material is a material with constitutive relation such that:

          ∫

            Γ

            f

        (

            ξ

        ,

            η

        )
        ⋅
        d

            η

        0

        ,

        ∀

           closed curve

        Γ
        ,

        ∀

            ξ

        ≠

              0

            ,

    {\displaystyle \int _{\Gamma }{\bf {f}}({\bf {\xi }},{\bf {\eta }})\cdot d{\bf {\eta }}=0\,,\quad \forall {\text{ closed curve }}\Gamma ,\ \ \ \ \forall {\bf {\xi }}\neq {\bf {{0},}}}

or, equivalently, by Stokes' theorem

          ∇

              η

        ×

            f

        (

            ξ

        ,

            η

        )

              0

    {\displaystyle \nabla _{\bf {\eta }}\times {\bf {f}}({\bf {\xi }},{\bf {\eta }})={\bf {{0}\,}}}

  ,

        ∀

            ξ

        ,

            η

    {\displaystyle \forall \,{\bf {\xi }},\,{\bf {\eta }}}

and, thus,

            f

        (

            ξ

        ,

            η

        )

          ∇

              η

        Φ
        (

            ξ

        ,

            η

        )

        ∀

            ξ

        ,

            η

        .

    {\displaystyle {\bf {f}}({\bf {\xi }},{\bf {\eta }})=\nabla _{\bf {\eta }}\Phi ({\bf {\xi }},\,{\bf {\eta }})\,\forall {\bf {\xi }},\,{\bf {\eta }}\,.}

In the equation above

        Φ
        (

            ξ

        ,

            η

        )

    {\displaystyle \Phi ({\bf {\xi }},{\bf {\eta }})}

 is the scalar valued potential function in

          C

            2

        (

            R

            n

        ∖

              {
              0
              }

            ×

                R

                n

            )

    {\displaystyle C^{2}(\mathbb {R} ^{n}\setminus {\bf {{{0}}\times \mathbb {R} ^{n})}}}

. Due to the necessity of satisfying angular momentum conservation, the condition below on the scalar valued function

        f
        (

            ξ

        ,

            η

        )

    {\displaystyle f({\bf {\xi }},{\bf {\eta }})}

 follows

              ∂
              f
              (

                  ξ

              ,

                  η

              )

              ∂

                  η

        g
        (

            ξ

        ,

            η

        )
        (

            ξ

        +

            η

        )
        .

    {\displaystyle {\frac {\partial f({\bf {\xi }},{\bf {\eta }})}{\partial {\bf {\eta }}}}=g({\bf {\xi }},{\bf {\eta }})({\bf {\xi }}+{\bf {\eta }}).}

where

        g
        (

            ξ

        ,

            η

        )

    {\displaystyle g({\bf {\xi }},{\bf {\eta }})}

 is a scalar valued function. Integrating both sides of the equation, the following condition on

        g
        (

            ξ

        ,

            η

        )

    {\displaystyle g({\bf {\xi }},{\bf {\eta }})}

 is obtained

            f

        (

            ξ

        ,

            η

        )

        h
        (

            ξ

        +

            η

        ,

            ξ

        )
        (

            ξ

        +

            η

        )

    {\displaystyle {\bf {f}}({\bf {\xi }},{\bf {\eta }})=h(|{\bf {\xi }}+{\bf {\eta }}|,{\bf {\xi }})({\bf {\xi }}+{\bf {\eta }})}

,
for

        h
        (

            ξ

        +

            η

        ,

            ξ

        )

    {\displaystyle h(|{\bf {\xi }}+{\bf {\eta }}|,{\bf {\xi }})}

 a scalar valued function. The elastic nature of

            f

    {\displaystyle {\bf {f}}}

 is evident: the interaction force depends only on the initial relative position between points

            x

    {\displaystyle {\bf {x}}}

 and

              x

          ′

    {\displaystyle {\bf {x}}'}

 and the modulus of their relative position,

            ξ

        +

            η

    {\displaystyle |{\bf {\xi }}+{\bf {\eta }}|}

, in the deformed configuration

          Ω

            t

    {\displaystyle \Omega _{t}}

 at time

        t

    {\displaystyle t}

. Applying the isotropy hypothesis, the dependence on vector

            ξ

    {\displaystyle {\bf {\xi }}}

 can be substituted with a dependence on its modulus

            ξ

    {\displaystyle |{\bf {\xi }}|}

,

            f

        (

            ξ

        ,

            η

        )

        h
        (

            ξ

        +

            η

        ,

            ξ

        )
        (

            ξ

        +

            η

        )
        .

    {\displaystyle {\bf {f}}({\bf {\xi }},{\bf {\eta }})=h(|{\bf {\xi }}+{\bf {\eta }}|,|{\bf {\xi }}|)({\bf {\xi }}+{\bf {\eta }}).}

Bond forces can, thus, be considered as modeling a spring net that connects each point

            x

        ∈

          Ω

            0

    {\displaystyle {\bf {x}}\in \Omega _{0}}

 pairwise with

              x

          ′

        ∈

          B

            δ

        (

            x

        )
        ∩

          Ω

            0

    {\displaystyle {\bf {x}}'\in B_{\delta }({\bf {x}})\cap \Omega _{0}}

.

Linear elastic material
If

            η

        ≪
        1

    {\displaystyle |{\bf {\eta }}|\ll 1}

, the peridynamic kernel can be linearised around

            η

            0

    {\displaystyle {\bf {\eta }}={\bf {0}}}

:

            f

        (

            ξ

        ,

            η

        )
        ≈

            f

        (

            ξ

        ,

              0

            )
            +

                      ∂

                          f

                      (

                          ξ

                      ,

                          η

                      )

                      ∂

                          η

                    η

                    0

                η

            ;

    {\displaystyle {\bf {f}}({\bf {\xi }},{\bf {\eta }})\approx {\bf {f}}({\bf {\xi }},{\bf {{0})+\left.{\frac {\partial {\bf {f}}({\bf {\xi }},{\bf {\eta }})}{\partial {\bf {\eta }}}}\right|_{{\bf {\eta }}={\bf {0}}}{\bf {\eta }};}}}

then, a second-order micro-modulus tensor can be defined as

            C

        (

            ξ

        )

                  ∂

                      f

                  (

                      ξ

                  ,

                      η

                  )

                  ∂

                      η

                η

                0

            ξ

        ⊗

                  ∂
                  f
                  (

                      ξ

                  ,

                      η

                  )

                  ∂

                      η

                η

                0

        +

          f

            0

        I

    {\displaystyle {\bf {C}}({\bf {\xi }})=\left.{\frac {\partial {\bf {f}}({\bf {\xi }},{\bf {\eta }})}{\partial {\bf {\eta }}}}\right|{{\bf {\eta }}={\bf {0}}}={\bf {\xi }}\otimes \left.{\frac {\partial f({\bf {\xi }},{\bf {\eta }})}{\partial {\bf {\eta }}}}\right|{{\bf {\eta }}={\bf {0}}}+f_{0}I}

where

          f

            0

        :=
        f
        (

            ξ

        ,

            0

        )

    {\displaystyle f_{0}:=f({\bf {\xi }},{\bf {0}})}

 and

        I

    {\displaystyle I}

 is the identity tensor. Following application of linear momentum balance, elasticity and isotropy condition, the micro-modulus tensor can be expressed in this form

            C

        (

            ξ

        )

        λ
        (

            ξ

        )

            ξ

        ⊗

            ξ

        +

          f

            0

        I
        .

    {\displaystyle {\bf {C}}({\bf {\xi }})=\lambda (|{\bf {\xi }}|){\bf {\xi }}\otimes {\bf {\xi }}+f_{0}I.}

Therefore, for a linearised hyperelastic material, its peridynamic kernel holds the following structure

            f

        (

            ξ

        ,

            η

        )
        ≈

            f

        (

            ξ

        ,

            0

        )
        +

          (

            λ
            (

                ξ

            )

                ξ

            ⊗

                ξ

            +

              f

                0

            I

          )

            η

        .

    {\displaystyle {\bf {f}}({\bf {\xi }},{\bf {\eta }})\approx {\bf {f}}({\bf {\xi }},{\bf {0}})+\left(\lambda (|{\bf {\xi }}|){\bf {\xi }}\otimes {\bf {\xi }}+f_{0}I\right){\bf {\eta }}.}

Expressions for the peridynamic kernel
The peridynamic kernel is a versatile function that characterizes the constitutive behavior of materials within the framework of peridynamic theory. One commonly employed formulation of the kernel is used to describe a class of materials known as prototype micro-elastic brittle (PMB) materials. In the case of isotropic PMB materials, the pairwise force is assumed to be linearly proportional to the finite stretch experienced by the material, defined as

        s
        :=
        (

            ξ

        +

            η

        −

            ξ

        )

          /

            ξ

    {\displaystyle s:=(|{\bf {\xi }}+{\bf {\eta }}|-|{\bf {\xi }}|)/|{\bf {\xi }}|}

,
so that

          f

        (

            η

        ,

            ξ

        )

        f
        (

            ξ

        +

            η

        ,

            ξ

        )

              n

            ,

    {\displaystyle \mathbf {f} ({\bf {\eta }},{\bf {\xi }})=f(|{\bf {\xi }}+{\bf {\eta }}|,|{\bf {\xi }}|){\bf {{n},}}}

where

              n

            :=
            (

                ξ

            +

                η

            )

              /

                ξ

            +

                η

    {\displaystyle {\bf {{n}:=({\bf {\xi }}+{\bf {\eta }})/|{\bf {\xi }}+{\bf {\eta }}|}}}

and where the scalar function

        f

    {\displaystyle f}

 is defined as follow

        f

        c
        s
        μ
        (
        s
        ,
        t
        )

        c

                  ξ

              +

                  η

              −

                  ξ

                  ξ

        μ
        (
        s
        ,
        t
        )
        ,

    {\displaystyle f=cs\mu (s,t)=c\;{\frac {|{\bf {\xi }}+{\bf {\eta }}|-|{\bf {\xi }}|}{|{\bf {\xi }}|}}\mu (s,t),}

 with

        μ
        (
        s
        ,
        t
        )

          {

                    1

                    ,

                       if

                    s

                      (

                          t

                            ′

                        ,

                            ξ

                      )

                    <

                      s

                        0

                    ,

                    0

                    ,

                       otherwise,

               for all

            0
            ≤

              t

                ′

            ≤
            t

        ;

    {\displaystyle \mu (s,t)=\left{{\begin{array}{ll}1\,,&{\text{ if }}s\left(t^{\prime },{\bf {\xi }}\right)<s_{0}\,,\0\,,&{\text{ otherwise, }}\end{array}}\ \ \ \ {\text{ for all }}0\leq t^{\prime }\leq t\right.;}

The constant

        c

    {\displaystyle c}

 is referred to as the micro-modulus constant, and the function

        μ
        (
        s
        ,
        t
        )

    {\displaystyle \mu (s,t)}

 serves to indicate whether, at a given time

          t
          ′

        ≤
        t

    {\displaystyle t'\leq t}

, the bond stretch

        s

    {\displaystyle s}

 associated with the pair

        (

            x
            ,

              x
              ′

        )

    {\displaystyle ({\bf {x,\,x'}})}

 has surpassed the critical value

          s

            0

    {\displaystyle s_{0}}

. If the critical value is exceeded, the bond is considered broken, and a pairwise force of zero is assigned for all

        t
        ≥

          t
          ′

    {\displaystyle t\geq t'}

.
After a comparison between the strain energy density value obtained under isotropic extension respectively employing peridynamics and classical continuum theory framework, the physical coherent value of micro-modulus

        c

    {\displaystyle c}

 can be found

        c

              18
              k

              π

                δ

                  4

        ,

    {\displaystyle c={\frac {18k}{\pi \delta ^{4}}},}

where

        k

    {\displaystyle k}

 is the material bulk modulus.
Following the same approach the micro-modulus constant

        c

    {\displaystyle c}

 can be extended to

        c
        (

            ξ

        ,
        δ
        )

    {\displaystyle c({\bf {\xi }},\delta )}

, where

        c

    {\displaystyle c}

 is now a micro-modulus function. This function provides a more detailed description of how the intensity of pairwise forces is distributed over the peridynamic horizon

          B

            δ

        (

            x

        )

    {\displaystyle B_{\delta }({\bf {x}})}

. Intuitively, the intensity of forces decreases as the distance between

            x

    {\displaystyle {\bf {x}}}

 and

              x

          ′

        ∈

          B

            δ

        (

            x

        )

    {\displaystyle {\bf {x}}'\in B_{\delta }({\bf {x}})}

 increases, but the specific manner in which this decrease occurs can vary.
The micro-modulus function is expressed as

        c
        (

            ξ

        ,
        δ
        )
        :=
        c
        (

              0

            ,
            δ
            )
            k
            (

                ξ

            ,
            δ
            )

            ,

    {\displaystyle c({\bf {\xi }},\delta ):=c({\bf {{0},\delta )k({\bf {\xi }},\delta )\,,}}}

where the constant

        c
        (

              0

            ,
            δ
            )

    {\displaystyle c({\bf {{0},\delta )}}}

 is obtained by comparing peridynamic strain density with the classical mechanical theories;

        k
        (

            ξ

        ,
        δ
        )

    {\displaystyle k({\bf {\xi }},\delta )}

 is a function defined on

          Ω

            0

    {\displaystyle \Omega _{0}}

 with the following properties (given the restrictions of momentum conservation and isotropy)

          {

                  k
                  (

                      ξ

                  ,
                  δ
                  )

                  k
                  (
                  −

                      ξ

                  ,
                  δ
                  )

                  ,

                    lim

                          ξ

                      →

                          0

                  k
                  (

                      ξ

                  ,
                  δ
                  )

                    max

                          ξ

                      ∈

                          R

                          n

                  {
                  k
                  (

                      ξ

                  ,
                  δ
                  )
                  }

                  ,

                    lim

                          ξ

                      →
                      δ

                  k
                  (

                      ξ

                  ,
                  δ
                  )

                  0

                  ,

                    ∫

                          R

                          n

                    lim

                      δ
                      →
                      0

                  k
                  (

                      ξ

                  ,
                  δ
                  )
                  d

                      x

                    ∫

                          R

                          n

                  Δ
                  (

                      ξ

                  )
                  d

                      x

                  1

                  ,

    {\displaystyle \left{{\begin{array}{l}k({\bf {\xi }},\delta )=k(-{\bf {\xi }},\delta )\,,\\lim _{{\bf {\xi }}\rightarrow {\bf {0}}}k({\bf {\xi }},\delta )=\max _{{\bf {\xi }}\ \in \mathbb {R} ^{n}}{k({\bf {\xi }},\delta )}\,,\\lim _{{\bf {\xi }}\rightarrow \delta }k({\bf {\xi }},\delta )=0\,,\\int _{\mathbb {R} ^{n}}\lim _{\delta \rightarrow 0}k({\bf {\xi }},\delta )d{\bf {x}}=\int _{\mathbb {R} ^{n}}\Delta ({\bf {\xi }})d{\bf {x}}=1\,,\end{array}}\right.}

where

        Δ
        (

            ξ

        )

    {\displaystyle \Delta ({\bf {\xi }})}

 is the Dirac delta function.

Cylindrical micro-modulus
The simplest expression for the micro-modulus function is

        c
        (

              0

            ,
            δ
            )
            k
            (

                ξ

            ,
            δ
            )

            c

                    1

                      B

                        δ

                    (

                          x

                      ′

                    )

    {\displaystyle c({\bf {{0},\delta )k({\bf {\xi }},\delta )=c{\bf {{1}{B{\delta }({\bf {x}}')}}}}}}

,
where

                1

                A

    {\displaystyle {\bf {{1}_{A}}}}

:

        X
        →

          R

    {\displaystyle X\rightarrow \mathbb {R} }

 is the indicator function of the subset

        A
        ⊂
        X

    {\displaystyle A\subset X}

, defined as

            1

            A

        (
        x
        )
        :=

            {

                  1
                  ,

                  x
                  ∈
                  A

                  ,

                  0
                  ,

                  x
                  ∉
                  A

                  ,

        ;

    {\displaystyle \mathbf {1} _{A}(x):={\begin{cases}1,&x\in A\,,\0,&x\notin A\,,\end{cases}}\;\;;}

Triangular micro-modulus
It is characterized by

        k
        (

            ξ

        ,
        δ
        )

    {\displaystyle k({\bf {\xi }},\delta )}

 to a be a linear function

        k
        (

            ξ

        ,
        δ
        )

          (

            1
            −

                      ξ

                δ

          )

                1

                  B

                    δ

                (

                      x

                  ′

                )

            .

    {\displaystyle k({\bf {\xi }},\delta )=\left(1-{\frac {|{\bf {\xi }}|}{\delta }}\right){\bf {{1}{B{\delta }({\bf {x}}')}.}}}

Normal micro-modulus
If one wants to reflects the fact that most common discrete physical systems are characterized by a Maxwell-Boltzmann distribution, in order to include this behavior in peridynamics, the following expression for

        k
        (

            ξ

        ,
        δ
        )

    {\displaystyle k({\bf {\xi }},\delta )}

 can be utilized

        k
        (

            ξ

        ,
        δ
        )

          e

            −
            (

                ξ

              /

            δ

              )

                2

                1

                  B

                    δ

                (

                      x

                  ′

                )

            ;

    {\displaystyle k({\bf {\xi }},\delta )=e^{-(|{\bf {\xi }}|/\delta )^{2}}{\bf {{1}{B{\delta }({\bf {x}}')};}}}

Quartic micro-modulus
In the literature one can find also the following expression for the

        k
        (

            ξ

        ,
        δ
        )

    {\displaystyle k({\bf {\xi }},\delta )}

function

        k
        (

            ξ

        ,
        δ
        )

            (

              1
              −

                  (

                      ξ
                      δ

                  )

                  2

            )

            2

                1

                  B

                    δ

                (

                      x

                  ′

                )

            .

    {\displaystyle k({\bf {\xi }},\delta )=\left(1-\left({\frac {\xi }{\delta }}\right)^{2}\right)^{2}{\bf {{1}{B{\delta }({\bf {x}}')}.}}}

Overall, depending on the specific material property to be modeled, there exists a wide range of expressions for the micro-modulus and, in general, for the peridynamic kernel. The above list is, thus, not exhaustive.

Damage
Damage is incorporated in the pairwise force function by allowing bonds to break when their elongation exceeds some prescribed value. After a bond breaks, it no longer sustains any force, and the endpoints are effectively disconnected from each other. When a bond breaks, the force it was carrying is redistributed to other bonds that have not yet broken. This increased load makes it more likely that these other bonds will break. The process of bond breakage and load redistribution, leading to further breakage, is how cracks grow in the peridynamic model.
Analytically, the bond breaking is specified inside the expression of the peridynamic kernel, by the function

        μ
        (
        s
        ,
        t
        )

          {

                    1

                    ,

                       if

                    s

                      (

                          t

                            ′

                        ,

                            ξ

                      )

                    <

                      s

                        0

                    ,

                    0

                    ,

                       otherwise,

               for all

            0
            ≤

              t

                ′

            ≤
            t

        ;

    {\displaystyle \mu (s,t)=\left{{\begin{array}{ll}1\,,&{\text{ if }}s\left(t^{\prime },{\bf {\xi }}\right)<s_{0}\,,\0\,,&{\text{ otherwise, }}\end{array}}\ \ \ \ {\text{ for all }}0\leq t^{\prime }\leq t\right.;}

If the graph of

            f

        (
        s
        ,
        t
        )

    {\displaystyle {\bf {f}}(s,t)}

 versus bond stretching

        s

    {\displaystyle s}

 is plotted, the action of the bond breaking function

        μ

    {\displaystyle \mu }

 in the fracture formation is clear. However, not only abrupt fracture can be modeled in the peridynamic framework and more general expressions for

        μ

    {\displaystyle \mu }

 can be employed.

State-based peridynamics
The theory described above assumes that each peridynamic bond responds independently of all the others. This is an oversimplification for most materials and leads to restrictions on the types of materials that can be modeled. In particular, this assumption implies that any isotropic linear elastic solid is restricted to a Poisson ratio of 1/4.
To address this lack of generality, the idea of peridynamic states was introduced. This framework allows the force density in each bond to depend on the stretches in all the bonds connected to its endpoints, in addition to its own stretch. For example, the force in a bond could depend on the net volume changes at the endpoints. The effect of this volume change, relative to the effect of the bond stretch, determines the Poisson ratio. With peridynamic states, any material that can be modeled within the standard theory of continuum mechanics can be modeled as a peridynamic material, while retaining the advantages of the peridynamic theory for fracture.
Mathematically the equation of the internal and external force term

              F

          (

              x

          ,
          t
          )
          :=

            ∫

                Ω

                  0

              ∩

                B

                  δ

              (

                  x

              )

              f

            (

                    x

                ′

              ,

                  x

              ,

                  u

                (

                      x

                  ′

                )

              ,

                  u

              (

                  x

              )

            )

          d

            V

                    x

                ′

          +

              b

          (

              x

          ,
          t
          )

        .

    {\displaystyle {{\bf {F}}({\bf {x}},t):=\int _{\Omega {0}\cap B{\delta }({\bf {x}})}{\bf {f}}\left({\bf {x}}',{\bf {x}},{\bf {u}}\left({\bf {x}}'\right),{\bf {u}}({\bf {x}})\right)dV_{{\bf {x}}'}+{\bf {b}}({\bf {x}},t)}\,.}

used in the bond-based formulations is substituted by

            F

        (

            x

        ,
        t
        )
        :=

          ∫

              B

                δ

            (

                x

            )

          {

                  T

                _

            [

              x

            ,
            t
            ]

              ⟨

                    x

                    ′

                −

                  x

              ⟩

            −

                  T

                _

              [

                    x

                    ′

                ,
                t

              ]

              ⟨

                  x

                −

                    x

                    ′

              ⟩

          }

        d

          V

                x

                ′

        +

          b

        (

          x

        ,
        t
        )
        ,

    {\displaystyle {\bf {F}}({\bf {x}},t):=\int {B{\delta }({\bf {x}})}\left{{\underline {\mathbf {T} }}[\mathbf {x} ,t]\left\langle \mathbf {x} ^{\prime }-\mathbf {x} \right\rangle -{\underline {\mathbf {T} }}\left[\mathbf {x} ^{\prime },t\right]\left\langle \mathbf {x} -\mathbf {x} ^{\prime }\right\rangle \right}dV_{\mathbf {x} ^{\prime }}+\mathbf {b} (\mathbf {x} ,t),}

where

              T

            _

    {\displaystyle {\underline {\mathbf {T} }}}

 is the force vector state field.
A general m-order state

              A

            _

        ⟨
        ⋅
        ⟩
        :

          B

            δ

        (

            x

        )
        →

              L

            m

        .

    {\displaystyle {\underline {\mathbf {A} }}\langle \cdot \rangle :B_{\delta }({\bf {x}})\rightarrow {\mathcal {L}}_{m}.}

 is a mathematical object similar to a tensor, with the exception that it is

in general non-linear;
in general non-continuous;
is not finite dimensional.
Vector states are states of order equal to 2. For so called simple material,

              T

            _

    {\displaystyle {\underline {\mathbf {T} }}}

 is defined as

              T

            _

        :=

                  T
                  ^

            _

        (

              Y

            _

        )

    {\displaystyle {\underline {\mathbf {T} }}:={\underline {\mathbf {\hat {T}} }}({\underline {\mathbf {Y} }})}

where

                  T
                  ^

            _

        :

            V

        →

            V

    {\displaystyle {\underline {\mathbf {\hat {T}} }}:{\mathcal {V}}\rightarrow {\mathcal {V}}}

 is a Riemann-integrable function on

          B

            δ

        (

            x

        )

    {\displaystyle B_{\delta }({\bf {x}})}

 , and

              Y

            _

    {\displaystyle {\underline {\mathbf {Y} }}}

 is called deformation vector state field and is defined by the following relation

              Y

            _

        [

          x

        ,
        t
        ]
        ⟨

          ξ

        ⟩

          y

        (

          x

        +

          ξ

        ,
        t
        )
        −

          y

        (

          x

        ,
        t
        )

        ∀

          x

        ∈

          Ω

            0

        ,
        ξ
        ∈

          B

            δ

        (

            x

        )
        ,
        t
        ≥
        0

    {\displaystyle {\underline {\mathbf {Y} }}[\mathbf {x} ,t]\langle {\boldsymbol {\xi }}\rangle =\mathbf {y} (\mathbf {x} +{\boldsymbol {\xi }},t)-\mathbf {y} (\mathbf {x} ,t)\quad \forall \mathbf {x} \in \Omega {0},\xi \in B{\delta }({\bf {x}}),t\geq 0}

thus

              Y

            _

          ⟨

                x

                ′

            −

              x

          ⟩

    {\displaystyle {\underline {\mathbf {Y} }}\left\langle \mathbf {x} ^{\prime }-\mathbf {x} \right\rangle }

 is the image of the bond

            x

            ′

        −

          x

    {\displaystyle \mathbf {x} ^{\prime }-\mathbf {x} }

 under the deformation
such that

              Y

            _

        ⟨

          ξ

        ⟩

          0

           if and only if

          ξ

          0

        ,

    {\displaystyle {\underline {\mathbf {Y} }}\langle {\boldsymbol {\xi }}\rangle =\mathbf {0} {\text{ if and only if }}{\boldsymbol {\xi }}=\mathbf {0} ,}

which means that two distinct particles never occupy the same point as the deformation progresses.
It can be proved that balance of linear momentum follow from the definition of

            F

        (

            x
            ,

            t

        )

    {\displaystyle {\bf {F}}({\bf {x,\,t}})}

, while, if the constitutive relation is such that

          ∫

              B

                δ

            (

                x

            )

              Y

            _

        ⟨

          ξ

        ⟩
        ×

              T

            _

        ⟨

          ξ

        ⟩
        d

          V

            ξ

        0

        ∀

              Y

            _

        ∈

            V

    {\displaystyle \int {B{\delta }({\bf {x}})}{\underline {\mathbf {Y} }}\langle {\boldsymbol {\xi }}\rangle \times {\underline {\mathbf {T} }}\langle {\boldsymbol {\xi }}\rangle dV_{\boldsymbol {\xi }}=0\quad \forall {\underline {\mathbf {Y} }}\in {\mathcal {V}}}

the force vector state field satisfy balance of angular momentum.

Applications
The growing interest in peridynamics come from its capability to fill the gap between atomistic theories of matter and classical local continuum mechanics. It is applied effectively to micro-scale phenomena, such as crack formation and propagation, wave dispersion, intra-granular fracture. These phenomena can be described by appropriate adjustment of the peridynamic horizon radius, which is directly linked to the extent of non-local interactions between points within the material.
In addition to the aforementioned research fields, peridynamics' non-local approach to discontinuities has found applications in various other areas. In geo-mechanics, it has been employed to study water-induced soil cracks, geo-material failure, rocks fragmentation, and so on. In biology, peridynamics has been used to model long-range interactions in living tissues, cellular ruptures, cracking of bio-membranes, and more. Furthermore, peridynamics has been extended to thermal diffusion theory, enabling the modeling of heat conduction in materials with discontinuities, defects, inhomogeneities, and cracks. It has also been applied to study advection-diffusion phenomena in multi-phase fluids and to construct models for transient advection-diffusion problems. With its versatility, peridynamics has been used in various multi-physics analyses, including micro-structural analysis, fatigue and heat conduction in composite materials, galvanic corrosion in metals, electricity-induced cracks in dielectric materials and more.
