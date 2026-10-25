# Moving frame

Moving frame

In mathematics, a moving frame is a flexible generalization of the notion of a coordinate frame (an ordered basis of a vector space, in conjunction with an origin) often used to study the extrinsic differential geometry of smooth manifolds embedded in a homogeneous space.

Introduction
In lay terms, a frame of reference is a system of measuring rods used by an observer to measure the surrounding space by providing coordinates. A moving frame is then a frame of reference which moves with the observer along a trajectory (a curve). The method of the moving frame, in this simple example, seeks to produce a "preferred" moving frame out of the kinematic properties of the observer. In a geometrical setting, this problem was solved in the mid 19th century by Jean Frédéric Frenet and Joseph Alfred Serret. The Frenet–Serret frame is a moving frame defined on a curve which can be constructed purely from the velocity and acceleration of the curve.
The Frenet–Serret frame plays a key role in the differential geometry of curves, ultimately leading to a more or less complete classification of smooth curves in Euclidean space up to congruence. The Frenet–Serret formulas show that there is a pair of functions defined on the curve, the torsion and curvature, which are obtained by differentiating the frame, and which describe completely how the frame evolves in time along the curve. A key feature of the general method is that a preferred moving frame, provided it can be found, gives a complete kinematic description of the curve.

In the late 19th century, Gaston Darboux studied the problem of constructing a preferred moving frame on a surface in Euclidean space instead of a curve, the Darboux frame (or the trièdre mobile as it was then called). It turned out to be impossible in general to construct such a frame, and that there were integrability conditions which needed to be satisfied first.
Later, moving frames were developed extensively by Élie Cartan and others in the study of submanifolds of more general homogeneous spaces (such as projective space). In this setting, a frame carries the geometric idea of a basis of a vector space over to other sorts of geometrical spaces (Klein geometries). Some examples of frames are:

A linear frame is an ordered basis of a vector space.
An orthonormal frame of a vector space is an ordered basis consisting of orthogonal unit vectors (an orthonormal basis).
An affine frame of an affine space consists of a choice of origin along with an ordered basis of vectors in the associated difference space.
A Cartesian frame of an affine space is a choice of origin along with an orthonormal basis of the difference space.
A projective frame on n-dimensional projective space is an ordered collection of n+2 points such that any subset of n+1 points is linearly independent.
Frame fields in general relativity are four-dimensional frames, or vierbeins, in German.
In each of these examples, the collection of all frames is homogeneous in a certain sense. In the case of linear frames, for instance, any two frames are related by an element of the general linear group. Projective frames are related by the projective linear group. This homogeneity, or symmetry, of the class of frames captures the geometrical features of the linear, affine, Euclidean, or projective landscape. A moving frame, in these circumstances, is just that: a frame which varies from point to point.
Formally, a frame on a homogeneous space G/H consists of a point in the tautological bundle G → G/H. A moving frame is a section of this bundle. It is moving in the sense that as the point of the base varies, the frame in the fibre changes by an element of the symmetry group G. A moving frame on a submanifold M of G/H is a section of the pullback of the tautological bundle to M. Intrinsically a moving frame can be defined on a principal bundle P over a manifold. In this case, a moving frame is given by a G-equivariant mapping φ : P → G, thus framing the manifold by elements of the Lie group G.
One can extend the notion of frames to a more general case: one can "solder" a fiber bundle to a smooth manifold, in such a way that the fibers behave as if they were tangent. When the fiber bundle is a homogenous space, this reduces to the above-described frame-field. When the homogenous space is a quotient of special orthogonal groups, this reduces to the standard conception of a vierbein.
Although there is a substantial formal difference between extrinsic and intrinsic moving frames, they are both alike in the sense that a moving frame is always given by a mapping into G. The strategy in Cartan's method of moving frames, as outlined briefly in Cartan's equivalence method, is to find a natural moving frame on the manifold and then to take its Darboux derivative, in other words pullback the Maurer-Cartan form of G to M (or P), and thus obtain a complete set of structural invariants for the manifold.

Method of the moving frame

Cartan (1937) formulated the general definition of a moving frame and the method of the moving frame, as elaborated by Weyl (1938). The elements of the theory are

A Lie group G.
A Klein space X whose group of geometric automorphisms is G.
A smooth manifold Σ which serves as a space of (generalized) coordinates for X.
A collection of frames ƒ each of which determines a coordinate function from X to Σ (the precise nature of the frame is left vague in the general axiomatization).
The following axioms are then assumed to hold between these elements:

There is a free and transitive group action of G on the collection of frames: it is a principal homogeneous space for G. In particular, for any pair of frames ƒ and ƒ′, there is a unique transition of frame (ƒ→ƒ′) in G determined by the requirement (ƒ→ƒ′)ƒ = ƒ′.
Given a frame ƒ and a point A ∈ X, there is associated a point x = (A,ƒ) belonging to Σ. This mapping determined by the frame ƒ is a bijection from the points of X to those of Σ. This bijection is compatible with the law of composition of frames in the sense that the coordinate x′ of the point A in a different frame ƒ′ arises from (A,ƒ) by application of the transformation (ƒ→ƒ′). That is,

        (
        A
        ,

          f
          ′

        )

        (
        f
        →

          f
          ′

        )
        ∘
        (
        A
        ,
        f
        )
        .

    {\displaystyle (A,f')=(f\to f')\circ (A,f).}

Of interest to the method are parameterized submanifolds of X. The considerations are largely local, so the parameter domain is taken to be an open subset of Rλ. Slightly different techniques apply depending on whether one is interested in the submanifold along with its parameterization, or the submanifold up to reparameterization.

Moving tangent frames

The most commonly encountered case of a moving frame is for the bundle of tangent frames (also called the frame bundle) of a manifold. In this case, a moving tangent frame on a manifold M consists of a collection of vector fields e1, e2, …, en forming a basis of the tangent space at each point of an open set U ⊂ M.
If

        (

          x

            1

        ,

          x

            2

        ,
        …
        ,

          x

            n

        )

    {\displaystyle (x^{1},x^{2},\dots ,x^{n})}

 is a coordinate system on U, then each vector field ej can be expressed as a linear combination of the coordinate vector fields

            ∂

              ∂

                x

                  i

    {\textstyle {\frac {\partial }{\partial x^{i}}}}

:

          e

            j

          ∑

            i

            1

            n

          A

            j

            i

            ∂

              ∂

                x

                  i

        ,

    {\displaystyle e_{j}=\sum {i=1}^{n}A{j}^{i}{\frac {\partial }{\partial x^{i}}},}

where each

          A

            j

            i

    {\displaystyle A_{j}^{i}}

 is a function on U. These can be seen as the components of a matrix

        A

    {\displaystyle A}

. This matrix is useful for finding the coordinate expression of the dual coframe, as explained in the next section.

Coframes
A moving frame determines a dual frame or coframe of the cotangent bundle over U, which is sometimes also called a moving frame. This is a n-tuple of smooth 1-forms

θ1, θ2, …, θn
which are linearly independent at each point q in U. Conversely, given such a coframe, there is a unique moving frame e1, e2, …, en which is dual to it, i.e., satisfies the duality relation θi(ej) = δij, where δij is the Kronecker delta function on U.
If

        (

          x

            1

        ,

          x

            2

        ,
        …
        ,

          x

            n

        )

    {\displaystyle (x^{1},x^{2},\dots ,x^{n})}

 is a coordinate system on U, as in the preceding section, then each covector field θi can be expressed as a linear combination of the coordinate covector fields

        d

          x

            i

    {\displaystyle dx^{i}}

:

          θ

            i

          ∑

            j

            1

            n

          B

            j

            i

        d

          x

            j

        ,

    {\displaystyle \theta ^{i}=\sum {j=1}^{n}B{j}^{i}dx^{j},}

where each

          B

            j

            i

    {\displaystyle B_{j}^{i}}

 is a function on U. Since

        d

          x

            i

          (

              ∂

                ∂

                  x

                    j

          )

          δ

            j

            i

    {\textstyle dx^{i}\left({\frac {\partial }{\partial x^{j}}}\right)=\delta _{j}^{i}}

, the two coordinate expressions above combine to yield

          ∑

            k

            1

            n

          B

            k

            i

          A

            j

            k

          δ

            j

            i

    {\textstyle \sum {k=1}^{n}B{k}^{i}A_{j}^{k}=\delta _{j}^{i}}

; in terms of matrices, this just says that

        A

    {\displaystyle A}

 and

        B

    {\displaystyle B}

 are inverses of each other.
In the setting of classical mechanics, when working with canonical coordinates, the canonical coframe is given by the tautological one-form. Intuitively, it relates the velocities of a mechanical system (given by vector fields on the tangent bundle of the coordinates) to the corresponding momenta of the system (given by vector fields in the cotangent bundle; i.e. given by forms). The tautological one-form is a special case of the more general solder form, which provides a (co-)frame field on a general fiber bundle.

Uses
Moving frames are important in general relativity, where there is no privileged way of extending a choice of frame at an event p (a point in spacetime, which is a manifold of dimension four) to nearby points, and so a choice must be made. In contrast in special relativity, M is taken to be a vector space V (of dimension four). In that case a frame at a point p can be translated from p to any other point q in a well-defined way. Broadly speaking, a moving frame corresponds to an observer, and the distinguished frames in special relativity represent inertial observers.
In relativity and in Riemannian geometry, the most useful kind of moving frames are the orthogonal and orthonormal frames, that is, frames consisting of orthogonal (unit) vectors at each point. At a given point p a general frame may be made orthonormal by orthonormalization; in fact this can be done smoothly, so that the existence of a moving frame implies the existence of a moving orthonormal frame.

Further details
A moving frame always exists locally, i.e., in some neighbourhood U of any point p in M; however, the existence of a moving frame globally on M requires topological conditions. For example when M is a circle, or more generally a torus, such frames exist; but not when M is a 2-sphere. A manifold that does have a global moving frame is called parallelizable. Note for example how the unit directions of latitude and longitude on the Earth's surface break down as a moving frame at the north and south poles.
The method of moving frames of Élie Cartan is based on taking a moving frame that is adapted to the particular problem being studied. For example, given a curve in space, the first three derivative vectors of the curve can in general define a frame at a point of it (cf. torsion tensor for a quantitative description – it is assumed here that the torsion is not zero). In fact, in the method of moving frames, one more often works with coframes rather than frames. More generally, moving frames may be viewed as sections of principal bundles over open sets U. The general Cartan method exploits this abstraction using the notion of a Cartan connection.

Atlases
In many cases, it is impossible to define a single frame of reference that is valid globally. To overcome this, frames are commonly pieced together to form an atlas, thus arriving at the notion of a local frame. In addition, it is often desirable to endow these atlases with a smooth structure, so that the resulting frame fields are differentiable.

Generalizations
Although this article constructs the frame fields as a coordinate system on the tangent bundle of a manifold, the general ideas move over easily to the concept of a vector bundle, which is a manifold endowed with a vector space at each point, that vector space being arbitrary, and not in general related to the tangent bundle.

Applications

Body-fixed frames are widely used in rigid body mechanics.
Aircraft maneuvers can be expressed in terms of the moving frame (aircraft principal axes) when described by the pilot.
