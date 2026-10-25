# Free body diagram

Free body diagram

In physics and engineering, a free body diagram (FBD; also called a force diagram) is a graphical illustration used to visualize the applied forces, moments, and resulting reactions on a free body in a given condition. It depicts a body or connected bodies with all the applied forces and moments, and reactions, which act on the body(ies). The body may consist of multiple internal members (such as a truss), or be a compact body (such as a beam). A series of free bodies and other diagrams may be necessary to solve complex problems. Sometimes in order to calculate the resultant force graphically the applied forces are arranged as the edges of a polygon of forces or force polygon (see § Polygon of forces).

Free body

A body is said to be "free" when it is singled out from other bodies for the purposes of dynamic or static analysis. The object does not have to be "free" in the sense of being unforced, and it may or may not be in a state of equilibrium; rather, it is not fixed in place and is thus "free" to move in response to forces and torques it may experience.

Figure 1 shows, on the left, green, red, and blue widgets stacked on top of each other, and for some reason the red cylinder happens to be the body of interest. (It may be necessary to calculate the stress to which it is subjected, for example.) On the right, the red cylinder has become the free body. In figure 2, the interest has shifted to just the left half of the red cylinder and so now it is the free body on the right. The example illustrates the context sensitivity of the term "free body". A cylinder can be part of a free body, it can be a free body by itself, and, as it is composed of parts, any of those parts may be a free body in itself.
Figure 1 and 2 are not yet free body diagrams. In a completed free body diagram, the free body would be shown with forces acting on it.

Purpose
Free body diagrams are used to visualize forces and moments applied to a body and to calculate reactions in mechanics and design problems. These diagrams are frequently used both to determine the loading of individual structural components and to calculate internal forces within a structure. They are used by most engineering disciplines from biomechanics to Structural Engineering.
In the educational environment, a free body diagram is an important step in understanding certain topics, such as statics, dynamics and other forms of classical mechanics.

Features
A free body diagram is not a scaled drawing, it is a diagram. The symbols used in a free body diagram depends upon how a body is modeled.
Free body diagrams consist of:

A simplified version of the body (often a dot or a box)
Forces shown as straight arrows pointing in the direction they act on the body
Moments are shown as curves with an arrow head or a vector with two arrow heads pointing in the direction they act on the body
One or more reference coordinate systems
By convention, reactions to applied forces are shown with hash marks through the stem of the vector
The number of forces and moments shown depends upon the specific problem and the assumptions made. Common assumptions are neglecting air resistance and friction and assuming rigid body action.
In statics all forces and moments must balance to zero; the physical interpretation is that if they do not, the body is accelerating and the principles of statics do not apply. In dynamics the resultant forces and moments can be non-zero.
Free body diagrams may not represent an entire physical body. Portions of a body can be selected for analysis. This technique allows calculation of internal forces, making them appear external, allowing analysis. This can be used multiple times to calculate internal forces at different locations within a physical body.
For example, a gymnast performing the iron cross: modeling the ropes and person allows calculation of overall forces (body weight, neglecting rope weight, breezes, buoyancy, electrostatics, relativity, rotation of the earth, etc.). Then remove the person and show only one rope; you get force direction. Then only looking at the person the forces on the hand can be calculated. Now only look at the arm to calculate the forces and moments at the shoulders, and so on until the component you need to analyze can be calculated.

Modeling the body
A body may be modeled in three ways:

a particle. This model may be used when any rotational effects are zero or have no interest even though the body itself may be extended. The body may be represented by a small symbolic blob and the diagram reduces to a set of concurrent arrows. A force on a particle is a bound vector.
rigid extended. Stresses and strains are of no interest but rotational effects are. A force arrow should lie along the line of force, but where along the line is irrelevant. A force on an extended rigid body is a sliding vector.
non-rigid extended. The point of application of a force becomes crucial and has to be indicated on the diagram. A force on a non-rigid body is a bound vector. Some use the tail of the arrow to indicate the point of application. Others use the tip.

What is included
An FBD represents the body of interest and the external forces acting on it.

The body: This is usually a schematic depending on the body—particle/extended, rigid/non-rigid—and on what questions are to be answered. Thus if rotation of the body and torque is in consideration, an indication of size and shape of the body is needed. For example, the brake dive of a motorcycle cannot be found from a single point, and a sketch with finite dimensions is required.
The external forces: These are indicated by labelled arrows. In a fully solved problem, a force arrow is capable of indicating
the direction and the line of action
the magnitude
the point of application
a reaction, as opposed to an applied force, if a hash is present through the stem of the arrow
Often a provisional free body is drawn before everything is known. The purpose of the diagram is to help to determine magnitude, direction, and point of application of external loads. When a force is originally drawn, its length may not indicate the magnitude. Its line may not correspond to the exact line of action. Even its orientation may not be correct.
External forces known to have negligible effect on the analysis may be omitted after careful consideration (e.g. buoyancy forces of the air in the analysis of a chair, or atmospheric pressure on the analysis of a frying pan).
External forces acting on an object may include friction, gravity, normal force, drag, tension, or a human force due to pushing or pulling. When in a non-inertial reference frame (see coordinate system, below), fictitious forces, such as centrifugal pseudoforce are appropriate.
At least one coordinate system is always included, and chosen for convenience. Judicious selection of a coordinate system can make defining the vectors simpler when writing the equations of motion or statics. The x direction may be chosen to point down the ramp in an inclined plane problem, for example. In that case the friction force only has an x component, and the normal force only has a y component. The force of gravity would then have components in both the x and y directions: mgsin(θ) in the x and mgcos(θ) in the y, where θ is the angle between the ramp and the horizontal.

Exclusions
A free body diagram should not show:

Bodies other than the free body.
Constraints.
(The body is not free from constraints; the constraints have just been replaced by the forces and moments exerted on the body.)
Forces exerted by the free body.
(A diagram showing the forces exerted both on and by a body is likely to be confusing since all the forces will cancel out. By Newton's 3rd law if body A exerts a force on body B then B exerts an equal and opposite force on A. This should not be confused with the equal and opposite forces that are necessary to hold a body in equilibrium.)
Internal forces.
(For example, if an entire truss is being analyzed, the forces between the individual truss members are not included.)
Velocity or acceleration vectors.

Analysis
In an analysis, a free body diagram is used by summing all forces and moments (often accomplished along or about each of the axes). When the sum of all forces and moments is zero, the body is at rest or moving and/or rotating at a constant velocity, by Newton's first law. If the sum is not zero, then the body is accelerating in a direction or about an axis according to Newton's second law.

Forces not aligned to an axis

Determining the sum of the forces and moments is straightforward if they are aligned with coordinate axes, but it is more complex if some are not. It is convenient to use the components of the forces, in which case the symbols ΣFx and ΣFy are used instead of ΣF (the variable M is used for moments).
Forces and moments that are at an angle to a coordinate axis can be rewritten as two vectors that are equivalent to the original (or three, for three dimensional problems)—each vector directed along one of the axes (Fx) and (Fy).

Example: A block on an inclined plane
A simple free-body diagram, shown above, of a block on a ramp, illustrates this.

All external supports and structures have been replaced by the forces they generate. These include:
mg: the product of the mass of the block and the constant of gravitation acceleration: its weight.
N: the normal force of the ramp.
Ff: the friction force of the ramp.
The force vectors show the direction and point of application and are labelled with their magnitude.
It contains a coordinate system that can be used when describing the vectors.
Some care is needed in interpreting the diagram.

The normal force has been shown to act at the midpoint of the base, but if the block is in static equilibrium its true location is directly below the centre of mass, where the weight acts because that is necessary to compensate for the moment of the friction.
Unlike the weight and normal force, which are expected to act at the tip of the arrow, the friction force is a sliding vector and thus the point of application is not relevant, and the friction acts along the whole base.

Polygon of forces

In the case of two applied forces, their sum (resultant force) can be found graphically using a parallelogram of forces.
To graphically determine the resultant force of multiple forces, the acting forces can be arranged as edges of a polygon by attaching the beginning of one force vector to the end of another in an arbitrary order. Then the vector value of the resultant force would be determined by the missing edge of the polygon. In the diagram, the forces P1 to P6 are applied to the point O. The polygon is constructed starting with P1 and P2 using the parallelogram of forces (vertex a). The process is repeated (adding P3 yields the vertex b, etc.). The remaining edge of the polygon O-e represents the resultant force R.

Kinetic diagram

In dynamics a kinetic diagram is a pictorial device used in analyzing mechanics problems when there is determined to be a net force and/or moment acting on a body. They are related to and often used with free body diagrams, but depict only the net force and moment rather than all of the forces being considered.
Kinetic diagrams are not required to solve dynamics problems; their use in teaching dynamics is argued against by some in favor of other methods that they view as simpler. They appear in some dynamics texts but are absent in others.
