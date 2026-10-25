# Ogden hyperelastic model

Ogden hyperelastic model

The Ogden material model is a hyperelastic material model used to describe the non-linear stress–strain behaviour of complex materials such as rubbers, polymers, and biological tissue. The model was developed by Raymond Ogden in 1972. The Ogden model, like other hyperelastic material models, assumes that the material behaviour can be described by means of a strain energy density function, from which the stress–strain relationships can be derived.

Ogden material model
In the Ogden material model, the strain energy density is expressed in terms of the principal stretches

          λ

            j

    {\displaystyle \,!\lambda _{j}}

,

        j

        1
        ,
        2
        ,
        3

    {\displaystyle \,!j=1,2,3}

 as:

        W

          (

              λ

                1

            ,

              λ

                2

            ,

              λ

                3

          )

          ∑

            p

            1

            N

              μ

                p

              α

                p

          (

              λ

                1

                  α

                    p

            +

              λ

                2

                  α

                    p

            +

              λ

                3

                  α

                    p

            −
            3

          )

    {\displaystyle W\left(\lambda _{1},\lambda _{2},\lambda _{3}\right)=\sum _{p=1}^{N}{\frac {\mu _{p}}{\alpha _{p}}}\left(\lambda _{1}^{\alpha _{p}}+\lambda _{2}^{\alpha _{p}}+\lambda _{3}^{\alpha _{p}}-3\right)}

where

        N

    {\displaystyle N}

,

          μ

            p

    {\displaystyle \,!\mu _{p}}

 and

          α

            p

    {\displaystyle \,!\alpha _{p}}

 are material constants. Under the assumption of incompressibility one can rewrite as

        W

          (

              λ

                1

            ,

              λ

                2

          )

          ∑

            p

            1

            N

              μ

                p

              α

                p

          (

              λ

                1

                  α

                    p

            +

              λ

                2

                  α

                    p

            +

              λ

                1

                −

                  α

                    p

              λ

                2

                −

                  α

                    p

            −
            3

          )

    {\displaystyle W\left(\lambda _{1},\lambda _{2}\right)=\sum _{p=1}^{N}{\frac {\mu _{p}}{\alpha _{p}}}\left(\lambda _{1}^{\alpha _{p}}+\lambda _{2}^{\alpha _{p}}+\lambda _{1}^{-\alpha _{p}}\lambda _{2}^{-\alpha _{p}}-3\right)}

In general the shear modulus results from

        2
        μ

          ∑

            p

            1

            N

          μ

            p

          α

            p

        .

    {\displaystyle 2\mu =\sum _{p=1}^{N}\mu _{p}\alpha _{p}.}

With

        N

        3

    {\displaystyle N=3}

 and by fitting the material parameters, the material behaviour of rubbers can be described very accurately. For particular values of material constants the Ogden model will reduce to either the Neo-Hookean solid (

        N

        1

    {\displaystyle N=1}

,

        α

        2

    {\displaystyle \alpha =2}

) or the Mooney-Rivlin material (

        N

        2

    {\displaystyle N=2}

,

          α

            1

        2

    {\displaystyle \alpha _{1}=2}

,

          α

            2

        −
        2

    {\displaystyle \alpha _{2}=-2}

, with the constraint condition

          λ

            1

          λ

            2

          λ

            3

        1

    {\displaystyle \lambda _{1}\lambda _{2}\lambda _{3}=1}

).
Using the Ogden material model, the three principal values of the Cauchy stresses can now be computed as

          σ

            j

        −
        p
        +

          λ

            j

              ∂
              W

              ∂

                λ

                  j

        −
        p
        +

          ∑

            p

            1

            N

          μ

            p

          λ

            j

              α

                p

    {\displaystyle \sigma _{j}=-p+\lambda _{j}{\frac {\partial W}{\partial \lambda _{j}}}=-p+\sum _{p=1}^{N}\mu _{p}\lambda _{j}^{\alpha _{p}}}

.

Uniaxial tension
We now consider an incompressible material under uniaxial tension, with the stretch ratio given as

        λ

            l

              l

                0

    {\displaystyle \lambda ={\frac {l}{l_{0}}}}

, where

        l

    {\displaystyle l}

 is the stretched length and

            l

              0

    {\displaystyle {l_{0}}}

 is the original unstretched length. The pressure

        p

    {\displaystyle p}

 is determined from incompressibility and boundary condition

          σ

            2

          σ

            3

        0

    {\displaystyle \sigma _{2}=\sigma _{3}=0}

, yielding:

          σ

            1

          ∑

            p

            1

            N

          μ

            p

          (

              λ

                  α

                    p

            −

              λ

                −

                    1
                    2

                  α

                    p

          )

    {\displaystyle \sigma _{1}=\sum _{p=1}^{N}\mu _{p}\left(\lambda ^{\alpha _{p}}-\lambda ^{-{\frac {1}{2}}\alpha _{p}}\right)}

.

Equi-biaxial tension
Considering an incompressible material under eqi-biaxial tension, with

          λ

            1

          λ

            2

            l

              l

                0

    {\displaystyle \lambda _{1}=\lambda {2}={\frac {l}{l{0}}}}

. The pressure

        p

    {\displaystyle p}

 is determined from incompressibility, and boundary condition

          σ

            3

        0

    {\displaystyle \sigma _{3}=0}

, gives:

          σ

            1

          σ

            2

          ∑

            p

            1

            N

          μ

            p

          (

              λ

                  α

                    p

            −

              λ

                −
                2

                  α

                    p

          )

    {\displaystyle \sigma _{1}=\sigma _{2}=\sum _{p=1}^{N}\mu _{p}\left(\lambda ^{\alpha _{p}}-\lambda ^{-2\alpha _{p}}\right)}

.

Other hyperelastic models
For rubber and biological materials, more sophisticated models are necessary. Such materials may exhibit a non-linear stress–strain behaviour at modest strains, or are elastic up to huge strains. These complex non-linear stress–strain behaviours need to be accommodated by specifically tailored strain-energy density functions.
The simplest of these hyperelastic models, is the Neo-Hookean solid.

        W
        (

          C

        )

            μ
            2

        (

          I

            1

            C

        −
        3
        )

    {\displaystyle W(\mathbf {C} )={\frac {\mu }{2}}(I_{1}^{C}-3)}

where

        μ

    {\displaystyle \mu }

 is the shear modulus, which can be determined by experiments. From experiments it is known that for rubbery materials under moderate straining up to 30–70%, the Neo-Hookean model usually fits the material behaviour with sufficient accuracy. To model rubber at high strains, the one-parametric Neo-Hookean model is replaced by more general models, such as the Mooney-Rivlin solid where the strain energy

        W

    {\displaystyle W}

 is a linear combination of two invariants

        W
        (

          C

        )

              μ

                1

            2

          (

              I

                1

                C

            −
            3

          )

        −

              μ

                2

            2

          (

              I

                2

                C

            −
            3

          )

    {\displaystyle W(\mathbf {C} )={\frac {\mu {1}}{2}}\left(I{1}^{C}-3\right)-{\frac {\mu {2}}{2}}\left(I{2}^{C}-3\right)}

The Mooney-Rivlin material was originally also developed for rubber, but is today often applied to model (incompressible) biological tissue. For modeling rubbery and biological materials at even higher strains, the more sophisticated Ogden material model has been developed.
