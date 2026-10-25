# Support polygon

Support polygon

For a rigid object in contact with a fixed environment and acted upon by gravity in the vertical direction, its support polygon is a horizontal region over which the center of mass must lie to achieve static stability. For example, for an object resting on a horizontal surface (e.g. a table), the support polygon is the convex hull of its "footprint" on the table.
The support polygon succinctly represents the conditions necessary for an object to be at equilibrium under gravity. That is, if the object's center of mass lies over the support polygon, then there exist a set of forces over the region of contact that exactly counteracts the forces of gravity. Note that this is a necessary condition for stability, but not a sufficient one.

Derivation
Source:
Let the object be in contact at a finite number of points

          C

            1

        ,
        …
        ,

          C

            N

    {\displaystyle C_{1},\ldots ,C_{N}}

. At each point

          C

            k

    {\displaystyle C_{k}}

, let

        F

          C

            k

    {\displaystyle FC_{k}}

 be the set of forces that can be applied on the object at that point. Here,

        F

          C

            k

    {\displaystyle FC_{k}}

 is known as the friction cone, and for the Coulomb model of friction, is actually a cone with apex at the origin, extending to infinity in the normal direction of the contact.
Let

          f

            1

        ,
        …
        ,

          f

            N

    {\displaystyle f_{1},\ldots ,f_{N}}

 be the (unspecified) forces at the contact points. To balance the object in static equilibrium, the following Newton-Euler equations must be met on

          f

            1

        ,
        …
        ,

          f

            N

    {\displaystyle f_{1},\ldots ,f_{N}}

:

          ∑

            k

            1

            N

          f

            k

        +
        G

        0

    {\displaystyle \sum {k=1}^{N}f{k}+G=0}

          ∑

            k

            1

            N

          f

            k

        ×

          C

            k

        +
        G
        ×
        C
        M

        0

    {\displaystyle \sum {k=1}^{N}f{k}\times C_{k}+G\times CM=0}

          f

            k

        ∈
        F

          C

            k

    {\displaystyle f_{k}\in FC_{k}}

 for all

        k

    {\displaystyle k}

where

        G

    {\displaystyle G}

 is the force of gravity on the object, and

        C
        M

    {\displaystyle CM}

 is its center of mass. The first two equations are the Newton-Euler equations, and the third requires all forces to be valid. If there is no set of forces

          f

            1

        ,
        …
        ,

          f

            N

    {\displaystyle f_{1},\ldots ,f_{N}}

 that meet all these conditions, the object will not be in equilibrium.
The second equation has no dependence on the vertical component of the center of mass, and thus if a solution exists for one

        C
        M

    {\displaystyle CM}

, the same solution works for all

        C
        M
        +
        α
        G

    {\displaystyle CM+\alpha G}

. Therefore, the set of all

        C
        M

    {\displaystyle CM}

 that have solutions to the above conditions is a set that extends infinitely in the up and down directions. The support polygon is simply the projection of this set on the horizontal plane.
These results can easily be extended to different friction models and an infinite number of contact points (i.e. a region of contact).

Properties
Even though the word "polygon" is used to describe this region, in general it can be any convex shape with curved edges. The support polygon is invariant under translations and rotations about the gravity vector (that is, if the contact points and friction cones were translated and rotated about the gravity vector, the support polygon is simply translated and rotated).
If the friction cones are convex cones (as they typically are), the support polygon is always a convex region. It is also invariant to the mass of the object (provided it is nonzero).
If all contacts lie on a (not necessarily horizontal) plane, and the friction cones at all contacts contain the negative gravity vector

        −
        G

    {\displaystyle -G}

, then the support polygon is the convex hull of the contact points projected onto the horizontal plane.
