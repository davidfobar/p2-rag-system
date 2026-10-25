# Tennis racket theorem

Tennis racket theorem

The tennis racket theorem, or intermediate axis theorem, is a kinetic phenomenon of classical mechanics which describes the movement of a rigid body with three distinct principal moments of inertia. It has also been dubbed the Dzhanibekov effect, after Soviet cosmonaut Vladimir Dzhanibekov, who noticed one of the theorem's logical consequences whilst in space in 1985. The effect was known for at least 150 years prior, having been described by Louis Poinsot in 1834 and included in standard physics textbooks such as Classical Mechanics by Herbert Goldstein throughout the 20th century.
The theorem describes the following effect: rotation of an object around its first and third principal axes is stable, whereas rotation around its second principal axis (or intermediate axis) is not.
This can be demonstrated by the following experiment: Hold a tennis racket at its handle, with its face being horizontal, and throw it in the air such that it performs a full rotation around its horizontal axis perpendicular to the handle (ê2 in the diagram), and then catch the handle. In almost all cases, during that rotation the face will also have completed a half rotation, so that the other face is now up. By contrast, it is easy to throw the racket so that it will rotate around the handle axis (ê1) without accompanying half-rotation around another axis; it is also possible to make it rotate around the vertical axis perpendicular to the handle (ê3) without any accompanying half-rotation.
The experiment can be performed with any object that has three different moments of inertia, for instance with a (rectangular) book, remote control, or smartphone. The effect occurs whenever the axis of rotation differs – even only slightly – from the object's second principal axis; air resistance or gravity are not necessary.

Theory

The tennis racket theorem can be qualitatively analysed with the help of Euler's equations.
Under torque–free conditions, they take the following form:

                  I

                    1

                        ω
                        ˙

                    1

                −
                (

                  I

                    3

                −

                  I

                    2

                )

                  ω

                    3

                  ω

                    2

                  (1)

                  I

                    2

                        ω
                        ˙

                    2

                −
                (

                  I

                    1

                −

                  I

                    3

                )

                  ω

                    1

                  ω

                    3

                  (2)

                  I

                    3

                        ω
                        ˙

                    3

                −
                (

                  I

                    2

                −

                  I

                    1

                )

                  ω

                    2

                  ω

                    1

                  (3)

    {\displaystyle {\begin{aligned}I_{1}{\dot {\omega }}{1}&=-(I{3}-I_{2})\omega _{3}\omega {2}~~~~{\text{(1)}}\I{2}{\dot {\omega }}{2}&=-(I{1}-I_{3})\omega _{1}\omega {3}~~~~{\text{(2)}}\I{3}{\dot {\omega }}{3}&=-(I{2}-I_{1})\omega _{2}\omega _{1}~~~~{\text{(3)}}\end{aligned}}}

Here

          I

            1

        ,

          I

            2

        ,

          I

            3

    {\displaystyle I_{1},I_{2},I_{3}}

 denote the object's principal moments of inertia, and we assume

          I

            1

        <

          I

            2

        <

          I

            3

    {\displaystyle I_{1}<I_{2}<I_{3}}

. The angular velocities around the object's three principal axes are

          ω

            1

        ,

          ω

            2

        ,

          ω

            3

    {\displaystyle \omega _{1},\omega _{2},\omega _{3}}

 and their time derivatives are denoted by

                ω
                ˙

            1

        ,

                ω
                ˙

            2

        ,

                ω
                ˙

            3

    {\displaystyle {\dot {\omega }}{1},{\dot {\omega }}{2},{\dot {\omega }}_{3}}

.

Stable rotation around the first and third principal axis
Consider the situation when the object is rotating around the axis with moment of inertia

          I

            1

    {\displaystyle I_{1}}

. To determine the nature of equilibrium, assume small initial angular velocities along the other two axes. As a result, according to equation (1),

                ω
                ˙

            1

    {\displaystyle ~{\dot {\omega }}_{1}}

 is very small. Therefore, the time dependence of

          ω

            1

    {\displaystyle ~\omega _{1}}

 may be neglected.
Now, differentiating equation (2) and substituting

                ω
                ˙

            3

    {\displaystyle {\dot {\omega }}_{3}}

 from equation (3),

                  I

                    2

                        ω
                        ¨

                    2

                −
                (

                  I

                    1

                −

                  I

                    3

                )

                  ω

                    1

                        ω
                        ˙

                    3

                  I

                    3

                  I

                    2

                        ω
                        ¨

                    2

                (

                  I

                    1

                −

                  I

                    3

                )
                (

                  I

                    2

                −

                  I

                    1

                )
                (

                  ω

                    1

                  )

                    2

                  ω

                    2

                  i.e.

                        ω
                        ¨

                    2

                  (negative quantity)

                ⋅

                  ω

                    2

    {\displaystyle {\begin{aligned}I_{2}{\ddot {\omega }}{2}&=-(I{1}-I_{3})\omega {1}{\dot {\omega }}{3}\I_{3}I_{2}{\ddot {\omega }}{2}&=(I{1}-I_{3})(I_{2}-I_{1})(\omega _{1})^{2}\omega {2}\{\text{i.e. }}~~~~{\ddot {\omega }}{2}&={\text{(negative quantity)}}\cdot \omega _{2}\end{aligned}}}

because

          I

            2

        −

          I

            1

        0

    {\displaystyle I_{2}-I_{1}>0}

 and

          I

            1

        −

          I

            3

        <
        0

    {\displaystyle I_{1}-I_{3}<0}

.
Note that

          ω

            2

    {\displaystyle \omega _{2}}

 is being opposed and so rotation around this axis is stable for the object.
Similar reasoning gives that rotation around the axis with moment of inertia

          I

            3

    {\displaystyle I_{3}}

 is also stable.

Unstable rotation around the second principal axis
Now apply the same analysis to the axis with moment of inertia

          I

            2

        .

    {\displaystyle I_{2}.}

 This time

                ω
                ˙

            2

    {\displaystyle {\dot {\omega }}_{2}}

 is very small. Therefore, the time dependence of

          ω

            2

    {\displaystyle ~\omega _{2}}

 may be neglected.
Now, differentiating equation (1) and substituting

                ω
                ˙

            3

    {\displaystyle {\dot {\omega }}_{3}}

 from equation (3),

                  I

                    1

                  I

                    3

                        ω
                        ¨

                    1

                (

                  I

                    3

                −

                  I

                    2

                )
                (

                  I

                    2

                −

                  I

                    1

                )
                (

                  ω

                    2

                  )

                    2

                  ω

                    1

                  i.e.

                        ω
                        ¨

                    1

                  (positive quantity)

                ⋅

                  ω

                    1

    {\displaystyle {\begin{aligned}I_{1}I_{3}{\ddot {\omega }}{1}&=(I{3}-I_{2})(I_{2}-I_{1})(\omega _{2})^{2}\omega {1}\{\text{i.e.}}~~~~{\ddot {\omega }}{1}&={\text{(positive quantity)}}\cdot \omega _{1}\end{aligned}}}

Note that

          ω

            1

    {\displaystyle \omega _{1}}

 is not opposed (and therefore will grow) and so rotation around the second axis is unstable. Therefore, even a small disturbance, in the form of a very small initial value of

          ω

            1

    {\displaystyle \omega _{1}}

 or

          ω

            3

    {\displaystyle \omega _{3}}

, causes the object to 'flip'.

Matrix analysis
If the object is mostly rotating along its third axis, so

          ω

            3

        ≫

          ω

            1

        ,

          ω

            2

    {\displaystyle |\omega _{3}|\gg |\omega _{1}|,|\omega _{2}|}

, we can assume

          ω

            3

    {\displaystyle \omega _{3}}

 does not vary much, and write the equations of motion as a matrix equation:

            d

              d
              t

            [

                    ω

                      1

                    ω

                      2

            ]

            [

                  0

                  −

                    ω

                      3

                  (

                    I

                      3

                  −

                    I

                      2

                  )

                    /

                    I

                      1

                  −

                    ω

                      3

                  (

                    I

                      1

                  −

                    I

                      3

                  )

                    /

                    I

                      2

                  0

            ]

            [

                    ω

                      1

                    ω

                      2

            ]

    {\displaystyle {\frac {d}{dt}}{\begin{bmatrix}\omega _{1}\\omega _{2}\end{bmatrix}}={\begin{bmatrix}0&-\omega {3}(I{3}-I_{2})/I_{1}\-\omega {3}(I{1}-I_{3})/I_{2}&0\end{bmatrix}}{\begin{bmatrix}\omega _{1}\\omega _{2}\end{bmatrix}}}

which has zero trace and positive determinant, implying the motion of

        (

          ω

            1

        ,

          ω

            2

        )

    {\displaystyle (\omega _{1},\omega _{2})}

 is a stable rotation around the origin—thus

        (
        0
        ,
        0
        ,

          ω

            3

        )

    {\displaystyle (0,0,\omega _{3})}

 is a neutral equilibrium point. Similarly, the point

        (

          ω

            1

        ,
        0
        ,
        0
        )

    {\displaystyle (\omega _{1},0,0)}

 is a neutral equilibrium point, but

        (
        0
        ,

          ω

            2

        ,
        0
        )

    {\displaystyle (0,\omega _{2},0)}

 is a saddle point.

Geometric analysis
During motion, both the energy and angular momentum-squared are conserved, thus we have two conserved quantities:

            {

                  2
                  E

                    ∑

                      i

                    I

                      i

                    ω

                      i

                      2

                    L

                      2

                    ∑

                      i

                    I

                      i

                      2

                    ω

                      i

                      2

    {\displaystyle {\begin{cases}2E=\sum {i}I{i}\omega _{i}^{2}\L^{2}=\sum {i}I{i}^{2}\omega _{i}^{2}\end{cases}}}

and so for any initial condition

        ω
        (
        0
        )

    {\displaystyle \omega (0)}

, the trajectory of

        ω
        (
        t
        )

    {\displaystyle \omega (t)}

 must stay on the intersection curve between two ellipsoids defined by

            {

                    ∑

                      i

                    I

                      i

                    ω

                      i

                      2

                    ∑

                      i

                    I

                      i

                    ω

                      i

                  (
                  0

                    )

                      2

                    ∑

                      i

                    I

                      i

                      2

                    ω

                      i

                      2

                    ∑

                      i

                    I

                      i

                      2

                    ω

                      i

                  (
                  0

                    )

                      2

    {\displaystyle {\begin{cases}\sum {i}I{i}\omega _{i}^{2}=\sum {i}I{i}\omega _{i}(0)^{2}\\sum {i}I{i}^{2}\omega _{i}^{2}=\sum {i}I{i}^{2}\omega _{i}(0)^{2}\end{cases}}}

This is shown on the animation to the right.
By inspecting Euler's equations, we see that

              ω
              ˙

        (
        t
        )

        0

    {\displaystyle {\dot {\omega }}(t)=0}

 implies that two components of

        ω
        (
        t
        )

    {\displaystyle \omega (t)}

 are zero—that is, the object is exactly spinning around one of the principal axes. In all other situations,

        ω
        (
        t
        )

    {\displaystyle \omega (t)}

 must remain in motion.
By Euler's equations, if

        ω
        (
        t
        )

    {\displaystyle \omega (t)}

 is a solution, then so is

        c
        ω
        (
        c
        t
        )

    {\displaystyle c\omega (ct)}

 for any constant

        c

        0

    {\displaystyle c>0}

. In particular, the motion of the body in free space (obtained by integrating

        c
        ω
        (
        c
        t
        )
        d
        t

    {\displaystyle c\omega (ct)dt}

) is exactly the same, just completed faster by a ratio of

        c

    {\displaystyle c}

.
Consequently, we can analyze the geometry of motion with a fixed value of

          L

            2

    {\displaystyle L^{2}}

, and vary

        ω
        (
        0
        )

    {\displaystyle \omega (0)}

 on the fixed ellipsoid of constant squared angular momentum. As

        ω
        (
        0
        )

    {\displaystyle \omega (0)}

 varies, the value of

        2
        E

    {\displaystyle 2E}

 also varies—thus giving us a varying ellipsoid of constant energy. This is shown in the animation as a fixed orange ellipsoid and increasing blue ellipsoid.
For concreteness, consider

          I

            1

        1
        ,

          I

            2

        2
        ,

          I

            3

        3

    {\displaystyle I_{1}=1,I_{2}=2,I_{3}=3}

, then the angular momentum ellipsoid's major axes are in ratios of

        1
        :
        1

          /

        2
        :
        1

          /

        3

    {\displaystyle 1:1/2:1/3}

, and the energy ellipsoid's major axes are in ratios of

        1
        :
        1

          /

            2

        :
        1

          /

            3

    {\displaystyle 1:1/{\sqrt {2}}:1/{\sqrt {3}}}

. Thus the angular momentum ellipsoid is both flatter and sharper, as visible in the animation. In general, the angular momentum ellipsoid is always more "exaggerated" than the energy ellipsoid.
Now inscribe on a fixed ellipsoid of

          L

            2

    {\displaystyle L^{2}}

 its intersection curves with the ellipsoid of

        2
        E

    {\displaystyle 2E}

, as

        2
        E

    {\displaystyle 2E}

 increases from zero to infinity. We can see that the curves evolve as follows:

For small energy, there is no intersection, since we need a minimum of energy to stay on the angular momentum ellipsoid.
The energy ellipsoid first intersects the momentum ellipsoid when

        2
        E

          L

            2

          /

          I

            3

    {\displaystyle 2E=L^{2}/I_{3}}

, at the points

        (
        0
        ,
        0
        ,
        ±
        L

          /

          I

            3

        )

    {\displaystyle (0,0,\pm L/I_{3})}

. This is when the body rotates around its axis with the largest moment of inertia.
They intersect at two cycles around the points

        (
        0
        ,
        0
        ,
        ±
        L

          /

          I

            3

        )

    {\displaystyle (0,0,\pm L/I_{3})}

. Since each cycle contains no point at which

              ω
              ˙

        0

    {\displaystyle {\dot {\omega }}=0}

, the motion of

        ω
        (
        t
        )

    {\displaystyle \omega (t)}

 must be a periodic motion around each cycle.
They intersect at two "diagonal" curves that intersects at the points

        (
        0
        ,
        ±
        L

          /

          I

            2

        ,
        0
        )

    {\displaystyle (0,\pm L/I_{2},0)}

, when

        2
        E

          L

            2

          /

          I

            2

    {\displaystyle 2E=L^{2}/I_{2}}

. If

        ω
        (
        t
        )

    {\displaystyle \omega (t)}

 starts anywhere on the diagonal curves, it would approach one of the points, distance exponentially decreasing, but never actually reach the point. In other words, we have 4 heteroclinic orbits between the two saddle points.
They intersect at two cycles around the points

        (
        ±
        L

          /

          I

            1

        ,
        0
        ,
        0
        )

    {\displaystyle (\pm L/I_{1},0,0)}

. Since each cycle contains no point at which

              ω
              ˙

        0

    {\displaystyle {\dot {\omega }}=0}

, the motion of

        ω
        (
        t
        )

    {\displaystyle \omega (t)}

 must be a periodic motion around each cycle.
The energy ellipsoid last intersects the momentum ellipsoid when

        2
        E

          L

            2

          /

          I

            1

    {\displaystyle 2E=L^{2}/I_{1}}

, at the points

        (
        ±
        L

          /

          I

            1

        ,
        0
        ,
        0
        )

    {\displaystyle (\pm L/I_{1},0,0)}

. This is when the body rotates around its axis with the smallest moment of inertia.
The tennis racket effect occurs when

        ω
        (
        0
        )

    {\displaystyle \omega (0)}

 is very close to a saddle point. The body would linger near the saddle point, then rapidly move to the other saddle point, near

        ω
        (
        T

          /

        2
        )

    {\displaystyle \omega (T/2)}

, linger again for a long time, and so on. The motion repeats with period

        T

    {\displaystyle T}

.
The above analysis is all done in the perspective of an observer which is rotating with the body. An observer watching the body's motion in free space would see its angular momentum vector

              L
              →

        I

              ω
              →

    {\displaystyle {\vec {L}}=I{\vec {\omega }}}

 conserved, while both its angular velocity vector

              ω
              →

        (
        t
        )

    {\displaystyle {\vec {\omega }}(t)}

 and its moment of inertia

        I
        (
        t
        )

    {\displaystyle I(t)}

 undergo complicated motions in space. At the beginning, the observer would see both

              ω
              →

        (
        0
        )
        ,

              L
              →

    {\displaystyle {\vec {\omega }}(0),{\vec {L}}}

 mostly aligned with the second major axis of

        I
        (
        0
        )

    {\displaystyle I(0)}

. After a while, the body performs a complicated motion and ends up with

        I
        (
        T

          /

        2
        )
        ,

              ω
              →

        (
        T

          /

        2
        )

    {\displaystyle I(T/2),{\vec {\omega }}(T/2)}

, and again both

              L
              →

        ,

              ω
              →

        (
        T

          /

        2
        )

    {\displaystyle {\vec {L}},{\vec {\omega }}(T/2)}

 are mostly aligned with the second major axis of

        I
        (
        T

          /

        2
        )

    {\displaystyle I(T/2)}

.
Consequently, there are two possibilities: either the rigid body's second major axis is in the same direction, or it has reversed direction. If it is still in the same direction, then

              ω
              →

        (
        0
        )
        ,

              ω
              →

        (
        T

          /

        2
        )

    {\displaystyle {\vec {\omega }}(0),{\vec {\omega }}(T/2)}

 viewed in the rigid body's reference frame are also mostly in the same direction. However, we have just seen that

        ω
        (
        0
        )

    {\displaystyle \omega (0)}

 and

        ω
        (
        T

          /

        2
        )

    {\displaystyle \omega (T/2)}

 are near opposite saddle points

        (
        0
        ,
        ±
        L

          /

          I

            2

        ,
        0
        )

    {\displaystyle (0,\pm L/I_{2},0)}

. Contradiction.
Qualitatively, then, this is what an observer watching in free space would observe:

The body rotates around its second major axis for a while.
The body rapidly undergoes a complicated motion, until its second major axis has reversed direction.
The body rotates around its second major axis again for a while. Repeat.
This can be easily seen in the video demonstration in microgravity.

With dissipation
When the body is not exactly rigid, but can flex and bend or contain liquid that sloshes around, it can dissipate energy through its internal degrees of freedom. In this case, the body still has constant angular momentum, but its energy would decrease, until it reaches the minimal point. As analyzed geometrically above, this happens when the body's angular velocity is exactly aligned with its axis of maximal moment of inertia.
This happened to Explorer 1, the first satellite launched by the United States in 1958. The elongated body of the spacecraft had been designed to spin about its long (least-inertia) axis but refused to do so, and instead started precessing due to energy dissipation from flexible structural elements. It also played a role in the near-loss of the joint NASA-ESA Solar and Heliospheric Observatory in 1998, when an unintentional spin about the spacecraft-Sun axis destabilized the control laws, leading to the spacecraft tumbling until internal dissipation (in its liquid hydrazine tanks) caused it to settle around its maximum moment axis, such that the Sun remained in the plane of the solar array.
In general, celestial bodies larger than a few kilometres in diameter converge to a constant rotation around their axes of maximal moment of inertia. Whenever a celestial body is found in a complex rotational state, its rotation is either destabilized by a recent impact or fragmentation event; or externally torqued, for instance by tidal interactions with other bodies or the YORP effect. Smaller asteroids cannot damp rotational energy quickly enough to prevent chaotic rotation driven by YORP forces.
