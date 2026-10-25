# Rock mass plasticity

Rock mass plasticity

In geotechnical engineering, rock mass plasticity is the study of the response of rocks to loads beyond the elastic limit. Historically, conventional wisdom has it that rock is brittle and fails by fracture, while plasticity (irreversible deformation without fracture) is identified with ductile materials such as metals. In field-scale rock masses, structural discontinuities exist in the rock indicating that failure has taken place. Since the rock has not fallen apart, contrary to expectation of brittle behavior, clearly elasticity theory is not the last word.
Theoretically, the concept of rock plasticity is based on soil plasticity which is different from metal plasticity. In metal plasticity, for example in steel, the size of a dislocation is sub-grain size while for soil it is the relative movement of microscopic grains. The theory of soil plasticity was developed in the 1960s at Rice University to provide for inelastic effects not observed in metals. Typical behaviors observed in rocks include strain softening, perfect plasticity, and work hardening.
Application of continuum theory is possible in jointed rocks because of the continuity of tractions across joints even though displacements may be discontinuous. The difference between an aggregate with joints and a continuous solid is in the type of constitutive law and the values of constitutive parameters.

Experimental evidence
Experiments are usually carried out with the intention of characterizing the mechanical behavior of rock in terms of rock strength. The strength is the limit to elastic behavior and delineates the regions where plasticity theory is applicable. Laboratory tests for characterizing rock plasticity fall into four overlapping categories: confining pressure tests, pore pressure or effective stress tests, temperature-dependent tests, and strain rate-dependent tests. Plastic behavior has been observed in rocks using all these techniques since the early 1900s.
The Boudinage experiments show that localized plasticity is observed in certain rock specimens that have failed in shear. Other examples of rock displaying plasticity can be seen in the work of Cheatham and Gnirk. Test using compression and tension show necking of rock specimens while tests using wedge penetration show lip formation. The tests carried out by Robertson show plasticity occurring at high confining pressures. Similar results are observable in the experimental work carried out by Handin and Hager, Paterson, and Mogi. From these results it appears that the transition from elastic to plastic behavior may also indicate the transition from softening to hardening. More evidence is presented by Robinson and Schwartz. It is observed that the higher the confining pressure, the greater the ductility observed. However, the strain to rupture remains roughly the same at around 1.
The effect of temperature on rock plasticity has been explored by several teams of researchers. It is observed that the peak stress decreases with temperature. Extension tests (with confining pressure greater than the compressive stress) show that the intermediate principal stress as well as the strain rate has an effect on the strength. The experiments on the effect of strain rate by Serdengecti and Boozer show that increasing the strain rate makes rock stronger but also makes it appear more brittle. Thus dynamic loading may actually cause the strength of the rock to increase substantially. Increase in temperature appears to increase the rate effect in the plastic behavior of rocks.
After these early explorations in the plastic behavior of rocks, a significant amount of research has been carried out on the subject, primarily by the petroleum industry. From the accumulated evidence, it is clear that rock does exhibit remarkable plasticity under certain conditions and the application of a plasticity theory to rock is appropriate.

Governing equations
The equations that govern the deformation of jointed rocks are the same as those used to describe the motion of a continuum:

                      ρ
                      ˙

                +
                ρ

                  ∇

                ⋅

                  v

                0

                  Balance of Mass

                ρ

                        v

                      ˙

                −

                  ∇

                ⋅

                  σ

                −
                ρ

                  b

                0

                  Balance of Linear Momentum

                  σ

                    σ

                    T

                  Balance of Angular Momentum

                ρ

                      e
                      ˙

                −

                  σ

                :
                (

                  ∇

                  v

                )
                +

                  ∇

                ⋅

                  q

                −
                ρ

                s

                0

                  Balance of Energy.

    {\displaystyle {\begin{aligned}{\dot {\rho }}+\rho ~{\boldsymbol {\nabla }}\cdot \mathbf {v} &=0&&\qquad {\text{Balance of Mass}}\\rho ~{\dot {\mathbf {v} }}-{\boldsymbol {\nabla }}\cdot {\boldsymbol {\sigma }}-\rho ~\mathbf {b} &=0&&\qquad {\text{Balance of Linear Momentum}}\{\boldsymbol {\sigma }}&={\boldsymbol {\sigma }}^{T}&&\qquad {\text{Balance of Angular Momentum}}\\rho ~{\dot {e}}-{\boldsymbol {\sigma }}:({\boldsymbol {\nabla }}\mathbf {v} )+{\boldsymbol {\nabla }}\cdot \mathbf {q} -\rho ~s&=0&&\qquad {\text{Balance of Energy.}}\end{aligned}}}

where

        ρ
        (

          x

        ,
        t
        )

    {\displaystyle \rho (\mathbf {x} ,t)}

 is the mass density,

              ρ
              ˙

    {\displaystyle {\dot {\rho }}}

 is the material time derivative of

        ρ

    {\displaystyle \rho }

,

          v

        (

          x

        ,
        t
        )

                u

              ˙

        (

          x

        ,
        t
        )

    {\displaystyle \mathbf {v} (\mathbf {x} ,t)={\dot {\mathbf {u} }}(\mathbf {x} ,t)}

 is the particle velocity,

          u

    {\displaystyle \mathbf {u} }

 is the particle displacement,

                v

              ˙

    {\displaystyle {\dot {\mathbf {v} }}}

 is the material time derivative of

          v

    {\displaystyle \mathbf {v} }

,

          σ

        (

          x

        ,
        t
        )

    {\displaystyle {\boldsymbol {\sigma }}(\mathbf {x} ,t)}

 is the Cauchy stress tensor,

          b

        (

          x

        ,
        t
        )

    {\displaystyle \mathbf {b} (\mathbf {x} ,t)}

 is the body force density,

        e
        (

          x

        ,
        t
        )

    {\displaystyle e(\mathbf {x} ,t)}

 is the internal energy per unit mass,

              e
              ˙

    {\displaystyle {\dot {e}}}

 is the material time derivative of

        e

    {\displaystyle e}

,

          q

        (

          x

        ,
        t
        )

    {\displaystyle \mathbf {q} (\mathbf {x} ,t)}

 is the heat flux vector,

        s
        (

          x

        ,
        t
        )

    {\displaystyle s(\mathbf {x} ,t)}

 is an energy source per unit mass,

          x

    {\displaystyle \mathbf {x} }

 is the location of the point in the deformed configuration, and t is the time.
In addition to the balance equations, initial conditions, boundary conditions, and constitutive models are needed for a problem to be well-posed. For bodies with internal discontinuities such as jointed rock, the balance of linear momentum is more conveniently expressed in the integral form, also called the principle of virtual work:

          ∫

            Ω

        [

          σ

        ⋅
        ∇

            w

        −
        ρ

          b

        ⋅

          w

        +
        ρ

                v

              ˙

        ⋅

          w

        ]

          dV

          ∫

            ∂
            Ω

          t

        ⋅

          w

          dS

    {\displaystyle \int _{\Omega }[{\boldsymbol {\sigma }}\cdot \nabla {\mathbf {w} }-\rho \,\mathbf {b} \cdot \mathbf {w} +\rho \,{\dot {\mathbf {v} }}\cdot \mathbf {w} ]\,{\text{dV}}=\int _{\partial \Omega }\mathbf {t} \cdot \mathbf {w} \,{\text{dS}}}

where

        Ω

    {\displaystyle \Omega }

 represents the volume of the body and

        ∂
        Ω

    {\displaystyle \partial \Omega }

 is its surface (including any internal discontinuities),

          w

    {\displaystyle \mathbf {w} }

 is an admissible variation that satisfies the displacement (or velocity) boundary conditions, the divergence theorem has been used to eliminate derivatives of the stress tensor, and

          t

    {\displaystyle \mathbf {t} }

 are surface tractions on the surfaces

        ∂
        Ω

    {\displaystyle \partial \Omega }

. The jump conditions across stationary internal stress discontinuities require that the tractions across these surfaces be continuous, i.e.,

          n

        ⋅

            σ

            +

        +

          n

        ⋅

            σ

            −
            1

          0

          or

          n

        ⋅
        [
        [

          σ

        ]
        ]

          0

    {\displaystyle \mathbf {n} \cdot {\boldsymbol {\sigma }}^{+}+\mathbf {n} \cdot {\boldsymbol {\sigma }}^{-1}=\mathbf {0} \qquad {\text{or}}\qquad \mathbf {n} \cdot [[{\boldsymbol {\sigma }}]]=\mathbf {0} }

where

            σ

            +

        ,

            σ

            −

    {\displaystyle {\boldsymbol {\sigma }}^{+},{\boldsymbol {\sigma }}^{-}}

 are the stresses in the sub-bodies

          Ω

            +

        ,

          Ω

            −

    {\displaystyle \Omega ^{+},\Omega ^{-}}

, and

          n

    {\displaystyle \mathbf {n} }

 is the normal to the surface of discontinuity.

Constitutive relations

For small strains, the kinematic quantity that is used to describe rock mechanics is the small strain tensor

          ε

              1
              2

          [

            ∇

              u

            +
            (
            ∇

              u

              )

                T

          ]

        .

    {\displaystyle {\boldsymbol {\varepsilon }}={\tfrac {1}{2}}\left[\nabla \mathbf {u} +(\nabla \mathbf {u} )^{T}\right]\,.}

If temperature effects are ignored, four types of constitutive relations are typically used to describe small strain deformations of rocks. These relations encompass elastic, plastic, viscoelastic, and viscoplastic behavior and have the following forms:

Elastic material:

          σ

            H

        :

          ε

    {\displaystyle \,\,{\boldsymbol {\sigma }}={\mathsf {H}}:{\boldsymbol {\varepsilon }}\,\,}

 or

          σ

            i
            j

          H

            i
            j
            k
            l

          ε

            k
            l

    {\displaystyle \,\,\sigma {ij}=H{ijkl}\,\varepsilon _{kl}\,\,}

. For an isotropic, linear elastic, material this relation takes the form

          σ

        2
        μ

          ε

        +
        λ

          tr

        (

          ε

        )

          I

    {\displaystyle \,\,{\boldsymbol {\sigma }}=2\mu \,{\boldsymbol {\varepsilon }}+\lambda \,{\text{tr}}({\boldsymbol {\varepsilon }})\,{\boldsymbol {I}}\,\,}

 or

          σ

            i
            j

        2
        μ

          ε

            i
            j

        +
        λ

          ε

            k
            k

          δ

            i
            j

    {\displaystyle \,\,\sigma _{ij}=2\mu \varepsilon _{ij}+\lambda \varepsilon _{kk}\delta _{ij}}

. The quantities

        μ
        ,
        λ

    {\displaystyle \mu ,\lambda }

 are the Lamé parameters.
Viscous fluid: For isotropic materials,

          σ

        −
        p

          I

        +
        2
        μ

              ε
              ˙

        +
        λ

          tr

        (

              ε
              ˙

        )

          I

    {\displaystyle \,\,{\boldsymbol {\sigma }}=-p\,{\boldsymbol {I}}+2\mu \,{\dot {\boldsymbol {\varepsilon }}}+\lambda \,{\text{tr}}({\dot {\boldsymbol {\varepsilon }}})\,{\boldsymbol {I}}\,\,}

 or

          σ

            i
            j

        −
        P

          δ

            i
            j

        +
        2
        μ

                ε
                ˙

            i
            j

        +
        λ

                ε
                ˙

            k
            k

          δ

            i
            j

    {\displaystyle \,\,\sigma _{ij}=-P\,\delta {ij}+2\mu {\dot {\varepsilon }}{ij}+\lambda {\dot {\varepsilon }}_{kk}\delta _{ij}}

 where

        μ

    {\displaystyle \mu }

 is the shear viscosity and

        λ

    {\displaystyle \lambda }

 is the bulk viscosity.
Nonlinear material: Isotropic nonlinear material relations take the form

          σ

        2
        μ

          ε

        +
        λ

          tr

        (

          ε

        )

          I

        +

          λ
          ′

          ε

        ⋅

          ε

    {\displaystyle \,\,{\boldsymbol {\sigma }}=2\mu \,{\boldsymbol {\varepsilon }}+\lambda \,{\text{tr}}({\boldsymbol {\varepsilon }})\,{\boldsymbol {I}}+\lambda '\,{\boldsymbol {\varepsilon }}\cdot {\boldsymbol {\varepsilon }}\,\,}

 or

          σ

            i
            j

        2
        μ

          ε

            i
            j

        +
        λ

          ε

            k
            k

          δ

            i
            j

        +

          λ
          ′

          ε

            i
            k

          ε

            k
            j

    {\displaystyle \,\,\sigma _{ij}=2\mu \varepsilon _{ij}+\lambda \varepsilon _{kk}\delta _{ij}+\lambda '\,\varepsilon _{ik}\,\varepsilon _{kj}}

. This type of relation is typically used to fit experimental data and may include inelastic behavior.
Quasi-linear materials: Constitutive relations for these materials are typically expressed in rate form, e.g.,

              σ
              ˙

            H

        (

          σ

        )
        :

              ε
              ˙

    {\displaystyle \,\,{\dot {\boldsymbol {\sigma }}}={\mathsf {H}}({\boldsymbol {\sigma }}):{\dot {\boldsymbol {\varepsilon }}}\,\,}

 or

                σ
                ˙

            i
            j

          H

            i
            j
            k
            l

        (

          σ

            m
            n

        )

                ε
                ˙

            k
            l

    {\displaystyle \,\,{\dot {\sigma }}{ij}=H{ijkl}(\sigma {mn})\,{\dot {\varepsilon }}{kl}\,\,}

.
A failure criterion or yield surface for the rock may then be expressed in the general form

        F
        (

          σ

        ,

              σ
              ˙

        ,

          ε

        ,

              ε
              ˙

        ,

          x

        ,
        t
        )

        0

        .

    {\displaystyle F({\boldsymbol {\sigma }},{\dot {\boldsymbol {\sigma }}},{\boldsymbol {\varepsilon }},{\dot {\boldsymbol {\varepsilon }}},\mathbf {x} ,t)=0\,.}

Typical constitutive relations for rocks assume that the deformation process is isothermal, the material is isotropic, quasi-linear, and homogenous and material properties do not depend upon position at the start of the deformation process, that there is no viscous effect and therefore no intrinsic time scale, that the failure criterion is rate-independent, and that there is no size effect. However, these assumptions are made only to simplify analysis and should be abandoned if necessary for a particular problem.

Yield surfaces for rocks

Design of mining and civil structures in rock typically involves a failure criterion that is cohesive-frictional. The failure criterion is used to determine whether a state of stress in the rock will lead to inelastic behavior, including brittle failure. For rocks under high hydrostatic stresses, brittle failure is preceded by plastic deformation and the failure criterion is used to determine the onset of plastic deformation. Typically, perfect plasticity is assumed beyond the yield point. However strain hardening and softening relations with nonlocal inelasticity and damage have also been used. Failure criteria and yield surfaces are also often augmented with a cap to avoid unphysical situations where extreme hydrostatic stress states do not lead to failure or plastic deformation.

Two widely used yield surfaces/failure criteria for rocks are the Mohr-Coulomb model and the Drucker-Prager model. The Hoek–Brown failure criterion is also used, notwithstanding the serious consistency problem with the model. The defining feature of these models is that tensile failure is predicted at low stresses. On the other hand, as the stress state becomes increasingly compressive, failure and yield requires higher and higher values of stress.

Plasticity theory
The governing equations, constitutive models, and yield surfaces discussed above are not sufficient if we are to compute the stresses and displacements in a rock body that is undergoing plastic deformation. An additional kinematic assumption is needed, i.e., that the strain in the body can be decomposed additively (or multiplicatively in some cases) into an elastic part and a plastic part. The elastic part of the strain can be computed from a linear elastic constitutive model. However, determination of the plastic part of the strain requires a flow rule and a hardening model.
Typical flow plasticity theories (for small deformation perfect plasticity or hardening plasticity) are developed on the basis of the following requirements:

The rock has a linear elastic range.
The rock has an elastic limit defined as the stress at which plastic deformation first takes place, i.e.,

        σ

          σ

            0

    {\displaystyle \sigma =\sigma _{0}}

.
Beyond the elastic limit the stress state always remains on the yield surface, i.e.,

        σ

          σ

            y

    {\displaystyle \sigma =\sigma _{y}}

.
Loading is defined as the situation under which increments of stress are greater than zero, i.e.,

        d
        σ

        0

    {\displaystyle d\sigma >0}

. If loading takes the stress state to the plastic domain then the increment of plastic strain is always greater than zero, i.e.,

        d

          ε

            p

        0

    {\displaystyle d\varepsilon _{p}>0}

.
Unloading is defined as the situation under which increments of stress are less than zero, i.e.,

        d
        σ
        <
        0

    {\displaystyle d\sigma <0}

. The material is elastic during unloading and no additional plastic strain is accumulated.
The total strain is a linear combination of the elastic and plastic parts, i.e.,

        d
        ε

        d

          ε

            e

        +
        d

          ε

            p

    {\displaystyle d\varepsilon =d\varepsilon _{e}+d\varepsilon _{p}}

. The plastic part cannot be recovered while the elastic part is fully recoverable.
The work done of a loading-unloading cycle is positive or zero, i.e.,

        d
        σ

        d
        ε

        d
        σ

        (
        d

          ε

            e

        +
        d

          ε

            p

        )
        ≥
        0

    {\displaystyle d\sigma \,d\varepsilon =d\sigma \,(d\varepsilon _{e}+d\varepsilon _{p})\geq 0}

. This is also called the Drucker stability postulate and eliminates the possibility of strain softening behavior.

Three-dimensional plasticity
The above requirements can be expressed in three dimensions as follows.

Elasticity (Hooke's law). In the linear elastic regime the stresses and strains in the rock are related by

          σ

            C

        :

          ε

    {\displaystyle {\boldsymbol {\sigma }}={\mathsf {C}}:{\boldsymbol {\varepsilon }}}

where the stiffness matrix

            C

    {\displaystyle {\mathsf {C}}}

 is constant.
Elastic limit (Yield surface). The elastic limit is defined by a yield surface that does not depend on the plastic strain and has the form

        f
        (

          σ

        )

        0

        .

    {\displaystyle f({\boldsymbol {\sigma }})=0\,.}

Beyond the elastic limit. For strain hardening rocks, the yield surface evolves with increasing plastic strain and the elastic limit changes. The evolving yield surface has the form

        f
        (

          σ

        ,

            ε

            p

        )

        0

        .

    {\displaystyle f({\boldsymbol {\sigma }},{\boldsymbol {\varepsilon }}_{p})=0\,.}

Loading. It is not straightforward to translate the condition geology

        d
        σ

        0

    {\displaystyle d\sigma >0}

 to three dimensions, particularly for rock plasticity which is dependent not only on the deviatoric stress but also on the mean stress. However, during loading

        f
        ≥
        0

    {\displaystyle f\geq 0}

 and it is assumed that the direction of plastic strain is identical to the normal to the yield surface (

        ∂
        f

          /

        ∂

          σ

    {\displaystyle \partial f/\partial {\boldsymbol {\sigma }}}

) and that

        d

            ε

            p

        :
        d

          σ

        ≥
        0

    {\displaystyle d{\boldsymbol {\varepsilon }}_{p}:d{\boldsymbol {\sigma }}\geq 0}

, i.e.,

        d

          σ

        :

              ∂
              f

              ∂

                σ

        ≥
        0

        .

    {\displaystyle d{\boldsymbol {\sigma }}:{\frac {\partial f}{\partial {\boldsymbol {\sigma }}}}\geq 0\,.}

The above equation, when it is equal to zero, indicates a state of neutral loading where the stress state moves along the yield surface without changing the plastic strain.
Unloading: A similar argument is made for unloading for which situation

        f
        <
        0

    {\displaystyle f<0}

, the material is in the elastic domain, and

        d

          σ

        :

              ∂
              f

              ∂

                σ

        <
        0

        .

    {\displaystyle d{\boldsymbol {\sigma }}:{\frac {\partial f}{\partial {\boldsymbol {\sigma }}}}<0\,.}

Strain decomposition: The additive decomposition of the strain into elastic and plastic parts can be written as

        d

          ε

        d

            ε

            e

        +
        d

            ε

            p

        .

    {\displaystyle d{\boldsymbol {\varepsilon }}=d{\boldsymbol {\varepsilon }}{e}+d{\boldsymbol {\varepsilon }}{p}\,.}

Stability postulate: The stability postulate is expressed as

        d

          σ

        :
        d

          ε

        ≥
        0

        .

    {\displaystyle d{\boldsymbol {\sigma }}:d{\boldsymbol {\varepsilon }}\geq 0\,.}

Flow rule
In metal plasticity, the assumption that the plastic strain increment and deviatoric stress tensor have the same principal directions is encapsulated in a relation called the flow rule. Rock plasticity theories also use a similar concept except that the requirement of pressure-dependence of the yield surface requires a relaxation of the above assumption. Instead, it is typically assumed that the plastic strain increment and the normal to the pressure-dependent yield surface have the same direction, i.e.,

        d

            ε

            p

        d
        λ

              ∂
              f

              ∂

                σ

    {\displaystyle d{\boldsymbol {\varepsilon }}_{p}=d\lambda \,{\frac {\partial f}{\partial {\boldsymbol {\sigma }}}}}

where

        d
        λ

        0

    {\displaystyle d\lambda >0}

 is a hardening parameter. This form of the flow rule is called an associated flow rule and the assumption of co-directionality is called the normality condition. The function

        f

    {\displaystyle f}

 is also called a plastic potential.
The above flow rule is easily justified for perfectly plastic deformations for which

        d

          σ

        0

    {\displaystyle d{\boldsymbol {\sigma }}=0}

 when

        d

            ε

            p

        0

    {\displaystyle d{\boldsymbol {\varepsilon }}_{p}>0}

, i.e., the yield surface remains constant under increasing plastic deformation. This implies that the increment of elastic strain is also zero,

        d

            ε

            e

        0

    {\displaystyle d{\boldsymbol {\varepsilon }}_{e}=0}

, because of Hooke's law. Therefore,

        d

          σ

        :

              ∂
              f

              ∂

                σ

        0

          and

        d

          σ

        :
        d

            ε

            p

        0

        .

    {\displaystyle d{\boldsymbol {\sigma }}:{\frac {\partial f}{\partial {\boldsymbol {\sigma }}}}=0\quad {\text{and}}\quad d{\boldsymbol {\sigma }}:d{\boldsymbol {\varepsilon }}_{p}=0\,.}

Hence, both the normal to the yield surface and the plastic strain tensor are perpendicular to the stress tensor and must have the same direction.
For a work hardening material, the yield surface can expand with increasing stress. We assume Drucker's second stability postulate which states that for an infinitesimal stress cycle this plastic work is positive, i.e.,

        d

          σ

        :
        d

            ε

            p

        ≥
        0

        .

    {\displaystyle d{\boldsymbol {\sigma }}:d{\boldsymbol {\varepsilon }}_{p}\geq 0\,.}

The above quantity is equal to zero for purely elastic cycles. Examination of the work done over a cycle of plastic loading-unloading can be used to justify the validity of the associated flow rule.

Consistency condition
The Prager consistency condition is needed to close the set of constitutive equations and to eliminate the unknown parameter

        d
        λ

    {\displaystyle d\lambda }

 from the system of equations. The consistency condition states that

        d
        f

        0

    {\displaystyle df=0}

 at yield because

        f
        (

          σ

        ,

            ε

            p

        )

        0

    {\displaystyle f({\boldsymbol {\sigma }},{\boldsymbol {\varepsilon }}_{p})=0}

, and hence

        d
        f

              ∂
              f

              ∂

                σ

        :
        d

          σ

        +

              ∂
              f

              ∂

                  ε

                  p

        :
        d

            ε

            p

        0

        .

    {\displaystyle df={\frac {\partial f}{\partial {\boldsymbol {\sigma }}}}:d{\boldsymbol {\sigma }}+{\frac {\partial f}{\partial {\boldsymbol {\varepsilon }}{p}}}:d{\boldsymbol {\varepsilon }}{p}=0\,.}
