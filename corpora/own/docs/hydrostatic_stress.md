# Hydrostatic stress

Hydrostatic stress

In continuum mechanics, hydrostatic stress, also known as isotropic stress or volumetric stress, is a component of stress which contains uniaxial stresses, but not shear stresses. A specialized case of hydrostatic stress contains isotropic compressive stress, which changes only in volume, but not in shape. Pure hydrostatic stress can be experienced by a point in a fluid such as water. It is often used interchangeably with "mechanical pressure" and is also known as confining stress, particularly in the field of geomechanics.
Hydrostatic stress is equivalent to the average of the uniaxial stresses along three orthogonal axes, so it is one third of the first invariant of the stress tensor (i.e. the trace of the stress tensor):

          σ

            h

              I

                i

            3

            1
            3

        tr
        ⁡
        (

          σ

        )

    {\displaystyle \sigma {h}={\frac {I{i}}{3}}={\frac {1}{3}}\operatorname {tr} ({\boldsymbol {\sigma }})}

For example in cartesian coordinates (x,y,z) the hydrostatic stress is simply:

          σ

            h

                σ

                  x
                  x

              +

                σ

                  y
                  y

              +

                σ

                  z
                  z

            3

    {\displaystyle \sigma _{h}={\frac {\sigma _{xx}+\sigma _{yy}+\sigma _{zz}}{3}}}

Hydrostatic stress and thermodynamic pressure
In the particular case of an incompressible fluid,
the thermodynamic pressure coincides with the mechanical pressure (i.e. the opposite of the hydrostatic stress):

        p

        −

          σ

            h

        −

            1
            3

        tr
        ⁡
        (

          σ

        )

    {\displaystyle p=-\sigma _{h}=-{\frac {1}{3}}\operatorname {tr} ({\boldsymbol {\sigma }})}

In the general case of a compressible fluid, the thermodynamic pressure

        p

    {\displaystyle p}

 is no more proportional to the isotropic stress term (the mechanical pressure), since there is an additional term dependent on the trace of the strain rate tensor:

        p

        −

            1
            3

        tr
        ⁡
        (

          σ

        )
        +
        ζ
        tr
        ⁡
        (

          ϵ

        )

    {\displaystyle p=-{\frac {1}{3}}\operatorname {tr} ({\boldsymbol {\sigma }})+\zeta \operatorname {tr} ({\boldsymbol {\epsilon }})}

where the coefficient

        ζ

    {\displaystyle \zeta }

 is the bulk viscosity. The trace of the strain rate tensor corresponds to the flow compression (the divergence of the flow velocity):

        tr
        ⁡
        (

          ϵ

        )

        tr
        ⁡

          (

                1
                2

            (
            ∇

              u

            +
            (
            ∇

              u

              )

                T

            )

          )

        ∇
        ⋅

          u

    {\displaystyle \operatorname {tr} ({\boldsymbol {\epsilon }})=\operatorname {tr} \left({\frac {1}{2}}(\nabla \mathbf {u} +(\nabla \mathbf {u} )^{T})\right)=\nabla \cdot \mathbf {u} }

So the expression for the thermodynamic pressure is usually expressed as:

        p

        −

          σ

            h

        +
        ζ
        ∇
        ⋅

          u

              p
              ¯

        +
        ζ
        ∇
        ⋅

          u

    {\displaystyle p=-\sigma _{h}+\zeta \nabla \cdot \mathbf {u} ={\bar {p}}+\zeta \nabla \cdot \mathbf {u} }

where the mechanical pressure has been denoted with

              p
              ¯

    {\textstyle {\bar {p}}}

.
In some cases, the second viscosity

        ζ

    {\textstyle \zeta }

 can be assumed to be constant in which case, the effect of the volume viscosity

        ζ

    {\textstyle \zeta }

 is that the mechanical pressure is not equivalent to the thermodynamic pressure as stated above.

              p
              ¯

        ≡
        p
        −
        ζ

        ∇
        ⋅

          u

        ,

    {\displaystyle {\bar {p}}\equiv p-\zeta \,\nabla \cdot \mathbf {u} ,}

However, this difference is usually neglected most of the time (that is whenever we are not dealing with processes such as sound absorption and attenuation of shock waves, where second viscosity coefficient becomes important) by explicitly assuming

        ζ

        0

    {\textstyle \zeta =0}

. The assumption of setting

        ζ

        0

    {\textstyle \zeta =0}

 is called as the Stokes hypothesis. The validity of Stokes hypothesis can be demonstrated for monoatomic gas both experimentally and from the kinetic theory; for other gases and liquids, Stokes hypothesis is generally incorrect.

Potential external field in a fluid
Its magnitude in a fluid,

          σ

            h

    {\displaystyle \sigma _{h}}

, can be given by Stevin's Law:

          σ

            h

            ∑

              i

              1

              n

            ρ

              i

          g

            h

              i

    {\displaystyle \sigma _{h}=\displaystyle \sum _{i=1}^{n}\rho {i}gh{i}}

where

i is an index denoting each distinct layer of material above the point of interest;

          ρ

            i

    {\displaystyle \rho _{i}}

 is the density of each layer;

        g

    {\displaystyle g}

 is the gravitational acceleration (assumed constant here; this can be substituted with any acceleration that is important in defining weight);

          h

            i

    {\displaystyle h_{i}}

 is the height (or thickness) of each given layer of material.
For example, the magnitude of the hydrostatic stress felt at a point under ten meters of fresh water would be

          σ

            h

          ρ

            w

        g

          h

            w

        1000

            kg m

            −
            3

        ⋅
        9.8

            m s

            −
            2

        ⋅
        10

          m

        9.8
        ⋅

            10

              4

             kg m

            −
            1

            s

            −
            2

        9.8
        ⋅

          10

            4

             N m

            −
            2

    {\displaystyle \sigma _{h}=\rho {w}gh{w}=1000\,{\text{kg m}}^{-3}\cdot 9.8\,{\text{m s}}^{-2}\cdot 10\,{\text{m}}=9.8\cdot {10^{4}}{\text{ kg m}}^{-1}{\text{s}}^{-2}=9.8\cdot 10^{4}{\text{ N m}}^{-2}}

where the index w indicates "water".
Because the hydrostatic stress is isotropic, it acts equally in all directions. In tensor form, the hydrostatic stress is equal to

          σ

            h

        ⋅

          I

            3

          σ

            h

          [

                  1

                  0

                  0

                  0

                  1

                  0

                  0

                  0

                  1

          ]

          [

                    σ

                      h

                  0

                  0

                  0

                    σ

                      h

                  0

                  0

                  0

                    σ

                      h

          ]

    {\displaystyle \sigma {h}\cdot I{3}=\sigma _{h}\left[{\begin{array}{ccc}1&0&0\0&1&0\0&0&1\end{array}}\right]=\left[{\begin{array}{ccc}\sigma _{h}&0&0\0&\sigma _{h}&0\0&0&\sigma _{h}\end{array}}\right]}

where

          I

            3

    {\displaystyle I_{3}}

 is the 3-by-3 identity matrix.
Hydrostatic compressive stress is used for the determination of the bulk modulus for materials.
