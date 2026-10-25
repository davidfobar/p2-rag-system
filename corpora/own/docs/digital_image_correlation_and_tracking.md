# Digital image correlation and tracking

Digital image correlation and tracking

Digital image correlation and tracking is an optical method that employs tracking and image registration techniques for accurate 2D and 3D measurements of changes in 2D images or 3D volumes. This method is often used to measure full-field displacement and strains, and it is widely applied in many areas of science and engineering. Compared to strain gauges and extensometers, digital image correlation methods provide finer details about deformation, due to the ability to provide both local and average data.

Overview
Digital image correlation (DIC) techniques have been increasing in popularity, especially in micro- and nano-scale mechanical testing applications due to their relative ease of implementation and use. Advances in computer technology and digital cameras have been the enabling technologies for this method and while white-light optics has been the predominant approach, DIC can be and has been extended to almost any imaging technology.
The concept of using cross-correlation to measure shifts in datasets has been known for a long time, and it has been applied to digital images since at least the early 1970s. The present-day applications are almost innumerable, including image analysis, image compression, velocimetry, and strain estimation. Much early work in DIC in the field of mechanics was led by researchers at the University of South Carolina in the early 1980s and has been optimized and improved in recent years. Commonly, DIC relies on finding the maximum of the correlation array between pixel intensity array subsets on two or more corresponding images, which gives the integer translational shift between them. It is also possible to estimate shifts to a finer resolution than the resolution of the original images, which is often called "sub-pixel" registration because the measured shift is smaller than an integer pixel unit. For sub-pixel interpolation of the shift, other methods do not simply maximize the correlation coefficient. An iterative approach can also be used to maximize the interpolated correlation coefficient by using non-linear optimization techniques. The non-linear optimization approach tends to be conceptually simpler and can handle large deformations more accurately, but as with most nonlinear optimization techniques, it is slower.
The two-dimensional discrete cross correlation

          r

            i
            j

    {\displaystyle r_{ij}}

 can be defined in several ways, one possibility being:

          r

            i
            j

                ∑

                  m

                ∑

                  n

              [
              f
              (
              m
              +
              i
              ,
              n
              +
              j
              )
              −

                    f
                    ¯

              ]
              [
              g
              (
              m
              ,
              n
              )
              −

                    g
                    ¯

              ]

                ∑

                  m

                ∑

                  n

                [
                f
                (
                m
                ,
                n
                )
                −

                      f
                      ¯

                  ]

                    2

                ∑

                  m

                ∑

                  n

                [
                g
                (
                m
                ,
                n
                )
                −

                      g
                      ¯

                  ]

                    2

        .

    {\displaystyle r_{ij}={\frac {\sum _{m}\sum _{n}[f(m+i,n+j)-{\bar {f}}][g(m,n)-{\bar {g}}]}{\sqrt {\sum _{m}\sum _{n}{[f(m,n)-{\bar {f}}]^{2}}\sum _{m}\sum _{n}{[g(m,n)-{\bar {g}}]^{2}}}}}.}

Here f(m, n) is the pixel intensity or the gray-scale value at a point (m, n) in the original image, g(m, n) is the gray-scale value at a point (m, n) in the translated image,

              f
              ¯

    {\displaystyle {\bar {f}}}

 and

              g
              ¯

    {\displaystyle {\bar {g}}}

 are mean values of the intensity matrices f and g respectively.
However, in practical applications, the correlation array is usually computed using Fourier-transform methods, since the fast Fourier transform is a much faster method than directly computing the correlation.

          F

            F

        {
        f
        }
        ,

          G

            F

        {
        g
        }
        .

    {\displaystyle \mathbf {F} ={\mathcal {F}}{f},\quad \mathbf {G} ={\mathcal {F}}{g}.}

Then taking the complex conjugate of the second result and multiplying the Fourier transforms together elementwise, we obtain the Fourier transform of the correlogram,

        R

    {\displaystyle \ R}

:

        R

          F

        ∘

            G

            ∗

        ,

    {\displaystyle R=\mathbf {F} \circ \mathbf {G} ^{*},}

where

        ∘

    {\displaystyle \circ }

 is the Hadamard product (entry-wise product). It is also fairly common to normalize the magnitudes to unity at this point, which results in a variation called phase correlation.
Then the cross-correlation is obtained by applying the inverse Fourier transform:

        r

              F

            −
            1

        {
        R
        }
        .

    {\displaystyle \ r={\mathcal {F}}^{-1}{R}.}

At this point, the coordinates of the maximum of

          r

            i
            j

    {\displaystyle r_{ij}}

 give the integer shift:

        (
        Δ
        x
        ,
        Δ
        y
        )

        arg
        ⁡

          max

            (
            i
            ,
            j
            )

        {
        r
        }
        .

    {\displaystyle (\Delta x,\Delta y)=\arg \max _{(i,j)}{r}.}

Deformation mapping
For deformation mapping, the mapping function that relates the images can be derived from comparing a set of subwindow pairs over the whole images. (Figure 1). The coordinates or grid points (xi, yj) and (xi*, yj*) are related by the translations that occur between the two images. If the deformation is small and perpendicular to the optical axis of the camera, then the relation between (xi, yj) and (xi*, yj*) can be approximated by a 2D affine transformation such as:

          x

            ∗

        x
        +
        u
        +

              ∂
              u

              ∂
              x

        Δ
        x
        +

              ∂
              u

              ∂
              y

        Δ
        y
        ,

    {\displaystyle x^{*}=x+u+{\frac {\partial u}{\partial x}}\Delta x+{\frac {\partial u}{\partial y}}\Delta y,}

          y

            ∗

        y
        +
        v
        +

              ∂
              v

              ∂
              x

        Δ
        x
        +

              ∂
              v

              ∂
              y

        Δ
        y
        .

    {\displaystyle y^{*}=y+v+{\frac {\partial v}{\partial x}}\Delta x+{\frac {\partial v}{\partial y}}\Delta y.}

Here u and v are translations of the center of the sub-image in the X and Y directions respectively. The distances from the center of the sub-image to the point (x, y) are denoted by

        Δ
        x

    {\displaystyle \Delta x}

 and

        Δ
        y

    {\displaystyle \Delta y}

. Thus, the correlation coefficient rij is a function of displacement components (u, v) and displacement gradients

              ∂
              u

              ∂
              x

        ,

              ∂
              u

              ∂
              y

        ,

              ∂
              v

              ∂
              x

        ,

              ∂
              v

              ∂
              y

        .

    {\displaystyle {\frac {\partial u}{\partial x}},{\frac {\partial u}{\partial y}},{\frac {\partial v}{\partial x}},{\frac {\partial v}{\partial y}}.}

DIC has proven to be very effective at mapping deformation in macroscopic mechanical testing, where the application of specular markers (e.g. paint, toner powder) or surface finishes from machining and polishing provide the needed contrast to correlate images well. However, these methods for applying surface contrast do not extend to the application of free-standing thin films for several reasons. First, vapor deposition at normal temperatures on semiconductor grade substrates results in mirror-finish quality films with RMS roughnesses that are typically on the order of several nanometers. No subsequent polishing or finishing steps are required, and unless electron imaging techniques are employed that can resolve microstructural features, the films do not possess enough useful surface contrast to adequately correlate images. Typically this challenge can be circumvented by applying paint that results in a random speckle pattern on the surface, although the large and turbulent forces resulting from either spraying or applying paint to the surface of a free-standing thin film are too high and would break the specimens. In addition, the sizes of individual paint particles are on the order of μms, while the film thickness is only several hundred nanometers, which would be analogous to supporting a large boulder on a thin sheet of paper.

Digital volume correlation
Digital Volume Correlation (DVC, and sometimes called Volumetric-DIC) extends the 2D-DIC algorithms into three dimensions to calculate the full-field 3D deformation from a pair of 3D images. This technique is distinct from 3D-DIC, which only calculates the 3D deformation of an exterior surface using conventional optical images. The DVC algorithm is able to track full-field displacement information in the form of voxels instead of pixels. The theory is similar to above except that another dimension is added: the z-dimension. The displacement is calculated from the correlation of 3D subsets of the reference and deformed volumetric images, which is analogous to the correlation of 2D subsets described above.
DVC can be performed using volumetric image datasets. These images can be obtained using confocal microscopy, X-ray computed tomography, Magnetic Resonance Imaging or other techniques. Similar to the other DIC techniques, the images must exhibit a distinct, high-contrast 3D "speckle pattern" to ensure accurate displacement measurement.
DVC was first developed in 1999 to study the deformation of trabecular bone using X-ray computed tomography images. Since then, applications of DVC have grown to include granular materials, metals, foams, composites and biological materials. To date it has been used with images acquired by MRI imaging, Computer Tomography (CT), micro-CT, confocal microscopy, and lightsheet microscopy. DVC is currently considered to be ideal in the research world for 3D quantification of local displacements, strains, and stress in biological specimens. It is preferred because of the non-invasiveness of the method over traditional experimental methods.
Two of the key challenges are improving the speed and reliability of the DVC measurement. The 3D imaging techniques produce noisier images than conventional 2D optical images, which reduces the quality of the displacement measurement. Computational speed is restricted by the file sizes of 3D images, which are significantly larger than 2D images. For example, an 8-bit (1024x1024) pixel 2D image has a file size of 1 MB, while an 8-bit (1024x1024x1024) voxel 3D image has a file size of 1 GB. This can be partially offset using parallel computing.

Uses
Digital image correlation has demonstrated uses in the following industries:

Automotive
Aerospace
Biological
Industrial
Research and Education
Government and Military
Biomechanics
Robotics
Electronics
It has also been used for mapping earthquake deformation.

DIC Standardization
The International Digital Image Correlation Society (iDICs) is a body composed of members from academia, government, and industry, and is involved in training and educating end-users about DIC systems and the standardization of DIC practice for general applications. Created in 2015, the iDIC has been focused on creating standardizations for DIC users.
