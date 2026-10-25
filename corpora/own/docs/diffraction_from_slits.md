# Diffraction from slits

Diffraction from slits

Diffraction processes affecting waves are amenable to quantitative description and analysis. Such treatments are applied to a wave passing through one or more slits whose width is specified as a proportion of the wavelength. Numerical approximations may be used, including the Fresnel and Fraunhofer approximations.

General diffraction
Because diffraction is the result of addition of all waves (of given wavelength) along all unobstructed paths, the usual procedure is to consider the contribution of an infinitesimally small neighborhood around a certain path (this contribution is usually called a wavelet) and then integrate over all paths (= add all wavelets) from the source to the detector (or given point on a screen).
Thus in order to determine the pattern produced by diffraction, the phase and the amplitude of each of the wavelets is calculated. That is, at each point in space we must determine the distance to each of the simple sources on the incoming wavefront. If the distance to each of the simple sources differs by an integer number of wavelengths, all the wavelets will be in phase, resulting in constructive interference. If the distance to each source is an integer plus one half of a wavelength, there will be complete destructive interference. Usually, it is sufficient to determine these minima and maxima to explain the observed diffraction effects.
The simplest descriptions of diffraction are those in which the situation can be reduced to a two-dimensional problem. For water waves, this is already the case, as water waves propagate only on the surface of the water. For light, we can often neglect one dimension if the diffracting object extends in that direction over a distance far greater than the wavelength. In the case of light shining through small circular holes we will have to take into account the full three-dimensional nature of the problem.
Several qualitative observations can be made of diffraction in general:

The angular spacing of the features in the diffraction pattern is inversely proportional to the dimensions of the object causing the diffraction. In other words: the smaller the diffracting object, the wider the resulting diffraction pattern, and vice versa. (More precisely, this is true of the sines of the angles.)
The diffraction angles are invariant under scaling; that is, they depend only on the ratio of the wavelength to the size of the diffracting object.
When the diffracting object has a periodic structure, for example in a diffraction grating, the features generally become sharper. The fourth figure, for example, shows a comparison of a double-slit pattern with a pattern formed by five slits, both sets of slits having the same spacing between the center of one slit and the next.

Approximations
The problem of calculating what a diffracted wave looks like, is the problem of determining the phase of each of the simple sources on the incoming wave front. It is mathematically easier to consider the case of far-field or Fraunhofer diffraction, where the point of observation is far from that of the diffracting obstruction, and as a result, involves less complex mathematics than the more general case of near-field or Fresnel diffraction. To make this statement more quantitative, consider a diffracting object at the origin that has a size

        a

    {\displaystyle a}

. For definiteness let us say we are diffracting light and we are interested in what the intensity looks like on a screen a distance

        L

    {\displaystyle L}

 away from the object. At some point on the screen the path length to one side of the object is given by the Pythagorean theorem

        S

              L

                2

            +
            (
            x
            +
            a

              /

            2

              )

                2

    {\displaystyle S={\sqrt {L^{2}+(x+a/2)^{2}}}}

If we now consider the situation where

        L
        ≫
        (
        x
        +
        a

          /

        2
        )

    {\displaystyle L\gg (x+a/2)}

, the path length becomes

        S
        ≈

          (

            L
            +

                  (
                  x
                  +
                  a

                    /

                  2

                    )

                      2

                  2
                  L

          )

        L
        +

              x

                2

              2
              L

        +

              x
              a

              2
              L

        +

              a

                2

              8
              L

    {\displaystyle S\approx \left(L+{\frac {(x+a/2)^{2}}{2L}}\right)=L+{\frac {x^{2}}{2L}}+{\frac {xa}{2L}}+{\frac {a^{2}}{8L}}}

This is the Fresnel approximation. To further simplify things: If the diffracting object is much smaller than the distance

        L

    {\displaystyle L}

, the last term will contribute much less than a wavelength to the path length, and will then not change the phase appreciably. That is

              a

                2

            L

        ≪
        λ

    {\displaystyle {\frac {a^{2}}{L}}\ll \lambda }

. The result is the Fraunhofer approximation, which is only valid very far away from the object

        S
        ≈
        L
        +

              x

                2

              2
              L

        +

              x
              a

              2
              L

    {\displaystyle S\approx L+{\frac {x^{2}}{2L}}+{\frac {xa}{2L}}}

Depending on the size of the diffraction object, the distance to the object and the wavelength of the wave, the Fresnel approximation, the Fraunhofer approximation or neither approximation may be valid. As the distance between the measured point of diffraction and the obstruction point increases, the diffraction patterns or results predicted converge towards those of Fraunhofer diffraction, which is more often observed in nature due to the extremely small wavelength of visible light.

Multiple narrow slits

A simple quantitative description

Multiple-slit arrangements can be mathematically considered as multiple simple wave sources, if the slits are narrow enough. For light, a slit is an opening that is infinitely extended in one dimension, and this has the effect of reducing a wave problem in 3D-space to a simpler problem in 2D-space.
The simplest case is that of two narrow slits, spaced a distance

        a

    {\displaystyle \ a}

 apart. To determine the maxima and minima in the amplitude we must determine the path difference to the first slit and to the second one. In the Fraunhofer approximation, with the observer far away from the slits, the difference in path length to the two slits can be seen from the image to be

        Δ
        S

          a

        sin
        ⁡
        θ

    {\displaystyle \Delta S={a}\sin \theta }

Maxima in the intensity occur if this path length difference is an integer number of wavelengths.

        a
        sin
        ⁡
        θ

        n
        λ

    {\displaystyle a\sin \theta =n\lambda }

where

        n

    {\displaystyle n}

 is an integer that labels the order of each maximum,

        λ

    {\displaystyle \lambda }

 is the wavelength,

        a

    {\displaystyle a}

 is the distance between the slits, and

        θ

    {\displaystyle \theta }

 is the angle at which constructive interference occurs.
The corresponding minima are at path differences of an integer number plus one half of the wavelength:

        a
        sin
        ⁡
        θ

        λ
        (
        n
        +
        1

          /

        2
        )

        .

    {\displaystyle a\sin \theta =\lambda (n+1/2)\,.}

For an array of slits, positions of the minima and maxima are not changed, the fringes visible on a screen however do become sharper, as can be seen in the image.

Mathematical description

To calculate this intensity pattern, one needs to introduce some more sophisticated methods. The mathematical representation of a radial wave is given by

        E
        (
        r
        )

        A
        cos
        ⁡
        (
        k
        r
        −
        ω
        t
        +
        ϕ
        )

          /

        r

    {\displaystyle E(r)=A\cos(kr-\omega t+\phi )/r}

where

        k

              2
              π

            λ

    {\displaystyle k={\frac {2\pi }{\lambda }}}

,

        λ

    {\displaystyle \lambda }

 is the wavelength,

        ω

    {\displaystyle \omega }

 is frequency of the wave and

        ϕ

    {\displaystyle \phi }

 is the phase of the wave at the slits at time t = 0. The wave at a screen some distance away from the plane of the slits is given by the sum of the waves emanating from each of the slits.
To make this problem a little easier, we introduce the complex wave

        Ψ

    {\displaystyle \Psi }

, the real part of which is equal to

        E

    {\displaystyle E}

        Ψ
        (
        r
        )

        A

          e

            i
            (
            k
            r
            −
            ω
            t
            +
            ϕ
            )

          /

        r

    {\displaystyle \Psi (r)=Ae^{i(kr-\omega t+\phi )}/r}

        E
        (
        r
        )

        Re
        ⁡
        (
        Ψ
        (
        r
        )
        )

    {\displaystyle E(r)=\operatorname {Re} (\Psi (r))}

The absolute value of this function gives the wave amplitude, and the complex phase of the function corresponds to the phase of the wave.

        Ψ

    {\displaystyle \Psi }

 is referred to as the complex amplitude.
With

        N

    {\displaystyle N}

 slits, the total wave at point

        x

    {\displaystyle \ x}

 on the screen is

          Ψ

            total

        A

          e

            i
            (
            −
            ω
            t
            +
            ϕ
            )

          ∑

            n

            0

            N
            −
            1

              e

                i
                k

                    (
                    x
                    −
                    n
                    a

                      )

                        2

                    +

                      L

                        2

                  (

                    x
                    −
                    n
                    a

                  )

                  2

              +

                L

                  2

        .

    {\displaystyle \Psi _{\text{total}}=Ae^{i(-\omega t+\phi )}\sum _{n=0}^{N-1}{\frac {e^{ik{\sqrt {(x-na)^{2}+L^{2}}}}}{\sqrt {\left(x-na\right)^{2}+L^{2}}}}.}

Since we are for the moment only interested in the amplitude and relative phase, we can ignore any overall phase factors that are not dependent on

        x

    {\displaystyle x}

 or

        n

    {\displaystyle n}

. We approximate

            (
            x
            −
            n
            a

              )

                2

            +

              L

                2

        ≈
        L
        +
        (
        x
        −
        n
        a

          )

            2

          /

        2
        L

    {\displaystyle {\sqrt {(x-na)^{2}+L^{2}}}\approx L+(x-na)^{2}/2L}

. In the Fraunhofer limit we can neglect terms of order

              a

                2

              2
              L

    {\displaystyle {\frac {a^{2}}{2L}}}

 in the exponential, and any terms involving

        a

          /

        L

    {\displaystyle a/L}

  or

        x

          /

        L

    {\displaystyle x/L}

 in the denominator. The sum becomes

        Ψ

        A

              e

                i

                  (

                    k
                    (

                          x

                            2

                          2
                          L

                    +
                    L
                    )
                    −
                    ω
                    t
                    +
                    ϕ

                  )

            L

          ∑

            n

            0

            N
            −
            1

          e

            −
            i
            k

                  x
                  n
                  a

                L

    {\displaystyle \Psi =A{\frac {e^{i\left(k({\frac {x^{2}}{2L}}+L)-\omega t+\phi \right)}}{L}}\sum _{n=0}^{N-1}e^{-ik{\frac {xna}{L}}}}

The sum has the form of a geometric sum and can be evaluated to give

        Ψ

        A

              e

                i

                  (

                    k
                    (

                            x

                              2

                          −
                          (
                          N
                          −
                          1
                          )
                          a
                          x

                          2
                          L

                    +
                    L
                    )
                    −
                    ω
                    t
                    +
                    ϕ

                  )

            L

              sin
              ⁡

                (

                      N
                      k
                      a
                      x

                      2
                      L

                )

              sin
              ⁡

                (

                      k
                      a
                      x

                      2
                      L

                )

    {\displaystyle \Psi =A{\frac {e^{i\left(k({\frac {x^{2}-(N-1)ax}{2L}}+L)-\omega t+\phi \right)}}{L}}{\frac {\sin \left({\frac {Nkax}{2L}}\right)}{\sin \left({\frac {kax}{2L}}\right)}}}

The intensity is given by the absolute value of the complex amplitude squared

        I
        (
        x
        )

        Ψ

          Ψ

            ∗

        Ψ

            2

          I

            0

            (

                  sin
                  ⁡

                    (

                          N
                          k
                          a
                          x

                          2
                          L

                    )

                  sin
                  ⁡

                    (

                          k
                          a
                          x

                          2
                          L

                    )

            )

            2

    {\displaystyle I(x)=\Psi \Psi ^{*}=|\Psi |^{2}=I_{0}\left({\frac {\sin \left({\frac {Nkax}{2L}}\right)}{\sin \left({\frac {kax}{2L}}\right)}}\right)^{2}}

where

          Ψ

            ∗

    {\displaystyle \Psi ^{*}}

 denotes the complex conjugate of

        Ψ

    {\displaystyle \Psi }

.

Single slit

As an example, an exact equation can now be derived for the intensity of the diffraction pattern as a function of angle in the case of single-slit diffraction.
A mathematical representation of Huygens' principle can be used to start an equation.
Consider a monochromatic complex plane wave

          Ψ

            ′

    {\displaystyle \Psi ^{\prime }}

 of wavelength λ incident on a slit of width a.
If the slit lies in the x′-y′ plane, with its center at the origin, then it can be assumed that diffraction generates a complex wave ψ, traveling radially in the r direction away from the slit, and this is given by:

        Ψ

          ∫

              s
              l
              i
              t

            i

              r
              λ

          Ψ

            ′

          e

            −
            i
            k
            r

        d

          s
          l
          i
          t

    {\displaystyle \Psi =\int _{\mathrm {slit} }{\frac {i}{r\lambda }}\Psi ^{\prime }e^{-ikr}\,d\mathrm {slit} }

Let (x′, y′, 0) be a point inside the slit over which it is being integrated. If (x, 0, z) is the location at which the intensity of the diffraction pattern is being computed, the slit extends from

          x
          ′

        −
        a

          /

        2

    {\displaystyle x'=-a/2}

 to

        +
        a

          /

        2

    {\displaystyle +a/2\,}

, and from

          y
          ′

        −
        ∞

    {\displaystyle y'=-\infty }

 to

        ∞

    {\displaystyle \infty }

.
The distance r from the slit is:

        r

                (

                  x
                  −

                    x

                      ′

                )

                2

            +

              y

                ′
                2

            +

              z

                2

    {\displaystyle r={\sqrt {\left(x-x^{\prime }\right)^{2}+y^{\prime 2}+z^{2}}}}

        r

        z

            (

              1
              +

                        (

                          x
                          −

                            x

                              ′

                        )

                        2

                    +

                      y

                        ′
                        2

                    z

                      2

            )

              1
              2

    {\displaystyle r=z\left(1+{\frac {\left(x-x^{\prime }\right)^{2}+y^{\prime 2}}{z^{2}}}\right)^{\frac {1}{2}}}

Assuming Fraunhofer diffraction will result in the conclusion

        z
        ≫

          (

            x
            −

              x

                ′

          )

    {\displaystyle z\gg {\big |}\left(x-x^{\prime }\right){\big |}}

. In other words, the distance to the target is much larger than the diffraction width on the target.
By the binomial expansion rule, ignoring terms quadratic and higher, the quantity on the right can be estimated to be:

        r
        ≈
        z

          (

            1
            +

                1
                2

                      (

                        x
                        −

                          x
                          ′

                      )

                      2

                  +

                    y

                      ′
                      2

                  z

                    2

          )

    {\displaystyle r\approx z\left(1+{\frac {1}{2}}{\frac {\left(x-x'\right)^{2}+y^{\prime 2}}{z^{2}}}\right)}

        r
        ≈
        z
        +

                  (

                    x
                    −

                      x
                      ′

                  )

                  2

              +

                y

                  ′
                  2

              2
              z

    {\displaystyle r\approx z+{\frac {\left(x-x'\right)^{2}+y^{\prime 2}}{2z}}}

It can be seen that 1/r in front of the equation is non-oscillatory, i.e. its contribution to the magnitude of the intensity is small compared to our exponential factors. Therefore, we will lose little accuracy by approximating it as 1/z.

                Ψ

                      i

                        Ψ
                        ′

                      z
                      λ

                  ∫

                    −

                        a
                        2

                      a
                      2

                  ∫

                    −
                    ∞

                    ∞

                  e

                    −
                    i
                    k

                      [

                        z
                        +

                                  (

                                    x
                                    −

                                      x
                                      ′

                                  )

                                  2

                              +

                                y

                                  ′
                                  2

                              2
                              z

                      ]

                d

                  y
                  ′

                d

                  x
                  ′

                      i

                        Ψ

                          ′

                      z
                      λ

                  e

                    −
                    i
                    k
                    z

                  ∫

                    −

                        a
                        2

                      a
                      2

                  e

                    −
                    i
                    k

                      [

                              (

                                x
                                −

                                  x
                                  ′

                              )

                              2

                            2
                            z

                      ]

                d

                  x

                    ′

                  ∫

                    −
                    ∞

                    ∞

                  e

                    −
                    i
                    k

                      [

                            y

                              ′
                              2

                            2
                            z

                      ]

                d

                  y
                  ′

                  Ψ

                    ′

                      i

                        z
                        λ

                  e

                        −
                        i
                        k

                          x

                            2

                        2
                        z

                  ∫

                    −

                        a
                        2

                      a
                      2

                  e

                        i
                        k
                        x

                          x
                          ′

                      z

                  e

                        −
                        i
                        k

                          x

                            ′
                            2

                        2
                        z

                d

                  x
                  ′

    {\displaystyle {\begin{aligned}\Psi &={\frac {i\Psi '}{z\lambda }}\int _{-{\frac {a}{2}}}^{\frac {a}{2}}\int _{-\infty }^{\infty }e^{-ik\left[z+{\frac {\left(x-x'\right)^{2}+y^{\prime 2}}{2z}}\right]}\,dy'\,dx'\&={\frac {i\Psi ^{\prime }}{z\lambda }}e^{-ikz}\int _{-{\frac {a}{2}}}^{\frac {a}{2}}e^{-ik\left[{\frac {\left(x-x'\right)^{2}}{2z}}\right]}\,dx^{\prime }\int _{-\infty }^{\infty }e^{-ik\left[{\frac {y^{\prime 2}}{2z}}\right]}\,dy'\&=\Psi ^{\prime }{\sqrt {\frac {i}{z\lambda }}}e^{\frac {-ikx^{2}}{2z}}\int _{-{\frac {a}{2}}}^{\frac {a}{2}}e^{\frac {ikxx'}{z}}e^{\frac {-ikx^{\prime 2}}{2z}}\,dx'\end{aligned}}}

To make things cleaner, a placeholder C is used to denote constants in the equation. It is important to keep in mind that C can contain imaginary numbers, thus the wave function will be complex. However, at the end, the ψ will be bracketed, which will eliminate any imaginary components.
Now, in Fraunhofer diffraction,

        k

          x

            ′
            2

          /

        z

    {\displaystyle kx^{\prime 2}/z}

 is small, so

          e

                −
                i
                k

                  x

                    ′
                    2

                2
                z

        ≈
        1

    {\displaystyle e^{\frac {-ikx^{\prime 2}}{2z}}\approx 1}

 (note that

          x

            ′

    {\displaystyle x^{\prime }}

 participates in this exponential and it is being integrated).
In contrast the term

          e

                −
                i
                k

                  x

                    2

                2
                z

    {\displaystyle e^{\frac {-ikx^{2}}{2z}}}

 can be eliminated from the equation, since when bracketed it gives 1.

          ⟨

              e

                    −
                    i
                    k

                      x

                        2

                    2
                    z

              e

                    −
                    i
                    k

                      x

                        2

                    2
                    z

          ⟩

          e

                −
                i
                k

                  x

                    2

                2
                z

            (

              e

                    −
                    i
                    k

                      x

                        2

                    2
                    z

            )

            ∗

          e

                −
                i
                k

                  x

                    2

                2
                z

          e

                +
                i
                k

                  x

                    2

                2
                z

          e

            0

        1

    {\displaystyle \left\langle e^{\frac {-ikx^{2}}{2z}}|e^{\frac {-ikx^{2}}{2z}}\right\rangle =e^{\frac {-ikx^{2}}{2z}}\left(e^{\frac {-ikx^{2}}{2z}}\right)^{*}=e^{\frac {-ikx^{2}}{2z}}e^{\frac {+ikx^{2}}{2z}}=e^{0}=1}

(For the same reason we have also eliminated the term

          e

            −
            i
            k
            z

    {\displaystyle e^{-ikz}}

)
Taking

        C

          Ψ

            ′

              i

                z
                λ

    {\displaystyle C=\Psi ^{\prime }{\sqrt {\frac {i}{z\lambda }}}}

 results in:

        Ψ

        C

          ∫

            −

                a
                2

              a
              2

          e

                i
                k
                x

                  x

                    ′

              z

        d

          x

            ′

        C

                e

                      i
                      k
                      a
                      x

                      2
                      z

              −

                e

                      −
                      i
                      k
                      a
                      x

                      2
                      z

                i
                k
                x

              z

    {\displaystyle \Psi =C\int _{-{\frac {a}{2}}}^{\frac {a}{2}}e^{\frac {ikxx^{\prime }}{z}}\,dx^{\prime }=C{\frac {e^{\frac {ikax}{2z}}-e^{\frac {-ikax}{2z}}}{\frac {ikx}{z}}}}

It can be noted through Euler's formula and its derivatives that

        sin
        ⁡
        x

                e

                  i
                  x

              −

                e

                  −
                  i
                  x

              2
              i

    {\displaystyle \sin x={\frac {e^{ix}-e^{-ix}}{2i}}}

and from the geometry that

        sin
        ⁡
        θ

            x
            z

    {\displaystyle \sin \theta ={\frac {x}{z}}}

.
Therefore, we have

        Ψ

        a
        C

              sin
              ⁡

                    k
                    a
                    sin
                    ⁡
                    θ

                  2

                k
                a
                sin
                ⁡
                θ

              2

        a
        C

          [

            sinc
            ⁡

              (

                    k
                    a
                    sin
                    ⁡
                    θ

                  2

              )

          ]

    {\displaystyle \Psi =aC{\frac {\sin {\frac {ka\sin \theta }{2}}}{\frac {ka\sin \theta }{2}}}=aC\left[\operatorname {sinc} \left({\frac {ka\sin \theta }{2}}\right)\right]}

where the (unnormalized) sinc function is defined by

        sinc
        ⁡
        (
        x
        )

                  d
                  e
                  f

              sin
              ⁡
              (
              x
              )

            x

    {\displaystyle \operatorname {sinc} (x)\ {\stackrel {\mathrm {def} }{=}}\ {\frac {\sin(x)}{x}}}

.
Now, substituting in

              2
              π

            λ

        k

    {\displaystyle {\frac {2\pi }{\lambda }}=k}

, the intensity (squared amplitude)

        I

    {\displaystyle I}

 of the diffracted waves at an angle θ is given by:

        I
        (
        θ
        )

          I

            0

              [

                sinc
                ⁡

                  (

                          π
                          a

                        λ

                    sin
                    ⁡
                    θ

                  )

              ]

            2

    {\displaystyle I(\theta )=I_{0}{\left[\operatorname {sinc} \left({\frac {\pi a}{\lambda }}\sin \theta \right)\right]}^{2}}

Multiple slits

Let us again start with the mathematical representation of Huygens' principle.

        Ψ

          ∫

              s
              l
              i
              t

            i

              r
              λ

          Ψ

            ′

          e

            −
            i
            k
            r

        d

          s
          l
          i
          t

    {\displaystyle \Psi =\int _{\mathrm {slit} }{\frac {i}{r\lambda }}\Psi ^{\prime }e^{-ikr}\,d\mathrm {slit} }

Consider

        N

    {\displaystyle N}

 slits in the prime plane of equal size

        a

    {\displaystyle a}

 and spacing

        d

    {\displaystyle d}

 spread along the

          x

            ′

    {\displaystyle x^{\prime }}

 axis. As above, the distance

        r

    {\displaystyle r}

 from slit 1 is:

        r

        z

            (

              1
              +

                        (

                          x
                          −

                            x

                              ′

                        )

                        2

                    +

                      y

                        ′
                        2

                    z

                      2

            )

              1
              2

    {\displaystyle r=z\left(1+{\frac {\left(x-x^{\prime }\right)^{2}+y^{\prime 2}}{z^{2}}}\right)^{\frac {1}{2}}}

To generalize this to

        N

    {\displaystyle N}

 slits, we make the observation that while

        z

    {\displaystyle z}

 and

        y

    {\displaystyle y}

 remain constant,

          x

            ′

    {\displaystyle x^{\prime }}

 shifts by

          x

            j

            0
            ⋯
            n
            −
            1

            ′

          x

            0

            ′

        −
        j
        d

    {\displaystyle x_{j=0\cdots n-1}^{\prime }=x_{0}^{\prime }-jd}

Thus

          r

            j

        z

            (

              1
              +

                        (

                          x
                          −

                            x

                              ′

                          −
                          j
                          d

                        )

                        2

                    +

                      y

                        ′
                        2

                    z

                      2

            )

              1
              2

    {\displaystyle r_{j}=z\left(1+{\frac {\left(x-x^{\prime }-jd\right)^{2}+y^{\prime 2}}{z^{2}}}\right)^{\frac {1}{2}}}

and the sum of all

        N

    {\displaystyle N}

 contributions to the wave function is:

        Ψ

          ∑

            j

            0

            N
            −
            1

        C

          ∫

            −

              a

              /

              2

              a

              /

              2

          e

                i
                k
                x

                  (

                      x
                      ′

                    −
                    j
                    d

                  )

              z

          e

                −
                i
                k

                    (

                        x
                        ′

                      −
                      j
                      d

                    )

                    2

                2
                z

        d

          x

            ′

    {\displaystyle \Psi =\sum _{j=0}^{N-1}C\int _{-{a}/{2}}^{{a}/{2}}e^{\frac {ikx\left(x'-jd\right)}{z}}e^{\frac {-ik\left(x'-jd\right)^{2}}{2z}}\,dx^{\prime }}

Again noting that

              k

                  (

                      x

                        ′

                    −
                    j
                    d

                  )

                  2

            z

    {\displaystyle {\frac {k\left(x^{\prime }-jd\right)^{2}}{z}}}

 is small, so

          e

                −
                i
                k

                    (

                        x
                        ′

                      −
                      j
                      d

                    )

                    2

                2
                z

        ≈
        1

    {\displaystyle e^{\frac {-ik\left(x'-jd\right)^{2}}{2z}}\approx 1}

, we have:

                Ψ

                C

                  ∑

                    j

                    0

                    N
                    −
                    1

                  ∫

                    −

                      a

                      /

                      2

                      a

                      /

                      2

                  e

                        i
                        k
                        x

                          (

                              x

                                ′

                            −
                            j
                            d

                          )

                      z

                d

                  x

                    ′

                a
                C

                  ∑

                    j

                    0

                    N
                    −
                    1

                      (

                          e

                                  i
                                  k
                                  a
                                  x

                                  2
                                  z

                            −

                                  i
                                  j
                                  k
                                  x
                                  d

                                z

                        −

                          e

                                  −
                                  i
                                  k
                                  a
                                  x

                                  2
                                  z

                            −

                                  i
                                  j
                                  k
                                  x
                                  d

                                z

                      )

                        2
                        i
                        k
                        a
                        x

                        2
                        z

                a
                C

                  ∑

                    j

                    0

                    N
                    −
                    1

                  e

                        i
                        j
                        k
                        x
                        d

                      z

                      (

                          e

                                i
                                k
                                a
                                x

                                2
                                z

                        −

                          e

                                −
                                i
                                k
                                a
                                x

                                2
                                z

                      )

                        2
                        i
                        k
                        a
                        x

                        2
                        z

                a
                C

                      sin
                      ⁡

                            k
                            a
                            sin
                            ⁡
                            θ

                          2

                        k
                        a
                        sin
                        ⁡
                        θ

                      2

                  ∑

                    j

                    0

                    N
                    −
                    1

                  e

                    i
                    j
                    k
                    d
                    sin
                    ⁡
                    θ

    {\displaystyle {\begin{aligned}\Psi &=C\sum _{j=0}^{N-1}\int _{-{a}/{2}}^{{a}/{2}}e^{\frac {ikx\left(x^{\prime }-jd\right)}{z}}\,dx^{\prime }\&=aC\sum _{j=0}^{N-1}{\frac {\left(e^{{\frac {ikax}{2z}}-{\frac {ijkxd}{z}}}-e^{{\frac {-ikax}{2z}}-{\frac {ijkxd}{z}}}\right)}{\frac {2ikax}{2z}}}\&=aC\sum _{j=0}^{N-1}e^{\frac {ijkxd}{z}}{\frac {\left(e^{\frac {ikax}{2z}}-e^{\frac {-ikax}{2z}}\right)}{\frac {2ikax}{2z}}}\&=aC{\frac {\sin {\frac {ka\sin \theta }{2}}}{\frac {ka\sin \theta }{2}}}\sum _{j=0}^{N-1}e^{ijkd\sin \theta }\end{aligned}}}

Now, we can use the following identity

          ∑

            j

            0

            N
            −
            1

          e

            x
            j

              1
              −

                e

                  N
                  x

              1
              −

                e

                  x

        .

    {\displaystyle \sum _{j=0}^{N-1}e^{xj}={\frac {1-e^{Nx}}{1-e^{x}}}.}

Substituting into our equation, we find:

                Ψ

                a
                C

                      sin
                      ⁡

                            k
                            a
                            sin
                            ⁡
                            θ

                          2

                        k
                        a
                        sin
                        ⁡
                        θ

                      2

                  (

                        1
                        −

                          e

                            i
                            N
                            k
                            d
                            sin
                            ⁡
                            θ

                        1
                        −

                          e

                            i
                            k
                            d
                            sin
                            ⁡
                            θ

                  )

                a
                C

                      sin
                      ⁡

                            k
                            a
                            sin
                            ⁡
                            θ

                          2

                        k
                        a
                        sin
                        ⁡
                        θ

                      2

                  (

                          e

                            −
                            i
                            N
                            k
                            d

                                  sin
                                  ⁡
                                  θ

                                2

                        −

                          e

                            i
                            N
                            k
                            d

                                  sin
                                  ⁡
                                  θ

                                2

                          e

                            −
                            i
                            k
                            d

                                  sin
                                  ⁡
                                  θ

                                2

                        −

                          e

                            i
                            k
                            d

                                  sin
                                  ⁡
                                  θ

                                2

                  )

                  (

                        e

                          i
                          N
                          k
                          d

                                sin
                                ⁡
                                θ

                              2

                        e

                          i
                          k
                          d

                                sin
                                ⁡
                                θ

                              2

                  )

                a
                C

                      sin
                      ⁡

                            k
                            a
                            sin
                            ⁡
                            θ

                          2

                        k
                        a
                        sin
                        ⁡
                        θ

                      2

                          e

                            −
                            i
                            N
                            k
                            d

                                  sin
                                  ⁡
                                  θ

                                2

                        −

                          e

                            i
                            N
                            k
                            d

                                  sin
                                  ⁡
                                  θ

                                2

                        2
                        i

                          e

                            −
                            i
                            k
                            d

                                  sin
                                  ⁡
                                  θ

                                2

                        −

                          e

                            i
                            k
                            d

                                  sin
                                  ⁡
                                  θ

                                2

                        2
                        i

                  (

                    e

                      i
                      (
                      N
                      −
                      1
                      )
                      k
                      d

                            sin
                            ⁡
                            θ

                          2

                  )

                a
                C

                      sin
                      ⁡

                        (

                              k
                              a
                              sin
                              ⁡
                              θ

                            2

                        )

                        k
                        a
                        sin
                        ⁡
                        θ

                      2

                      sin
                      ⁡

                        (

                              N
                              k
                              d
                              sin
                              ⁡
                              θ

                            2

                        )

                      sin
                      ⁡

                        (

                              k
                              d
                              sin
                              ⁡
                              θ

                            2

                        )

                  e

                    i

                      (

                        N
                        −
                        1

                      )

                    k
                    d

                          sin
                          ⁡
                          θ

                        2

    {\displaystyle {\begin{aligned}\Psi &=aC{\frac {\sin {\frac {ka\sin \theta }{2}}}{\frac {ka\sin \theta }{2}}}\left({\frac {1-e^{iNkd\sin \theta }}{1-e^{ikd\sin \theta }}}\right)\[1ex]&=aC{\frac {\sin {\frac {ka\sin \theta }{2}}}{\frac {ka\sin \theta }{2}}}\left({\frac {e^{-iNkd{\frac {\sin \theta }{2}}}-e^{iNkd{\frac {\sin \theta }{2}}}}{e^{-ikd{\frac {\sin \theta }{2}}}-e^{ikd{\frac {\sin \theta }{2}}}}}\right)\left({\frac {e^{iNkd{\frac {\sin \theta }{2}}}}{e^{ikd{\frac {\sin \theta }{2}}}}}\right)\[1ex]&=aC{\frac {\sin {\frac {ka\sin \theta }{2}}}{\frac {ka\sin \theta }{2}}}{\frac {\frac {e^{-iNkd{\frac {\sin \theta }{2}}}-e^{iNkd{\frac {\sin \theta }{2}}}}{2i}}{\frac {e^{-ikd{\frac {\sin \theta }{2}}}-e^{ikd{\frac {\sin \theta }{2}}}}{2i}}}\left(e^{i(N-1)kd{\frac {\sin \theta }{2}}}\right)\[1ex]&=aC{\frac {\sin \left({\frac {ka\sin \theta }{2}}\right)}{\frac {ka\sin \theta }{2}}}{\frac {\sin \left({\frac {Nkd\sin \theta }{2}}\right)}{\sin \left({\frac {kd\sin \theta }{2}}\right)}}e^{i\left(N-1\right)kd{\frac {\sin \theta }{2}}}\end{aligned}}}

We now make our

        k

    {\displaystyle k}

 substitution as before and represent all non-oscillating constants by the

          I

            0

    {\displaystyle I_{0}}

 variable as in the 1-slit diffraction and bracket the result. Remember that

          ⟨

              e

                i
                x

              e

                i
                x

          ⟩

          e

            0

        1

    {\displaystyle \left\langle e^{ix}{\Big |}e^{ix}\right\rangle =e^{0}=1}

This allows us to discard the tailing exponent and we have our answer:

        I

          (
          θ
          )

          I

            0

            [

              sinc
              ⁡

                (

                        π
                        a

                      λ

                  sin
                  ⁡
                  θ

                )

            ]

            2

        ⋅

            [

                  sin
                  ⁡

                    (

                            N
                            π
                            d

                          λ

                      sin
                      ⁡
                      θ

                    )

                  sin
                  ⁡

                    (

                            π
                            d

                          λ

                      sin
                      ⁡
                      θ

                    )

            ]

            2

    {\displaystyle I\left(\theta \right)=I_{0}\left[\operatorname {sinc} \left({\frac {\pi a}{\lambda }}\sin \theta \right)\right]^{2}\cdot \left[{\frac {\sin \left({\frac {N\pi d}{\lambda }}\sin \theta \right)}{\sin \left({\frac {\pi d}{\lambda }}\sin \theta \right)}}\right]^{2}}

General case for far field
The following section uses a more mathematical approach where treating the problem as a summation over the spherical waves mentioned earlier is derived from the relevant wave equation; see for instance Born and Wolf for details. The wave that emerges from a point source has amplitude

        ψ

    {\displaystyle \psi }

 at location

          r

    {\displaystyle \mathbf {r} }

 that is given by the solution of the frequency domain wave equation for a point source (the Helmholtz equation),

          ∇

            2

        ψ
        +

          k

            2

        ψ

        δ
        (

          r

        )
        ,

    {\displaystyle \nabla ^{2}\psi +k^{2}\psi =\delta (\mathbf {r} ),}

where

        δ
        (

          r

        )

    {\displaystyle \delta (\mathbf {r} )}

 is the 3-dimensional delta function. The delta function has only radial dependence, so the Laplace operator (a.k.a. scalar Laplacian) in the spherical coordinate system simplifies to

          ∇

            2

        ψ

            1
            r

              ∂

                2

              ∂

                r

                  2

        (
        r
        ψ
        )
        .

    {\displaystyle \nabla ^{2}\psi ={\frac {1}{r}}{\frac {\partial ^{2}}{\partial r^{2}}}(r\psi ).}

(See del in cylindrical and spherical coordinates.) By direct substitution, the solution to this equation can be readily shown to be the scalar Green's function, which in the spherical coordinate system (and using the physics time convention

          e

            −
            i
            ω
            t

    {\displaystyle e^{-i\omega t}}

) is

        ψ
        (
        r
        )

              e

                i
                k
                r

              4
              π
              r

        .

    {\displaystyle \psi (r)={\frac {e^{ikr}}{4\pi r}}.}

which is a spherical wave emanating from the origin. This solution assumes that the delta function source is located at the origin. If the source is located at an arbitrary source point, denoted by the vector

            r

          ′

    {\displaystyle \mathbf {r} '}

 and the field point is located at the point

          r

    {\displaystyle \mathbf {r} }

, then we may represent the scalar Green's function (for arbitrary source location) as

        ψ
        (

          r

            r

          ′

        )

              e

                i
                k

                  r

                −

                    r

                  ′

              4
              π

                r

              −

                  r

                ′

        .

    {\displaystyle \psi (\mathbf {r} |\mathbf {r} ')={\frac {e^{ik|\mathbf {r} -\mathbf {r} '|}}{4\pi |\mathbf {r} -\mathbf {r} '|}}.}

Therefore, if an electric field

          E

              i
              n
              c

        (
        x
        ,
        y
        )

    {\displaystyle E_{\mathrm {inc} }(x,y)}

 is incident on the aperture, the field produced by this aperture distribution is given by the surface integral

        Ψ
        (
        r
        )
        ∝

          ∬

              a
              p
              e
              r
              t
              u
              r
              e

          E

              i
              n
              c

        (

          x
          ′

        ,

          y
          ′

        )

              e

                i
                k

                  r

                −

                    r

                  ′

              4
              π

                r

              −

                  r

                ′

        d

          x
          ′

        d

          y
          ′

        ,

    {\displaystyle \Psi (r)\propto \iint \limits {\mathrm {aperture} }!!E{\mathrm {inc} }(x',y')~{\frac {e^{ik|\mathbf {r} -\mathbf {r} '|}}{4\pi |\mathbf {r} -\mathbf {r} '|}}\,dx'\,dy',}

where the source point in the aperture is given by the vector

            r

          ′

          x
          ′

              x
              ^

        +

          y
          ′

              y
              ^

        .

    {\displaystyle \mathbf {r} '=x'\mathbf {\hat {x}} +y'\mathbf {\hat {y}} .}

In the far field, wherein the parallel rays approximation can be employed, the Green's function,

        ψ
        (

          r

            r

          ′

        )

              e

                i
                k

                  r

                −

                    r

                  ′

              4
              π

                r

              −

                  r

                ′

        ,

    {\displaystyle \psi (\mathbf {r} |\mathbf {r} ')={\frac {e^{ik|\mathbf {r} -\mathbf {r} '|}}{4\pi |\mathbf {r} -\mathbf {r} '|}},}

simplifies to

        ψ
        (

          r

            r

          ′

        )

              e

                i
                k
                r

              4
              π
              r

          e

            −
            i
            k
            (

                r

              ′

            ⋅

                  r
                  ^

            )

    {\displaystyle \psi (\mathbf {r} |\mathbf {r} ')={\frac {e^{ikr}}{4\pi r}}e^{-ik(\mathbf {r} '\cdot \mathbf {\hat {r}} )}}

as can be seen in the adjacent figure.
The expression for the far-zone (Fraunhofer region) field becomes

        Ψ
        (
        r
        )
        ∝

              e

                i
                k
                r

              4
              π
              r

          ∬

              a
              p
              e
              r
              t
              u
              r
              e

          E

              i
              n
              c

        (

          x
          ′

        ,

          y
          ′

        )

          e

            −
            i
            k
            (

                r

              ′

            ⋅

                  r
                  ^

            )

        d

          x
          ′

        d

          y
          ′

        .

    {\displaystyle \Psi (r)\propto {\frac {e^{ikr}}{4\pi r}}\iint \limits {\mathrm {aperture} }!!E{\mathrm {inc} }(x',y')e^{-ik(\mathbf {r} '\cdot \mathbf {\hat {r}} )}\,dx'\,dy'.}

Now, since

            r

          ′

          x
          ′

              x
              ^

        +

          y
          ′

              y
              ^

    {\displaystyle \mathbf {r} '=x'\mathbf {\hat {x}} +y'\mathbf {\hat {y}} }

and

              r
              ^

        sin
        ⁡
        θ
        cos
        ⁡
        ϕ

              x
              ^

        +
        sin
        ⁡
        θ

        sin
        ⁡
        ϕ

              y
              ^

        +
        cos
        ⁡
        θ

              z
              ^

        ,

    {\displaystyle \mathbf {\hat {r}} =\sin \theta \cos \phi \mathbf {\hat {x}} +\sin \theta ~\sin \phi ~\mathbf {\hat {y}} +\cos \theta \mathbf {\hat {z}} ,}

the expression for the Fraunhofer region field from a planar aperture now becomes

        Ψ
        (
        r
        )
        ∝

              e

                i
                k
                r

              4
              π
              r

          ∬

              a
              p
              e
              r
              t
              u
              r
              e

          E

              i
              n
              c

        (

          x
          ′

        ,

          y
          ′

        )

          e

            −
            i
            k
            sin
            ⁡
            θ
            (
            cos
            ⁡
            ϕ

              x
              ′

            +
            sin
            ⁡
            ϕ

              y
              ′

            )

        d

          x
          ′

        d

          y
          ′

        .

    {\displaystyle \Psi (r)\propto {\frac {e^{ikr}}{4\pi r}}\iint \limits {\mathrm {aperture} }!!E{\mathrm {inc} }(x',y')e^{-ik\sin \theta (\cos \phi x'+\sin \phi y')}\,dx'\,dy'.}

Letting

          k

            x

        k
        sin
        ⁡
        θ
        cos
        ⁡
        ϕ

    {\displaystyle k_{x}=k\sin \theta \cos \phi }

and

          k

            y

        k
        sin
        ⁡
        θ
        sin
        ⁡
        ϕ

        ,

    {\displaystyle k_{y}=k\sin \theta \sin \phi \,,}

the Fraunhofer region field of the planar aperture assumes the form of a Fourier transform

        Ψ
        (
        r
        )
        ∝

              e

                i
                k
                r

              4
              π
              r

          ∬

              a
              p
              e
              r
              t
              u
              r
              e

          E

              i
              n
              c

        (

          x
          ′

        ,

          y
          ′

        )

          e

            −
            i
            (

              k

                x

              x
              ′

            +

              k

                y

              y
              ′

            )

        d

          x
          ′

        d

          y
          ′

        ,

    {\displaystyle \Psi (r)\propto {\frac {e^{ikr}}{4\pi r}}\iint \limits {\mathrm {aperture} }!!E{\mathrm {inc} }(x',y')e^{-i(k_{x}x'+k_{y}y')}\,dx'\,dy',}

In the far-field / Fraunhofer region, this becomes the spatial Fourier transform of the aperture distribution. Huygens' principle when applied to an aperture simply says that the far-field diffraction pattern is the spatial Fourier transform of the aperture shape, and this is a direct by-product of using the parallel-rays approximation, which is identical to doing a plane wave decomposition of the aperture plane fields (see Fourier optics).
In the far field, where r is essentially constant, then the equation:

        Ψ

          ∫

              s
              l
              i
              t

            i

              r
              λ

          Ψ

            ′

          e

            −
            i
            k
            r

        d

          s
          l
          i
          t

    {\displaystyle \Psi =\int _{\mathrm {slit} }{\frac {i}{r\lambda }}\Psi ^{\prime }e^{-ikr}\,d\mathrm {slit} }

is equivalent to doing a Fourier transform on the gaps in the barrier.
