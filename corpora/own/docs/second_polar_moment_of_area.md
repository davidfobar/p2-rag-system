# Second polar moment of area

Second polar moment of area

The second polar moment of area, also known as "polar moment of inertia" or even "moment of inertia", is a quantity used to describe resistance to torsional deformation (deflection), in objects (or segments of an object) with an invariant cross-section and no significant warping or out-of-plane deformation. It is a constituent of the second moment of area, linked through the perpendicular axis theorem. Where the planar second moment of area describes an object's resistance to deflection (bending) when subjected to a force applied to a plane parallel to the central axis, the polar second moment of area describes an object's resistance to deflection when subjected to a moment applied in a plane perpendicular to the object's central axis (i.e. parallel to the cross-section). Similar to planar second moment of area calculations (

          I

            x

    {\displaystyle I_{x}}

,

          I

            y

    {\displaystyle I_{y}}

, and

          I

            x
            y

    {\displaystyle I_{xy}}

), the polar second moment of area is often denoted as

          I

            z

    {\displaystyle I_{z}}

. While several engineering textbooks and academic publications also denote it as

        J

    {\displaystyle J}

 or

          J

            z

    {\displaystyle J_{z}}

, this designation should be given careful attention so that it does not become confused with the torsion constant,

          J

            t

    {\displaystyle J_{t}}

, used for non-cylindrical objects.
Simply put, the polar moment of area is a shaft or beam's resistance to being distorted by torsion, as a function of its shape. The rigidity comes from the object's cross-sectional area only, and does not depend on its material composition or shear modulus. The greater the magnitude of the second polar moment of area, the greater the torsional stiffness of the object.

Definition

The equation describing the polar moment of area is a multiple integral over the cross-sectional area,

        A

    {\displaystyle A}

, of the object.

        J

          ∬

            A

          r

            2

        d
        A

    {\displaystyle J=\iint _{A}r^{2}\,dA}

where

        r

    {\displaystyle r}

 is the distance to the element

        d
        A

    {\displaystyle dA}

.
Substituting the

        x

    {\displaystyle x}

 and

        y

    {\displaystyle y}

 components, using the Pythagorean theorem:

        J

          ∬

            A

          (

              x

                2

            +

              y

                2

          )

        d
        x

        d
        y

    {\displaystyle J=\iint _{A}\left(x^{2}+y^{2}\right)dx\,dy}

        J

          ∬

            A

          x

            2

        d
        x

        d
        y
        +

          ∬

            A

          y

            2

        d
        x

        d
        y

    {\displaystyle J=\iint _{A}x^{2}\,dx\,dy+\iint _{A}y^{2}\,dx\,dy}

Given the planar second moments of area equations, where:

          I

            x

          ∬

            A

          y

            2

        d
        x

        d
        y

    {\displaystyle I_{x}=\iint _{A}y^{2}dx\,dy}

          I

            y

          ∬

            A

          x

            2

        d
        x

        d
        y

    {\displaystyle I_{y}=\iint _{A}x^{2}dx\,dy}

It is shown that the polar moment of area can be described as the summation of the

        x

    {\displaystyle x}

 and

        y

    {\displaystyle y}

 planar moments of area,

          I

            x

    {\displaystyle I_{x}}

 and

          I

            y

    {\displaystyle I_{y}}

        ∴
        J

          I

            z

          I

            x

        +

          I

            y

    {\displaystyle \therefore J=I_{z}=I_{x}+I_{y}}

This is also shown in the perpendicular axis theorem. For objects that have rotational symmetry, such as a cylinder or hollow tube, the equation can be simplified to:

        J

        2

          I

            x

    {\displaystyle J=2I_{x}}

 or

        J

        2

          I

            y

    {\displaystyle J=2I_{y}}

For a circular section with radius

        R

    {\displaystyle R}

:

          I

            z

          ∫

            0

            2
            π

          ∫

            0

            R

          r

            2

        (
        r

        d
        r

        d
        ϕ
        )

              π

                R

                  4

            2

    {\displaystyle I_{z}=\int _{0}^{2\pi }\int _{0}^{R}r^{2}(r\,dr\,d\phi )={\frac {\pi R^{4}}{2}}}

Unit
The SI unit for polar second moment of area, like the planar second moment of area, is meters to the fourth power (m4), and inches to the fourth power (in4) in U.S. Customary units and imperial units.

Limitations
The polar second moment of area can be insufficient for use to analyze beams and shafts with non-circular cross-sections, due their tendency to warp when twisted, causing out-of-plane deformations. In such cases, a torsion constant should be substituted, where an appropriate deformation constant is included to compensate for the warping effect. Within this, there are articles that differentiate between the polar second moment of area,

          I

            z

    {\displaystyle I_{z}}

, and the torsional constant,

          J

            t

    {\displaystyle J_{t}}

, no longer using

        J

    {\displaystyle J}

 to describe the polar second moment of area.
In objects with significant cross-sectional variation (along the axis of the applied torque), which cannot be analyzed in segments, a more complex approach may have to be used. See 3-D elasticity.

Application
Though the polar second moment of area is most often used to calculate the angular displacement of an object subjected to a moment (torque) applied parallel to the cross-section, the provided value of rigidity does not have any bearing on the torsional resistance provided to an object as a function of its constituent materials. The rigidity provided by an object's material is a characteristic of its shear modulus,

        G

    {\displaystyle G}

. Combining these two features with the length of the shaft,

        L

    {\displaystyle L}

, one is able to calculate a shaft's angular deflection,

        θ

    {\displaystyle \theta }

, due to the applied torque,

        T

    {\displaystyle T}

:

        θ

              T
              L

              J
              G

    {\displaystyle \theta ={\frac {TL}{JG}}}

As shown, the larger the material's shear modulus and polar second moment of area (i.e. larger cross-sectional area), the greater resistance to torsional deflection.
The polar second moment of area appears in the formulae that describe torsional stress and angular displacement.
Torsional stresses:

        τ

              T

              r

              J

                z

    {\displaystyle \tau ={\frac {T\,r}{J_{z}}}}

where

        τ

    {\displaystyle \tau }

 is the torsional shear stress,

        T

    {\displaystyle T}

 is the applied torque,

        r

    {\displaystyle r}

 is the distance from the central axis, and

          J

            z

    {\displaystyle J_{z}}

 is the polar second moment of area.
Note: In a circular shaft, the shear stress is maximal at the surface of the shaft.

Sample calculation

Calculation of the steam turbine shaft radius for a turboset:
Assumptions:

Power carried by the shaft is 1000 MW; this is typical for a large nuclear power plant.
Yield stress of the steel used to make the shaft (τyield) is: 250 × 106 N/m2.
Electricity has a frequency of 50 Hz; this is the typical frequency in Europe. In North America the frequency is 60 Hz. This is assuming that there is a 1:1 correlation between rotational velocity of turbine and the frequency of mains power.
The angular frequency can be calculated with the following formula:

        ω

        2
        π
        f

    {\displaystyle \omega =2\pi f}

The torque carried by the shaft is related to the power by the following equation:

        P

        T
        ω

    {\displaystyle P=T\omega }

The angular frequency is therefore 314.16 rad/s and the torque 3.1831 × 106 N·m.
The maximal torque is:

          T

            max

                τ

                  max

                J

                  z

            r

    {\displaystyle T_{\max }={\frac {\tau {\max }J{z}}{r}}}

After substitution of the polar second moment of area the following expression is obtained:

        r

                2

                  T

                    max

                π

                  τ

                    max

              3

    {\displaystyle r={\sqrt[{3}]{\frac {2T_{\max }}{\pi \tau _{\max }}}}}

The radius is r=0.200 m = 200 mm, or a diameter of 400 mm. If one adds a factor of safety of 5 and re-calculates the radius with the admissible stress equal to the τadm=τyield/5 the result is a radius of 0.343 m, or a diameter of 690 mm, the approximate size of a turboset shaft in a nuclear power plant.

Comparing polar second moments of area and moments of inertia (second moments of mass)

Hollow Cylinder
Polar second moment of area:

          I

            z

              π

                (

                    D

                      4

                  −

                    d

                      4

                )

            32

    {\displaystyle I_{z}={\frac {\pi \left(D^{4}-d^{4}\right)}{32}}}

Moment of inertia:

          I

            c

          I

            z

        ρ
        l

              π
              ρ
              l

                (

                    D

                      4

                  −

                    d

                      4

                )

            32

    {\displaystyle I_{c}=I_{z}\rho l={\frac {\pi \rho l\left(D^{4}-d^{4}\right)}{32}}}

Solid cylinder
Polar second moment of area

          I

            z

              π

                D

                  4

            32

    {\displaystyle I_{z}={\frac {\pi D^{4}}{32}}}

Moment of inertia

          I

            c

          I

            z

        ρ
        l

              π
              ρ
              l

                D

                  4

            32

    {\displaystyle I_{c}=I_{z}\rho l={\frac {\pi \rho lD^{4}}{32}}}

where:

        d

    {\displaystyle d}

 is the inner diameter in meters (m)

        D

    {\displaystyle D}

 is the outer diameter in meters (m)

          I

            c

    {\displaystyle I_{c}}

 is the moment of inertia in kg·m2

          I

            z

    {\displaystyle I_{z}}

 is the polar second moment of area in meters to the fourth power (m4)

        l

    {\displaystyle l}

 is the length of cylinder in meters (m)

        ρ

    {\displaystyle \rho }

 is the specific mass in kg/m3
