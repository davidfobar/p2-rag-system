# Order tracking (signal processing)

Order tracking (signal processing)

In rotordynamics, order tracking, also known as angular resampling, is a family of signal processing tools aimed at transforming a measured signal from time domain to angular (or order) domain. These techniques are applied to asynchronously sampled signals (i.e. with a constant sample rate in Hertz) to obtain the same signal sampled at constant angular increments of a reference shaft. In some cases the outcome of the Order Tracking is directly the Fourier transform of such angular domain signal, whose frequency counterpart is defined as "order". Each order represents a fraction of the angular velocity of the reference shaft.
Order tracking is based on a velocity measurement, generally obtained by means of a tachometer or encoder, needed to estimate the instantaneous velocity and/or the angular position of the shaft.
Three main families of computed order tracking techniques have been developed in the past: Computed Order Tracking (COT), Vold-Kalman Filter (VKF) and Order Tracking Transforms.
Order tracking refers to a signal processing technique used to extract the periodic content of a signal and track its frequency variations over time. This technique is often used in Condition-based maintenance of rotating machinery by vibration analysis, such as engines, gears, turbines, and pumps.
In order to track the order of a signal, the signal is first transformed into the frequency domain using techniques such as the Fourier transform. The resulting frequency spectrum shows the frequency content of the signal. From the frequency spectrum, it is possible to identify the dominant frequency components, which correspond to the various orders of the rotating machinery.
Once the orders are identified, a tracking algorithm is used to track the frequency variations of each order over time. This is done by comparing the frequency content of the signal at different time instants and identifying the shifts in the frequency components.

One method of implementing order tracking is illustrated in the accompanying block diagram. First, the shaft speed is measured to calculate its phase as a function of time. Next, new sampling points with constant angular intervals are determined. The vibration signal is then resampled to synchronize with the shaft angle. The effect of this process is shown in the following figure: order tracking successfully transforms smeared frequency bands into sharp, distinct peaks.

Computed order tracking
Computed order tracking is a resampling technique based on interpolation.
The procedure begins by estimating the time instants

          T

            k

    {\displaystyle T_{k}}

        (
        k

        1
        :
        K
        )

    {\displaystyle (k=1:K)}

 corresponding to integer rotations of the shaft (i.e. angle equal to

        2
        π
        k

    {\displaystyle 2\pi k}

). Then an angular rotation vector is defined:

          α

            i

        2
        ⋅
        π

              i
              K

            N

    {\displaystyle \alpha _{i}=2\cdot \pi {\frac {iK}{N}}}

accordingly to the desired angular resolution:

        Δ
        α

            K
            N

    {\displaystyle \Delta \alpha ={\frac {K}{N}}}

A corresponding vector of time instants is obtained by means of a first interpolation step

        t
        (
        i
        Δ
        α
        )

          interpolation

        (
        {
        2
        π
        k
        ,

          T

            k

        }
        ,

          α

            i

        )

    {\displaystyle t(i\Delta \alpha )={\text{interpolation}}({2\pi k,T_{k}},\alpha _{i})}

A second interpolation step is then applied to obtain the angular resampled signal

        x
        (
        i
        Δ
        α
        )

    {\displaystyle x(i\Delta \alpha )}

 from the original time domain signal

        x
        (
        j
        Δ
        t
        )

    {\displaystyle x(j\Delta t)}

:

        x
        (
        i
        Δ
        α
        )

          interpolation

        (
        {
        x
        (
        j
        Δ
        t
        )
        ,
        j
        Δ
        t
        }
        ,
        t
        (
        i
        Δ
        α
        )
        )

    {\displaystyle x(i\Delta \alpha )={\text{interpolation}}({x(j\Delta t),j\Delta t},t(i\Delta \alpha ))}

Vold-Kalman filter
Vold-Kalman filter is a particular formulation of Kalman filter, able to estimate both instantaneous speed and amplitude of a series of harmonics of the shaft rotational velocity.

Order tracking transforms
Order tracking transforms are mathematical transforms which perform in a single step both the order tracking (synchronization of the signal domain with the reference shaft) and the Fourier transform to assess amplitude and phase of each order of the so obtained spectrum. With such transforms it is possible to directly assess the amplitude of a synchronous, sub-synchronous or super-synchronous shaft-locked harmonics, without an additional resampling step.
The most recent formulation of such transforms is the Velocity Synchronous Discrete Fourier Transform, defined as follows:

        X
        (
        Ω
        )

              Δ
              t

            Θ

          ∑

            n

            1

            N

        x
        (
        n
        Δ
        t
        )

          e

            −
            j
            Ω
            θ
            (
            n
            Δ
            t
            )

        ω
        (
        n
        Δ
        t
        )

    {\displaystyle X(\Omega )={\frac {\Delta t}{\Theta }}\sum _{n=1}^{N}x(n\Delta t)e^{-j\Omega \theta (n\Delta t)}\omega (n\Delta t)}

where

        Ω

    {\displaystyle \Omega }

 is the order of the harmonics to be estimated,

        Θ

    {\displaystyle \Theta }

 is the total angular rotation of the shaft in the acquisition window,

        θ

    {\displaystyle \theta }

 and

        ω

    {\displaystyle \omega }

 are respectively the instantaneous angular rotation and velocity of the reference shaft.
