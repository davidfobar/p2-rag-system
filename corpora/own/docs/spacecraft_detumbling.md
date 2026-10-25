# Spacecraft detumbling

Spacecraft detumbling

Spacecraft detumbling is the process of reducing or eliminating unwanted angular velocity (tumbling) of a spacecraft following launcher separation or an external perturbation. Detumbling is the first task to be performed by the spacecraft's attitude control system and it is therefore critical to ensure safe satellite operations, enabling reliable communication, solar power generation, navigation, and the subsequent nominal mission.
In order to minimize the risk of failure during this process, stringent requirements on the reliability of the involved actuators and sensors and on the simplicity of the adopted control algorithm are usually driving the design of the detumbling.
Spacecraft detumbling techniques can also be applied to the handling and removal of space debris.

History
Early efforts investigating detumbling strategies focused on passive methods like magnetic damping and gravity-gradient stabilization. Modern satellites typically employ an active detumbling control, either purely magnetic or including additional actuators, such as reaction wheels or thrusters. Current efforts in detumbling research focus on advanced control for underactuated systems or the integration of machine learning to improve detumbling performance.

Common detumbling strategies

Magnetic control
The basic magnetic attitude control system is composed of magnetorquers as actuators and magnetometers as sensing elements. A fully-magnetic attitude control system is currently implemented in several space missions, especially for smaller classes of satellites. Magnetic rods and magnetometers are selected for their reliability, low mass and energy efficiency advantages.
Magnetorquers are able to control the satellite through electromagnetic interaction between the generated magnetic moment and the external magnetic field:

          τ

          m

        ×

          B

    {\displaystyle {\boldsymbol {\tau }}={\boldsymbol {m}}\times {\boldsymbol {B}}}

where

        τ

    {\displaystyle \tau }

 is the torque acting on the satellite,

        B

    {\displaystyle B}

 is Earth's magnetic field, and

        m

    {\displaystyle m}

 is the torquer magnetic moment. The cross product reveals a limitation of magnetic control: the control torque cannot be applied along any possible direction but only its projection on the plane orthogonal to

        B

    {\displaystyle B}

 is available. The system under control is consequently underactuated.

Magnetic control: B-dot
Currently, the most widely used strategy for spacecraft detumbling employs a magnetic control algorithm called B-dot. The resulting control architecture has proven reliable, simple and easy to implement, establishing the baseline against which new detumbling strategies are evaluated.
The B-dot control law is based on the rate of change of magnetic field measurements:

          m

          −
          k

              B
              ˙

    {\displaystyle {\boldsymbol {m}}={\boldsymbol {-k}}{\dot {\boldsymbol {B}}}}

where

        m

    {\displaystyle m}

 is the commanded torquer magnetic moment,

        k

    {\displaystyle k}

 is the controller gain and

              B
              ˙

    {\displaystyle {\dot {B}}}

 is the rate of change of the measured magnetic field. The magnetic field derivative is used as a coarse estimate of the spacecraft angular velocity. Because of this underlying assumption, the B-dot controller suffers performance degradation when the spacecraft angular velocity is low, which is usually the case when the spacecraft is close to being fully detumbled, or if the initial angular velocity is small.

Magnetic control: beyond the B-dot
Over the years, a number of magnetic controllers beyond the classic B-dot have been investigated. The drivers for this research span from power saving, improving the convergence rate and solution robustness, or trying to overcome the inherently underactuated nature of magnetic control.

Flywheel-based control
Spacecraft detumbling using momentum-exchange flywheel-based devices like reaction wheels or control moment gyros can significantly shorten detumbling times, thus helping reduce mass and volume of the power system, due to the much larger torque available from non-magnetic actuators. Furthermore, flywheel-based control can help overcome the underactuation problem typical of magnetic-only control.
However, as these devices exploit the principle of conservation of angular momentum to control the spacecraft, the flywheels' angular momentum builds up over time. Therefore, momentum-exchange devices must be employed together with an additional actuator that removes the flywheels' accumulated momentum without affecting the satellite attitude. This process is known as momentum dumping, and is typically realized through magnetorquers or thrusters.

Thruster-based control
Similarly to flywheel-based control, thrusters can be used during the detumbling phase for missions characterized by demanding power or torque requirements.
Furthermore, as Earth's magnetic field intensity decreases with altitude, there exists a practical boundary to the use of magnetic control due to degraded magnetorquer efficiency. This boundary is set to low Earth Orbit (LEO), below an altitude of 2,000 km. Beyond LEO, thrusters can be employed for detumbling purposes. However, the use of thrusters is in general limited by the mass and propellant capacity of the thruster system.

Mass redistribution
Spacecraft detumbling can be performed through a movable-mass control device that is internal to the spacecraft and can move along a fixed direction track. The physical principle behind this strategy consists in controlling the mass distribution such that the system angular kinetic energy decreases over time.

The performance of the control system can be improved through larger mass amplitudes along the track or larger mass sizes. In this approach, the location and displacement amplitude of any internal control mass is limited by the physical dimensions of the spacecraft.
Externally movable appendages solve this limitation and allow for a greater range of location and displacement amplitudes. However, as the size of the appendages increases, flexibility problems associated with such structures have to be considered. One example of this strategy is the so-called yo-yo de-spin.

Applications and ongoing development

Space debris mitigation
The increasing number of space debris in recent years led to the development of several detumbling techniques for uncontrolled satellites or generic uncooperative object. According to the specific interaction between the active satellite responsible for the debris handling (chaser) and the uncooperative object (target), detumbling strategies can be separated into contact-based and contactless approaches.
Contact-based strategies require a physical connection between target and chaser. This connection can be a rigid link, such as a robotic arm or a flexible link, like a harpoon. Contactless strategies, instead, employ detumbling approaches that do not require a physical connection between target and chaser, for example eddy currents, plume impingement or lasers.

Underactuation
Advanced control techniques including model predictive control have recently been employed to design detumbling techniques for underactuated systems, such as spacecraft using a single magnetorquer.
