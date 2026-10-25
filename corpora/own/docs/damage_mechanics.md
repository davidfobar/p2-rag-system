# Damage mechanics

Damage mechanics

Damage mechanics is concerned with the representation, or modeling, of damage of materials that is suitable for making engineering predictions about the initiation, propagation, and fracture of materials without resorting to a microscopic description that would be too complex for practical engineering analysis.
Damage mechanics illustrates the typical engineering approach to model complex phenomena. To quote Dusan Krajcinovic, "It is often argued that the ultimate task of engineering research is to provide not so much a better insight into the examined phenomenon but to supply a rational predictive tool applicable in design." Damage mechanics is a topic of applied mechanics that relies heavily on continuum mechanics. Most of the work on damage mechanics uses state variables to represent the effects of damage on the stiffness and remaining life of the material that is damaging as a result of thermomechanical load and ageing. The state variables may be measurable, e.g., crack density, or inferred from the effect they have on some macroscopic property, such as stiffness, coefficient of thermal expansion, remaining life, etc. The state variables have conjugate thermodynamic forces that motivate further damage. Initially the material is pristine, or intact. A damage activation criterion is needed to predict damage initiation. Damage evolution does not progress spontaneously after initiation, thus requiring a damage evolution model. In plasticity like formulations, the damage evolution is controlled by a hardening function but this requires additional phenomenological parameters that must be found through experimentation, which is expensive, time consuming, and virtually no one does. On the other hand, micromechanics of damage formulations are able to predict both damage initiation and evolution without additional material properties.

Creep continuum damage mechanics
When mechanical structures are exposed to temperatures exceeding one-third of the melting temperature of the material of construction, time-dependent deformation (creep) and associated material degradation mechanisms become dominant modes of structural failure. While these deformation and damage mechanisms originate at the microscale where discrete processes dominate, practical application of failure theories to macroscale components is most readily achieved using the formalism of continuum mechanics. In this context, microscopic damage is idealized as a continuous state variable defined at all points within a structure. State equations are defined which govern the time evolution of damage. These equations may be readily integrated into finite element codes to analyze the damage evolution in complex 3D structures and calculate how long a component may safely be used before failure occurs.

Lumped damage state variable
L. M. Kachanov and Y. N. Rabotnov suggested the following evolution equations for the creep strain ε and a lumped damage state variable ω:

              ϵ
              ˙

                ϵ
                ˙

            0

            (

                σ

                  1
                  −
                  ω

            )

            n

    {\displaystyle {\dot {\epsilon }}={\dot {\epsilon }}_{0}\left({\frac {\sigma }{1-\omega }}\right)^{n}}

              ω
              ˙

                ω
                ˙

            0

            (

                σ

                  1
                  −
                  ω

            )

            m

    {\displaystyle {\dot {\omega }}={\dot {\omega }}_{0}\left({\frac {\sigma }{1-\omega }}\right)^{m}}

where

              ϵ
              ˙

    {\displaystyle {\dot {\epsilon }}}

 is the creep strain rate,

                ϵ
                ˙

            0

    {\displaystyle {\dot {\epsilon }}_{0}}

 is the creep-rate multiplier,

        σ

    {\displaystyle \sigma }

 is the applied stress,

        n

    {\displaystyle n}

 is the creep stress exponent of the material of interest,

              ω
              ˙

    {\displaystyle {\dot {\omega }}}

 is the rate of damage accumulation,

                ω
                ˙

            0

    {\displaystyle {\dot {\omega }}_{0}}

 is the damage-rate multiplier, and

        m

    {\displaystyle m}

 is the damage stress exponent.
In this simple case, the strain rate is governed by power-law creep with the stress enhanced by the damage state variable as damage accumulates. The damage term ω is interpreted as a distributed loss of load bearing area which results in an increased local stress at the microscale. The time to failure is determined by integrating the damage evolution equation from an initial undamaged state

        (
        ω

        0
        )

    {\displaystyle (\omega =0)}

 to a specified critical damage

          (

            ω

              ω

                f

          )

    {\displaystyle \left(\omega =\omega _{f}\right)}

. If

          ω

            f

    {\displaystyle \omega _{f}}

 is taken to be 1, this results in the following prediction for a structure loaded under a constant uniaxial stress

        σ

    {\displaystyle \sigma }

:

          t

            f

            1

                (

                  m
                  +
                  1

                )

                      ω
                      ˙

                  0

                σ

                  m

    {\displaystyle t_{f}={\frac {1}{\left(m+1\right){\dot {\omega }}_{0}\sigma ^{m}}}}

Model parameters

                ϵ

                  0

              ˙

    {\displaystyle {\dot {\epsilon _{0}}}}

 and n are found by fitting the creep strain rate equation at zero damage to minimum creep rate measurements. Model parameters

                ω

                  0

              ˙

    {\displaystyle {\dot {\omega _{0}}}}

 and m are found by fitting the above equation to creep rupture life data.

Mechanistically informed damage state variables
While easy to apply, the lumped damage model proposed by Kachanov and Robotnov is limited by the fact that the damage state variable cannot be directly tied to a specific mechanism of strain and damage evolution. Correspondingly, extrapolation of the model beyond the original dataset of test data is not justified. This limitation was remedied by researchers such as A.C.F. Cocks, M.F. Ashby, and B.F. Dyson, who proposed mechanistically informed strain and damage evolution equations. Extrapolation using such equations is justified if the dominant damage mechanism remains the same at the conditions of interest.

Void-growth by power-law creep
In the power-law creep regime, global deformation is controlled by glide and climb of dislocations. If internal voids are present within the microstructure, global structural continuity requires that the voids must both elongate and expand laterally, further reducing the local section. When cast in the damage mechanics formalism, the growth of internal voids by power-law creep can be represented by the following equations.

              ϵ
              ˙

                ϵ
                ˙

            0

          σ

            n

          (

            1
            +

                  2

                    r

                      h

                      0

                d

              [

                    1

                        (

                          1
                          −
                          ω

                        )

                        n

                −
                1

              ]

          )

    {\displaystyle {\dot {\epsilon }}={\dot {\epsilon }}{0}\sigma ^{n}\left(1+{\frac {2r{h}^{0}}{d}}\left[{\frac {1}{\left(1-\omega \right)^{n}}}-1\right]\right)}

              ω
              ˙

                ϵ
                ˙

            0

          σ

            n

          (

                1

                    (

                      1
                      −
                      ω

                    )

                    n

            −

              (

                1
                −
                ω

              )

          )

    {\displaystyle {\dot {\omega }}={\dot {\epsilon }}_{0}\sigma ^{n}\left({\frac {1}{\left(1-\omega \right)^{n}}}-\left(1-\omega \right)\right)}

where

                ϵ
                ˙

            0

    {\displaystyle {\dot {\epsilon }}_{0}}

 is the creep-rate multiplier,

        σ

    {\displaystyle \sigma }

 is the applied stress, n is the creep stress exponent,

          r

            h

            0

    {\displaystyle r_{h}^{0}}

 is the average initial void radius, and d is the grain size.

Void-growth by boundary diffusion
At very high temperature and/or low stresses, void growth on grain boundaries is primarily controlled by the diffusive flux of vacancies along the grain boundary. As matter diffuses away from the void and plates onto the adjacent grain boundaries, a roughly spherical void is maintained by rapid diffusion of vacancies along the surface of the void. When cast in the damage mechanics formalism, the growth of internal voids by boundary diffusion can be represented by the following equations.

              ϵ
              ˙

                ϵ
                ˙

            0

          ϕ

            0

        σ

              2
              l

              d
              ln
              ⁡

                (

                    1
                    ω

                )

    {\displaystyle {\dot {\epsilon }}={\dot {\epsilon }}_{0}\phi _{0}\sigma {\frac {2l}{d\ln \left({\frac {1}{\omega }}\right)}}}

              ω
              ˙

                ϵ
                ˙

            0

          ϕ

            0

        σ

            1

                ω

                  1

                    /

                  2

              ln
              ⁡

                (

                    1
                    ω

                )

    {\displaystyle {\dot {\omega }}={\dot {\epsilon }}_{0}\phi _{0}\sigma {\frac {1}{\omega ^{1/2}\ln \left({\frac {1}{\omega }}\right)}}}

          ϕ

            0

              2

                D

                  B

                δ

                  B

              Ω

              k
              T

                l

                  3

            1

                    ε
                    ˙

                0

    {\displaystyle \phi {0}={\frac {2D{B}\delta {B}\Omega }{kTl^{3}}}{\frac {1}{{\dot {\varepsilon }}{0}}}}

where

                ϵ
                ˙

            0

    {\displaystyle {\dot {\epsilon }}_{0}}

 is the creep-rate multiplier,

        σ

    {\displaystyle \sigma }

 is the applied stress,

        2
        l

    {\displaystyle 2l}

 is the center-to-center void spacing,

        d

    {\displaystyle d}

 is the grain size,

          D

            B

    {\displaystyle D_{B}}

 is the grain-boundary diffusion coefficient,

          δ

            B

    {\displaystyle \delta _{B}}

 is the grain boundary thickness,

        Ω

    {\displaystyle \Omega }

 is the atomic volume,

        k

    {\displaystyle k}

 is the Boltzmann constant, and

        T

    {\displaystyle T}

 is the absolute temperatures. It is noted that factors present in

          ϕ

            0

    {\displaystyle \phi _{0}}

 are very similar to the Coble creep pre-factors due to the similarity of the two mechanisms.

Precipitate coarsening
Many modern steels and alloys are designed such that precipitates will precipitate either within the matrix or along grain boundaries during casting. These precipitates restrict dislocation motion and, if present on grain boundaries, grain boundary sliding during creep. Many precipitates are not thermodynamically stable and grow via diffusion when exposed to elevated temperatures. As the precipitates coarsen, their ability to restrict dislocation motion decreases as the average spacing between particles increases, thus decreasing the required Orowan stress for bowing. In the case of grain boundary precipitates, precipitate growth means that fewer grain boundaries are impeded from grain boundary sliding. When cast into the damage mechanics formalism, precipitation coarsening and its effect on strain rate may be represented by the following equations.

              ϵ
              ˙

                ϵ
                ˙

            0

          σ

            n

            (

              1
              +

                K

                  ′
                  ′

              ω

            )

            n

    {\displaystyle {\dot {\epsilon }}={\dot {\epsilon }}_{0}\sigma ^{n}\left(1+K^{\prime \prime }\omega \right)^{n}}

              ω
              ˙

              K

                ′

            3

            (

              1
              −
              ω

            )

            4

    {\displaystyle {\dot {\omega }}={\frac {K^{\prime }}{3}}\left(1-\omega \right)^{4}}

where

                ϵ
                ˙

            0

    {\displaystyle \ {\dot {\epsilon }}_{0}}

 is the creep-rate multiplier,

        σ

    {\displaystyle \sigma }

 is the applied stress,

        n

    {\displaystyle n}

 is the creep-rate stress exponent,

          K

            ′
            ′

    {\displaystyle K^{\prime \prime }}

 is a parameter linking the precipitation damage to the strain rate,

          K

            ′

    {\displaystyle K^{\prime }}

 determines the rate of precipitate coarsening.

Combining damage mechanisms
Multiple damage mechanism can be combined to represent a broader range of phenomena. For instance, if both void-growth by power-law creep and precipitate coarsening are relevant mechanisms, the following combined set of equations may be used:

              ϵ
              ˙

                ϵ
                ˙

            0

          σ

            n

          (

            1
            +

                  2

                    r

                      h

                      0

                d

              [

                    1

                        (

                          1
                          −

                            ω

                              1

                        )

                        n

                −
                1

              ]

          )

            (

              1
              +

                K

                  ′
                  ′

                ω

                  2

            )

            n

    {\displaystyle {\dot {\epsilon }}={\dot {\epsilon }}{0}\sigma ^{n}\left(1+{\frac {2r{h}^{0}}{d}}\left[{\frac {1}{\left(1-\omega _{1}\right)^{n}}}-1\right]\right)\left(1+K^{\prime \prime }\omega _{2}\right)^{n}}

                ω
                ˙

            1

                ϵ
                ˙

            0

          σ

            n

          (

                1

                    (

                      1
                      −

                        ω

                          1

                    )

                    n

            −

              (

                1
                −

                  ω

                    1

              )

          )

            (

              1
              +

                K

                  ′
                  ′

                ω

                  2

            )

            n

    {\displaystyle {\dot {\omega }}{1}={\dot {\epsilon }}{0}\sigma ^{n}\left({\frac {1}{\left(1-\omega _{1}\right)^{n}}}-\left(1-\omega _{1}\right)\right)\left(1+K^{\prime \prime }\omega _{2}\right)^{n}}

                ω
                ˙

            2

              K

                ′

            3

            (

              1
              −

                ω

                  2

            )

            4

    {\displaystyle {\dot {\omega }}_{2}={\frac {K^{\prime }}{3}}\left(1-\omega _{2}\right)^{4}}

Note that both damage mechanisms are included in the creep strain rate equation. The precipitate coarsening damage mechanisms influences the void-growth damage mechanism as the void-growth mechanism depends on the global strain rate. The precipitate growth mechanisms is only time and temperature dependent and hence does not depend on the void-growth damage

          ω

            1

    {\displaystyle \omega _{1}}

.

Multiaxial effects
The preceding equations are valid under uniaxial tension only. When a multiaxial state of stress is present in the system, each equation must be adapted so that the driving multiaxial stress is considered. For void-growth by power-law creep, the relevant stress is the von Mises stress as this drives the global creep deformation; however, for void-growth by boundary diffusion, the maximum principal stress drives the vacancy flux.
