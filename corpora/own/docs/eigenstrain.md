# Eigenstrain

Eigenstrain

In continuum mechanics an eigenstrain is any mechanical deformation in a material that is not caused by an external mechanical stress, with thermal expansion often given as a familiar example. The term was coined in the 1970s by Toshio Mura, who worked extensively on generalizing their mathematical treatment. A non-uniform distribution of eigenstrains in a material (e.g., in a composite material) leads to corresponding eigenstresses, which affect the mechanical properties of the material.

Overview
Many distinct physical causes for eigenstrains exist, such as crystallographic defects, thermal expansion, the inclusion of additional phases in a material, and previous plastic strains. All of these result from internal material characteristics, not from the application of an external mechanical load. As such, eigenstrains have also been referred to as "stress-free strains" and "inherent strains". When one region of material experiences a different eigenstrain than its surroundings, the restraining effect of the surroundings leads to a stress state on both regions. Analyzing the distribution of this residual stress for a known eigenstrain distribution or inferring the total eigenstrain distribution from a partial data set are both two broad goals of eigenstrain theory.

Analysis of eigenstrains and eigenstresses
Eigenstrain analysis usually relies on the assumption of linear elasticity, such that different contributions to the total strain

        ϵ

    {\displaystyle \epsilon }

 are additive. In this case, the total strain of a material is divided into the elastic strain e and the inelastic eigenstrain

          ϵ

            ∗

    {\displaystyle \epsilon ^{*}}

:

          ϵ

            i
            j

          e

            i
            j

        +

          ϵ

            i
            j

            ∗

    {\displaystyle \epsilon {ij}=e{ij}+\epsilon _{ij}^{*}}

where

        i

    {\displaystyle i}

 and

        j

    {\displaystyle j}

 indicate the directional components in 3 dimensions in Einstein notation.
Another assumption of linear elasticity is that the stress

        σ

    {\displaystyle \sigma }

 can be linearly related to the elastic strain

        e

    {\displaystyle e}

 and the stiffness

          C

            i
            j
            k
            l

    {\displaystyle C_{ijkl}}

 by Hooke's Law:

          σ

            i
            j

          C

            i
            j
            k
            l

          e

            k
            l

    {\displaystyle \sigma {ij}=C{ijkl}e_{kl}}

In this form, the eigenstrain is not in the equation for stress, hence the term "stress-free strain". However, a non-uniform distribution of eigenstrain alone will cause elastic strains to form in response, and therefore a corresponding elastic stress. When performing these calculations, closed-form expressions for

        e

    {\displaystyle e}

 (and thus, the total stress and strain fields) can only be found for specific geometries of the distribution of

          ϵ

            ∗

    {\displaystyle \epsilon ^{*}}

.

Ellipsoidal inclusion in an infinite medium

One of the earliest examples providing such a closed-form solution analyzed a ellipsoidal inclusion of material

          Ω

            0

    {\displaystyle \Omega _{0}}

 with a uniform eigenstrain, constrained by an infinite medium

        Ω

    {\displaystyle \Omega }

 with the same elastic properties. This can be imagined with the figure on the right. The inner ellipse represents the region

          Ω

            0

    {\displaystyle \Omega _{0}}

. The outer region represents the extent of

          Ω

            0

    {\displaystyle \Omega _{0}}

 if it fully expanded to the eigenstrain without being constrained by the surrounding

        Ω

    {\displaystyle \Omega }

. Because the total strain, shown by the solid outlined ellipse, is the sum of the elastic and eigenstrains, it follows that in this example the elastic strain in the region

          Ω

            0

    {\displaystyle \Omega _{0}}

 is negative, corresponding to a compression by

        Ω

    {\displaystyle \Omega }

 on the region

          Ω

            0

    {\displaystyle \Omega _{0}}

.
The solutions for the total stress and strain within

          Ω

            0

    {\displaystyle \Omega _{0}}

 are given by:

          ϵ

            i
            j

          S

            i
            j
            k
            l

          ϵ

            k
            l

            ∗

    {\displaystyle \epsilon {ij}=S{ijkl}\epsilon _{kl}^{*}}

          σ

            i
            j

          C

            i
            j
            k
            l

        (

          ϵ

            i
            j

        −

          ϵ

            k
            l

            ∗

        )

    {\displaystyle \sigma {ij}=C{ijkl}(\epsilon _{ij}-\epsilon _{kl}^{*})}

Where

        S

    {\displaystyle S}

 is the Eshelby Tensor, whose value for each component is determined only by the geometry of the ellipsoid. The solution demonstrates that the total strain and stress state within the inclusion

          Ω

            0

    {\displaystyle \Omega _{0}}

 are uniform. Outside of

          Ω

            0

    {\displaystyle \Omega _{0}}

, the stress decays towards zero with increasing distance away from the inclusion. In the general case, the resulting stresses and strains may be asymmetric, and due to the asymmetry of

        S

    {\displaystyle S}

, the eigenstrain may not be coaxial with the total strain.

Inverse problem
Eigenstrains and the residual stresses that accompany them are difficult to measure (see:Residual stress). Engineers can usually only acquire partial information about the eigenstrain distribution in a material. Methods to fully map out the eigenstrain, called the inverse problem of eigenstrain, are an active area of research. Understanding the total residual stress state, based on knowledge of the eigenstrains, informs the design process in many fields.

Applications

Structural engineering
Residual stresses, e.g. introduced by manufacturing processes or by welding of structural members, reflect the eigenstrain state of the material. This can be unintentional or by design, e.g. shot peening. In either case, the final stress state can affect the fatigue, wear, and corrosion behavior of structural components. Eigenstrain analysis is one way to model these residual stresses.

Composite materials
Since composite materials have large variations in the thermal and mechanical properties of their components, eigenstrains are particularly relevant to their study. Local stresses and strains can cause decohesion between composite phases or cracking in the matrix. These may be driven by changes in temperature, moisture content, piezoelectric effects, or phase transformations. Particular solutions and approximations to the stress fields taking into account the periodic or statistical character of the composite material's eigenstrain have been developed.

Strain engineering
Lattice misfit strains are also a class of eigenstrains, caused by growing a crystal of one lattice parameter on top of a crystal with a different lattice parameter. Controlling these strains can improve the electronic properties of an epitaxially grown semiconductor. See: strain engineering.
