# Wave impedance

Wave impedance

The wave impedance of an electromagnetic wave is the ratio of the transverse components of the electric and magnetic fields (the transverse components being those at right angles to the direction of propagation). For a transverse-electric-magnetic (TEM) plane wave traveling through a homogeneous medium, the wave impedance is everywhere equal to the intrinsic impedance of the medium. In particular, for a plane wave travelling through empty space, the wave impedance is equal to the impedance of free space. The symbol Z is used to represent it and it is expressed in units of ohms. The symbol η (eta) may be used instead of Z for wave impedance to avoid confusion with electrical impedance.

Definition

The wave impedance is given by

        Z

                E

                  0

                  −

              (
              x
              )

                H

                  0

                  −

              (
              x
              )

    {\displaystyle Z={E_{0}^{-}(x) \over H_{0}^{-}(x)}}

where

          E

            0

            −

        (
        x
        )

    {\displaystyle E_{0}^{-}(x)}

 is the electric field and

          H

            0

            −

        (
        x
        )

    {\displaystyle H_{0}^{-}(x)}

 is the magnetic field, in phasor representation. The impedance is, in general, a complex number.
In terms of the parameters of an electromagnetic wave and the medium it travels through, the wave impedance is given by

        Z

                j
                ω
                μ

                σ
                +
                j
                ω
                ε

    {\displaystyle Z={\sqrt {j\omega \mu \over \sigma +j\omega \varepsilon }}}

where μ is the magnetic permeability, ε is the (real) electric permittivity and σ is the electrical conductivity of the material the wave is travelling through (corresponding to the imaginary component of the permittivity multiplied by omega). In the equation, j is the imaginary unit, and ω is the angular frequency of the wave. Just as for electrical impedance, the impedance is a function of frequency. In the case of an ideal dielectric (where the conductivity is zero), the equation reduces to the real number

        Z

              μ
              ε

        .

    {\displaystyle Z={\sqrt {\mu \over \varepsilon }}.}

In free space

In free space the wave impedance of plane waves is:

          Z

            0

                μ

                  0

                ε

                  0

    {\displaystyle Z_{0}={\sqrt {\frac {\mu _{0}}{\varepsilon _{0}}}}}

(where ε0 is the permittivity constant in free space and μ0 is the permeability constant in free space). Now, since

        c

            1

                μ

                  0

                ε

                  0

        299

        792

        458

           m/s

    {\displaystyle c={\frac {1}{\sqrt {\mu _{0}\varepsilon _{0}}}}=299\,792\,458{\text{ m/s}}}

 (by definition of the metre),

          Z

            0

          μ

            0

        c

            1

                ε

                  0

              c

    {\displaystyle Z_{0}=\mu _{0}c={\frac {1}{\varepsilon _{0}c}}}

.
The currently accepted value of

          Z

            0

    {\displaystyle Z_{0}}

 is 376.730313412(59) Ω.

In an unbounded dielectric
In an isotropic, homogeneous dielectric with negligible magnetic properties, i.e.

        μ

          μ

            0

    {\displaystyle \mu =\mu _{0}}

 and

        ε

          ε

            r

          ε

            0

    {\displaystyle \varepsilon =\varepsilon _{r}\varepsilon _{0}}

. So, the value of wave impedance in a perfect dielectric is

        Z

              μ
              ε

                μ

                  0

                  ε

                    0

                  ε

                    r

              Z

                0

                  ε

                    r

        ≈

            377

                  ε

                    r

        Ω

    {\displaystyle Z={\sqrt {\mu \over \varepsilon }}={\sqrt {\mu _{0} \over \varepsilon _{0}\varepsilon {r}}}={Z{0} \over {\sqrt {\varepsilon _{r}}}}\approx {377 \over {\sqrt {\varepsilon _{r}}}}\,\Omega }

,
where

          ε

            r

    {\displaystyle \varepsilon _{r}}

 is the relative dielectric constant.

In a waveguide
For any waveguide in the form of a hollow metal tube, (such as rectangular guide, circular guide, or double-ridge guide), the wave impedance of a travelling wave is dependent on the frequency

        f

    {\displaystyle f}

, but is the same throughout the guide. For transverse electric (TE) modes of propagation the wave impedance is:

        Z

              Z

                0

              1
              −

                  (

                        f

                          c

                      f

                  )

                  2

            (TE modes)

        ,

    {\displaystyle Z={\frac {Z_{0}}{\sqrt {1-\left({\frac {f_{c}}{f}}\right)^{2}}}}\qquad {\mbox{(TE modes)}},}

where fc is the cut-off frequency of the mode, and for transverse magnetic (TM) modes of propagation the wave impedance is:

        Z

          Z

            0

            1
            −

                (

                      f

                        c

                    f

                )

                2

            (TM modes)

    {\displaystyle Z=Z_{0}{\sqrt {1-\left({\frac {f_{c}}{f}}\right)^{2}}}\qquad {\mbox{(TM modes)}}}

Above the cut-off (f > fc), the impedance is real (resistive) and the wave carries energy. Below cut-off the impedance is imaginary (reactive) and the wave is evanescent. These expressions neglect the effect of resistive loss in the walls of the waveguide. For a waveguide entirely filled with a homogeneous dielectric medium, similar expressions apply, but with the wave impedance of the medium replacing Z0. The presence of the dielectric also modifies the cut-off frequency fc.
For a waveguide or transmission line containing more than one type of dielectric medium (such as microstrip), the wave impedance will in general vary over the cross-section of the line.
