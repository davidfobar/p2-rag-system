# Poromechanics

Poromechanics

Poromechanics is a branch of physics and specifically continuum mechanics that studies the behavior of fluid-saturated porous media. A porous medium or a porous material is a solid (referred to as matrix) permeated by an interconnected network of pores or voids filled with a fluid. In general, the fluid may be composed of liquid or gas phases or both. In the simplest case, both the solid matrix and the pore space occupy two separate, continuously connected domains, such as in a kitchen sponge. Some porous media has a more complex microstructure in which, for example, the pore space is disconnected. Pore space that is unable to exchange fluid with the exterior is termed occluded pore space. Alternatively, in the case of granular porous media, the solid phase may constitute disconnected domains, termed the "grains", which are load-bearing under compression, though can flow when sheared.

Natural substances including rocks, soils, biological tissues including plants, heart, and cancellous bone, and man-made materials such as foams, gels, ceramics, and concrete can be considered as porous media. Porous materials share common coupled processes such as diffusion and consolidation, hydration and swelling, drying and shrinkage, heating and build-up of pore pressure, freezing and spalling, capillarity and cracking. Porous media whose solid matrix is elastic and the fluid is viscous are called poroelastic. The structural properties of a porous medium is characterized by its porosity, pore size and shape, connectivity, and specific surface area. The physical (mechanical, hydraulic, thermal) properties of a porous media are determined by its microstructure as well as the properties of its constituents (solid matrix and fluid). Porous media whose pore space is filled with a single fluid phase, typically a liquid, is considered to be saturated. Porous media whose pore space is only partially fluid is a fluid is known to be unsaturated.

Basic equations

Definitions of porosity
Poromechanics relates the loading of solid and fluid phases within a porous body to the deformation of the solid skeleton and pore space. A representative elementary volume (REV) of a porous medium and the superposition of the domains of the skeleton and connected pores is shown in Fig. 1. In tracking the material deformation, one must be careful to properly apportion sub-volumes that correspond to the solid matrix and pore space. To do this, it is often convenient to introduce a porosity, which measures the fraction of the REV that constitutes pore space. To keep track of the porosity in a deforming material volume, mechanicians consider two descriptions, namely:

The Eulerian porosity,

        n
        (

          x

        )

    {\displaystyle n(\mathbf {x} )}

 , which measures the porosity with respect to the current or deformed configuration. Specifically, if

          d

          V

            t

    {\displaystyle \mathrm {d} V_{t}}

 represents an infinitesimal volume in the deformed material body, then the pore volume is calculated from

        n
        (

          x

        )

          d

          V

            t

    {\displaystyle n(\mathbf {x} )\mathrm {d} V_{t}}

.
The Lagrangian porosity,

        ϕ
        (

          x

        )

    {\displaystyle \phi (\mathbf {x} )}

, which measures the porosity with respect to the initial or undeformed configuration. In a Lagrangian description of porosity, the pore volume is measured by

        ϕ
        (

          x

        )

          d

          V

            0

    {\displaystyle \phi (\mathbf {x} )\mathrm {d} V_{0}}

, where

          d

          V

            0

    {\displaystyle \mathrm {d} V_{0}}

 represents an infinitesimal volume of the material in its undeformed state.
The Eulerian and Lagrangian descriptions of porosity are readily related by noting that

        ϕ
        (

          x

        )

        n
        (

          x

        )

                d

                V

                  t

                d

                V

                  0

        J
        (

          x

        )
        n
        (

          x

        )
        ,

    {\displaystyle \phi (\mathbf {x} )=n(\mathbf {x} ){\frac {\mathrm {d} V_{t}}{\mathrm {d} V_{0}}}=J(\mathbf {x} )n(\mathbf {x} ),}

where

        J

        det
        (

          F

        )

    {\displaystyle J=\det(\mathbf {F} )}

 is the Jacobian of the deformation with

          F

    {\displaystyle \mathbf {F} }

 being the deformation gradient. In a small-strain, linearized theory of deformation, the volume ratio is approximated by

        J
        ≃
        (
        1
        +

          ϵ

              v

        )

    {\displaystyle J\simeq (1+\epsilon _{\mathrm {v} })}

, where

          ϵ

              v

    {\displaystyle \epsilon _{\mathrm {v} }}

 is the infinitesimal volume strain. Another useful descriptor of the REV's pore space is the void ratio, which compares the current volume of the pores to the current volume of the solid matrix. As such, the void ratio takes definition in an Eulerian frame of reference and is calculated as

        e

            n

              1
              −
              n

        ,

    {\displaystyle e={\frac {n}{1-n}},}

where

        1
        −
        n

    {\displaystyle 1-n}

 measures the fraction of the volume occupied by the solid skeleton.
When a material element of a porous medium undergoes a deformation, the porosity changes due to i) the material's observable macroscopic dilation and ii) the volume dilation of the material's solid skeleton. The latter cannot be assess from experiments on the material's bulk structure. The volume of the solid skeleton in an infinitesimal material element, which is denoted by

          d

          V

            t

              s

    {\displaystyle \mathrm {d} V_{t}^{\mathrm {s} }}

, is related to the deformed and undeformed total material volumes by

          d

          V

            t

              s

        (
        1
        −
        n
        )

          d

          V

            t

          d

          V

            t

        −
        ϕ

          d

          V

            0

    {\displaystyle \mathrm {d} V_{t}^{\mathrm {s} }=(1-n)\mathrm {d} V_{t}=\mathrm {d} V_{t}-\phi \mathrm {d} V_{0}}

where the definition of the Lagrangian porosity further requires

        1
        −

          ϕ

            0

          d

          V

            0

              s

          /

          d

          V

            0

    {\displaystyle 1-\phi {0}=\mathrm {d} V{0}^{\mathrm {s} }/\mathrm {d} V_{0}}

. Thus, under the assumption of infinitesimal strain theory, the total volumetric strain of a material element can be separated into strain contributions of the solid matrix and pore space as follows:

          ϵ

              v

                (
                1
                −

                  ϕ

                    0

                )

                  ϵ

                      s

              ⏟

            solid

        +

                ϕ
                −

                  ϕ

                    0

              ⏟

            pore

        ,

    {\displaystyle \epsilon _{\mathrm {v} }=\underbrace {(1-\phi _{0})\epsilon _{\mathrm {s} }} _{\text{solid}}+\underbrace {\phi -\phi _{0}} _{\text{pore}},}

where

          ϵ

              s

          d

          V

            t

              s

          /

          d

          V

            0

              s

        −
        1

    {\displaystyle \epsilon {\mathrm {s} }=\mathrm {d} V{t}^{\mathrm {s} }/\mathrm {d} V_{0}^{\mathrm {s} }-1}

 is recognized as the linearized volume strain acting in the solid.

Small-strain linear isotropic poroelasticity
Considering a fluid saturated, deformable porous solid, we follow an observation frame that moves together with the solid skeleton but allows pore fluid exchange with the surroundings (i.e., an open system). There is no chemical reaction (i.e., mass exchange) between the solid and the fluid phases. Summoning mass balance, momentum balance, the First and the Second laws of thermodynamics of individual phases, one can arrive at the energy balance and entropy imbalance of the overall mixture. By separately discussing the energy dissipation due to mechanical deformation and mass/heat transport, it is possible to arrive at the following free energy imbalance for the porous skeleton

            Φ

              s

            S

              i
              j

        d

            E

              i
              j

        +
        p
        d
        ϕ
        −

            S

              s

        d
        T
        −
        d

            Ψ

              s

        ≥
        0

    {\displaystyle {\Phi ^{s}}={S_{ij}}d{E_{ij}}+pd\phi -{S^{s}}dT-d{\Psi ^{s}}\geq 0}

where

            S

              i
              j

    {\displaystyle {S_{ij}}}

 is the Second Piola-Kirchoff stress;

          E

            i
            j

    {\displaystyle E_{ij}}

 is the Green-Lagrangian strain;

        p

    {\displaystyle p}

 the pore fluid pressure;

        ϕ

    {\displaystyle \phi }

 the Lagrangian porosity;

        T

    {\displaystyle T}

 is temperature;

          S

            s

    {\displaystyle S^{s}}

 and

          Ψ

            s

    {\displaystyle \Psi ^{s}}

 are the entropy and the elastic stored energy (Helmholtz free energy) of the solid skeleton;

          Φ

            s

    {\displaystyle \Phi ^{s}}

 is the rate of energy dissipation. Assuming small deformation, elastic solid, and isothermal condition, the previous equation simplifies to:

        d

            Ψ

              s

            σ

              i
              j

        d

            ε

              i
              j

        +
        p
        d
        ϕ

    {\displaystyle d{\Psi _{s}}={\sigma _{ij}}d{\varepsilon _{ij}}+pd\phi }

where

            ε

              i
              j

            1
            2

          (

                  ∂

                      u

                        i

                  ∂

                      x

                        j

            +

                  ∂

                      u

                        j

                  ∂

                      x

                        i

          )

    {\displaystyle {\varepsilon {ij}}={\frac {1}{2}}\left({{\frac {\partial {u{i}}}{\partial {x_{j}}}}+{\frac {\partial {u_{j}}}{\partial {x_{i}}}}}\right)}

 is the infinitesimal strain;

          u

            i

    {\displaystyle u_{i}}

 and

          x

            i

    {\displaystyle x_{i}}

 are the displacement and position vectors, respectively;

          σ

            i
            j

    {\displaystyle \sigma _{ij}}

 is Cauchy stress. The constitutive equation for an elastic porous media can thus be generally stated as:

            σ

              i
              j

              ∂

                  Ψ

                    s

              ∂

                  ε

                    i
                    j

        ;
        p

              ∂

                  Ψ

                    s

              ∂
              ϕ

    {\displaystyle {\sigma _{ij}}={\frac {\partial {\Psi _{s}}}{\partial {\varepsilon _{ij}}}};p={\frac {\partial {\Psi _{s}}}{\partial \phi }}}

Let us specify the following quadratic form of

            Ψ

              s

          (

                ε

                  i
                  j

            ,
            ϕ

          )

    {\displaystyle {\Psi _{s}}\left({{\varepsilon _{ij}},\phi }\right)}

:

            Ψ

              s

          (

                ε

                  i
                  j

            ,
            ϕ

          )

            1
            2

          (

            K
            −

                2
                3

            G
            +

                α

                  2

            N

          )

              ε

                k
                k

            2

        +
        G

            ε

              i
              j

            ε

              i
              j

        −
        α
        N

            ε

              k
              k

          (

            ϕ
            −

                ϕ

                  0

          )

        +

            1
            2

        N

              (

                ϕ
                −

                    ϕ

                      0

              )

              2

    {\displaystyle {\Psi _{s}}\left({{\varepsilon _{ij}},\phi }\right)={\frac {1}{2}}\left({K-{\frac {2}{3}}G+{\alpha ^{2}}N}\right){\varepsilon _{kk}}^{2}+G{\varepsilon _{ij}}{\varepsilon _{ij}}-\alpha N{\varepsilon _{kk}}\left({\phi -{\phi _{0}}}\right)+{\frac {1}{2}}N{\left({\phi -{\phi _{0}}}\right)^{2}}}

where

            e

              i
              j

            ε

              i
              j

        −

            δ

              i
              j

            ε

              k
              k

          /

        3

    {\displaystyle {e_{ij}}={\varepsilon _{ij}}-{\delta _{ij}}{\varepsilon _{kk}}/3}

 is the strain deviator;

            ϕ

              0

    {\displaystyle {\phi _{0}}}

 is the initial porosity of the undeformed porous medium;

        K

    {\displaystyle K}

,

        G

    {\displaystyle G}

,

        α

    {\displaystyle \alpha }

,

        N

    {\displaystyle N}

 are material constants. We can immediately obtain Biot's linear isotropic poroelasticity in terms of

          ϕ

    {\displaystyle {\phi }}

:

          {

                      σ

                        i
                        j

                        ∂

                            Ψ

                              s

                        ∂

                            ε

                              i
                              j

                    (

                      K
                      +

                          α

                            2

                      N
                      −

                          2
                          3

                      G

                    )

                      δ

                        i
                        j

                      ε

                        k
                        k

                  +
                  2
                  G

                      ε

                        i
                        j

                  −
                  α
                  N

                      δ

                        i
                        j

                    (

                      ϕ
                      −

                          ϕ

                            0

                    )

                  p

                        ∂

                            Ψ

                              s

                        ∂
                        ϕ

                  −
                  α
                  N

                      ε

                        k
                        k

                  +
                  N

                    (

                      ϕ
                      −

                          ϕ

                            0

                    )

    {\displaystyle \left{{\begin{array}{l}{\sigma _{ij}}={\frac {\partial {\Psi _{s}}}{\partial {\varepsilon _{ij}}}}=\left({K+{\alpha ^{2}}N-{\frac {2}{3}}G}\right){\delta _{ij}}{\varepsilon _{kk}}+2G{\varepsilon _{ij}}-\alpha N{\delta _{ij}}\left({\phi -{\phi _{0}}}\right)\p={\frac {\partial {\Psi _{s}}}{\partial \phi }}=-\alpha N{\varepsilon _{kk}}+N\left({\phi -{\phi _{0}}}\right)\end{array}}\right.}

or more commonly in incremental form:

          {

                  d

                      σ

                        i
                        j

                    (

                      K
                      −

                          2
                          3

                      G

                    )

                      δ

                        i
                        j

                  d

                      ε

                        k
                        k

                  +
                  2
                  G
                  d

                      ε

                        i
                        j

                  −
                  α

                      δ

                        i
                        j

                  d
                  p

                  d
                  ϕ

                      1
                      N

                  d
                  p
                  +
                  α
                  d

                      ε

                        k
                        k

    {\displaystyle \left{{\begin{array}{l}d{\sigma _{ij}}=\left({K-{\frac {2}{3}}G}\right){\delta _{ij}}d{\varepsilon _{kk}}+2Gd{\varepsilon _{ij}}-\alpha {\delta _{ij}}dp\d\phi ={\frac {1}{N}}dp+\alpha d{\varepsilon _{kk}}\end{array}}\right.}

Comparing with the usual linear elasticity equations, one can identify that

        K

    {\displaystyle K}

 and

        G

    {\displaystyle G}

 are the bulk and shear modulus of the porous material under drained (

        d
        p

        0

    {\displaystyle dp=0}

) conditions;

        α

    {\displaystyle \alpha }

, named the Biot's coefficient, is a new property for porous media that relates the change of porosity to the strain variation under drained condition;

        N

    {\displaystyle N}

 is a tangent modulus linking the pressure variation and porosity variation under constant volumetric strain (

        d

          ε

            k
            k

        0

    {\displaystyle d\varepsilon _{kk}=0}

).

The first equation can be rewritten in such a way that the right-hand side is exactly the same as the linear elasticity equation:

            σ

              i
              j

            ″

            σ

              i
              j

        +
        α
        p

            δ

              i
              j

          (

            K
            −

                2
                3

            G

          )

            δ

              i
              j

            ε

              k
              k

        +
        2
        G

            ε

              i
              j

    {\displaystyle {\sigma ''_{ij}}={\sigma _{ij}}+\alpha p{\delta _{ij}}=\left({K-{\frac {2}{3}}G}\right){\delta _{ij}}{\varepsilon _{kk}}+2G{\varepsilon _{ij}}}

Term

            σ

              i
              j

            ″

    {\displaystyle {\sigma ''_{ij}}}

 is called the Biot's effective stress that represents the stress transmitted solely through the solid skeleton. Terzaghi's effective stress which is widely used in soil mechanics can be retrieved by setting

        α

        1

    {\displaystyle \alpha =1}

.

Although the

          ϕ

    {\displaystyle {\phi }}

-based formulation is rooted in the free energy balance of the porous skeleton, it is typically difficult to track porosity changes during experiments, making the model calibration/validation inconvenient. In rock mechanics testing, the usual controlled/monitored variables are stress, strain, pore fluid pressure, and the net flux of pore fluid of the test sample. A better external variable in replace of

          ϕ

    {\displaystyle {\phi }}

 is therefore the variation of fluid content,

        ζ

    {\displaystyle \zeta }

, defined as the amount of fluid volume entering the solid frame per unit volume of solid frame. Its increment can be written as

        d
        ζ

              d

                m

                  f

              ρ

                f

              d

                (

                      ρ

                        f

                  ϕ

                )

              ρ

                f

        d
        ϕ
        +
        ϕ

              d

                  ρ

                    f

              ρ

                f

    {\displaystyle d\zeta ={\frac {dm_{f}}{\rho _{f}}}={\frac {d\left({{\rho _{f}}\phi }\right)}{\rho _{f}}}=d\phi +\phi {\frac {d{\rho _{f}}}{\rho _{f}}}}

where

          m

            f

    {\displaystyle m_{f}}

 is the fluid mass content;

          ρ

            f

    {\displaystyle \rho _{f}}

 is the fluid density. By replacing

        d
        ϕ

    {\displaystyle d\phi }

 with

        d
        ζ

    {\displaystyle d\zeta }

, and considering fluid state equation

        d

            ρ

              f

          /

            ρ

              f

        d
        p

          /

          K

            f

    {\displaystyle d{\rho _{f}}/{\rho {f}}=dp/K{f}}

, Biot's theory can be also written in the following

        ζ

    {\displaystyle \zeta }

-based form:

          {

                  d

                      σ

                        i
                        j

                    (

                      K
                      −

                          2
                          3

                      G

                    )

                      δ

                        i
                        j

                  d

                      ε

                        k
                        k

                  +
                  2
                  G
                  d

                      ε

                        i
                        j

                  −
                  α

                      δ

                        i
                        j

                  d
                  p

                  d
                  ζ

                      1
                      M

                  d
                  p
                  +
                  α
                  d

                      ε

                        k
                        k

    {\displaystyle \left{{\begin{array}{l}d{\sigma _{ij}}=\left({K-{\frac {2}{3}}G}\right){\delta _{ij}}d{\varepsilon _{kk}}+2Gd{\varepsilon _{ij}}-\alpha {\delta _{ij}}dp\d\zeta ={\frac {1}{M}}dp+\alpha d{\varepsilon _{kk}}\end{array}}\right.}

or

          {

                  d

                      σ

                        i
                        j

                    (

                          K

                            u

                      −

                          2
                          3

                      G

                    )

                      δ

                        i
                        j

                  d

                      ε

                        k
                        k

                  +
                  2
                  G
                  d

                      ε

                        i
                        j

                  −
                  α
                  M

                      δ

                        i
                        j

                  d
                  ζ

                  d
                  p

                  M

                    (

                      d
                      ζ
                      −
                      α
                      d

                          ε

                            k
                            k

                    )

    {\displaystyle \left{{\begin{array}{l}d{\sigma {ij}}=\left({{K{u}}-{\frac {2}{3}}G}\right){\delta _{ij}}d{\varepsilon _{kk}}+2Gd{\varepsilon _{ij}}-\alpha M{\delta _{ij}}d\zeta \dp=M\left({d\zeta -\alpha d{\varepsilon _{kk}}}\right)\end{array}}\right.}

where

          K

            f

    {\displaystyle K_{f}}

 is the fluid tangent bulk modulus;

        M

            K

              f

        N

          /

          (

                K

                  f

            +
            N
            ϕ

          )

    {\displaystyle M={K_{f}}N/\left({{K_{f}}+N\phi }\right)}

  is Biot modulus;

            K

              u

        K
        +

            b

              2

        M

    {\displaystyle {K_{u}}=K+{b^{2}}M}

 is the undrained bulk modulus. Note that both

        M

    {\displaystyle M}

 and

        N

    {\displaystyle N}

 have been called Biot modulus in different literatures. It is expected that

        M

    {\displaystyle M}

 would be dependent on the property of the fluid while

        N

    {\displaystyle N}

 is a sole property of the porous skeleton. Indeed, in-depth micromechanical analysis permits one to quantitatively connect the macroscopic poroelastic parameters with the intrinsic properties of the constituents of the porous media such as matrix bulk modulus and fluid bulk modulus.
When measuring the linear elastic properties of porous solids, laboratory experiments are typically performed under one of two limit cases:

Poroelastic solids are loaded under drained conditions, in which fluid exchange between domains of the porous solid and the exterior occurs rapidly, and the fluid pressure in pore space is held constant,

        d
        p

        0

    {\displaystyle dp=0}

. Such a system is considered to be an open system.
Poroelastic solids are loaded under undrained conditions, in which fluid exchange between the porous solid and the exterior is precluded,

        d

          m

            f

        0

    {\displaystyle dm_{f}=0}

. A saturated poroelastic solid loaded under undrained conditions typically experiences significant changes in fluid pressure. Such a system is considered to be a closed system.

Governing equations for poromechanical problems
The constitutive equation above describes the response of a local porous material in response to stress and fluid pressure changes. The full description of coupled hydromechanical processes relevant for practical applications also requires the complete governing equations and compatible initial and boundary conditions. The governing equations are summarized below:

Balance of linear momentum:

            σ

              i
              j
              ,
              j

        +
        ρ

            b

              i

        0

    {\displaystyle {\sigma {ij,j}}+\rho {b{i}}=0}

 (static) or

            σ

              i
              j
              ,
              j

        +
        ρ

            b

              i

        ρ

                  u
                  ¨

              i

              s

        +

            ρ

              f

                  w
                  ¨

              i

    {\displaystyle {\sigma {ij,j}}+\rho {b{i}}=\rho {{\ddot {u}}_{i}^{s}}+{\rho {f}}{{\ddot {w}}{i}}}

 (dynamic)Balance of mass (of the pore fluid):

              ζ
              ˙

        +

            q

              i
              ,
              i

        0

    {\displaystyle {\dot {\zeta }}+{q_{i,i}}=0}

Darcy's law

            q

              i

        −
        K

            ∂

              ∂

                  x

                    i

          (

                p

                      ρ

                        f

                  g

            +
            z

          )

    {\displaystyle {q_{i}}=-K{\frac {\partial }{\partial {x_{i}}}}\left({{\frac {p}{{\rho _{f}}g}}+z}\right)}

Compatibility of infinitesimal strains

            ε

              i
              j

            1
            2

          (

                u

                  i
                  ,
                  j

                  s

            +

                u

                  j
                  ,
                  i

                  s

          )

    {\displaystyle {\varepsilon {ij}}={\frac {1}{2}}\left({{u{i,j}^{s}}+{u_{j,i}^{s}}}\right)}

where

        ρ

          (

            1
            −
            ϕ

          )

            ρ

              s

        +
        ϕ

            ρ

              f

    {\displaystyle \rho =\left({1-\phi }\right){\rho _{s}}+\phi {\rho _{f}}}

 is the total density of the porous medium;

          b

            i

    {\displaystyle b_{i}}

 is the body force;

            w

              i

        ϕ

          (

                u

                  i

                  f

            −

                u

                  i

                  s

          )

    {\displaystyle {w_{i}}=\phi \left({{u_{i}^{f}}-{u_{i}^{s}}}\right)}

 is the relative fluid to solid displacement;

          u

            i

            s

    {\displaystyle u_{i}^{s}}

 and

          u

            i

            f

    {\displaystyle u_{i}^{f}}

 denote solid and fluid displacements, respectively; an overdot denotes a derivative with respect to time;

          q

            i

    {\displaystyle q_{i}}

 is specific discharge vector;

        K

    {\displaystyle K}

 is hydraulic conductivity;

        g

    {\displaystyle g}

 is gravitational acceleration. The governing equations (13) combined with the constitutive equations (7) given the previous section provide a total of 20 equations, which correspond to a total of 20 unknowns (

            u

              i

        ,

            ε

              i
              j

        ,

            σ

              i
              j

        ,

            q

              i

        ,
        p
        ,
        ζ

    {\displaystyle {u_{i}},{\varepsilon _{ij}},{\sigma {ij}},{q{i}},p,\zeta }

). The system is closed and can be solved when supplied with proper initial and boundary conditions.
Solutions to poromechanical problems can be sought analytically or numerically. Numerical techniques including finite difference and finite element methods are frequently invoked in industrial applications. Closed-form analytical solutions have been also developed for many practically relevant problems and are well-documented in textbooks. Analytical solutions are useful for verification of computational codes and developing qualitative intuitions about poromechanical problems.

Historical background

General
Reinhard Woltman (1757–1837), a German hydraulic and geotechnical engineer, first introduced the concepts of volume fractions and angles of internal friction within porous media in his study on the connection between soil moisture and its apparent cohesion. His work addressed the calculation of earth pressure against retaining walls. Achille Delesse (1817–1881), a French geologist and mineralogist, reasoned that the volume fraction of voids – otherwise termed the volumetric porosity – equals the surface fraction of voids – otherwise termed the areal porosity – when the size, shape, and orientation of the pores are randomly distributed. Henry Darcy (1803–1858), a French hydraulic engineer, observed the proportionality between the rate of discharge and the loss of water pressure in tests with natural sand, now known as Darcy's law. The first important concept related to saturated, deformable porous solids might be considered the principle of effective stress introduced by Karl von Terzaghi (1883–1963), an Austrian engineer. Terzaghi postulated that the mean effective stress experienced by the solid skeleton of a porous medium with incompressible constituents,

          σ
          ′

        σ
        −
        p

    {\displaystyle \sigma '=\sigma -p}

, is the total stress acting on the volume element,

        σ

    {\displaystyle \sigma }

, subtracted by the pressure of the fluid acting in the pore space,

        p

    {\displaystyle p}

. Terzaghi combined his effective stress concept with Darcy's law for fluid flow and derived a one-dimensional consolidation theory explaining the time-dependent deformation of soils as the pore fluid drains, which might be the first mathematical treatise on coupled hydromechanical problems in porous media.
A more general and formal introduction of poroelasticity and poromechanics is attributed to Maurice Anthony Biot (1905–1985), a Belgian-American applied physicist. In a series of papers published between 1935 and 1962, Biot developed the theory of linear isotropic poroelasticity (now known as Biot theory) which gives a complete description of the mechanical behavior of a poroelastic medium. The generality of Biot theory lies in its three-dimensional formulation in the framework of continuum mechanics, its accountant for the compressibility of solid and fluid phases, its consistency with micromechanical analyses which explicitly considers the inclusions and heterogeneities of porous media, and its compatibility with thermodynamics. Different from Terzaghi's, Biot's effective stress accounts for the compressibility of the solid and applies generally for deeper rocks and other compliant porous materials.
It is worth mentioning that, parallel to Biot's developments, another lesser-known path towards a theory of porous media follows the formulation of mixture theory (see). One may consider Biot theory as a phenomenological, macroscopic approach to poromechanics as it is grounded on experimentally measurable quantities (stress, strain, pore fluid pressure, and variation in fluid content). The mixture theory of porous media, on the other hand, takes a different route by focusing on the fundamental balance laws of spatially superposed and interacting constituents (solid, fluid). The constitutive relations of each constituent are separately derived first, and the macroscopic behavior of the mixture is a result of averaging. The mixture theory can account for arbitrary number of constituents that can be miscible or immiscible and inert or active. However, it usually comes with excessive number of material parameters that may be difficult to calibrate experimentally. Coussy showed that it is possible to derive Biot's theory from mixture theory, revealing the profound connection between the two. Controversy exists between Terzaghi, father of soil mechanics, and Paul Fillunger (1883–1937), father of mixture theory, on the correct form of the effectives stress in the early developments of poromechanics.
Since Biot's pioneering works, the linear isotropic poroelasticity theory have been reinterpreted and reformulated, generalized to material anisotropy, large deformation, and inelasticity, and coupled with multiphysical (thermal, chemical, electromagnetic) fields. Poromechanics theories for partially saturated porous materials, microporous materials, and surface-active materials have also been developed.

Poroelastodynamics
By introducing inertia terms in the set of governing equations shown above, the resulting solutions can capture fast dynamic effects such as wave propagation through porous medium, and thus the system is referred to as the theory of poroelastodynamics. One of the key findings is that there exist three types of elastic waves in poroelastic media: a shear or transverse wave, and two types of longitudinal or compressional waves, which Biot called type I and type II waves. The transverse and type I (or fast) longitudinal wave are similar to the transverse and longitudinal waves in an elastic solid, respectively. The slow compressional wave (also known as Biot's slow wave), is unique to poroelastic materials and is characterized by the out-of-phase movement between solid and fluid. The prediction of the Biot's slow wave generated some controversy, until it was experimentally observed by Thomas Plona in 1980. Conversion of energy from fast compressional and shear waves into the highly attenuating slow compressional wave is a significant cause of elastic wave attenuation in porous media.
Other important early contributors to the theory of poroelastodynamics were Yakov Frenkel and Fritz Gassmann. Further reading about the dynamics and acoustics of porous media.
Recent applications of poroelasticity to biology, such as modeling blood flows through the beating heart muscle, have also required an extension of the equations to nonlinear (large deformation) elasticity and the inclusion of inertia forces.

Applications
Civil Engineering: geotechnical engineering (soil and rock), structural engineering (concrete, wood).
Petroleum Engineering: hydraulic fracturing, borehole mechanics, ground subsidence.
Environmental Engineering: contaminate transport, ground water flow.
Mechanical engineering and material science: porous polymers for membranes, sorption-driven actuators, foam materials for cushioning/defense, Li-batteries.
Biomechanics: tumor, bone, lung.
