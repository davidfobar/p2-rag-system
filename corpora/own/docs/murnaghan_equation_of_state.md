# Murnaghan equation of state

Murnaghan equation of state

The Murnaghan equation of state is a relationship between the volume of a body and the pressure to which it is subjected. This is one of many state equations that have been used in earth sciences and shock physics to model the behavior of matter under conditions of high pressure. It owes its name to Francis D. Murnaghan who proposed it in 1944 to reflect material behavior under a pressure range as wide as possible to reflect an experimentally established fact: the more a solid is compressed, the more difficult it is to compress further.
The Murnaghan equation is derived, under certain assumptions, from the equations of continuum mechanics. It involves two adjustable parameters: the modulus of incompressibility K0 and its first derivative with respect to the pressure, K'0, both measured at ambient pressure. In general, these coefficients are determined by a regression on experimentally obtained values of volume V as a function of the pressure P. These experimental data can be obtained by X-ray diffraction or by shock tests. Regression can also be performed on the values of the energy as a function of the volume obtained from ab-initio and molecular dynamics calculations.
The Murnaghan equation of state is typically expressed as:

        P
        (
        V
        )

              K

                0

              K

                0

              ′

          [

                (

                    V

                      V

                        0

                )

                −

                  K

                    0

                  ′

            −
            1

          ]

        .

    {\displaystyle P(V)={\frac {K_{0}}{K_{0}'}}\left[\left({\frac {V}{V_{0}}}\right)^{-K_{0}'}-1\right]\,.}

If the reduction in volume under compression is low, i.e., for V/V0 greater than about 90%, the Murnaghan equation can model experimental data with satisfactory accuracy. Moreover, unlike many proposed equations of state, it gives an explicit expression of the volume as a function of pressure V(P). But its range of validity is limited and physical interpretation inadequate. However, this equation of state continues to be widely used in models of solid explosives. Of more elaborate equations of state, the most used in earth physics is the Birch–Murnaghan equation of state. In shock physics of metals and alloys, another widely used equation of state is the Mie–Gruneisen equation of state.

Background
The study of the internal structure of the earth through the knowledge of the mechanical properties of the constituents of the inner layers of the planet involves extreme conditions; the pressure can be counted in hundreds of gigapascal and temperatures in thousands of degrees. The study of the properties of matter under these conditions can be done experimentally through devices such as diamond anvil cell for static pressures, or by subjecting the material to shock waves. It also gave rise to theoretical work to determine the equation of state, that is to say the relations among the different parameters that define in this case the state of matter: the volume (or density), temperature and pressure.
There are two approaches:

the state equations derived from interatomic potentials, or possibly ab initio calculations;
derived from the general relations of the state equations mechanics and thermodynamics. The Murnaghan equation belongs to this second category.
Dozens of equations have been proposed by various authors. These are empirical relationships, the quality and relevance depend on the use made of it and can be judged by different criteria: the number of independent parameters that are involved, the physical meaning that can be assigned to these parameters, the quality of the experimental data, and the consistency of theoretical assumptions that underlie their ability to extrapolate the behavior of solids at high compression.

Expressions for the equation of state
Generally, at constant temperature, the bulk modulus is defined by:

        K

        −
        V

            (

                  ∂
                  P

                  ∂
                  V

            )

            T

        .

    {\displaystyle K=-V\left({\frac {\partial P}{\partial V}}\right)_{T}.}

The easiest way to get an equation of state linking P and V is to assume that K is constant, that is to say, independent of pressure and deformation of the solid, then we simply find Hooke's law. In this case, the volume decreases exponentially with pressure. This is not a satisfactory result because it is experimentally established that as a solid is compressed, it becomes more difficult to compress. To go further, we must take into account the variations of the elastic properties of the solid with compression.
The assumption Murnaghan is to assume that the bulk modulus is a linear function of pressure :

        K

          K

            0

        +
        P

          K

            0

          ′

    {\displaystyle K=K_{0}+P\ K_{0}'}

Murnaghan equation is the result of the integration of the differential equation:

        P
        (
        V
        )

              K

                0

              K

                0

              ′

          [

                (

                    V

                      V

                        0

                )

                −

                  K

                    0

                  ′

            −
            1

          ]

    {\displaystyle P(V)={\frac {K_{0}}{K_{0}'}}\left[\left({\frac {V}{V_{0}}}\right)^{-K_{0}'}-1\right]}

We can also express the volume depending on the pressure:

        V
        (
        P
        )

          V

            0

            [

              1
              +
              P

                (

                      K

                        0

                      ′

                      K

                        0

                )

            ]

            −
            1

              /

              K

                0

              ′

    {\displaystyle V(P)=V_{0}\left[1+P\left({\frac {K'{0}}{K{0}}}\right)\right]^{-1/K'_{0}}}

This simplified presentation is however criticized by Poirier as lacking rigor. The same relationship can be shown in a different way from the fact that the incompressibility of the product of the modulus and the thermal expansion coefficient is not dependent on the pressure for a given material. This equation of state is also a general case of the older Polytrope relation which also has a constant power relation.
In some circumstances, particularly in connection with ab initio calculations, the expression of the energy as a function of the volume will be preferred, which can be obtained by integrating the above equation according to the relationship P = −dE/dV . It can be written to K'0 different from 1,

        E
        (
        V
        )

          E

            0

        +

          K

            0

          V

            0

          [

                1

                    K

                      0

                    ′

                  (

                    K

                      0

                    ′

                  −
                  1
                  )

                (

                    V

                      V

                        0

                )

                1
                −

                  K

                    0

                  ′

            +

                1

                  K

                    0

                  ′

                V

                  V

                    0

            −

                1

                    K

                      0

                    ′

                  −
                  1

          ]

        .

    {\displaystyle E(V)=E_{0}+K_{0}\,V_{0}\left[{\frac {1}{K_{0}'(K_{0}'-1)}}\left({\frac {V}{V_{0}}}\right)^{1-K_{0}'}+{\frac {1}{K_{0}'}}{\frac {V}{V_{0}}}-{\frac {1}{K_{0}'-1}}\right].}

Advantages and limitations
Despite its simplicity, the Murnaghan equation is able to reproduce the experimental data for a range of pressures that can be quite large, on the order of K0/2. It also remains satisfactory as the ratio V/V0 remains above about 90%. In this range, the Murnaghan equation has an advantage compared to other equations of state if one wants to express the volume as a function of pressure.
Nevertheless, other equations may provide better results and several theoretical and experimental studies show that the Murnaghan equation is unsatisfactory for many problems. Thus, to the extent that the ratio V/V0 becomes very low, the theory predicts that K' goes to 5/3, which is the Thomas–Fermi limit. However, in the Murnaghan equation, K' is constant and set to its initial value. In particular, the value K'0 = 5/3 becomes inconsistent with the theory under some situations. In fact, when extrapolated, the behavior predicted by the Murnaghan equation becomes quite quickly unlikely.
Regardless of this theoretical argument, experience clearly shows that K' decreases with pressure, or in other words that the second derivative of the incompressibility modulus K" is strictly negative. A second order theory based on the same principle (see next section) can account for this observation, but this approach is still unsatisfactory. Indeed, it leads to a negative bulk modulus in the limit where the pressure tends to infinity. In fact, this is an inevitable contradiction whatever polynomial expansion is chosen because there will always be a dominant term that diverges to infinity.
These important limitations have led to the abandonment of the Murnaghan equation, which W. Holzapfel calls "a useful mathematical form without any physical justification". In practice, the analysis of compression data is done by using more sophisticated equations of state. The most commonly used within the science community is the Birch–Murnaghan equation, second or third order in the quality of data collected.
Finally, a very general limitation of this type of equation of state is their inability to take into account the phase transitions induced by the pressure and temperature of melting, but also multiple solid-solid transitions that can cause abrupt changes in the density and bulk modulus based on the pressure.

Examples
In practice, the Murnaghan equation is used to perform a regression on a data set, where one gets the values of the coefficients K0 and K'0. These coefficients obtained, and knowing the value of the volume to ambient conditions, then we are in principle able to calculate the volume, density and bulk modulus for any pressure.
The data set is mostly a series of volume measurements for different values of applied pressure, obtained mostly by X-ray diffraction. It is also possible to work on theoretical data, calculating the energy for different values of volume by ab initio methods, and then regressing these results. This gives a theoretical value of the modulus of elasticity which can be compared to experimental results.
The following table lists some of the results of different materials, with the sole purpose of illustrating some numerical analyses that have been made using the Murnaghan equation, without prejudice to the quality of the models obtained. Given the criticisms that have been made in the previous section on the physical meaning of the Murnaghan equation, these results should be considered with caution.

Extensions and generalizations
To improve the models or avoid criticism outlined above, several generalizations of the Murnaghan equation have been proposed. They usually consist in dropping a simplifying assumption and adding another adjustable parameter. This can improve the qualities of refinement, but also lead to complicated expressions. The question of the physical meaning of these additional parameters is also raised.
A possible strategy is to include an additional term P2 in the previous development, requiring that

        K

          K

            0

        +
        P

          K

            0

          ′

        +

          P

            2

          K

            0

          ″

    {\displaystyle K=K_{0}+PK_{0}'+P^{2}K_{0}''}

. Solving this differential equation gives the equation of the second-order Murnaghan:

        P
        (
        V
        )

        2

              K

                0

              K

                0

              ′

            [

                  Γ

                    K

                      0

                    ′

                        (

                              V

                                0

                            V

                        )

                        Γ

                    +
                    1

                        (

                              V

                                0

                            V

                        )

                        Γ

                    −
                    1

              −
              1

            ]

            −
            1

    {\displaystyle P(V)=2{\frac {K_{0}}{K_{0}'}}\left[{\frac {\Gamma }{K_{0}'}}\,{\frac {\left({\frac {V_{0}}{V}}\right)^{\Gamma }+1}{\left({\frac {V_{0}}{V}}\right)^{\Gamma }-1}}-1\right]^{-1}}

where

          Γ

            2

          K

            0

            ′

              2

        −
        2

          K

            0

          K

            0

          ″

        0

    {\displaystyle \Gamma ^{2}=K_{0}'^{2}-2K_{0}K_{0}''>0}

. Found naturally in the first order equation taking

          K

            0

          ″

        0

    {\displaystyle K_{0}''=0}

. Developments to an order greater than 2 are possible in principle, but at the cost of adding an adjustable parameter for each term.
Other generalizations can be cited:

Kumari and Dass have proposed a generalization abandoning the condition K = 0 but assuming the report K / K ' independent of pressure;
Kumar proposed a generalization taking into account the dependence of the Anderson parameter as a function of volume. It was subsequently shown that this generalized equation was not new, but rather reducible to the Tait equation.

Notes and references
