# Viscoplasticity

Viscoplasticity

Viscoplasticity is a theory in continuum mechanics that describes the rate-dependent inelastic behavior of solids. Rate-dependence in this context means that the deformation of the material depends on the rate at which loads are applied. The inelastic behavior that is the subject of viscoplasticity is plastic deformation which means that the material undergoes unrecoverable deformations when a load level is reached. Rate-dependent plasticity is important for transient plasticity calculations. The main difference between rate-independent plastic and viscoplastic material models is that the latter exhibit not only permanent deformations after the application of loads but continue to undergo a creep flow as a function of time under the influence of the applied load.
The elastic response of viscoplastic materials can be represented in one-dimension by Hookean spring elements. Rate-dependence can be represented by nonlinear dashpot elements in a manner similar to viscoelasticity. Plasticity can be accounted for by adding sliding frictional elements as shown in Figure 1. In the figure

        E

    {\displaystyle E}

 is the modulus of elasticity,

        λ

    {\displaystyle \lambda }

 is the viscosity parameter and

        N

    {\displaystyle N}

 is a power-law type parameter that represents non-linear dashpot

        [
        σ
        (

          d

        ε

          /

          d

        t
        )

        σ

        λ
        (

          d

        ε

          /

          d

        t

          )

            1

              /

            N

        ]

    {\displaystyle [\sigma (\mathrm {d} \varepsilon /\mathrm {d} t)=\sigma =\lambda (\mathrm {d} \varepsilon /\mathrm {d} t)^{1/N}]}

. The sliding element can have a yield stress (

          σ

            y

    {\displaystyle \sigma _{y}}

) that is strain rate dependent, or even constant, as shown in Figure 1c.
Viscoplasticity is usually modeled in three-dimensions using overstress models of the Perzyna or Duvaut-Lions types. In these models, the stress is allowed to increase beyond the rate-independent yield surface upon application of a load and then allowed to relax back to the yield surface over time. The yield surface is usually assumed not to be rate-dependent in such models. An alternative approach is to add a strain rate dependence to the yield stress and use the techniques of rate independent plasticity to calculate the response of a material.
For metals and alloys, viscoplasticity is the macroscopic behavior caused by a mechanism linked to the movement of dislocations in grains, with superposed effects of inter-crystalline gliding. The mechanism usually becomes dominant at temperatures greater than approximately one third of the absolute melting temperature. However, certain alloys exhibit viscoplasticity at room temperature (300 K). For polymers, wood, and bitumen, the theory of viscoplasticity is required to describe behavior beyond the limit of elasticity or viscoelasticity.
In general, viscoplasticity theories are useful in areas such as:

the calculation of permanent deformations,
the prediction of the plastic collapse of structures,
the investigation of stability,
crash simulations,
systems exposed to high temperatures such as turbines in engines, e.g. a power plant,
dynamic problems and systems exposed to high strain rates.

History
Research on plasticity theories started in 1864 with the work of Henri Tresca, Saint Venant (1870) and Levy (1871) on the maximum shear criterion. An improved plasticity model was presented in 1913 by Von Mises which is now referred to as the von Mises yield criterion. In viscoplasticity, the development of a mathematical model heads back to 1910 with the representation of primary creep by Andrade's law. In 1929, Norton developed a one-dimensional dashpot model which linked the rate of secondary creep to the stress. In 1934, Odqvist generalized Norton's law to the multi-axial case.
Concepts such as the normality of plastic flow to the yield surface and flow rules for plasticity were introduced by Prandtl (1924) and Reuss (1930). In 1932, Hohenemser and Prager proposed the first model for slow viscoplastic flow. This model provided a relation between the deviatoric stress and the strain rate for an incompressible Bingham solid However, the application of these theories did not begin before 1950, where limit theorems were discovered.
In 1960, the first IUTAM Symposium "Creep in Structures" organized by Hoff provided a major development in viscoplasticity with the works of Hoff, Rabotnov, Perzyna, Hult, and Lemaitre for the isotropic hardening laws, and those of Kratochvil, Malinini and Khadjinsky, Ponter and Leckie, and Chaboche for the kinematic hardening laws. Perzyna, in 1963, introduced a viscosity coefficient that is temperature and time dependent. The formulated models were supported by the thermodynamics of irreversible processes and the phenomenological standpoint. The ideas presented in these works have been the basis for most subsequent research into rate-dependent plasticity.

Phenomenology
For a qualitative analysis, several characteristic tests are performed to describe the phenomenology of viscoplastic materials. Some examples of these tests are

hardening tests at constant stress or strain rate,
creep tests at constant force, and
stress relaxation at constant elongation.

Strain hardening test

One consequence of yielding is that as plastic deformation proceeds, an increase in stress is required to produce additional strain. This phenomenon is known as Strain/Work hardening. For a viscoplastic material the hardening curves are not significantly different from those of rate-independent plastic material. Nevertheless, three essential differences can be observed.

At the same strain, the higher the rate of strain the higher the stress
A change in the rate of strain during the test results in an immediate change in the stress–strain curve.
The concept of a plastic yield limit is no longer strictly applicable.
The hypothesis of partitioning the strains by decoupling the elastic and plastic parts is still applicable where the strains are small, i.e.,

          ε

            ε

              e

        +

            ε

              v
              p

    {\displaystyle {\boldsymbol {\varepsilon }}={\boldsymbol {\varepsilon }}{\mathrm {e} }+{\boldsymbol {\varepsilon }}{\mathrm {vp} }}

where

            ε

              e

    {\displaystyle {\boldsymbol {\varepsilon }}_{\mathrm {e} }}

 is the elastic strain and

            ε

              v
              p

    {\displaystyle {\boldsymbol {\varepsilon }}_{\mathrm {vp} }}

 is the viscoplastic strain. To obtain the stress–strain behavior shown in blue in the figure, the material is initially loaded at a strain rate of 0.1/s. The strain rate is then instantaneously raised to 100/s and held constant at that value for some time. At the end of that time period the strain rate is dropped instantaneously back to 0.1/s and the cycle is continued for increasing values of strain. There is clearly a lag between the strain-rate change and the stress response. This lag is modeled quite accurately by overstress models (such as the Perzyna model) but not by models of rate-independent plasticity that have a rate-dependent yield stress.

Creep test

Creep is the tendency of a solid material to slowly move or deform permanently under constant stresses. Creep tests measure the strain response due to a constant stress as shown in Figure 3. The classical creep curve represents the evolution of strain as a function of time in a material subjected to uniaxial stress at a constant temperature. The creep test, for instance, is performed by applying a constant force/stress and analyzing the strain response of the system. In general, as shown in Figure 3b this curve usually shows three phases or periods of behavior:

A primary creep stage, also known as transient creep, is the starting stage during which hardening of the material leads to a decrease in the rate of flow which is initially very high.

        (
        0
        ≤

          ε

        ≤

            ε

            1

        )

    {\displaystyle (0\leq {\boldsymbol {\varepsilon }}\leq {\boldsymbol {\varepsilon }}_{1})}

.
The secondary creep stage, also known as the steady state, is where the strain rate is constant.

        (

            ε

            1

        ≤

          ε

        ≤

            ε

            2

        )

    {\displaystyle ({\boldsymbol {\varepsilon }}{1}\leq {\boldsymbol {\varepsilon }}\leq {\boldsymbol {\varepsilon }}{2})}

.
A tertiary creep phase in which there is an increase in the strain rate up to the fracture strain.

        (

            ε

            2

        ≤

          ε

        ≤

            ε

            R

        )

    {\displaystyle ({\boldsymbol {\varepsilon }}{2}\leq {\boldsymbol {\varepsilon }}\leq {\boldsymbol {\varepsilon }}{R})}

.

Relaxation test

As shown in Figure 4, the relaxation test is defined as the stress response due to a constant strain for a period of time. In viscoplastic materials, relaxation tests demonstrate the stress relaxation in uniaxial loading at a constant strain. In fact, these tests characterize the viscosity and can be used to determine the relation which exists between the stress and the rate of viscoplastic strain. The decomposition of strain rate is

                    d

                    ε

                    d

                  t

                    d

                      ε

                        e

                    d

                  t

        +

                    d

                      ε

                        v
                        p

                    d

                  t

        .

    {\displaystyle {\cfrac {\mathrm {d} {\boldsymbol {\varepsilon }}}{\mathrm {d} t}}={\cfrac {\mathrm {d} {\boldsymbol {\varepsilon }}{\mathrm {e} }}{\mathrm {d} t}}+{\cfrac {\mathrm {d} {\boldsymbol {\varepsilon }}{\mathrm {vp} }}{\mathrm {d} t}}~.}

The elastic part of the strain rate is given by

                    d

                      ε

                        e

                    d

                  t

              E

            −
            1

                    d

                    σ

                    d

                  t

    {\displaystyle {\cfrac {\mathrm {d} {\boldsymbol {\varepsilon }}_{\mathrm {e} }}{\mathrm {d} t}}={\mathsf {E}}^{-1}~{\cfrac {\mathrm {d} {\boldsymbol {\sigma }}}{\mathrm {d} t}}}

For the flat region of the strain–time curve, the total strain rate is zero. Hence we have,

                    d

                      ε

                        v
                        p

                    d

                  t

        −

              E

            −
            1

                    d

                    σ

                    d

                  t

    {\displaystyle {\cfrac {\mathrm {d} {\boldsymbol {\varepsilon }}_{\mathrm {vp} }}{\mathrm {d} t}}=-{\mathsf {E}}^{-1}~{\cfrac {\mathrm {d} {\boldsymbol {\sigma }}}{\mathrm {d} t}}}

Therefore, the relaxation curve can be used to determine rate of viscoplastic strain and hence the viscosity of the dashpot in a one-dimensional viscoplastic material model. The residual value that is reached when the stress has plateaued at the end of a relaxation test corresponds to the upper limit of elasticity. For some materials such as rock salt such an upper limit of elasticity occurs at a very small value of stress and relaxation tests can be continued for more than a year without any observable plateau in the stress.
Relaxation tests are extremely difficult to perform, because maintaining the condition

                    d

                    ε

                    d

                  t

        0

    {\displaystyle {\cfrac {\mathrm {d} {\boldsymbol {\varepsilon }}}{\mathrm {d} t}}=0}

 in a test requires considerable delicacy.

Rheological models of viscoplasticity
One-dimensional constitutive models for viscoplasticity based on spring-dashpot-slider elements include the perfectly viscoplastic solid, the elastic perfectly viscoplastic solid, and the elastoviscoplastic hardening solid. The elements may be connected in series or in parallel. In models where the elements are connected in series the strain is additive while the stress is equal in each element. In parallel connections, the stress is additive while the strain is equal in each element. Many of these one-dimensional models can be generalized to three dimensions for the small strain regime. In the subsequent discussion, time rates strain and stress are written as

              ε
              ˙

    {\displaystyle {\dot {\boldsymbol {\varepsilon }}}}

 and

              σ
              ˙

    {\displaystyle {\dot {\boldsymbol {\sigma }}}}

, respectively.

Perfectly viscoplastic solid (Norton-Hoff model)

In a perfectly viscoplastic solid, also called the Norton-Hoff model of viscoplasticity, the stress (as for viscous fluids) is a function of the rate of permanent strain. The effect of elasticity is neglected in the model, i.e.,

            ε

            e

        0

    {\displaystyle {\boldsymbol {\varepsilon }}_{e}=0}

 and hence there is no initial yield stress, i.e.,

          σ

            y

        0

    {\displaystyle \sigma _{y}=0}

. The viscous dashpot has a response given by

          σ

        η

                ε
                ˙

              v
              p

        ⟹

                ε
                ˙

              v
              p

            σ
            η

    {\displaystyle {\boldsymbol {\sigma }}=\eta ~{\dot {\boldsymbol {\varepsilon }}}{!\mathrm {vp} }\implies {\dot {\boldsymbol {\varepsilon }}}{!\mathrm {vp} }={\frac {\boldsymbol {\sigma }}{\eta }}}

where

        η

    {\displaystyle \eta }

 is the viscosity of the dashpot. In the Norton-Hoff model the viscosity

        η

    {\displaystyle \eta }

 is a nonlinear function of the applied stress and is given by

        η

        λ

            (

                λ

                  ‖

                    σ

                  ‖

            )

            N
            −
            1

    {\displaystyle \eta =\lambda \left({\frac {\lambda }{|{\boldsymbol {\sigma }}|}}\right)^{N-1}}

where

        N

    {\displaystyle N}

 is a fitting parameter, λ is the kinematic viscosity of the material and

        ‖

          σ

        ‖

              σ

            :

              σ

              σ

                i
                j

              σ

                i
                j

    {\displaystyle |{\boldsymbol {\sigma }}|={\sqrt {{\boldsymbol {\sigma }}:{\boldsymbol {\sigma }}}}={\sqrt {\sigma _{ij}\sigma _{ij}}}}

. Then the viscoplastic strain rate is given by the relation

                ε
                ˙

              v
              p

                  σ

                  λ

            (

                  ‖

                    σ

                  ‖

                λ

            )

            N
            −
            1

    {\displaystyle {\dot {\boldsymbol {\varepsilon }}}_{\mathrm {vp} }={\cfrac {\boldsymbol {\sigma }}{\lambda }}\left({\frac {|{\boldsymbol {\sigma }}|}{\lambda }}\right)^{N-1}}

In one-dimensional form, the Norton-Hoff model can be expressed as

        σ

        λ

            (

                    ε
                    ˙

                  v
                  p

            )

            1

              /

            N

    {\displaystyle \sigma =\lambda ~\left({\dot {\varepsilon }}_{!\mathrm {vp} }\right)^{1/N}}

When

        N

        1.0

    {\displaystyle N=1.0}

 the solid is viscoelastic.
If we assume that plastic flow is isochoric (volume preserving), then the above relation can be expressed in the more familiar form

          s

        2
        K

            (

                  3

                      ε
                      ˙

                    e
                    q

            )

            m
            −
            1

                ε
                ˙

              v
              p

    {\displaystyle {\boldsymbol {s}}=2K~\left({\sqrt {3}}{\dot {\varepsilon }}{\mathrm {eq} }\right)^{m-1}~{\dot {\boldsymbol {\varepsilon }}}{\mathrm {vp} }}

where

          s

    {\displaystyle {\boldsymbol {s}}}

 is the deviatoric stress tensor,

                ε
                ˙

              e
              q

    {\displaystyle {\dot {\varepsilon }}_{\mathrm {eq} }}

 is the von Mises equivalent strain rate, and

        K
        ,
        m

    {\displaystyle K,m}

 are material parameters. The equivalent strain rate is defined as

                  ϵ
                  ¯

              ˙

                2
                3

                          ϵ
                          ¯

                      ¯

                  ˙

            :

                          ϵ
                          ¯

                      ¯

                  ˙

    {\displaystyle {\dot {\bar {\epsilon }}}={\sqrt {{\frac {2}{3}}{\dot {\bar {\bar {\epsilon }}}}:{\dot {\bar {\bar {\epsilon }}}}}}}

These models can be applied in metals and alloys at temperatures higher than two thirds of their absolute melting point (in kelvins) and polymers/asphalt at elevated temperature. The responses for strain hardening, creep, and relaxation tests of such material are shown in Figure 6.

Elastic perfectly viscoplastic solid (Bingham–Norton model)

Two types of elementary approaches can be used to build up an elastic-perfectly viscoplastic mode. In the first situation, the sliding friction element and the dashpot are arranged in parallel and then connected in series to the elastic spring as shown in Figure 7. This model is called the Bingham–Maxwell model (by analogy with the Maxwell model and the Bingham model) or the Bingham–Norton model. In the second situation, all three elements are arranged in parallel. Such a model is called a Bingham–Kelvin model by analogy with the Kelvin model.
For elastic-perfectly viscoplastic materials, the elastic strain is no longer considered negligible but the rate of plastic strain is only a function of the initial yield stress and there is no influence of hardening. The sliding element represents a constant yielding stress when the elastic limit is exceeded irrespective of the strain. The model can be expressed as

                  σ

                    E

                  ε

                  f
                  o
                  r

                ‖

                  σ

                ‖
                <

                  σ

                    y

                      ε
                      ˙

                        ε
                        ˙

                      e

                +

                        ε
                        ˙

                      v
                      p

                      E

                    −
                    1

                      σ
                      ˙

                +

                          σ

                          η

                  [

                    1
                    −

                                σ

                                  y

                              ‖

                                σ

                              ‖

                  ]

                  f
                  o
                  r

                ‖

                  σ

                ‖
                ≥

                  σ

                    y

    {\displaystyle {\begin{aligned}&{\boldsymbol {\sigma }}={\mathsf {E}}~{\boldsymbol {\varepsilon }}&&\mathrm {for} ~|{\boldsymbol {\sigma }}|<\sigma {y}\&{\dot {\boldsymbol {\varepsilon }}}={\dot {\boldsymbol {\varepsilon }}}{\mathrm {e} }+{\dot {\boldsymbol {\varepsilon }}}_{\mathrm {vp} }={\mathsf {E}}^{-1}~{\dot {\boldsymbol {\sigma }}}+{\cfrac {\boldsymbol {\sigma }}{\eta }}\left[1-{\cfrac {\sigma _{y}}{|{\boldsymbol {\sigma }}|}}\right]&&\mathrm {for} ~|{\boldsymbol {\sigma }}|\geq \sigma _{y}\end{aligned}}}

where

        η

    {\displaystyle \eta }

 is the viscosity of the dashpot element. If the dashpot element has a response that is of the Norton form

                  σ

                  η

                  σ

                  λ

            [

                      ‖

                        σ

                      ‖

                      λ

            ]

            N
            −
            1

    {\displaystyle {\cfrac {\boldsymbol {\sigma }}{\eta }}={\cfrac {\boldsymbol {\sigma }}{\lambda }}\left[{\cfrac {|{\boldsymbol {\sigma }}|}{\lambda }}\right]^{N-1}}

we get the Bingham–Norton model

              ε
              ˙

              E

            −
            1

              σ
              ˙

        +

                  σ

                  λ

            [

                      ‖

                        σ

                      ‖

                      λ

            ]

            N
            −
            1

          [

            1
            −

                        σ

                          y

                      ‖

                        σ

                      ‖

          ]

          f
          o
          r

        ‖

          σ

        ‖
        ≥

          σ

            y

    {\displaystyle {\dot {\boldsymbol {\varepsilon }}}={\mathsf {E}}^{-1}~{\dot {\boldsymbol {\sigma }}}+{\cfrac {\boldsymbol {\sigma }}{\lambda }}\left[{\cfrac {|{\boldsymbol {\sigma }}|}{\lambda }}\right]^{N-1}\left[1-{\cfrac {\sigma _{y}}{|{\boldsymbol {\sigma }}|}}\right]\quad \mathrm {for} ~|{\boldsymbol {\sigma }}|\geq \sigma _{y}}

Other expressions for the strain rate can also be observed in the literature with the general form

              ε
              ˙

              E

            −
            1

              σ
              ˙

        +
        f
        (

          σ

        ,

          σ

            y

        )

          σ

          f
          o
          r

        ‖

          σ

        ‖
        ≥

          σ

            y

    {\displaystyle {\dot {\boldsymbol {\varepsilon }}}={\mathsf {E}}^{-1}~{\dot {\boldsymbol {\sigma }}}+f({\boldsymbol {\sigma }},\sigma _{y})~{\boldsymbol {\sigma }}\quad \mathrm {for} ~|{\boldsymbol {\sigma }}|\geq \sigma _{y}}

The responses for strain hardening, creep, and relaxation tests of such material are shown in Figure 8.

Elastoviscoplastic hardening solid
An elastic-viscoplastic material with strain hardening is described by equations similar to those for an elastic-viscoplastic material with perfect plasticity. However, in this case the stress depends both on the plastic strain rate and on the plastic strain itself. For an elastoviscoplastic material the stress, after exceeding the yield stress, continues to increase beyond the initial yielding point. This implies that the yield stress in the sliding element increases with strain and the model may be expressed in generic terms as

                  ε

                    ε

                      e

                      E

                    −
                    1

                  σ

                  ε

                  f
                  o
                  r

                ‖

                  σ

                ‖
                <

                  σ

                    y

                      ε
                      ˙

                        ε
                        ˙

                      e

                +

                        ε
                        ˙

                      v
                      p

                      E

                    −
                    1

                      σ
                      ˙

                +
                f
                (

                  σ

                ,

                  σ

                    y

                ,

                    ε

                      v
                      p

                )

                  σ

                  f
                  o
                  r

                ‖

                  σ

                ‖
                ≥

                  σ

                    y

    {\displaystyle {\begin{aligned}&{\boldsymbol {\varepsilon }}={\boldsymbol {\varepsilon }}_{\mathrm {e} }={\mathsf {E}}^{-1}~{\boldsymbol {\sigma }}=~{\boldsymbol {\varepsilon }}&&\mathrm {for} ~|{\boldsymbol {\sigma }}|<\sigma {y}\&{\dot {\boldsymbol {\varepsilon }}}={\dot {\boldsymbol {\varepsilon }}}{!\mathrm {e} }+{\dot {\boldsymbol {\varepsilon }}}_{!\mathrm {vp} }={\mathsf {E}}^{-1}~{\dot {\boldsymbol {\sigma }}}+f({\boldsymbol {\sigma }},\sigma {y},{\boldsymbol {\varepsilon }}{\mathrm {vp} })~{\boldsymbol {\sigma }}&&\mathrm {for} ~|{\boldsymbol {\sigma }}|\geq \sigma _{y}\end{aligned}}}

This model is adopted when metals and alloys are at medium and higher temperatures and wood under high loads. The responses for strain hardening, creep, and relaxation tests of such a material are shown in Figure 9.

Strain-rate dependent plasticity models
Classical phenomenological viscoplasticity models for small strains are usually categorized into two types:

the Perzyna formulation
the Duvaut–Lions formulation

Perzyna formulation
In the Perzyna formulation the plastic strain rate is assumed to be given by a constitutive relation of the form

                ε
                ˙

              v
              p

                    ⟨

                      f
                      (

                        σ

                      ,

                        q

                      )

                    ⟩

                  τ

                  ∂
                  f

                  ∂

                    σ

            {

                            f
                            (

                              σ

                            ,

                              q

                            )

                            τ

                            ∂
                            f

                            ∂

                              σ

                    if

                  f
                  (

                    σ

                  ,

                    q

                  )

                  0

                  0

                    otherwise

    {\displaystyle {\dot {\varepsilon }}_{\mathrm {vp} }={\cfrac {\left\langle f({\boldsymbol {\sigma }},{\boldsymbol {q}})\right\rangle }{\tau }}{\cfrac {\partial f}{\partial {\boldsymbol {\sigma }}}}={\begin{cases}{\cfrac {f({\boldsymbol {\sigma }},{\boldsymbol {q}})}{\tau }}{\cfrac {\partial f}{\partial {\boldsymbol {\sigma }}}}&{\text{if}}~f({\boldsymbol {\sigma }},{\boldsymbol {q}})>0\0&{\text{otherwise}}\\end{cases}}}

where

        f
        (
        .
        ,
        .
        )

    {\displaystyle f(.,.)}

 is a yield function,

          σ

    {\displaystyle {\boldsymbol {\sigma }}}

 is the Cauchy stress,

          q

    {\displaystyle {\boldsymbol {q}}}

 is a set of internal variables (such as the plastic strain

            ε

              v
              p

    {\displaystyle {\boldsymbol {\varepsilon }}_{\mathrm {vp} }}

),

        τ

    {\displaystyle \tau }

 is a relaxation time. The notation

        ⟨
        …
        ⟩

    {\displaystyle \langle \dots \rangle }

 denotes the Macaulay brackets. The flow rule used in various versions of the Chaboche model is a special case of Perzyna's flow rule and has the form

                ε
                ˙

              v
              p

            ⟨

                f

                  f

                    0

            ⟩

            n

        sgn
        ⁡
        (

          σ

        −

          χ

        )

    {\displaystyle {\dot {\varepsilon }}{\mathrm {vp} }=\left\langle {\frac {f}{f{0}}}\right\rangle ^{n}\operatorname {sgn}({\boldsymbol {\sigma }}-{\boldsymbol {\chi }})}

where

          f

            0

    {\displaystyle f_{0}}

 is the quasistatic value of

        f

    {\displaystyle f}

  and

          χ

    {\displaystyle {\boldsymbol {\chi }}}

 is a backstress. Several models for the backstress also go by the name Chaboche model.

Duvaut–Lions formulation
The Duvaut–Lions formulation is equivalent to the Perzyna formulation and may be expressed as

                ε
                ˙

              v
              p

            {

                        C

                      −
                      1

                  :

                              σ

                            −

                                P

                              σ

                            τ

                    if

                  f
                  (

                    σ

                  ,

                    q

                  )

                  0

                  0

                    otherwise

    {\displaystyle {\dot {\varepsilon }}_{\mathrm {vp} }={\begin{cases}{\mathsf {C}}^{-1}:{\cfrac {{\boldsymbol {\sigma }}-{\mathcal {P}}{\boldsymbol {\sigma }}}{\tau }}&{\text{if}}~f({\boldsymbol {\sigma }},{\boldsymbol {q}})>0\0&{\text{otherwise}}\end{cases}}}

where

            C

    {\displaystyle {\mathsf {C}}}

 is the elastic stiffness tensor,

            P

          σ

    {\displaystyle {\mathcal {P}}{\boldsymbol {\sigma }}}

 is the closest point projection of the stress state on to the boundary of the region that bounds all possible elastic stress states. The quantity

            P

          σ

    {\displaystyle {\mathcal {P}}{\boldsymbol {\sigma }}}

 is typically found from the rate-independent solution to a plasticity problem.

Flow stress models
The quantity

        f
        (

          σ

        ,

          q

        )

    {\displaystyle f({\boldsymbol {\sigma }},{\boldsymbol {q}})}

 represents the evolution of the yield surface. The yield function

        f

    {\displaystyle f}

 is often expressed as an equation consisting of some invariant of stress and a model for the yield stress (or plastic flow stress). An example is von Mises or

          J

            2

    {\displaystyle J_{2}}

 plasticity. In those situations the plastic strain rate is calculated in the same manner as in rate-independent plasticity. In other situations, the yield stress model provides a direct means of computing the plastic strain rate.
Numerous empirical and semi-empirical flow stress models are used the computational plasticity. The following temperature and strain-rate dependent models provide a sampling of the models in current use:

the Johnson–Cook model
the Steinberg–Cochran–Guinan–Lund model.
the Zerilli–Armstrong model.
the Mechanical threshold stress model.
the Preston–Tonks–Wallace model.
The Johnson–Cook (JC) model is purely empirical and is the most widely used of the five. However, this model exhibits an unrealistically small strain-rate dependence at high temperatures. The Steinberg–Cochran–Guinan–Lund (SCGL) model is semi-empirical. The model is purely empirical and strain-rate independent at high strain-rates. A dislocation-based extension based on is used at low strain-rates. The SCGL model is used extensively by the shock physics community. The Zerilli–Armstrong (ZA) model is a simple physically based model that has been used extensively. A more complex model that is based on ideas from dislocation dynamics is the Mechanical Threshold Stress (MTS) model. This model has been used to model the plastic deformation of copper, tantalum, alloys of steel, and aluminum alloys. However, the MTS model is limited to strain-rates less than around 107/s. The Preston–Tonks–Wallace (PTW) model is also physically based and has a form similar to the MTS model. However, the PTW model has components that can model plastic deformation in the overdriven shock regime (strain-rates greater that 107/s). Hence this model is valid for the largest range of strain-rates among the five flow stress models.

Johnson–Cook flow stress model
The Johnson–Cook (JC) model is purely empirical and gives the following relation for the flow stress (

          σ

            y

    {\displaystyle \sigma _{y}}

)

          (1)

          σ

            y

        (

          ε

            p

        ,

                ε
                ˙

            p

        ,
        T
        )

          [

            A
            +
            B

                (

                  ε

                    p

                )

                n

          ]

          [

            1
            +
            C
            ln
            ⁡

                    ε
                    ˙

                  p

                ∗

          ]

          [

            1
            −
            (

              T

                ∗

              )

                m

          ]

    {\displaystyle {\text{(1)}}\qquad \sigma _{y}(\varepsilon {\text{p}},{\dot {\varepsilon }}{\text{p}},T)=\left[A+B\left(\varepsilon {\text{p}}\right)^{n}\right]\left[1+C\ln {\dot {\varepsilon }}{!{\text{p}}}^{}\right]\left[1-(T^{})^{m}\right]}

where

          ε

            p

    {\displaystyle \varepsilon _{\text{p}}}

 is the equivalent plastic strain,

                ε
                ˙

            p

    {\displaystyle {\dot {\varepsilon }}_{\text{p}}}

 is the plastic strain-rate, and

        A
        ,
        B
        ,
        C
        ,
        n
        ,
        m

    {\displaystyle A,B,C,n,m}

 are material constants.
The normalized strain-rate and temperature in equation (1) are defined as

                ε
                ˙

              p

            ∗

        :=

                    ε
                    ˙

                  p

                    ε
                    ˙

                  p0

          and

          T

            ∗

        :=

              T
              −

                T

                  0

                T

                  m

              −

                T

                  0

    {\displaystyle {\dot {\varepsilon }}{!{\text{p}}}^{}:={\frac {{\dot {\varepsilon }}{!{\text{p}}}}{{\dot {\varepsilon }}{!{\text{p0}}}}}\qquad {\text{and}}\qquad T^{}:={\frac {T-T{0}}{T_{m}-T_{0}}}}

where

                ε
                ˙

            p0

    {\displaystyle {\dot {\varepsilon }}_{\text{p0}}}

 is the effective plastic strain-rate of the quasi-static test used to determine the yield and hardening parameters A,B and n. This is not as it is often thought just a parameter to make

                ε
                ˙

            p

            ∗

    {\displaystyle {\dot {\varepsilon }}_{\text{p}}^{*}}

 non-dimensional.

          T

            0

    {\displaystyle T_{0}}

 is a reference temperature, and

          T

            m

    {\displaystyle T_{m}}

 is a reference melt temperature. For conditions where

          T

            ∗

        <
        0

    {\displaystyle T^{*}<0}

, we assume that

        m

        1

    {\displaystyle m=1}

.

Steinberg–Cochran–Guinan–Lund flow stress model
The Steinberg–Cochran–Guinan–Lund (SCGL) model is a semi-empirical model that was developed by Steinberg et al. for high strain-rate situations and extended to low strain-rates and bcc materials by Steinberg and Lund. The flow stress in this model is given by

          (2)

          σ

            y

        (

          ε

            p

        ,

                ε
                ˙

              p

        ,
        T
        )

          [

              σ

                a

            f
            (

              ε

                p

            )
            +

              σ

                t

            (

                    ε
                    ˙

                  p

            ,
            T
            )

          ]

              μ
              (
              p
              ,
              T
              )

              μ

                0

        ;

          σ

            a

        f
        ≤

          σ

            max

          and

          σ

            t

        ≤

          σ

            p

    {\displaystyle {\text{(2)}}\qquad \sigma _{y}(\varepsilon {\text{p}},{\dot {\varepsilon }}{!{\text{p}}},T)=\left[\sigma _{a}f(\varepsilon _{\text{p}})+\sigma {t}({\dot {\varepsilon }}{!{\text{p}}},T)\right]{\frac {\mu (p,T)}{\mu _{0}}};\quad \sigma _{a}f\leq \sigma _{\text{max}}{\text{and}}\sigma _{t}\leq \sigma _{p}}

where

          σ

            a

    {\displaystyle \sigma _{a}}

 is the athermal component of the flow stress,

        f
        (

          ε

            p

        )

    {\displaystyle f(\varepsilon _{\text{p}})}

 is a function that represents strain hardening,

          σ

            t

    {\displaystyle \sigma _{t}}

 is the thermally activated component of the flow stress,

        μ
        (
        p
        ,
        T
        )

    {\displaystyle \mu (p,T)}

 is the pressure- and temperature-dependent shear modulus, and

          μ

            0

    {\displaystyle \mu _{0}}

 is the shear modulus at standard temperature and pressure. The saturation value of the athermal stress is

          σ

            max

    {\displaystyle \sigma _{\text{max}}}

. The saturation of the thermally activated stress is the Peierls stress (

          σ

            p

    {\displaystyle \sigma _{p}}

). The shear modulus for this model is usually computed with the Steinberg–Cochran–Guinan shear modulus model.
The strain hardening function (

        f

    {\displaystyle f}

) has the form

        f
        (

          ε

            p

        )

        [
        1
        +
        β
        (

          ε

            p

        +

          ε

            p

        i
        )

          ]

            n

    {\displaystyle f(\varepsilon _{\text{p}})=[1+\beta (\varepsilon _{\text{p}}+\varepsilon _{\text{p}}i)]^{n}}

where

        β
        ,
        n

    {\displaystyle \beta ,n}

 are work hardening parameters, and

          ε

            p

        i

    {\displaystyle \varepsilon _{\text{p}}i}

 is the initial equivalent plastic strain.
The thermal component (

          σ

            t

    {\displaystyle \sigma _{t}}

) is computed using a bisection algorithm from the following equation.

                ε
                ˙

            p

            [

                  1

                    C

                      1

              exp
              ⁡

                [

                        2

                          U

                            k

                          k

                            B

                        T

                      (

                        1
                        −

                              σ

                                t

                              σ

                                p

                      )

                      2

                ]

              +

                    C

                      2

                    σ

                      t

            ]

            −
            1

        ;

          σ

            t

        ≤

          σ

            p

    {\displaystyle {\dot {\varepsilon }}{\text{p}}=\left[{\frac {1}{C{1}}}\exp \left[{\frac {2U_{k}}{k_{\text{B}}T}}\left(1-{\frac {\sigma _{t}}{\sigma {p}}}\right)^{2}\right]+{\frac {C{2}}{\sigma _{t}}}\right]^{-1};\quad \sigma _{t}\leq \sigma _{p}}

where

        2

          U

            k

    {\displaystyle 2U_{k}}

 is the energy to form a kink-pair in a dislocation segment of length

          L

            d

    {\displaystyle L_{d}}

,

          k

            b

    {\displaystyle k_{b}}

 is the Boltzmann constant,

          σ

            p

    {\displaystyle \sigma _{p}}

 is the Peierls stress. The constants

          C

            1

        ,

          C

            2

    {\displaystyle C_{1},C_{2}}

 are given by the relations

          C

            1

        :=

                ρ

                  d

                L

                  d

              a

                b

                  2

              ν

              2

                w

                  2

        ;

          C

            2

        :=

            D

                ρ

                  d

                b

                  2

    {\displaystyle C_{1}:={\frac {\rho {d}L{d}ab^{2}\nu }{2w^{2}}};\quad C_{2}:={\frac {D}{\rho _{d}b^{2}}}}

where

          ρ

            d

    {\displaystyle \rho _{d}}

 is the dislocation density,

          L

            d

    {\displaystyle L_{d}}

 is the length of a dislocation segment,

        a

    {\displaystyle a}

 is the distance between Peierls valleys,

        b

    {\displaystyle b}

 is the magnitude of the Burgers vector,

        ν

    {\displaystyle \nu }

 is the Debye frequency,

        w

    {\displaystyle w}

 is the width of a kink loop, and

        D

    {\displaystyle D}

 is the drag coefficient.

Zerilli–Armstrong flow stress model
The Zerilli–Armstrong (ZA) model is based on simplified dislocation mechanics. The general form of the equation for the flow stress is

          (3)

          σ

            y

        (

          ε

            p

        ,

                ε
                ˙

            p

        ,
        T
        )

          σ

            a

        +
        B
        exp
        ⁡
        (
        −
        β
        T
        )
        +

          B

            0

              ε

                p

        exp
        ⁡
        (
        −
        α
        T
        )

        .

    {\displaystyle {\text{(3)}}\qquad \sigma _{y}(\varepsilon {\text{p}},{\dot {\varepsilon }}{\text{p}},T)=\sigma {a}+B\exp(-\beta T)+B{0}{\sqrt {\varepsilon _{\text{p}}}}\exp(-\alpha T)~.}

In this model,

          σ

            a

    {\displaystyle \sigma _{a}}

 is the athermal component of the flow stress given by

          σ

            a

        :=

          σ

            g

        +

              k

                h

              ℓ

        +
        K

          ε

            p

            n

        ,

    {\displaystyle \sigma _{a}:=\sigma {g}+{\frac {k{h}}{\sqrt {\ell }}}+K\varepsilon _{\text{p}}^{n},}

where

          σ

            g

    {\displaystyle \sigma _{g}}

 is the contribution due to solutes and initial dislocation density,

          k

            h

    {\displaystyle k_{h}}

 is the microstructural stress intensity,

        ℓ

    {\displaystyle \ell }

 is the average grain diameter,

        K

    {\displaystyle K}

 is zero for fcc materials,

        B
        ,

          B

            0

    {\displaystyle B,B_{0}}

 are material constants.
In the thermally activated terms, the functional forms of the exponents

        α

    {\displaystyle \alpha }

 and

        β

    {\displaystyle \beta }

 are

        α

          α

            0

        −

          α

            1

        ln
        ⁡
        (

                ε
                ˙

              p

        )
        ;

        β

          β

            0

        −

          β

            1

        ln
        ⁡
        (

                ε
                ˙

              p

        )
        ;

    {\displaystyle \alpha =\alpha _{0}-\alpha {1}\ln({\dot {\varepsilon }}{!{\text{p}}});\quad \beta =\beta _{0}-\beta {1}\ln({\dot {\varepsilon }}{!{\text{p}}});}

where

          α

            0

        ,

          α

            1

        ,

          β

            0

        ,

          β

            1

    {\displaystyle \alpha _{0},\alpha _{1},\beta _{0},\beta _{1}}

 are material parameters that depend on the type of material (fcc, bcc, hcp, alloys). The Zerilli–Armstrong model has been modified by for better performance at high temperatures.

Mechanical threshold stress flow stress model
The Mechanical Threshold Stress (MTS) model) has the form

          (4)

          σ

            y

        (

          ε

            p

        ,

              ε
              ˙

        ,
        T
        )

          σ

            a

        +
        (

          S

            i

          σ

            i

        +

          S

            e

          σ

            e

        )

              μ
              (
              p
              ,
              T
              )

              μ

                0

    {\displaystyle {\text{(4)}}\qquad \sigma _{y}(\varepsilon _{\text{p}},{\dot {\varepsilon }},T)=\sigma {a}+(S{i}\sigma {i}+S{e}\sigma _{e}){\frac {\mu (p,T)}{\mu _{0}}}}

where

          σ

            a

    {\displaystyle \sigma _{a}}

 is the athermal component of mechanical threshold stress,

          σ

            i

    {\displaystyle \sigma _{i}}

 is the component of the flow stress due to intrinsic barriers to thermally activated dislocation motion and dislocation-dislocation interactions,

          σ

            e

    {\displaystyle \sigma _{e}}

 is the component of the flow stress due to microstructural evolution with increasing deformation (strain hardening), (

          S

            i

        ,

          S

            e

    {\displaystyle S_{i},S_{e}}

) are temperature and strain-rate dependent scaling factors, and

          μ

            0

    {\displaystyle \mu _{0}}

 is the shear modulus at 0 K and ambient pressure.
The scaling factors take the Arrhenius form

                  S

                    i

                    [

                      1
                      −

                          (

                                    k

                                      B

                                  T

                                    g

                                      0
                                      i

                                    b

                                      3

                                  μ
                                  (
                                  p
                                  ,
                                  T
                                  )

                            ln
                            ⁡

                                        ε
                                        ˙

                                    0

                                    ε
                                    ˙

                          )

                          1

                            /

                            q

                              i

                    ]

                    1

                      /

                      p

                        i

                  S

                    e

                    [

                      1
                      −

                          (

                                    k

                                      B

                                  T

                                    g

                                      0
                                      e

                                    b

                                      3

                                  μ
                                  (
                                  p
                                  ,
                                  T
                                  )

                            ln
                            ⁡

                                        ε
                                        ˙

                                    0

                                    ε
                                    ˙

                          )

                          1

                            /

                            q

                              e

                    ]

                    1

                      /

                      p

                        e

    {\displaystyle {\begin{aligned}S_{i}&=\left[1-\left({\frac {k_{\text{B}}T}{g_{0i}b^{3}\mu (p,T)}}\ln {\frac {{\dot {\varepsilon }}{!0}}{\dot {\varepsilon }}}\right)^{1/q{i}}\right]^{1/p_{i}}\S_{e}&=\left[1-\left({\frac {k_{\text{B}}T}{g_{0e}b^{3}\mu (p,T)}}\ln {\frac {{\dot {\varepsilon }}{!0}}{\dot {\varepsilon }}}\right)^{1/q{e}}\right]^{1/p_{e}}\end{aligned}}}

where

          k

            b

    {\displaystyle k_{b}}

 is the Boltzmann constant,

        b

    {\displaystyle b}

 is the magnitude of the Burgers' vector, (

          g

            0
            i

        ,

          g

            0
            e

    {\displaystyle g_{0i},g_{0e}}

) are normalized activation energies, (

              ε
              ˙

        ,

                ε
                ˙

            0

    {\displaystyle {\dot {\varepsilon }},{\dot {\varepsilon }}_{0}}

) are the strain-rate and reference strain-rate, and (

          q

            i

        ,

          p

            i

        ,

          q

            e

        ,

          p

            e

    {\displaystyle q_{i},p_{i},q_{e},p_{e}}

) are constants.
The strain hardening component of the mechanical threshold stress (

          σ

            e

    {\displaystyle \sigma _{e}}

) is given by an empirical modified Voce law

          (5)

              d

                σ

                  e

              d

                ε

                  p

        θ
        (

          σ

            e

        )

    {\displaystyle {\text{(5)}}\qquad {\frac {d\sigma _{e}}{d\varepsilon _{\text{p}}}}=\theta (\sigma _{e})}

where

                θ
                (

                  σ

                    e

                )

                  θ

                    0

                [
                1
                −
                F
                (

                  σ

                    e

                )
                ]
                +

                  θ

                    I
                    V

                F
                (

                  σ

                    e

                )

                  θ

                    0

                  a

                    0

                +

                  a

                    1

                ln
                ⁡

                        ε
                        ˙

                      p

                +

                  a

                    2

                            ε
                            ˙

                          p

                −

                  a

                    3

                T

                F
                (

                  σ

                    e

                )

                          tanh
                          ⁡

                            (

                              α

                                    σ

                                      e

                                    σ

                                      e
                                      s

                            )

                          tanh
                          ⁡
                          (
                          α
                          )

                ln
                ⁡

                            σ

                              e
                              s

                            σ

                              0
                              e
                              s

                        k

                          B

                      T

                        g

                          0
                          e
                          s

                        b

                          3

                      μ
                      (
                      p
                      ,
                      T
                      )

                ln
                ⁡

                                  ε
                                  ˙

                                p

                                  ε
                                  ˙

                                p

    {\displaystyle {\begin{aligned}\theta (\sigma _{e})&=\theta _{0}[1-F(\sigma _{e})]+\theta _{IV}F(\sigma _{e})\\theta {0}&=a{0}+a_{1}\ln {\dot {\varepsilon }}{!{\text{p}}}+a{2}{\sqrt {{\dot {\varepsilon }}{!{\text{p}}}}}-a{3}T\F(\sigma _{e})&={\cfrac {\tanh \left(\alpha {\frac {\sigma _{e}}{\sigma _{es}}}\right)}{\tanh(\alpha )}}\\ln {\cfrac {\sigma _{es}}{\sigma {0es}}}&={\frac {k{\text{B}}T}{g_{0es}b^{3}\mu (p,T)}}\ln {\cfrac {{\dot {\varepsilon }}{!{\text{p}}}}{{\dot {\varepsilon }}{!{\text{p}}}}}\end{aligned}}}

and

          θ

            0

    {\displaystyle \theta _{0}}

 is the hardening due to dislocation accumulation,

          θ

            I
            V

    {\displaystyle \theta _{IV}}

 is the contribution due to stage-IV hardening, (

          a

            0

        ,

          a

            1

        ,

          a

            2

        ,

          a

            3

        ,
        α

    {\displaystyle a_{0},a_{1},a_{2},a_{3},\alpha }

) are constants,

          σ

            e
            s

    {\displaystyle \sigma _{es}}

 is the stress at zero strain hardening rate,

          σ

            0
            e
            s

    {\displaystyle \sigma _{0es}}

 is the saturation threshold stress for deformation at 0 K,

          g

            0
            e
            s

    {\displaystyle g_{0es}}

 is a constant, and

                ε
                ˙

            p

    {\displaystyle {\dot {\varepsilon }}_{\text{p}}}

 is the maximum strain-rate. Note that the maximum strain-rate is usually limited to about

          10

            7

    {\displaystyle 10^{7}}

/s.

Preston–Tonks–Wallace flow stress model
The Preston–Tonks–Wallace (PTW) model attempts to provide a model for the flow stress for extreme strain-rates (up to 1011/s) and temperatures up to melt. A linear Voce hardening law is used in the model. The PTW flow stress is given by

          (6)

          σ

            y

        (

          ε

            p

        ,

                ε
                ˙

            p

        ,
        T
        )

            {

                  2

                    [

                        τ

                          s

                      +
                      α
                      ln
                      ⁡

                        [

                          1
                          −
                          φ
                          exp
                          ⁡

                            (

                              −
                              β
                              −

                                        θ

                                          ε

                                            p

                                        α
                                        φ

                            )

                        ]

                    ]

                  μ
                  (
                  p
                  ,
                  T
                  )

                    thermal regime

                  2

                    τ

                      s

                  μ
                  (
                  p
                  ,
                  T
                  )

                    shock regime

    {\displaystyle {\text{(6)}}\qquad \sigma _{y}(\varepsilon {\text{p}},{\dot {\varepsilon }}{\text{p}},T)={\begin{cases}2\left[\tau _{s}+\alpha \ln \left[1-\varphi \exp \left(-\beta -{\cfrac {\theta \varepsilon _{\text{p}}}{\alpha \varphi }}\right)\right]\right]\mu (p,T)&{\text{thermal regime}}\2\tau _{s}\mu (p,T)&{\text{shock regime}}\end{cases}}}

with

        α
        :=

                s

                  0

              −

                τ

                  y

            d

        ;

        β
        :=

                τ

                  s

              −

                τ

                  y

            α

        ;

        φ
        :=
        exp
        ⁡
        (
        β
        )
        −
        1

    {\displaystyle \alpha :={\frac {s_{0}-\tau _{y}}{d}};\quad \beta :={\frac {\tau _{s}-\tau _{y}}{\alpha }};\quad \varphi :=\exp(\beta )-1}

where

          τ

            s

    {\displaystyle \tau _{s}}

 is a normalized work-hardening saturation stress,

          s

            0

    {\displaystyle s_{0}}

 is the value of

          τ

            s

    {\displaystyle \tau _{s}}

 at 0K,

          τ

            y

    {\displaystyle \tau _{y}}

 is a normalized yield stress,

        θ

    {\displaystyle \theta }

 is the hardening constant in the Voce hardening law, and

        d

    {\displaystyle d}

 is a dimensionless material parameter that modifies the Voce hardening law.
The saturation stress and the yield stress are given by

                  τ

                    s

                max

                  {

                      s

                        0

                    −
                    (

                      s

                        0

                    −

                      s

                        ∞

                    )

                      erf

                      [

                        κ

                              T
                              ^

                        ln
                        ⁡

                                  γ

                                        ξ
                                        ˙

                                          ε
                                          ˙

                                      p

                      ]

                    ,

                      s

                        0

                        (

                                          ε
                                          ˙

                                      p

                                  γ

                                        ξ
                                        ˙

                        )

                          s

                            1

                  }

                  τ

                    y

                max

                  {

                      y

                        0

                    −
                    (

                      y

                        0

                    −

                      y

                        ∞

                    )

                      erf

                      [

                        κ

                              T
                              ^

                        ln
                        ⁡

                                  γ

                                        ξ
                                        ˙

                                          ε
                                          ˙

                                      p

                      ]

                    ,

                    min

                      {

                          y

                            1

                            (

                                              ε
                                              ˙

                                          p

                                      γ

                                            ξ
                                            ˙

                            )

                              y

                                2

                        ,

                          s

                            0

                            (

                                              ε
                                              ˙

                                          p

                                      γ

                                            ξ
                                            ˙

                            )

                              s

                                1

                      }

                  }

    {\displaystyle {\begin{aligned}\tau {s}&=\max \left{s{0}-(s_{0}-s_{\infty }){\text{erf}}\left[\kappa {\hat {T}}\ln {\cfrac {\gamma {\dot {\xi }}}{{\dot {\varepsilon }}{\text{p}}}}\right],\,s{0}\left({\cfrac {{\dot {\varepsilon }}{\text{p}}}{\gamma {\dot {\xi }}}}\right)^{s{1}}\right}\\tau {y}&=\max \left{y{0}-(y_{0}-y_{\infty }){\text{erf}}\left[\kappa {\hat {T}}\ln {\cfrac {\gamma {\dot {\xi }}}{{\dot {\varepsilon }}{\text{p}}}}\right],\,\min \left{y{1}\left({\cfrac {{\dot {\varepsilon }}{\text{p}}}{\gamma {\dot {\xi }}}}\right)^{y{2}},\,s_{0}\left({\cfrac {{\dot {\varepsilon }}{\text{p}}}{\gamma {\dot {\xi }}}}\right)^{s{1}}\right}\right}\end{aligned}}}

where

          s

            ∞

    {\displaystyle s_{\infty }}

 is the value of

          τ

            s

    {\displaystyle \tau _{s}}

 close to the melt temperature, (

          y

            0

        ,

          y

            ∞

    {\displaystyle y_{0},y_{\infty }}

) are the values of

          τ

            y

    {\displaystyle \tau _{y}}

 at 0 K and close to melt, respectively,

        (
        κ
        ,
        γ
        )

    {\displaystyle (\kappa ,\gamma )}

 are material constants,

              T
              ^

        T

          /

          T

            m

    {\displaystyle {\hat {T}}=T/T_{m}}

, (

          s

            1

        ,

          y

            1

        ,

          y

            2

    {\displaystyle s_{1},y_{1},y_{2}}

) are material parameters for the high strain-rate regime, and

              ξ
              ˙

            1
            2

            (

                      4
                      π
                      ρ

                      3
                      M

            )

            1

              /

            3

            (

                      μ
                      (
                      p
                      ,
                      T
                      )

                      ρ

            )

            1

              /

            2

    {\displaystyle {\dot {\xi }}={\frac {1}{2}}\left({\cfrac {4\pi \rho }{3M}}\right)^{1/3}\left({\cfrac {\mu (p,T)}{\rho }}\right)^{1/2}}

where

        ρ

    {\displaystyle \rho }

 is the density, and

        M

    {\displaystyle M}

 is the atomic mass.
