# Bloch–Siegert shift

Bloch–Siegert shift

The Bloch–Siegert shift is a phenomenon in quantum physics that becomes important for driven two-level systems when the driving gets strong (e.g. atoms driven by a strong laser drive or nuclear spins in NMR, driven by a strong oscillating magnetic field).
When the rotating-wave approximation (RWA) is invoked, the resonance between the driving field and a pseudospin occurs when the field frequency

        ω

    {\displaystyle \omega }

 is identical to the spin's transition frequency

          ω

            0

    {\displaystyle \omega _{0}}

. The RWA is, however, an approximation. In 1940 Felix Bloch and Arnold Siegert showed that the dropped parts oscillating rapidly can give rise to a shift in the true resonance frequency of the dipoles.
The Bloch–Siegert shift has been used for practical purposes in both NMR and MRI, including power calibration, image encoding, and magnetic field mapping.

Rotating-wave approximation
In the rotating-wave approximation, when the perturbation to the two level system is

          H

            a
            b

              V

                a
                b

            2

        cos
        ⁡

          (
          ω
          t
          )

    {\displaystyle H_{ab}={\frac {V_{ab}}{2}}\cos {(\omega t)}}

, a linearly polarized field is considered as a superposition of two circularly polarized fields of the same amplitude rotating in opposite directions with frequencies

        ω
        ,
        −
        ω

    {\displaystyle \omega ,-\omega }

. Then, in the rotating frame(

        ω

    {\displaystyle \omega }

), we can neglect the counter-rotating field and the Rabi frequency is

        Ω

              Ω

                0

                2

            +
            (
            ω
            −

              ω

                0

              )

                2

    {\displaystyle \Omega ={\sqrt {\Omega _{0}^{2}+(\omega -\omega _{0})^{2}}}}

where

          Ω

            0

          V

            a
            b

          /

        2
        ℏ

    {\displaystyle \Omega {0}=|V{ab}/2\hbar |}

 is the on-resonance Rabi frequency.

Bloch–Siegert shift
Consider the effect due to the counter-rotating field. In the counter-rotating frame (

          ω

              c
              r

        −
        ω

    {\displaystyle \omega _{\mathrm {cr} }=-\omega }

), the effective detuning is

        Δ

          ω

              c
              r

        ω
        +

          ω

            0

    {\displaystyle \Delta \omega _{\mathrm {cr} }=\omega +\omega _{0}}

 and the counter-rotating field adds a driving component perpendicular to the detuning, with equal amplitude

          Ω

            0

    {\displaystyle \Omega _{0}}

.
The counter-rotating field effectively dresses the system, where we can define a new quantization axis slightly tilted from the original one, with an effective detuning

        Δ

          ω

              e
              f
              f

        ±

              Ω

                0

                2

            +
            (
            ω
            +

              ω

                0

              )

                2

    {\displaystyle \Delta \omega _{\mathrm {eff} }=\pm {\sqrt {\Omega _{0}^{2}+(\omega +\omega _{0})^{2}}}}

Therefore, the resonance frequency (

          ω

              r
              e
              s

    {\displaystyle \omega _{\mathrm {res} }}

) of the system dressed by the counter-rotating field is

        Δ

          ω

              e
              f
              f

    {\displaystyle \Delta \omega _{\mathrm {eff} }}

 away from our frame of reference, which is rotating at

        −
        ω

    {\displaystyle -\omega }

          ω

              r
              e
              s

        +
        ω

        ±

              Ω

                0

                2

            +
            (
            ω
            +

              ω

                0

              )

                2

    {\displaystyle \omega _{\mathrm {res} }+\omega =\pm {\sqrt {\Omega _{0}^{2}+(\omega +\omega _{0})^{2}}}}

and there are two solutions for

          ω

              r
              e
              s

    {\displaystyle \omega _{\mathrm {res} }}

          ω

              r
              e
              s

          ω

            0

          [

            1
            +

                1
                4

                (

                      Ω

                        0

                      ω

                        0

                )

                2

          ]

    {\displaystyle \omega _{\mathrm {res} }=\omega _{0}\left[1+{\frac {1}{4}}\left({\frac {\Omega _{0}}{\omega _{0}}}\right)^{2}\right]}

and

          ω

              r
              e
              s

        −

            1
            3

          ω

            0

          [

            1
            +

                3
                4

                (

                      Ω

                        0

                      ω

                        0

                )

                2

          ]

        .

    {\displaystyle \omega _{\mathrm {res} }=-{\frac {1}{3}}\omega _{0}\left[1+{\frac {3}{4}}\left({\frac {\Omega _{0}}{\omega _{0}}}\right)^{2}\right].}

The shift from the RWA of the first solution is dominant, and the correction to

          ω

            0

    {\displaystyle \omega _{0}}

 is known as the Bloch–Siegert shift:

        δ

          ω

              B
              −
              S

            1
            4

              Ω

                0

                2

              ω

                0

    {\displaystyle \delta \omega _{\mathrm {B-S} }={\frac {1}{4}}{\frac {\Omega _{0}^{2}}{\omega _{0}}}}

The counter-rotating frequency gives rise to a population oscillation at

        2
        ω

    {\displaystyle 2\omega }

, with amplitude proportional to

        (
        Ω

          /

        ω
        )

    {\displaystyle (\Omega /\omega )}

, and phase that depends on the phase of the driving field. Such Bloch–Siegert oscillation may become relevant in spin flipping operations at high rate. This effect can be suppressed by using an off-resonant Λ transition.

Applications

NMR
When homonuclear nuclear magnetic resonance decoupling is performed, Bloch–Siegert shifts may become significant due to the strength of the homonuclear decoupling field. Direct measurement of the homonuclear decoupling mean field strength can be achieved by measuring the resulting Bloch–Siegert shift.

MRI
The Bloch–Siegert shift is currently being widely investigated a potential encoding mechanism for MRI. The first significant use of the phenomenon in the MR imaging community was to perform mapping of the RF transmit field, by using the imaging system to measure the spatial phase accrual produced by an off-resonant RF pulse. Since then, it has been recognized that Bloch–Siegert shifts can be used in MRI sequences within imaging systems with a transmit field gradient to provide slice selection, phase encoding, and frequency encoding. The motivation for this research is to provide an alternative to conventional

          B

            0

    {\displaystyle B_{0}}

 gradient encoding, which is currently used in clinical imaging systems but produces undesirable acoustic noise, peripheral nerve stimulation, and spatial design constraints.

AC-Stark shift
The AC-Stark shift is a similar shift in the resonance frequency, caused by a non-resonant field of the form

          H

              o
              r

              V

                  o
                  r

            2

        cos
        ⁡

          (

            ω

                o
                r

          t
          )

    {\displaystyle H_{\mathrm {or} }={\frac {V_{\mathrm {or} }}{2}}\cos {(\omega _{\mathrm {or} }t)}}

 perturbing the spin. It can be derived using a similar treatment as above, invoking the RWA on the off-resonant field. The resulting AC-Stark shift is:

        δ

          ω

              A
              C

            1
            2

              Ω

                  o
                  r

                2

              (

                ω

                  0

              −

                ω

                    o
                    r

              )

    {\displaystyle \delta \omega _{\mathrm {AC} }={\frac {1}{2}}{\frac {\Omega _{\mathrm {or} }^{2}}{(\omega _{0}-\omega _{\mathrm {or} })}}}

, with

          Ω

            o
            r

          V

            o
            r

          /

        2
        ℏ

    {\displaystyle \Omega {or}=|V{or}/2\hbar |}

.
