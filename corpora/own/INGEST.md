# Ingest report

Written by `uv run p2 ingest`.
It lists every document in this corpus that ingest added, with what the cleaning pass did and anything that looks wrong.
Running ingest again adds to the table and replaces the "last run" section, and `uv run p2 ingest --report` rewrites it for the documents in docs/ now, after you removed some.

## Summary

- Documents: 249 (the final check needs at least 200)
- Words: 476,132
- Estimated tokens (words times 1.4): 666,584 (`p2 check` warns above 800,000 and fails above 1,000,000)
- Flagged documents: 0

## Documents

| docid | words | characters per page | flags | cleaning |
|---|---:|---:|---|---|
| `absolute_rotation` | 1,001 | - | - | - |
| `acceleration` | 2,909 | - | - | - |
| `accretion_-astrophysics` | 2,407 | - | - | - |
| `adiabatic_shear_band` | 736 | - | - | - |
| `airy_beam` | 1,379 | - | - | - |
| `amplitude` | 1,329 | - | - | - |
| `angular_acceleration` | 1,393 | - | - | - |
| `anharmonicity` | 1,009 | - | - | - |
| `antenna_rotator` | 517 | - | - | - |
| `appell-s_equation_of_motion` | 1,186 | - | - | - |
| `area_density` | 1,047 | - | - | - |
| `aristotle-s_wheel_paradox` | 1,547 | - | - | - |
| `arnold_conjecture` | 916 | - | - | - |
| `arnold_diffusion` | 931 | - | - | - |
| `artificial_gravity` | 3,356 | - | - | - |
| `barycenter_-astronomy` | 1,054 | - | - | - |
| `bayesian_operational_modal_analysis` | 664 | - | - | - |
| `bending` | 4,012 | - | - | - |
| `berry_connection_and_curvature` | 3,074 | - | - | - |
| `bertrand-s_theorem` | 2,227 | - | - | - |
| `betti-s_theorem` | 1,052 | - | - | - |
| `biaxial_tensile_testing` | 3,333 | - | - | - |
| `blochsiegert_shift` | 941 | - | - | - |
| `block-stacking_problem` | 828 | - | - | - |
| `block_and_tackle` | 1,727 | - | - | - |
| `body_force` | 553 | - | - | - |
| `brittleness` | 722 | - | - | - |
| `bucket_argument` | 2,962 | - | - | - |
| `buoyancy` | 3,705 | - | - | - |
| `casimir_effect` | 4,995 | - | - | - |
| `cauchy_elastic_material` | 769 | - | - | - |
| `cell_transmission_model` | 843 | - | - | - |
| `central_force` | 634 | - | - | - |
| `centrifugal_force` | 4,394 | - | - | - |
| `chasles-_theorem_-kinematics` | 1,243 | - | - | - |
| `circular_motion` | 3,038 | - | - | - |
| `clapotis` | 564 | - | - | - |
| `classical_mechanics_-goldstein` | 1,247 | - | - | - |
| `classical_probability_density` | 1,252 | - | - | - |
| `coherence_-physics` | 3,118 | - | - | - |
| `coherent_potential_approximation` | 573 | - | - | - |
| `conjugate_variables` | 951 | - | - | - |
| `conservative_force` | 1,204 | - | - | - |
| `constant_of_motion` | 1,450 | - | - | - |
| `constitutive_equation` | 2,712 | - | - | - |
| `contact_dynamics` | 913 | - | - | - |
| `control_volume` | 819 | - | - | - |
| `coulomb-s_law` | 4,593 | - | - | - |
| `counterweight` | 576 | - | - | - |
| `covariant_classical_field_theory` | 1,166 | - | - | - |
| `critical_resolved_shear_stress` | 1,457 | - | - | - |
| `damage_mechanics` | 1,798 | - | - | - |
| `damping` | 2,383 | - | - | - |
| `deformation_-physics` | 2,614 | - | - | - |
| `derivative_-multivariable_calculus` | 3,719 | - | - | - |
| `diffraction_from_slits` | 4,772 | - | - | - |
| `digital_image_correlation_and_tracking` | 1,567 | - | - | - |
| `dilatant` | 2,127 | - | - | - |
| `dirac_structure` | 750 | - | - | - |
| `dispersion_-water_waves` | 2,806 | - | - | - |
| `dispersion_relation` | 1,625 | - | - | - |
| `displacement_field_-mechanics` | 1,364 | - | - | - |
| `dual_quaternion` | 3,954 | - | - | - |
| `dynamical_simulation` | 1,753 | - | - | - |
| `eigenstrain` | 955 | - | - | - |
| `elastic_energy` | 1,676 | - | - | - |
| `elastic_instability` | 1,154 | - | - | - |
| `elasticity_tensor` | 2,556 | - | - | - |
| `energy-based_model` | 1,507 | - | - | - |
| `engquistmajda_absorbing_boundary_condition` | 907 | - | - | - |
| `equation_of_state` | 3,955 | - | - | - |
| `falling_cat_problem` | 829 | - | - | - |
| `fermi_acceleration` | 565 | - | - | - |
| `flow_conditioning` | 4,050 | - | - | - |
| `four-force` | 1,044 | - | - | - |
| `fradkin_tensor` | 775 | - | - | - |
| `frame-dragging` | 2,573 | - | - | - |
| `free_body_diagram` | 2,019 | - | - | - |
| `frenkelkontorova_model` | 2,253 | - | - | - |
| `fringe_shift` | 896 | - | - | - |
| `fundamental_vector_field` | 1,004 | - | - | - |
| `generalized_coordinates` | 4,243 | - | - | - |
| `generalized_forces` | 763 | - | - | - |
| `gent_hyperelastic_model` | 1,724 | - | - | - |
| `geodesics_as_hamiltonian_flows` | 1,040 | - | - | - |
| `geometric_mechanics` | 640 | - | - | - |
| `glennye_flow_law` | 1,233 | - | - | - |
| `gomboc` | 1,430 | - | - | - |
| `halo_orbit` | 654 | - | - | - |
| `hamiltonian_-quantum_mechanics` | 4,776 | - | - | - |
| `helmholtz_theorem_-classical_mechanics` | 631 | - | - | - |
| `history_of_centrifugal_and_centripetal_forces` | 2,049 | - | - | - |
| `hitchin_system` | 994 | - | - | - |
| `holonomic_constraints` | 3,996 | - | - | - |
| `hula_hoop` | 1,584 | - | - | - |
| `hydrostatic_stress` | 834 | - | - | - |
| `hyperelastic_material` | 3,078 | - | - | - |
| `inelastic_collision` | 1,100 | - | - | - |
| `inner_core_super-rotation` | 1,561 | - | - | - |
| `integrable_system` | 2,874 | - | - | - |
| `irrational_rotation` | 810 | - | - | - |
| `izod_impact_strength_test` | 604 | - | - | - |
| `jerk_-physics` | 3,634 | - | - | - |
| `jet_force` | 1,037 | - | - | - |
| `julian_day` | 3,846 | - | - | - |
| `kepler_problem` | 1,363 | - | - | - |
| `kinematic_pair` | 1,057 | - | - | - |
| `kirchhofflove_plate_theory` | 3,043 | - | - | - |
| `koopmanvon_neumann_classical_mechanics` | 1,095 | - | - | - |
| `lagrange_bracket` | 903 | - | - | - |
| `lagrangian_system` | 585 | - | - | - |
| `lame-s_stress_ellipsoid` | 646 | - | - | - |
| `langevin_dynamics` | 3,584 | - | - | - |
| `linear_motion` | 1,430 | - | - | - |
| `liouville-s_theorem_-hamiltonian` | 3,429 | - | - | - |
| `liouvillearnold_theorem` | 1,577 | - | - | - |
| `list_of_common_coordinate_transformations` | 2,094 | - | - | - |
| `list_of_equations_in_classical_mechanics` | 930 | - | - | - |
| `longitudinal_wave` | 1,295 | - | - | - |
| `maupertuis-s_principle` | 1,008 | - | - | - |
| `miegruneisen_equation_of_state` | 1,879 | - | - | - |
| `minimal_coupling` | 1,460 | - | - | - |
| `momentum_map` | 2,698 | - | - | - |
| `mooneyrivlin_solid` | 2,743 | - | - | - |
| `moving_frame` | 2,169 | - | - | - |
| `murnaghan_equation_of_state` | 1,795 | - | - | - |
| `n-slit_interferometric_equation` | 1,315 | - | - | - |
| `nambu_mechanics` | 621 | - | - | - |
| `neo-hookean_solid` | 2,959 | - | - | - |
| `net_force` | 2,448 | - | - | - |
| `neutral_plane` | 621 | - | - | - |
| `newton-s_theorem_of_revolving_orbits` | 5,752 | - | - | - |
| `newtonian_dynamics` | 1,321 | - | - | - |
| `non-inertial_reference_frame` | 934 | - | - | - |
| `normal_force` | 1,363 | - | - | - |
| `normal_mode` | 3,001 | - | - | - |
| `norton-s_dome` | 678 | - | - | - |
| `ogden_hyperelastic_model` | 807 | - | - | - |
| `on_the_coloured_light_of_the_binary_stars_and_some_other_stars_o` | 1,153 | - | - | - |
| `openfoam` | 864 | - | - | - |
| `openlb` | 509 | - | - | - |
| `optical_lift` | 559 | - | - | - |
| `orbital_mechanics` | 5,186 | - | - | - |
| `order_tracking_-signal_processing` | 792 | - | - | - |
| `ostrogradsky_instability` | 983 | - | - | - |
| `p-delta_effect` | 615 | - | - | - |
| `parbuckle_salvage` | 1,352 | - | - | - |
| `perfect_obstruction_theory` | 547 | - | - | - |
| `peridynamics` | 4,752 | - | - | - |
| `planetary_migration` | 3,222 | - | - | - |
| `point_particle` | 703 | - | - | - |
| `poisson_bracket` | 3,845 | - | - | - |
| `ponderomotive_force` | 2,011 | - | - | - |
| `poromechanics` | 3,754 | - | - | - |
| `potential_well` | 904 | - | - | - |
| `projectile_motion` | 5,512 | - | - | - |
| `proper_frame` | 724 | - | - | - |
| `radiation_pressure` | 4,697 | - | - | - |
| `rankinehugoniot_conditions` | 3,398 | - | - | - |
| `rational_motion` | 1,430 | - | - | - |
| `rattleback` | 668 | - | - | - |
| `rayleigh_dissipation_function` | 538 | - | - | - |
| `rayleighlorentz_pendulum` | 577 | - | - | - |
| `reactive_centrifugal_force` | 988 | - | - | - |
| `reissnermindlin_plate_theory` | 3,404 | - | - | - |
| `relativistic_system_-mathematics` | 645 | - | - | - |
| `relaxation_-physics` | 1,457 | - | - | - |
| `representative_elementary_volume` | 984 | - | - | - |
| `resultant_force` | 1,338 | - | - | - |
| `revolutions_per_minute` | 1,344 | - | - | - |
| `rigid_transformation` | 1,170 | - | - | - |
| `roberval_balance` | 1,296 | - | - | - |
| `rock_mass_plasticity` | 3,145 | - | - | - |
| `rod_and_frame_test` | 718 | - | - | - |
| `rolling` | 1,655 | - | - | - |
| `rotating_locomotion_in_living_systems` | 3,447 | - | - | - |
| `rotating_spheres` | 2,724 | - | - | - |
| `rotating_unbalance` | 745 | - | - | - |
| `rotating_wheel_space_station` | 1,824 | - | - | - |
| `rotation` | 3,729 | - | - | - |
| `rotation_around_a_fixed_axis` | 2,690 | - | - | - |
| `rotation_number` | 594 | - | - | - |
| `rotation_of_axes_in_two_dimensions` | 1,579 | - | - | - |
| `rotational_brownian_motion_-astronomy` | 937 | - | - | - |
| `rotational_frequency` | 576 | - | - | - |
| `rotordynamics` | 1,526 | - | - | - |
| `sagnac_effect` | 5,422 | - | - | - |
| `scattering_generator` | 1,959 | - | - | - |
| `screw_axis` | 1,979 | - | - | - |
| `screw_theory` | 4,418 | - | - | - |
| `second_polar_moment_of_area` | 1,354 | - | - | - |
| `seismic_metamaterial` | 1,106 | - | - | - |
| `shear_and_moment_diagram` | 790 | - | - | - |
| `shear_stress` | 1,233 | - | - | - |
| `shear_thinning` | 846 | - | - | - |
| `signorini_problem` | 2,356 | - | - | - |
| `simple_harmonic_motion` | 1,950 | - | - | - |
| `simple_shear` | 611 | - | - | - |
| `soft-body_dynamics` | 1,981 | - | - | - |
| `solid_mechanics` | 1,057 | - | - | - |
| `soliton` | 2,454 | - | - | - |
| `sommerfeld_identity` | 781 | - | - | - |
| `spacecraft_attitude_determination_and_control` | 3,982 | - | - | - |
| `spacecraft_detumbling` | 1,011 | - | - | - |
| `spacecraft_electric_propulsion` | 2,837 | - | - | - |
| `spacetime_triangle_diagram_technique` | 2,442 | - | - | - |
| `specific_impulse` | 4,198 | - | - | - |
| `speed_wobble` | 779 | - | - | - |
| `spring_scale` | 520 | - | - | - |
| `stiffness` | 1,119 | - | - | - |
| `strain-rate_tensor` | 2,138 | - | - | - |
| `strain_-mechanics` | 2,284 | - | - | - |
| `stress_resultants` | 1,391 | - | - | - |
| `stress_triaxiality` | 3,207 | - | - | - |
| `structural_dynamics` | 1,588 | - | - | - |
| `summer_science_program` | 1,097 | - | - | - |
| `support_polygon` | 625 | - | - | - |
| `swinging_atwood-s_machine` | 2,323 | - | - | - |
| `symplectic_manifold` | 3,640 | - | - | - |
| `synchronous_frame` | 5,817 | - | - | - |
| `tennis_racket_theorem` | 2,521 | - | - | - |
| `theory_of_tides` | 2,903 | - | - | - |
| `thixotropy` | 1,027 | - | - | - |
| `thrust` | 1,504 | - | - | - |
| `tidal_bore` | 1,567 | - | - | - |
| `torricelli-s_equation` | 719 | - | - | - |
| `toughness` | 537 | - | - | - |
| `transverse_mode` | 1,555 | - | - | - |
| `tropical_instability_waves` | 604 | - | - | - |
| `truss` | 3,111 | - | - | - |
| `turn_-angle` | 858 | - | - | - |
| `variational_asymptotic_method` | 973 | - | - | - |
| `velocity` | 2,847 | - | - | - |
| `vibration_of_plates` | 2,963 | - | - | - |
| `vibronic_coupling` | 2,021 | - | - | - |
| `virial_stress` | 1,331 | - | - | - |
| `virtual_displacement` | 1,869 | - | - | - |
| `viscoelasticity` | 5,432 | - | - | - |
| `viscoplasticity` | 5,755 | - | - | - |
| `vortex` | 3,093 | - | - | - |
| `vorticity` | 1,991 | - | - | - |
| `walt_disney-s_carousel_of_progress` | 4,487 | - | - | - |
| `wave_action_-continuum_mechanics` | 501 | - | - | - |
| `wave_drag` | 824 | - | - | - |
| `wave_impedance` | 724 | - | - | - |
| `wave_interference` | 4,075 | - | - | - |
| `wave_packet` | 5,020 | - | - | - |
| `wavenumber` | 1,576 | - | - | - |
| `yo-yo` | 3,078 | - | - | - |

## Not added in the last run

- `sources.tsv`: A spreadsheet is rows of data, not a document. Leave it out, or turn the rows into sentences yourself and say so in DECISIONS.md.

## What to check by eye

Ingest cleans text by rules, and rules miss things.
Take five minutes to open the shortest, a middle one and the longest document next to its original and read one page of each.

- Search the documents for `þ`, `¼`, `(cid:` and the replacement character.
  A hit usually means the PDF's font map is wrong, which no tool can repair, so treat it as a defect and leave that document out.
- Look at the end of a few papers.
  Ingest drops a trailing reference list when it finds a References heading or a run of numbered entries.
  A paper whose list has neither can keep it, and then every author and journal name matches queries it should not.
- Open the first lines of a few documents.
  Author lists, copyright pages and tables of contents are not removed automatically, and you may want to cut them.
- Compare one table with the PDF.
  A PDF prints footnote marks as small raised digits, and the converter glues them onto the word or number next to them: `ALUMINUM1` is the heading ALUMINUM with footnote 1, and `11210,000` can be 210,000 with footnote 11.
  Quotes still match the stored text, but a number read from it can be wrong, so check before you trust a figure in a query, a judgment or an answer.
- Fix the `license` column in the manifest for every document, then run `uv run p2 license`.
  It is `unknown` until you do, and `unknown` does not pass.

## If a document is flagged as scanned

A scan is a picture of a page, so there is no text for ingest to read.
This template does not install an OCR tool, because it is large and most students never need it.
If you do need one, the opt-in route is pymupdf4llm with rapidocr, run on its own outside the template's environment:

```
uv run --no-project --with pymupdf4llm --with rapidocr python -c "import pymupdf4llm, sys, pathlib; pathlib.Path(sys.argv[2]).write_text(pymupdf4llm.to_markdown(sys.argv[1], use_ocr=True, force_ocr=True), encoding='utf-8')" scan.pdf scan.md
```

Put the resulting `.md` file in your folder and ingest the folder again.
It costs about 2 seconds a page, and OCR text needs a second look: it misreads ligatures, hyphens and numbers.
pymupdf4llm is AGPL-3.0 software, so use it only as a tool on your own machine, and do not add it to this repo's dependencies or copy its code into the repo.
