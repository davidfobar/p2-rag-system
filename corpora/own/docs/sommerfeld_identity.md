# Sommerfeld identity

Sommerfeld identity

The Sommerfeld identity is a mathematical identity, due Arnold Sommerfeld, used in the theory of propagation of waves,

              e

                i
                k
                R

            R

          ∫

            0

            ∞

          I

            0

        (
        λ
        r
        )

          e

            −
            μ

              z

              λ
              d
              λ

            μ

    {\displaystyle {\frac {e^{ikR}}{R}}=\int \limits {0}^{\infty }I{0}(\lambda r)e^{-\mu \left|z\right|}{\frac {\lambda d\lambda }{\mu }}}

where

        μ

              λ

                2

            −

              k

                2

    {\displaystyle \mu ={\sqrt {\lambda ^{2}-k^{2}}}}

is to be taken with positive real part, to ensure the convergence of the integral and its vanishing in the limit

        z
        →
        ±
        ∞

    {\displaystyle z\rightarrow \pm \infty }

 and

          R

            2

          r

            2

        +

          z

            2

    {\displaystyle R^{2}=r^{2}+z^{2}}

.
Here,

        R

    {\displaystyle R}

 is the distance from the origin while

        r

    {\displaystyle r}

 is the distance from the central axis of a cylinder as in the

        (
        r
        ,
        ϕ
        ,
        z
        )

    {\displaystyle (r,\phi ,z)}

 cylindrical coordinate system. Here the notation for Bessel functions follows the German convention, to be consistent with the original notation used by Sommerfeld. The function

          I

            0

        (
        z
        )

    {\displaystyle I_{0}(z)}

 is the zeroth-order Bessel function of the first kind, better known by the notation

          I

            0

        (
        z
        )

          J

            0

        (
        i
        z
        )

    {\displaystyle I_{0}(z)=J_{0}(iz)}

 in English literature.
This identity is known as the Sommerfeld identity in radial-spectral form.
In alternative notation, the Sommerfeld identity can be more easily seen as an expansion of a spherical wave in terms of cylindrically-symmetric waves:

              e

                i

                  k

                    0

                r

            r

        i

          ∫

            0

            ∞

          d

            k

              ρ

                k

                  ρ

                k

                  z

            J

              0

          (

            k

              ρ

          ρ
          )

            e

              i

                k

                  z

                z

    {\displaystyle {\frac {e^{ik_{0}r}}{r}}=i\int \limits {0}^{\infty }{dk{\rho }{\frac {k_{\rho }}{k_{z}}}J_{0}(k_{\rho }\rho )e^{ik_{z}\left|z\right|}}}

where

          k

            z

        (

          k

            0

            2

        −

          k

            ρ

            2

          )

            1

              /

            2

    {\displaystyle k_{z}=(k_{0}^{2}-k_{\rho }^{2})^{1/2}}

The notation used here is different from that above:

        r

    {\displaystyle r}

 is now the distance from the origin and

        ρ

    {\displaystyle \rho }

 is the radial distance in a cylindrical coordinate system defined as

        (
        ρ
        ,
        ϕ
        ,
        z
        )

    {\displaystyle (\rho ,\phi ,z)}

. The physical interpretation is that a spherical wave can be expanded into a summation of cylindrical waves in

        ρ

    {\displaystyle \rho }

 direction, multiplied by a two-sided plane wave in the

        z

    {\displaystyle z}

 direction; see the Jacobi-Anger expansion. The summation has to be taken over all the wavenumbers

          k

            ρ

    {\displaystyle k_{\rho }}

.
The Sommerfeld identity is closely related to the two-dimensional Fourier transform with cylindrical symmetry, i.e., the Hankel transform. It is found by transforming the spherical wave along the in-plane coordinates (

        x

    {\displaystyle x}

,

        y

    {\displaystyle y}

, or

        ρ

    {\displaystyle \rho }

,

        ϕ

    {\displaystyle \phi }

) but not transforming along the height coordinate

        z

    {\displaystyle z}

.

Axial-spectral representation of the Sommerfeld identity
The radial forms above integrate over the transverse spectral variable λ (equivalently

          k

            ρ

    {\displaystyle k_{\rho }}

), which leaves the axial dependence to appear through a two-sided exponential in

        z

    {\displaystyle z}

. A complementary form rather integrates over the axial wavenumber

          k

            z

    {\displaystyle k_{z}}

, keeping the axial phase explicit and expressing the transverse dependence through a cylindrical (Hankel) wave:

              e

                i

                  k

                    0

                R

            R

            i
            2

          ∫

            −
            ∞

            ∞

          H

            0

            (
            1
            )

        (

          k

            ρ

        ρ
        )

          e

            i

              k

                z

            z

        d

          k

            z

        ,

          k

            ρ

              k

                0

                2

            −

              k

                z

                2

        ,

          Im

        (

          k

            ρ

        )
        ≥
        0
        ,

    {\displaystyle {\frac {e^{ik_{0}R}}{R}}={\frac {i}{2}}\int {-\infty }^{\infty }H{0}^{(1)}(k_{\rho }\rho )e^{ik_{z}z}dk_{z},\quad k_{\rho }={\sqrt {k_{0}^{2}-k_{z}^{2}}},\ {\text{Im}}(k_{\rho })\geq 0,}

where

        ρ

    {\displaystyle \rho }

 is the radial distance in the cylindrical system

        (
        ρ
        ,
        ϕ
        ,
        z
        )

    {\displaystyle (\rho ,\phi ,z)}

,

        R

              ρ

                2

            +

              z

                2

    {\displaystyle R={\sqrt {\rho ^{2}+z^{2}}}}

, and

          H

            0

            (
            1
            )

    {\displaystyle H_{0}^{(1)}}

 is the Hankel function of zeroth-order of the first kind. The branch of

          k

            ρ

    {\displaystyle k_{\rho }}

 is chosen such that

          H

            0

            (
            1
            )

        (

          k

            ρ

        ρ
        )

    {\displaystyle H_{0}^{(1)}(k_{\rho }\rho )}

 is representative of an outgoing wave for

          k

            z

            2

        <

          k

            0

            2

    {\displaystyle k_{z}^{2}<k_{0}^{2}}

 and is evanescent for

          k

            z

            2

          k

            0

            2

    {\displaystyle k_{z}^{2}>k_{0}^{2}}

, which ensures convergence.
This form is obtained via the same spherical wave by transforming along thew axial coordinate

        z

    {\displaystyle z}

 alone, instead of along the in-place coordinates. This representation is used in spectral-domain analyses of cylindrical structures and layered media, where the

          e

            i

              k

                z

            z

    {\displaystyle e^{ik_{z}z}}

 factor allows axial and transverse operations to be separate, and where the Hankel-function argument makes the two-centre translation of cylindrical waves tractable (via Bessel-family addition theorems, for example).
