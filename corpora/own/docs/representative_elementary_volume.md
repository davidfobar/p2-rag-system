# Representative elementary volume

Representative elementary volume

In the theory of composite materials, the representative elementary volume (REV) (also called the representative volume element (RVE) or the unit cell) is the smallest volume over which a measurement can be made that will yield a value representative of the whole. In the case of periodic materials, one simply chooses a periodic unit cell (which, however, may be non-unique), but in random media, the situation is much more complicated. For volumes smaller than the RVE, a representative property cannot be defined and the continuum description of the material involves Statistical Volume Element (SVE) and random fields. The property of interest can include mechanical properties such as elastic moduli, hydrogeological properties, electromagnetic properties, thermal properties, and other averaged quantities that are used to describe physical systems.

Definition

Rodney Hill defined the RVE as a sample of a heterogeneous material that:

"is entirely typical of the whole mixture on average", and
"contains a sufficient number of inclusions for the apparent properties to be independent of the surface values of traction and displacement, so long as these values are macroscopically uniform."
In essence, statement (1) is about the material's statistics (i.e. spatially homogeneous and ergodic), while statement (2) is a pronouncement on the independence of effective constitutive response with respect to the applied boundary conditions.
Both of these are issues of mesoscale (L) of the domain of random microstructure over which smoothing (or homogenization) is being done relative to the microscale (d). As L/d goes to infinity, the RVE is obtained, while any finite mesoscale involves statistical scatter and, therefore, describes an SVE. With these considerations one obtains bounds on effective (macroscopic) response of elastic (non)linear and inelastic random microstructures. In general, the stronger the mismatch in material properties, or the stronger the departure from elastic behavior, the larger is the RVE. The finite-size scaling of elastic material properties from SVE to RVE can be grasped in compact forms with the help of scaling functions universally based on stretched exponentials. Considering that the SVE may be placed anywhere in the material domain, one arrives at a technique for characterization of continuum random fields.
Another definition of the RVE was proposed by Drugan and Willis:

"It is the smallest material volume element of the composite for which the usual spatially constant (overall modulus) macroscopic constitutive representation is a sufficiently accurate model to represent mean constitutive response."
The choice of RVE can be quite a complicated process. The existence of a RVE assumes that it is possible to replace a heterogeneous material with an equivalent homogeneous material. This assumption implies that the volume should be large enough to represent the microstructure without introducing non-existing macroscopic properties (such as anisotropy in a macroscopically isotropic material). On the other hand, the sample should be small enough to be analyzed analytically or numerically.

Examples

For mechanical properties

In continuum mechanics generally for a heterogeneous material, RVE can be considered as a volume V that represents a composite statistically, i.e., volume that effectively includes a sampling of all microstructural heterogeneities (grains, inclusions, voids, fibers, etc.) that occur in the composite. It must however remain small enough to be considered as a volume element of continuum mechanics. Several types of boundary conditions can be prescribed on V to impose a given mean strain or mean stress to the material element.
One of the tools available to calculate the elastic properties of an RVE is the use of the open-source EasyPBC ABAQUS plugin tool.
Analytical or numerical micromechanical analysis of fiber reinforced composites involves the study of a representative volume element (RVE). Although fibers are distributed randomly in real composites, many micromechanical models assume periodic arrangement of fibers from which RVE can be isolated in a straightforward manner. The RVE has the same elastic constants and fiber volume fraction as the composite. In general RVE can be considered same as a differential element with a large number of crystals.

For porous media
Establishing a given porous medium's properties requires measuring samples of the porous medium. If the sample is too small, the readings tend to oscillate. With increasing sample size, the oscillations begin to dampen out. Eventually the sample size will become large enough that readings are consistent. This sample size is referred to as the representative elementary volume.
If sample size is increased further, measurement will remain stable until the sample size gets large enough that it begins to include other hydrostratigraphic layers. This is referred to as the maximum elementary volume (MEV).
Groundwater flow equation has to be defined in an REV.

For electromagnetic media

While RVEs for electromagnetic media can have the same form as those for elastic or porous media, the fact that mechanical strength and stability are not concerns allow for a wide range of RVEs. In the adjacent figure, the RVE consists of a split-ring resonator and its surrounding backing material.

Alternatives
There does not exist one RVE size and depending on the studied mechanical properties, the RVE size can vary significantly. The concept of statistical volume element (SVE) and uncorrelated volume element (UVE) have been introduced as alternatives for RVE.

Statistical volume element (SVE)
Statistical volume element (SVE), which is also referred to as stochastic volume element in finite element analysis, takes into account the variability in the microstructure. Unlike RVE in which average value is assumed for all realizations, SVE can have a different value from one realization to another. SVE models have been developed to study polycrystalline microstructures. Grain features, including orientation, misorientation, grain size, grain shape, grain aspect ratio are considered in SVE model. SVE model was applied in the material characterization and damage prediction in microscale. Compared with RVE, SVE can provide a comprehensive representation of the microstructure of materials.

Uncorrelated volume element (UVE)
Uncorrelated volume element (UVE) is an extension of SVE which also considers the co-variance of adjacent microstructure to present an accurate length scale for stochastic modelling.
