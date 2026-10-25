# N-slit interferometric equation

N-slit interferometric equation

Quantum mechanics was first applied to optics, and interference in particular, by Paul Dirac. Richard Feynman, in his Lectures on Physics, uses Dirac's notation to describe thought experiments on double-slit interference of electrons. Feynman's approach was extended to N-slit interferometers for either single-photon illumination, or narrow-linewidth laser illumination, that is, illumination by indistinguishable photons, by Frank Duarte. The N-slit interferometer was first applied in the generation and measurement of complex interference patterns.
In this article the generalized N-slit interferometric equation, derived via Dirac's notation, is described. Although originally derived to reproduce and predict N-slit interferograms, this equation also has applications to other areas of optics.

Probability amplitudes and the N-slit interferometric equation

In this approach the probability amplitude for the propagation of a photon from a source s to an interference plane x, via an array of slits j, is given using Dirac's bra–ket notation as

        ⟨
        x

        s
        ⟩

          ∑

            j

            1

              N

        ⟨
        x

        j
        ⟩
        ⟨
        j

        s
        ⟩

    {\displaystyle \langle x|s\rangle =\sum _{j=1}^{\mathbb {N} }\langle x|j\rangle \langle j|s\rangle }

This equation represents the probability amplitude of a photon propagating from s to x via an array of j slits. Using a wavefunction representation for probability amplitudes, and defining the probability amplitudes as

                ⟨
                j

                s
                ⟩

                Ψ

                  (

                    r

                      j
                      ,
                      s

                  )

                  e

                    −
                    i

                      θ

                        j

                ⟨
                x

                j
                ⟩

                Ψ

                  (

                    r

                      x
                      ,
                      j

                  )

                  e

                    −
                    i

                      ϕ

                        j

    {\displaystyle {\begin{aligned}\langle j|s\rangle &=\Psi \left(r_{j,s}\right)e^{-i\theta {j}}\\langle x|j\rangle &=\Psi \left(r{x,j}\right)e^{-i\phi _{j}}\end{aligned}}}

where θj and Φj are the incidence and diffraction phase angles, respectively. Thus, the overall probability amplitude can be rewritten as

        ⟨
        x

        s
        ⟩

          ∑

            j

            1

            N

        Ψ

          (

            r

              j

          )

          e

            −
            i

              Ω

                j

    {\displaystyle \langle x|s\rangle =\sum {j=1}^{N}\Psi \left(r{j}\right)e^{-i\Omega _{j}}}

where

        Ψ

          (

            r

              j

          )

        Ψ

          (

            r

              x
              ,
              j

          )

        Ψ

          (

            r

              j
              ,
              s

          )

    {\displaystyle \Psi \left(r_{j}\right)=\Psi \left(r_{x,j}\right)\Psi \left(r_{j,s}\right)}

and

          Ω

            j

          θ

            j

        +

          ϕ

            j

    {\displaystyle \Omega _{j}=\theta _{j}+\phi _{j}}

after some algebra, the corresponding probability becomes

        ⟨
        x

        s
        ⟩

            2

          ∑

            j

            1

            N

        Ψ

            (

              r

                j

            )

            2

        +
        2

          ∑

            j

            1

            N

        Ψ

          (

            r

              j

          )

          (

              ∑

                m

                j
                +
                1

                N

            Ψ

              (

                r

                  m

              )

            cos
            ⁡

              (

                  Ω

                    m

                −

                  Ω

                    j

              )

          )

    {\displaystyle {\big |}\langle x|s\rangle {\big |}^{2}=\sum {j=1}^{N}\Psi \left(r{j}\right)^{2}+2\sum {j=1}^{N}\Psi \left(r{j}\right)\left(\sum {m=j+1}^{N}\Psi \left(r{m}\right)\cos \left(\Omega _{m}-\Omega _{j}\right)\right)}

where N is the total number of slits in the array, or transmission grating, and the term in parentheses represents the phase that is directly related to the exact path differences derived from the geometry of the N-slit array (j), the intra interferometric distance, and the interferometric plane x. In its simplest version, the phase term can be related to the geometry using

        cos
        ⁡
        (

          Ω

            m

        −

          Ω

            j

        )

        cos
        ⁡
        k

          L

            m

        −

          L

            m
            −
            1

    {\displaystyle \cos(\Omega _{m}-\Omega {j})=\cos k|L{m}-L_{m-1}|}

where k is the wavenumber, and Lm and Lm − 1 represent the exact path differences. Here the Dirac–Duarte (DD) interferometric equation is a probability distribution that is related to the intensity distribution measured experimentally. The calculations are performed numerically.
The DD interferometric equation applies to the propagation of a single photon, or the propagation of an ensemble of indistinguishable photons, and enables the accurate prediction of measured N-slit interferometric patterns continuously from the near to the far field. Interferograms generated with this equation have been shown to compare well with measured interferograms for both even (N = 2, 4, 6...) and odd (N = 3, 5, 7...) values of N from 2 to 1600.

Applications
At a practical level, the N-slit interferometric equation was introduced for imaging applications and is routinely applied to predict N-slit laser interferograms, both in the near and far field. Thus, it has become a valuable tool in the alignment of large, and very large, N-slit laser interferometers used in the study of clear air turbulence and the propagation of interferometric characters for secure laser communications in space. Other analytical applications are described below.

Generalized diffraction and refraction
The N-slit interferometric equation has been applied to describe classical phenomena such as interference, diffraction, refraction (Snell's law), and reflection, in a rational and unified approach, using quantum mechanics principles. In particular, this interferometric approach has been used to derive generalized refraction equations for both positive and negative refraction, thus providing a clear link between diffraction theory and generalized refraction.
From the phase term, of the interferometric equation, the expression

          d

            m

          (

            ±

              n

                1

            sin
            ⁡

                θ

                  m

            ±

              n

                2

            sin
            ⁡

                ϕ

                  m

          )

          (

                2
                π

              λ

          )

        M
        π

    {\displaystyle d_{m}\left(\pm n_{1}\sin {\theta {m}}\pm n{2}\sin {\phi _{m}}\right)\left({\frac {2\pi }{\lambda }}\right)=M\pi }

can be obtained, where M = 0, 2, 4....
For n1 = n2, this equation can be written as

          d

            m

          (

            ±
            sin
            ⁡

                θ

                  m

            ±
            sin
            ⁡

                ϕ

                  m

          )

        m
        λ

    {\displaystyle d_{m}\left(\pm \sin {\theta _{m}}\pm \sin {\phi _{m}}\right)=m\lambda }

which is the generalized diffraction grating equation. Here, θm is the angle of incidence, φm is the angle of diffraction, λ is the wavelength, and m = 0, 1, 2... is the order of diffraction.
Under certain conditions, dm ≪ λ, which can be readily obtained experimentally, the phase term becomes

          (

            ±

              n

                1

            sin
            ⁡

                θ

                  m

            ±

              n

                2

            sin
            ⁡

                ϕ

                  m

          )

        0

    {\displaystyle \left(\pm n_{1}\sin {\theta {m}}\pm n{2}\sin {\phi _{m}}\right)=0}

which is the generalized refraction equation, where θm is the angle of incidence, and φm now becomes the angle of refraction.

Cavity linewidth equation
Furthermore, the N-slit interferometric equation has been applied to derive the cavity linewidth equation applicable to dispersive oscillators, such as the multiple-prism grating laser oscillators:

        Δ
        λ
        ≈
        Δ
        θ

            (

                  ∂
                  Θ

                  ∂
                  λ

            )

            −
            1

    {\displaystyle \Delta \lambda \approx \Delta \theta \left({\frac {\partial \Theta }{\partial \lambda }}\right)^{-1}}

In this equation, Δθ is the beam divergence and the overall intracavity angular dispersion is the quantity in parentheses.

Fourier transform imaging
Researchers working on Fourier-transform ghost imaging consider the N-slit interferometric equation as an avenue to investigate the quantum nature of ghost imaging. Also, the N-slit interferometric approach is one of several approaches applied to describe basic optical phenomena in a cohesive and unified manner.
Note: given the various terminologies in use, for N-slit interferometry, it should be made explicit that the N-slit interferometric equation applies to two-slit interference, three-slit interference, four-slit interference, etc.

Quantum entanglement
The Dirac principles and probabilistic methodology used to derive the N-slit interferometric equation have also been used to derive the polarization quantum entanglement probability amplitude

          ψ
          ⟩

            1

              2

            (

            x
            ⟩

            1

            y
            ⟩

            2

        −

            y
            ⟩

            1

            x
            ⟩

            2

            )

    {\displaystyle \left|\psi \right\rangle ={\frac {1}{\sqrt {2}}}{\bigl (}\left|x\right\rangle _{1}\left|y\right\rangle _{2}-\left|y\right\rangle _{1}\left|x\right\rangle _{2}{\bigr )}}

and corresponding probability amplitudes depicting the propagation of multiple pairs of quanta.

Comparison with classical methods
A comparison of the Dirac approach with classical methods, in the performance of interferometric calculations, has been done by Travis S. Taylor et al. These authors concluded that the interferometric equation, derived via the Dirac formalism, was advantageous in the very near field.
Some differences between the DD interferometric equation and classical formalisms can be summarized as follows:

The classical Fresnel approach is used for near-field applications and the classical Fraunhofer approach is used for far-field applications. That division is not necessary when using the DD interferometric approach as this formalism applies to both the near and the far-field cases.
The Fraunhofer approach works for plane-wave illumination. The DD approach works for both, plane wave illumination or highly diffractive illumination patterns.
The DD interferometric equation is statistical in character. This is not the case of the classical formulations.
So far there has been no published comparison with more general classical approaches based on the Huygens–Fresnel principle or Kirchhoff's diffraction formula.
