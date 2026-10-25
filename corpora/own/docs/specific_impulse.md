# Specific impulse

Specific impulse

Specific impulse (usually abbreviated as Isp) is a physical quantity defined as the ratio of change in momentum (impulse) to the mass used, usually fuel. It typically uses units of metres per second (a SI unit) or feet per second (in imperial units). It is equivalent to thrust (a force, in newtons or pounds) per mass flow rate (in kg/s or lbm/s).
It serves as a measure of how efficiently an engine, such as a rocket or jet engine, generates thrust from propellant. Isp is the effective exhaust velocity used in the Tsiolkovsky rocket equation which calculates how much a vehicle's velocity can be changed with a given quantity of fuel.
Normalized specific impulse is the ratio of specific impulse to Earth's standard acceleration of gravity, g (in m/s2 or ft/s2). It is measured in seconds, and conveniently is the same number in both SI and imperial units. It can be understood as the time that one kilogram of fuel can produce one kilogram-force of thrust, which is equal to the time that one pound-mass of fuel can produce one pound-force of thrust.

Overview
Reaction engines, such as rockets and jet engines propel a vehicle by expelling mass in one direction, which pushes the vehicle in the other direction according to Newton's third law of motion. This expelled mass is called the reaction mass. An engine can push harder if it expels the reaction mass at a higher exhaust velocity

          v

            e

    {\displaystyle v_{e}}

, or expels mass at a faster rate,

                d

              m

                d

              t

    {\displaystyle {\frac {\mathrm {d} m}{\mathrm {d} t}}}

.
Assuming that the engine expels mass at a constant exhaust velocity

          v

            e

    {\displaystyle v_{\text{e}}}

, the thrust is

        T

          v

            e

                d

              m

                d

              t

        .

    {\displaystyle T=v_{\text{e}}{\frac {\mathrm {d} m}{\mathrm {d} t}}.}

If this is integrated over time, the result is the total change in momentum. Dividing by the mass shows that the specific impulse is equal to the exhaust velocity. In practice, the specific impulse is usually lower than the actual physical exhaust velocity due to inefficiencies in the rocket, and thus corresponds to an "effective" exhaust velocity.
The specific impulse

          I

            sp

    {\displaystyle I_{\text{sp}}}

 in units of velocity is defined by

          T

            avg

          I

            sp

                d

              m

                d

              t

        ,

    {\displaystyle T_{\text{avg}}=I_{\text{sp}}{\frac {\mathrm {d} m}{\mathrm {d} t}},}

where

          T

            avg

    {\displaystyle T_{\text{avg}}}

 is the average thrust.

Types of engines
The practical meaning of the measurement varies with different types of engines. Car engines consume onboard fuel, breathe environmental air to burn the fuel, and push against the ground beneath them. There is no reaction mass. In this case, Isp is momentum per fuel burned.
Chemical rocket engines, by contrast, carry their fuel, oxidizer, and reaction mass with them, so Isp is momentum per reaction mass.
Airplane engines are in the middle, as they only push against airflow through the engine. Some of this reaction mass is carried with them, and some is breathed from the air. Therefore, "specific impulse" could be taken to mean either "per reaction mass", as with a rocket, or "per fuel burned" as with cars. The latter is the traditional and more common choice. Because of these differences, specific impulse is not directly comparable between different types of engines.
Specific impulse can be taken as a measure of efficiency. In cars and planes, it typically corresponds with fuel efficiency, i.e. the distance travelled per unit mass or volume of fuel. In rocketry, it corresponds to the achievable delta-v, which is the typical way to measure changes between orbits, via the Tsiolkovsky rocket equation

        Δ
        v

          I

            sp

        ln
        ⁡

              m

                0

              m

                f

        ,

    {\displaystyle \Delta v=I_{\text{sp}}\ln {\frac {m_{0}}{m_{\text{f}}}},}

where

          I

            sp

    {\displaystyle I_{\text{sp}}}

 is the specific impulse measured in units of velocity, and

          m

            0

        ,

          m

            f

    {\displaystyle m_{0},m_{\text{f}}}

 are the initial and final masses of the rocket. The difference between

          m

            0

    {\displaystyle m_{0}}

 and

          m

            f

    {\displaystyle m_{\text{f}}}

 is the reaction mass that was expelled.

Propulsion systems

Rockets
For any chemical rocket engine, the momentum transfer efficiency depends heavily on the effectiveness of the nozzle. The nozzle is the primary means of converting reactant energy (e.g. thermal or pressure energy) into a flow of momentum moving the same direction. Nozzle shape and effectiveness have a great impact on total momentum transfer from the reaction mass to the rocket.
The efficiency of the conversion of input energy to reactant energy also affects Isp, either thermal energy in combustion engines or electrical energy in ion engines. This efficiency determines the amount of delta-v a rocket can perform with a given load of fuel. Optimizing the tradeoffs between fuel quantity and specific impulse is one of the fundamental engineering challenges in rocketry.
Although the specific impulse has units of velocity, it almost never corresponds to an actual physical velocity. In chemical and cold gas rockets, the shape of the nozzle has a high impact on the energy-to-momentum conversion. There are other sources of losses and inefficiencies as well, such as the details of the chemical combustion in such engines. The physical exhaust velocity is higher than the "effective exhaust velocity", which is the "velocity" of the specific impulse. The momentum exchanged and the mass used to generate it are physically real measurements. Typically, rocket nozzles work better when the ambient pressure is lower, such as in space versus in the atmosphere. Engines are typically described by a sea-level Isp, and a vacuum Isp, which is higher. Ion engines, however, do not use a nozzle, although they have other sources of losses so that the momentum transferred is lower than the physical exhaust velocity of their reaction mass.
It is common to express specific impulse as the product of two numbers: a characteristic velocity

          c

            ∗

    {\displaystyle c^{*}}

, which summarizes combustion-chamber performance into a quantity with units of speed, and a thrust coefficient

          C

            F

    {\displaystyle C_{F}}

, which is a dimensionless quantity that summarizes nozzle performance. An additional factor of

          g

            0

    {\displaystyle g_{0}}

 is a units conversion.

          I

            sp

                c

                  ∗

              ⋅

                C

                  F

              g

                0

        .

    {\displaystyle I_{\text{sp}}={\frac {c^{*}\cdot C_{F}}{g_{0}}}.}

Units of seconds
In rocketry, the specific impulse is often reported in seconds instead of effective exhaust velocity of an engine (m/s), by dividing through standard gravity

          g

            0

    {\displaystyle g_{0}}

:

          I

            sp

              v

                e

              g

                0

            F

                    m
                    ˙

              ⋅

                g

                  0

        .

    {\displaystyle I_{\text{sp}}={\frac {v_{e}}{g_{0}}}={\frac {F}{{\dot {m}}\cdot g_{0}}}.}

This is convenient when using gravitational force units (kgf or lbf), since Isp then expresses the amount of thrust per unit propellant flow (kg/s or lb/s). Representing specific impulse in units of time also has the advantage of being agnostic between imperial and SI units:

          I

            sp

          [s]

            (

              F

                [kgf]

                    m
                    ˙

                [kg/s]

            )

            (

              F

                [lbf]

                    m
                    ˙

                [lb/s]

            )

        .

    {\displaystyle I_{\text{sp}}{\text{[s]}}={\Bigl (}{\frac {F{\text{[kgf]}}}{{\dot {m}}{\text{[kg/s]}}}}{\Bigr )}={\Bigl (}{\frac {F{\text{[lbf]}}}{{\dot {m}}{\text{[lb/s]}}}}{\Bigr )}.}

Physically, Isp measured in seconds is the amount of time a rocket engine can generate thrust, given a quantity of propellant whose weight (under g0) is equal to the engine's thrust. It is the length of time that the engine can produce 1 kgf (or 1 lbf) of thrust from 1 kg (or 1 lb) of propellant.

Cars
Although the car industry almost never uses specific impulse on any practical level, the measure can be defined, and makes good contrast against other engine types. Car engines breathe external air to combust their fuel, and (via the wheels) react against the ground. The only meaningful way to interpret "specific impulse" is as "thrust per fuelflow", although one must also specify if the force is measured at the crankshaft or at the wheels, since there are transmission losses. Such a measure corresponds to fuel mileage.

Airplanes
In an aerodynamic context, there are similarities to both cars and rockets. Like cars, airplane engines breathe outside air; unlike cars they react only against fluids flowing through the engine (including the propellers as applicable). There are several possible ways to interpret "specific impulse": as thrust per fuel flow, as thrust per breathing-flow, or as thrust per "turbine-flow" (i.e. excluding air though the propeller/bypass fan). Since the air breathed is not a direct cost, with wide engineering leeway on how much to breathe, the industry traditionally chooses the "thrust per fuel flow" interpretation with its focus on cost efficiency. In this interpretation, the resulting specific impulse numbers are much higher than for rocket engines, although this comparison is quite different — one is with and the other is without reaction mass. It exemplifies the advantage an airplane engine has over a rocket due to not having to carry the air it uses.
As with all kinds of engines, there are many engineering choices and tradeoffs that affect specific impulse. Nonlinear air resistance and the engine's inability to keep a high specific impulse at a fast burn rate are limiting factors to the fuel consumption rate.
As with rocket engines, the interpretation of specific impulse as a "velocity" does not actually correspond to the physical exhaust velocity. Since the usual interpretation excludes much of the reaction mass, the physical velocity of the reactants downstream is much lower than the effective exhaust velocity suggested from the Isp.

General considerations
Specific impulse should not be confused with energy efficiency, which can decrease as specific impulse increases, since propulsion systems that give high specific impulse require high energy to do so.
Specific impulse should not be confused with total thrust. Thrust is the force supplied by the engine and depends on the propellant mass flow through the engine. Specific impulse measures the thrust per propellant mass flow. Thrust and specific impulse are related by the design and propellants of the engine in question, but this relationship is tenuous: in most cases, high thrust and high specific impulse are mutually exclusive engineering goals. For example, LH2/LO2 bipropellant produces higher Isp (due to higher chemical energy and lower exhaust molecular mass) but lower thrust than RP-1/LO2 (due to higher density and propellant flow). In many cases, propulsion systems with very high specific impulse—some ion thrusters reach 25–35 times better Isp than chemical engines—produce correspondingly low thrust.
When calculating specific impulse, only propellant carried with the vehicle before use is counted, in the standard interpretation. This usage best corresponds to the cost of operating the vehicle. For a chemical rocket, unlike a plane or car, the propellant mass therefore would include both fuel and oxidizer. For any vehicle, optimizing for specific impulse is generally not the same as optimizing for total performance or total cost. In rocketry, a heavier engine with a higher specific impulse may not be as effective in gaining altitude, distance, or velocity as a lighter engine with a lower specific impulse, especially if the latter engine possesses a higher thrust-to-weight ratio. This is a significant reason for most rocket designs having multiple stages. The first stage can optimized for high thrust to effectively fight gravity drag and air drag, while the later stages operating strictly in orbit and in vacuum can be more easily optimized for higher specific impulse, especially for high delta-v orbits.

Propellant quantity units
The amount of propellant could be defined either in units of mass or weight. If mass is used, specific impulse is an impulse per unit of mass, which dimensional analysis shows to be equivalent to units of speed; this interpretation is commonly labeled the effective exhaust velocity. If a force-based unit system is used, impulse is divided by propellant weight (weight is a measure of force), resulting in units of time. The problem with weight, as a measure of quantity, is that it depends on the acceleration applied to the propellant, which is arbitrary with no relation to the design of the engine. Historically, standard gravity was the reference conversion between weight and mass. But since technology has progressed to the point that we can measure Earth gravity's variation across the surface, and where such differences can cause differences in practical engineering projects (not to mention science projects on other solar bodies), modern science and engineering focus on mass as the measure of quantity, so as to remove the acceleration dependence. Measuring specific impulse by propellant mass gives it the same meaning for a car at sea level, an airplane at cruising altitude, or a helicopter on Mars.
No matter the choice of mass or weight, the resulting quotient of "velocity" or "time" usually doesn't correspond directly to an actual velocity or time. Due to various losses in real engines, the actual exhaust velocity is different from the Isp "velocity" (and for cars there isn't even a sensible definition of "actual exhaust velocity"). Rather, the specific impulse is just that: a physical momentum from a physical quantity of propellant (be that in mass or weight).

Units

The most common unit for specific impulse is the second, as values are identical regardless of whether the calculations are done in SI, imperial, or US customary units. Nearly all manufacturers quote their engine performance in seconds, and the unit is also useful for specifying aircraft engine performance.
The use of metres per second to specify effective exhaust velocity is also reasonably common. The unit is intuitive when describing rocket engines, although the effective exhaust speed of the engines may be significantly different from the actual exhaust speed, especially in gas-generator cycle engines. For airbreathing jet engines, the effective exhaust velocity does not account for the mass of the air used (as the air is taken in from the environment), although it can still be used for comparison purposes.
Metres per second are numerically equivalent to newton-seconds per kg (N·s/kg), and SI measurements of specific impulse can be written in terms of either units interchangeably. This unit highlights the definition of specific impulse as impulse per unit mass of propellant.
Specific fuel consumption is inversely proportional to specific impulse and has units of g/(kN·s) or lb/(lbf·h). Specific fuel consumption is used extensively for describing the performance of air-breathing jet engines.

Specific impulse in seconds

Specific impulse, measured in seconds, can be thought of as how many seconds one kilogram of fuel can produce one kilogram-force of thrust. Or, more precisely, how many seconds a given propellant, when paired with a given engine, can accelerate its own initial mass at 1 g. The longer it can accelerate its own mass, the more delta-V it delivers to the whole system.
In other words, given a particular engine and a mass of a particular propellant, specific impulse measures for how long a time that engine can exert a continuous force (thrust) until fully burning that mass of propellant. A given mass of a more energy-dense propellant can burn for a longer duration than some less energy-dense propellant made to exert the same force while burning in an engine. Different engine designs burning the same propellant may not be equally efficient at directing their propellant's energy into effective thrust.
For all vehicles, specific impulse (impulse per unit weight-on-Earth of propellant) in seconds can be defined by the following equation:

Isp in seconds is the amount of time a rocket engine can generate thrust, given a quantity of propellant the weight of which is equal to the engine's thrust.
The advantage of this formulation is that it may be used for rockets, where all the reaction mass is carried on board, as well as airplanes, where most of the reaction mass is taken from the atmosphere. In addition, giving the result as a unit of time makes the result easily comparable between calculations in SI units, imperial units, US customary units or other unit framework.

Imperial units conversion
The English unit pound mass is more commonly used than the slug, and when using pounds per second for mass flow rate, it is more convenient to express standard gravity as 1 pound-force per pound-mass. Note that this is equivalent to 32.17405 ft/s2, but expressed in more convenient units. This gives:

          F

            thrust

          I

            sp

        ⋅

              m
              ˙

        ⋅

          (

            1

                  l
                  b
                  f

                  l
                  b
                  m

          )

        .

    {\displaystyle F_{\text{thrust}}=I_{\text{sp}}\cdot {\dot {m}}\cdot \left(1\mathrm {\frac {lbf}{lbm}} \right).}

Rocketry
In rocketry, the only reaction mass is the propellant, so the specific impulse is calculated using an alternative method, giving results with units of seconds. Specific impulse is defined as the thrust integrated over time per unit weight-on-Earth of the propellant:

          I

            sp

              v

                e

              g

                0

        ,

    {\displaystyle I_{\text{sp}}={\frac {v_{\text{e}}}{g_{0}}},}

where

          I

            sp

    {\displaystyle I_{\text{sp}}}

 is the specific impulse measured in seconds,

          v

            e

    {\displaystyle v_{\text{e}}}

 is the average exhaust speed along the axis of the engine (in m/s or ft/s),

          g

            0

    {\displaystyle g_{0}}

 is the standard gravity (in m/s2 or ft/s2).
In rockets, due to atmospheric effects, the specific impulse varies with altitude, reaching a maximum in a vacuum. This is because the exhaust velocity is not simply a function of the chamber pressure, but is a function of the difference between the interior and exterior of the combustion chamber. Values are usually given for operation at sea level ("sl") or in a vacuum ("vac").

Specific impulse as effective exhaust velocity

Because of the geocentric factor of g0 in the equation for specific impulse, many prefer an alternative definition. The specific impulse of a rocket can be defined in terms of thrust per unit mass flow of propellant. This is an equally valid (and in some ways somewhat simpler) way of defining the effectiveness of a rocket propellant. For a rocket, the specific impulse defined in this way is simply the effective exhaust velocity relative to the rocket, ve. "In actual rocket nozzles, the exhaust velocity is not really uniform over the entire exit cross section and such velocity profiles are difficult to measure accurately. A uniform axial velocity, ve, is assumed for all calculations which employ one-dimensional problem descriptions. This effective exhaust velocity represents an average or mass equivalent velocity at which propellant is being ejected from the rocket vehicle." The two definitions of specific impulse are proportional to one another, and related to each other by:

          v

            e

          g

            0

        ⋅

          I

            sp

        ,

    {\displaystyle v_{\text{e}}=g_{0}\cdot I_{\text{sp}},}

where

          I

            sp

    {\displaystyle I_{\text{sp}}}

 is the specific impulse in seconds,

          v

            e

    {\displaystyle v_{\text{e}}}

 is the specific impulse measured in m/s, which is the same as the effective exhaust velocity measured in m/s (or ft/s if g is in ft/s2),

          g

            0

    {\displaystyle g_{0}}

 is the standard gravity, 9.80665 m/s2 (in United States customary units 32.174 ft/s2).
This equation is also valid for air-breathing jet engines, but is rarely used in practice.
(Note that different symbols are sometimes used; for example, c is also sometimes seen for exhaust velocity. While the symbol

          I

            sp

    {\displaystyle I_{\text{sp}}}

 might logically be used for specific impulse in units of (N·s3)/(m·kg); to avoid confusion, it is desirable to reserve this for specific impulse measured in seconds.)
It is related to the thrust, or forward force on the rocket by the equation:

          F

            thrust

          v

            e

        ⋅

              m
              ˙

        ,

    {\displaystyle F_{\text{thrust}}=v_{\text{e}}\cdot {\dot {m}},}

where

              m
              ˙

    {\displaystyle {\dot {m}}}

 is the propellant mass flow rate, which is the rate of decrease of the vehicle's mass.
A rocket must carry all its propellant with it, so the mass of the unburned propellant must be accelerated along with the rocket itself. Minimizing the mass of propellant required to achieve a given change in velocity is crucial to building effective rockets. The Tsiolkovsky rocket equation shows that for a rocket with a given empty mass and a given amount of propellant, the total change in velocity it can accomplish is proportional to the effective exhaust velocity.
A spacecraft without propulsion follows an orbit determined by its trajectory and any gravitational field. Deviations from the corresponding velocity pattern (these are called Δv) are achieved by sending exhaust mass in the direction opposite to that of the desired velocity change.

Actual exhaust speed versus effective exhaust speed
When an engine is run within the atmosphere, the exhaust velocity is reduced by atmospheric pressure, in turn reducing specific impulse. This is a reduction in the effective exhaust velocity, versus the actual exhaust velocity achieved in vacuum conditions. In the case of gas-generator cycle rocket engines, more than one exhaust gas stream is present as turbopump exhaust gas exits through a separate nozzle. Calculating the effective exhaust velocity requires averaging the two mass flows as well as accounting for any atmospheric pressure.
For air-breathing jet engines, particularly turbofans, the actual exhaust velocity and the effective exhaust velocity are different by orders of magnitude. This happens for several reasons. First, a good deal of additional momentum is obtained by using air as reaction mass, such that combustion products in the exhaust have more mass than the burned fuel. Next, inert gases in the atmosphere absorb heat from combustion, and through the resulting expansion provide additional thrust. Lastly, for turbofans and other designs there is even more thrust created by pushing against intake air which never sees combustion directly. These all combine to allow a better match between the airspeed and the exhaust speed, which saves energy/propellant and enormously increases the effective exhaust velocity while reducing the actual exhaust velocity. Again, this is because the mass of the air is not counted in the specific impulse calculation, thus attributing all of the thrust momentum to the mass of the fuel component of the exhaust, and omitting the reaction mass, inert gas, and effect of driven fans on overall engine efficiency from consideration.
Essentially, the momentum of engine exhaust includes a lot more than just fuel, but specific impulse calculation ignores everything but the fuel. Even though the effective exhaust velocity for an air-breathing engine seems nonsensical in the context of actual exhaust velocity, this is still useful for comparing absolute fuel efficiency of different engines.

Density specific impulse
A related measure, the density specific impulse, sometimes also referred to as Density Impulse and usually abbreviated as Isd is the product of the average specific gravity of a given propellant mixture and the specific impulse. While less important than the specific impulse, it is an important measure in launch vehicle design, as a low specific impulse implies that bigger tanks will be required to store the propellant, which in turn will have a detrimental effect on the launch vehicle's mass ratio.

Specific fuel consumption
Specific impulse is inversely proportional to specific fuel consumption (SFC) by the relationship Isp = 1/(go·SFC) for SFC in kg/(N·s) and Isp = 3600/SFC for SFC in lb/(lbf·hr).

Examples

An example of a specific impulse measured in time is 453 seconds, which is equivalent to an effective exhaust velocity of 4.440 km/s (14,570 ft/s), for the RS-25 engines when operating in a vacuum. An air-breathing jet engine typically has a much larger specific impulse than a rocket; for example a turbofan jet engine may have a specific impulse of 6,000 seconds or more at sea level whereas a rocket would be between 200 and 400 seconds.
An air-breathing engine is thus much more propellant efficient than a rocket engine, because the air serves as reaction mass and oxidizer for combustion which does not have to be carried as propellant, and the actual exhaust speed is much lower, so the kinetic energy the exhaust carries away is lower and thus the jet engine uses far less energy to generate thrust. While the actual exhaust velocity is lower for air-breathing engines, the effective exhaust velocity is very high for jet engines. This is because the effective exhaust velocity calculation assumes that the carried propellant is providing all the reaction mass and all the thrust. Hence effective exhaust velocity is not physically meaningful for air-breathing engines; nevertheless, it is useful for comparison with other types of engines.
The highest specific impulse for a chemical propellant ever test-fired in a rocket engine was 542 seconds (5.32 km/s) with a tripropellant of lithium, fluorine, and hydrogen. However, this combination is impractical. Lithium and fluorine are both extremely corrosive, lithium ignites on contact with air, fluorine ignites on contact with most fuels, and hydrogen, while not hypergolic, is an explosive hazard. Fluorine and the hydrogen fluoride (HF) in the exhaust are very toxic, which damages the environment, makes work around the launch pad difficult, and makes getting a launch license that much more difficult. The rocket exhaust is also ionized, which would interfere with radio communication with the rocket.
Nuclear thermal rocket engines differ from conventional rocket engines in that energy is supplied to the propellants by an external nuclear heat source instead of the heat of combustion. The nuclear rocket typically operates by passing liquid hydrogen gas through an operating nuclear reactor. Testing in the 1960s yielded specific impulses of about 850 seconds (8,340 m/s), about twice that of the Space Shuttle engines.
A variety of other rocket propulsion methods, such as ion thrusters, give much higher specific impulse but with much lower thrust; for example the Hall-effect thruster on the SMART-1 satellite has a specific impulse of 1,640 s (16.1 km/s) but a maximum thrust of only 68 mN (0.015 lbf). The variable specific impulse magnetoplasma rocket (VASIMR) engine currently in development will theoretically yield 20 to 300 km/s (66,000 to 984,000 ft/s), and a maximum thrust of 5.7 N (1.3 lbf).
