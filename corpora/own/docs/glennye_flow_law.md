# Glen–Nye flow law

Glen–Nye flow law

In theoretical glaciology and continuum mechanics, the Glen–Nye flow law, also referred to as Glen's flow law, is an empirically derived constitutive relation widely used as a model for the rheology of glacial ice. The Glen–Nye flow law treats ice as a purely viscous, incompressible, isotropic, non-Newtonian fluid, with a viscosity determined by a power law relation between strain rate and stress:

                ϵ
                ˙

            e

        A

          τ

            e

            n

    {\displaystyle {\dot {\epsilon }}_{e}=A\tau _{e}^{n}}

The effective strain rate

                ϵ
                ˙

            e

    {\displaystyle {\dot {\epsilon }}_{e}}

 (units of s−1) and effective stress

          τ

            e

    {\displaystyle \tau _{e}}

 (units of Pa) are related to the second principle invariants of their respective tensors. The parameters

        A

    {\displaystyle A}

 and

        n

    {\displaystyle n}

 are scalar constants which have been estimated through a combination of theory and measurements. The exponent

        n

    {\displaystyle n}

 is dimensionless, and the rate factor

        A

    {\displaystyle A}

 takes on the units Pa−

        n

    {\displaystyle n}

 s−1. The Glen–Nye flow law simplifies the viscous stress tensor to a single scalar value

        μ

    {\displaystyle \mu }

, the dynamic viscosity, which is determined by tensor invariants of the deviatoric stress tensor

          τ

    {\displaystyle {\boldsymbol {\tau }}}

 and the strain rate tensor

              ϵ
              ˙

    {\displaystyle {\boldsymbol {\dot {\epsilon }}}}

.
Under the application of sustained force ice will flow as a fluid, and changes to the force applied will result in non-linear changes to the resulting flow. This fluid behavior of ice, which the Glen–Nye flow law is intended to represent, is accommodated within the solid ice by creep, and is a dominant mode of glacial ice flow.

Viscosity definition
The constitutive relation is developed as a generalized Newtonian fluid, where the deviatoric stress and strain tensors are related by a viscosity scalar:

where

        μ

    {\displaystyle \mu }

 is the viscosity (units of Pa s),

          τ

    {\displaystyle {\boldsymbol {\tau }}}

 is the deviatoric stress tensor, and

              ϵ
              ˙

    {\displaystyle {\boldsymbol {\dot {\epsilon }}}}

 is the strain rate tensor. In some derivations,

        λ

        (
        2
        μ

          )

            −
            1

    {\displaystyle \lambda =(2\mu )^{-1}}

 (units of Pa−1 s−1) is substituted.
This construction makes several assumptions:

Isotropy, as the single proportionality scalar is the same for all tensor components.
Incompressibility, as volumetric stress is ignored and only the deviatoric stress can do work.
That corresponding components of the two tensors are directly proportional to one another, i.e.

          τ

            i
            j

        ∝

                ϵ
                ˙

            i
            j

    {\displaystyle \tau {ij}\propto {\dot {\epsilon }}{ij}}

. Theoretically, this assumption results from ignoring the third principle invariant of the tensors; physically, this means that the strain rate can only change along the same axes as the principal stresses.
While incompressibility is an accurate assumption for glacial ice, glacial ice can be anisotropic and in general the strain rate may respond perpendicularly to the principal stress.
With these assumptions, the stress and strain rate tensors here are symmetric and have a trace of zero, properties that allow their invariants and squares to be simplified from the general definitions.
The deviatoric stress tensor is related to an effective stress by its second principal invariant:

          τ

            e

            2

        I

          I

            τ

            1
            2

          τ

            i
            j

          τ

            i
            j

    {\displaystyle \tau {e}^{2}=II{\boldsymbol {\tau }}={\frac {1}{2}}\tau _{ij}\tau _{ij}}

where Einstein notation implies summation over repeated indices.
The same is defined for an effective strain rate:

                ϵ
                ˙

            e

            2

        I

          I

                ϵ
                ˙

            1
            2

                ϵ
                ˙

            i
            j

                ϵ
                ˙

            i
            j

    {\displaystyle {\dot {\epsilon }}{e}^{2}=II{\boldsymbol {\dot {\epsilon }}}={\frac {1}{2}}{\dot {\epsilon }}{ij}{\dot {\epsilon }}{ij}}

From this form, we can recognize that:

            τ

            2

          τ

            i
            j

          τ

            i
            j

        2

          τ

            e

            2

    {\displaystyle {\boldsymbol {\tau }}^{2}=\tau _{ij}\tau _{ij}=2\tau _{e}^{2}}

and

                ϵ
                ˙

            2

                ϵ
                ˙

            i
            j

                ϵ
                ˙

            i
            j

        2

                ϵ
                ˙

            e

            2

    {\displaystyle {\boldsymbol {\dot {\epsilon }}}^{2}={\dot {\epsilon }}{ij}{\dot {\epsilon }}{ij}=2{\dot {\epsilon }}_{e}^{2}}

The viscosity is scalar and cannot be negative (a fluid cannot gain energy as it flows), so

        μ

    {\displaystyle \mu }

 can be expressed in terms of the invariant effective stress and effective strain rate.

        μ

            τ

              2

                    ϵ
                    ˙

            1
            2

          τ

            e

                ϵ
                ˙

            e

            −
            1

    {\displaystyle \mu ={\frac {\boldsymbol {\tau }}{2{\dot {\boldsymbol {\epsilon }}}}}={\frac {1}{2}}\tau {e}{\dot {\epsilon }}{e}^{-1}}

Here, the Glen–Nye flow law allows us to substitute for either

          τ

            e

    {\displaystyle \tau _{e}}

 or

                ϵ
                ˙

            e

    {\displaystyle {\dot {\epsilon }}_{e}}

, and

        μ

    {\displaystyle \mu }

 can be defined in terms of either the effective strain rate or effective stress alone:

where

        B

          A

            −
            1

              /

            n

    {\displaystyle B=A^{-1/n}}

 (units of Pa s

            1

              /

            n

    {\displaystyle ^{1/n}}

) is sometimes substituted.

Parameter values
The Glen–Nye rheology model defines two parameters,

        A

    {\displaystyle A}

 and

        n

    {\displaystyle n}

.
The rate factor

        A

    {\displaystyle A}

 has been found empirically to vary with temperature and is often modeled with an Arrhenius relation describing the temperature dependence of creep:

        A

          A

            0

          e

            (
            −
            Q

              /

            R
            T
            )

    {\displaystyle A=A_{0}e^{(-Q/RT)}}

where

        Q

    {\displaystyle Q}

 is the activation energy,

        R

    {\displaystyle R}

 is the universal gas constant, and

        T

    {\displaystyle T}

 is the absolute temperature. The prefactor

          A

            0

    {\displaystyle A_{0}}

 may be dependent on crystal structure, impurities, damage, or other qualities of the ice. Estimates of

        A

    {\displaystyle A}

 vary by orders of magnitude and can be derived as a single value from an estimated value for

          A

            0

    {\displaystyle A_{0}}

, or by comparing measurements of multiple real world glaciers and experiments, or treated as a scalar field inferred from observations by a numerical inversion of the momentum equation for ice flow at a specific location.
Viscous ice flow is an example of shear thinning, which corresponds to

        n

        1

    {\displaystyle n>1}

. Review of research using a variety of methods and field sites have found the range of plausible values to be around

        2
        <
        n
        <
        4

    {\displaystyle 2<n<4}

 with the most commonly used assumption to be a constant

        n

        3

    {\displaystyle n=3}

. However, the value of

        n

    {\displaystyle n}

 is also stress dependent, and can reflect different microstructural mechanisms facilitating creep at different stress regimes.
Methods to improve estimations of these viscous parameters are an ongoing field of research.

Limitations
The use of the word "law" in referring to the Glen-Nye model of ice rheology may obscure the complexity of factors which determine the range of viscous ice flow parameter values even within a single glacier, as well as the significant assumptions and simplifications made by the model itself.
In particular, treatment of the ice as a fluid with bulk properties does not represent and may struggle to capture the cascade of mechanisms which allow the ice to deform at the grain scale in solid state. Glacial ice crystals grow on scales of millimeters up to 10 cm, and constant readjustment between grain structure and internal stress results in high variations in strain across the same length-scale as the crystals themselves. Additionally, individual ice crystals are not isotropic, and typically are not randomly oriented within the material fabric which undergoes dynamic recrystallization. Grain size and fabric orientation are known to influence the creep of glacial ice, but are dynamic properties which also evolve with the stress regime and are not simple to capture in a model.
The Glen-Nye flow law also does not render the full range of ice response to stress, including elastic deformation, fracture mechanics (i.e. crevasses), and transient phases of creep.
