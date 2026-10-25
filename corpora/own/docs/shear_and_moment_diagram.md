# Shear and moment diagram

Shear and moment diagram

Shear force and bending moment diagrams are analytical tools used in conjunction with structural analysis to help perform structural design by determining the value of shear forces and bending moments at a given point of a structural element such as a beam. These diagrams can be used to easily determine the type, size, and material of a member in a structure so that a given set of loads can be supported without structural failure. Another application of shear and moment diagrams is that the deflection of a beam can be easily determined using either the moment area method or the conjugate beam method. For common loading cases such as simply supported beams subjected to uniformly distributed loads, closed-form elastic solutions are widely used in practice to verify shear force, bending moment, and deflection behavior.

Convention
Although these conventions are relative and any convention can be used if stated explicitly, practicing engineers have adopted a standard convention used in design practices.

Normal convention
The normal convention used in most engineering applications is to label a positive shear force - one that spins an element clockwise (up on the left, and down on the right). Likewise the normal convention for a positive bending moment is to warp the element in a "u" shape manner (Clockwise on the left, and counterclockwise on the right). Another way to remember this is if the moment is bending the beam into a "smile" then the moment is positive, with compression at the top of the beam and tension on the bottom.

 This convention was selected to simplify the analysis of beams. Since a horizontal member is usually analyzed from left to right and positive in the vertical direction is normally taken to be up, the positive shear convention was chosen to be up from the left, and to make all drawings consistent down from the right. The positive bending convention was chosen such that a positive shear force would tend to create a positive moment.

Alternative drawing convention
In structural engineering and in particular concrete design the positive moment is drawn on the tension side of the member. This convention puts the positive moment below the beam described above. A convention of placing moment diagram on the tension side allows for frames to be dealt with more easily and clearly. Additionally, placing the moment on the tension side of the member shows the general shape of the deformation and indicates on which side of a concrete member rebar should be placed, as concrete is weak in tension.

Relationships among load, shear, and moment diagrams
Since this method can easily become unnecessarily complicated with relatively simple problems, it can be quite helpful to understand different relations between the loading, shear, and moment diagram. The first of these is the relationship between a distributed load on the loading diagram and the shear diagram. Since a distributed load varies the shear load according to its magnitude it can be derived that the slope of the shear diagram is equal to the magnitude of the distributed load. The relationship, described by Schwedler's theorem, between distributed load and shear force magnitude is:

              d
              Q

              d
              x

        −
        q

    {\displaystyle {\frac {dQ}{dx}}=-q}

Some direct results of this is that a shear diagram will have a point change in magnitude if a point load is applied to a member, and a linearly varying shear magnitude as a result of a constant distributed load.
Similarly it can be shown that the slope of the moment diagram at a given point is equal to the magnitude of the shear diagram at that distance. The relationship between distributed shear force and bending moment is:

              d
              M

              d
              x

        Q

    {\displaystyle {\frac {dM}{dx}}=Q}

A direct result of this is that at every point the shear diagram crosses zero the moment diagram will have a local maximum or minimum. Also if the shear diagram is zero over a length of the member, the moment diagram will have a constant value over that length. By calculus it can be shown that a point load will lead to a linearly varying moment diagram, and a constant distributed load will lead to a quadratic moment diagram.

Practical considerations
In practical applications the entire stepwise function is rarely written out. The only parts of the stepwise function that would be written out are the moment equations in a nonlinear portion of the moment diagram; this occurs whenever a distributed load is applied to the member. For constant portions the value of the shear and/or moment diagram is written right on the diagram, and for linearly varying portions of a member the beginning value, end value, and slope or the portion of the member are all that are required.
