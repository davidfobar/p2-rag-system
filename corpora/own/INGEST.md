# Ingest report

Written by `uv run p2 ingest`.
It lists every document in this corpus that ingest added, with what the cleaning pass did and anything that looks wrong.
Running ingest again adds to the table and replaces the "last run" section, and `uv run p2 ingest --report` rewrites it for the documents in docs/ now, after you removed some.

## Summary

- Documents: 321 (the final check needs at least 200)
- Words: 443,585
- Estimated tokens (words times 1.4): 621,019 (`p2 check` warns above 800,000 and fails above 1,000,000)
- Flagged documents: 14

## Documents

| docid | words | characters per page | flags | cleaning |
|---|---:|---:|---|---|
| `about-actions` | 389 | - | - | - |
| `about-build-system` | 1,280 | - | - | - |
| `about-client-libraries` | 1,228 | - | - | - |
| `about-command-line-tools` | 660 | - | - | - |
| `about-composition` | 813 | - | - | - |
| `about-cross-compilation` | 248 | - | - | - |
| `about-different-middleware-vendors` | 884 | - | - | - |
| `about-discovery` | 168 | - | - | - |
| `about-domain-id` | 912 | - | - | - |
| `about-executors` | 1,290 | - | - | - |
| `about-interfaces` | 1,196 | - | - | - |
| `about-internal-interfaces` | 2,565 | - | - | - |
| `about-launch` | 194 | - | - | - |
| `about-logging` | 1,956 | - | - | - |
| `about-middleware-implementations` | 624 | - | - | - |
| `about-nodes` | 185 | - | - | - |
| `about-parameters` | 1,213 | - | - | - |
| `about-quality-of-service-settings` | 2,059 | - | - | - |
| `about-ros` | 921 | - | - | - |
| `about-rqt` | 320 | - | - | - |
| `about-security` | 845 | - | - | - |
| `about-services` | 318 | - | - | - |
| `about-tf2` | 1,087 | - | - | - |
| `about-topic-statistics` | 474 | - | - | - |
| `about-topics` | 492 | - | - | - |
| `access-controls` | 691 | - | - | - |
| `add-your-project` | 195 | - | - | - |
| `adding-a-frame-cpp` | 1,980 | - | - | - |
| `adding-a-frame-py` | 1,780 | - | - | - |
| `adding-physical-and-collision-properties-to-a-urdf-model` | 907 | - | - | - |
| `adopters` | 42 | - | very short (42 words) | - |
| `advanced` | 35 | - | very short (35 words) | - |
| `allocator-template-tutorial` | 1,116 | - | - | - |
| `alpha-overview` | 2,596 | - | - | - |
| `alternatives` | 44 | - | very short (44 words) | - |
| `ament-cmake-documentation` | 4,609 | - | - | - |
| `ament-cmake-python-documentation` | 409 | - | - | - |
| `basic` | 95 | - | - | - |
| `beginner-cli-tools` | 43 | - | very short (43 words) | - |
| `beginner-client-libraries` | 87 | - | - | - |
| `beta1-overview` | 359 | - | - | - |
| `beta2-overview` | 501 | - | - | - |
| `beta3-overview` | 490 | - | - | - |
| `build-farms` | 1,027 | - | - | - |
| `buildfarmtesting` | 311 | - | - | - |
| `building-a-custom-deb-package` | 216 | - | - | - |
| `building-a-movable-robot-model-with-urdf` | 695 | - | - | - |
| `building-a-visual-robot-model-with-urdf-from-scratch` | 1,865 | - | - | - |
| `building-realtime-rt_preempt-kernel-for-ros-2` | 504 | - | - | - |
| `building-ros-2-with-tracing` | 375 | - | - | - |
| `building-ros2-package-with-eclipse-2021-06` | 190 | - | - | - |
| `citations` | 200 | - | - | - |
| `cli` | 165 | - | - | - |
| `code-style-language-versions` | 2,208 | - | - | - |
| `colcon-tutorial` | 1,471 | - | - | - |
| `composition` | 1,644 | - | - | - |
| `concepts` | 41 | - | very short (41 words) | - |
| `configure-zerocopy-loaned-messages` | 1,313 | - | - | - |
| `configuring-ros2-environment` | 981 | - | - | - |
| `contact` | 1,206 | - | - | - |
| `content-filtering-subscription` | 1,701 | - | - | - |
| `contributing` | 795 | - | - | - |
| `contributing-to-code` | 20 | - | very short (20 words) | - |
| `contributing-to-ros-2-documentation` | 3,768 | - | - | - |
| `core-maintainer-guide` | 1,277 | - | - | - |
| `cpp` | 198 | - | - | - |
| `create-an-rqtbag-plugin` | 1,552 | - | - | - |
| `creating-a-workspace` | 1,637 | - | - | - |
| `creating-an-action` | 767 | - | - | - |
| `creating-an-rmw-implementation` | 4,114 | - | - | - |
| `creating-launch-files` | 1,298 | - | - | - |
| `creating-your-first-ros2-package` | 1,545 | - | - | - |
| `cross-compilation` | 22 | - | very short (22 words) | - |
| `custom-ros2-interfaces` | 2,263 | - | - | - |
| `dds-implementations` | 114 | - | - | - |
| `dds-tuning` | 1,059 | - | - | - |
| `debugging-tf2-problems` | 1,375 | - | - | - |
| `defining-worlds-mvsim` | 1,353 | - | - | - |
| `demos` | 99 | - | - | - |
| `deploying-ros-2-on-ibm-cloud` | 2,759 | - | - | - |
| `deployment-guidelines` | 1,060 | - | - | - |
| `developer-guide` | 6,693 | - | - | - |
| `developing-a-ros-2-package` | 456 | - | - | - |
| `development` | 21 | - | very short (21 words) | - |
| `discovery-server` | 3,414 | - | - | - |
| `documenting-a-ros-2-package` | 1,365 | - | - | - |
| `dummy-robot-demo` | 441 | - | - | - |
| `eclipse-oxygen-with-ros-2-and-rviz2` | 689 | - | - | - |
| `end-of-life` | 63 | - | - | - |
| `examine-traffic` | 1,288 | - | - | - |
| `exporting-an-urdf-file` | 306 | - | - | - |
| `fastdds-configuration` | 3,349 | - | - | - |
| `feature-ideas` | 823 | - | - | - |
| `features` | 503 | - | - | - |
| `first-steps` | 541 | - | - | - |
| `galactic-geochelone-complete-changelog__part01` | 4,001 | - | - | - |
| `galactic-geochelone-complete-changelog__part02` | 4,010 | - | - | - |
| `galactic-geochelone-complete-changelog__part03` | 4,001 | - | - | - |
| `galactic-geochelone-complete-changelog__part04` | 4,011 | - | - | - |
| `galactic-geochelone-complete-changelog__part05` | 4,000 | - | - | - |
| `galactic-geochelone-complete-changelog__part06` | 4,008 | - | - | - |
| `galactic-geochelone-complete-changelog__part07` | 4,006 | - | - | - |
| `galactic-geochelone-complete-changelog__part08` | 3,290 | - | - | - |
| `gazebo` | 223 | - | - | - |
| `getting-backtraces-in-ros-2` | 2,385 | - | - | - |
| `getting-started-mvsim` | 698 | - | - | - |
| `getting-started-with-ros2doctor` | 1,052 | - | - | - |
| `glossary` | 312 | - | - | - |
| `governance` | 2,047 | - | - | - |
| `how-to-guides` | 288 | - | - | - |
| `humble-hawksbill-complete-changelog__part01` | 4,002 | - | - | - |
| `humble-hawksbill-complete-changelog__part02` | 4,001 | - | - | - |
| `humble-hawksbill-complete-changelog__part03` | 4,006 | - | - | - |
| `humble-hawksbill-complete-changelog__part04` | 4,001 | - | - | - |
| `humble-hawksbill-complete-changelog__part05` | 4,681 | - | - | - |
| `improved-dynamic-discovery` | 756 | - | - | - |
| `index` | 850 | - | - | - |
| `index-your-packages` | 756 | - | - | - |
| `installation` | 366 | - | - | - |
| `installation-macos` | 1,132 | - | - | - |
| `installation-troubleshooting` | 2,115 | - | - | - |
| `installation-ubuntu` | 385 | - | - | - |
| `installation-windows` | 843 | - | - | - |
| `installing-on-raspberry-pi` | 390 | - | - | - |
| `integration` | 1,437 | - | - | - |
| `intel-ros2-projects` | 318 | - | - | - |
| `interfaces-topics-services-actions` | 654 | - | - | - |
| `intermediate` | 57 | - | - | - |
| `intra-process-communication` | 2,417 | - | - | - |
| `introducing-ros2-security` | 1,177 | - | - | - |
| `introducing-turtlesim` | 1,383 | - | - | - |
| `introduction-to-tf2` | 733 | - | - | - |
| `iron-irwini-complete-changelog__part01` | 4,000 | - | - | - |
| `iron-irwini-complete-changelog__part02` | 4,000 | - | - | - |
| `iron-irwini-complete-changelog__part03` | 4,006 | - | - | - |
| `iron-irwini-complete-changelog__part04` | 4,001 | - | - | - |
| `iron-irwini-complete-changelog__part05` | 3,943 | - | - | - |
| `jazzy-jalisco-complete-changelog__part01` | 4,023 | - | - | - |
| `jazzy-jalisco-complete-changelog__part02` | 4,010 | - | - | - |
| `jazzy-jalisco-complete-changelog__part03` | 4,007 | - | - | - |
| `jazzy-jalisco-complete-changelog__part04` | 4,086 | - | - | - |
| `jazzy-jalisco-complete-changelog__part05` | 2,914 | - | - | - |
| `kilted-kaiju-complete-changelog__part01` | 4,001 | - | - | - |
| `kilted-kaiju-complete-changelog__part03` | 4,004 | - | - | - |
| `kilted-kaiju-complete-changelog__part04` | 4,000 | - | - | - |
| `kilted-kaiju-complete-changelog__part05` | 1,825 | - | - | - |
| `latest-development-setup` | 120 | - | - | - |
| `launch-file-different-formats` | 1,205 | - | - | - |
| `launch-main` | 172 | - | - | - |
| `launch-system` | 659 | - | - | - |
| `launching-composable-nodes` | 743 | - | - | - |
| `launching-multiple-nodes` | 562 | - | - | - |
| `learning-about-tf2-and-time-cpp` | 684 | - | - | - |
| `logging-and-logger-configuration` | 1,882 | - | - | - |
| `lyrical-luth-complete-changelog__part01` | 4,097 | - | - | - |
| `lyrical-luth-complete-changelog__part02` | 4,007 | - | - | - |
| `lyrical-luth-complete-changelog__part03` | 4,004 | - | - | - |
| `lyrical-luth-complete-changelog__part04` | 4,002 | - | - | - |
| `lyrical-luth-complete-changelog__part05` | 4,000 | - | - | - |
| `lyrical-luth-complete-changelog__part06` | 3,343 | - | - | - |
| `macos-development-setup` | 923 | - | - | - |
| `maintaining-a-source-checkout` | 474 | - | - | - |
| `making-a-pr` | 1,021 | - | - | - |
| `makoa-release-timeline` | 71 | - | - | - |
| `makoa-supported-platforms` | 40 | - | very short (40 words) | - |
| `managed-nodes` | 271 | - | - | - |
| `marker-display-types` | 1,633 | - | - | - |
| `marker-points-and-lines` | 1,010 | - | - | - |
| `marker-sending-basic-shapes` | 1,131 | - | - | - |
| `metrics` | 259 | - | - | - |
| `migrating-cpp-package-example` | 1,195 | - | - | - |
| `migrating-cpp-packages` | 1,560 | - | - | - |
| `migrating-from-ros1` | 162 | - | - | - |
| `migrating-interfaces` | 281 | - | - | - |
| `migrating-launch-files` | 1,911 | - | - | - |
| `migrating-package-xml` | 479 | - | - | - |
| `migrating-packages` | 462 | - | - | - |
| `migrating-parameters` | 509 | - | - | - |
| `migrating-python-package-example` | 2,391 | - | - | - |
| `migrating-python-packages` | 487 | - | - | - |
| `migrating-scripts` | 291 | - | - | - |
| `miscellaneous` | 30 | - | very short (30 words) | - |
| `monitoring-for-parameter-changes-cpp` | 1,915 | - | - | - |
| `monitoring-for-parameter-changes-python` | 1,586 | - | - | - |
| `node-arguments` | 663 | - | - | - |
| `non-dds-implementations` | 69 | - | - | - |
| `nvidia-ros2-projects` | 526 | - | - | - |
| `overriding-qos-policies-for-recording-and-playback` | 423 | - | - | - |
| `package-docs` | 211 | - | - | - |
| `platform-eol-policy` | 342 | - | - | - |
| `platform-support-tiers` | 311 | - | - | - |
| `pluginlib` | 1,432 | - | - | - |
| `py` | 1,802 | - | - | - |
| `python` | 289 | - | - | - |
| `quality-guide` | 1,363 | - | - | - |
| `quality-of-service` | 788 | - | - | - |
| `quaternion-fundamentals` | 1,082 | - | - | - |
| `reading-from-a-bag-file-cpp` | 1,161 | - | - | - |
| `real-time-programming` | 1,390 | - | - | - |
| `recording-a-bag-from-your-own-node-cpp` | 2,477 | - | - | - |
| `recording-a-bag-from-your-own-node-py` | 2,348 | - | - | - |
| `recording-and-playing-back-data` | 1,890 | - | - | - |
| `related-projects` | 254 | - | - | - |
| `release-ardent-apalone` | 759 | - | - | - |
| `release-bouncy-bolson` | 833 | - | - | - |
| `release-crystal-clemmys` | 1,344 | - | - | - |
| `release-dashing-diademata` | 4,922 | - | - | - |
| `release-eloquent-elusor` | 2,022 | - | - | - |
| `release-foxy-fitzroy` | 3,238 | - | - | - |
| `release-galactic-geochelone` | 5,173 | - | - | - |
| `release-humble-hawksbill` | 5,616 | - | - | - |
| `release-iron-irwini` | 6,417 | - | - | - |
| `release-jazzy-jalisco` | 3,334 | - | - | - |
| `release-kilted-kaiju` | 2,347 | - | - | - |
| `release-lyrical-luth` | 3,395 | - | - | - |
| `release-makoa-mata-mata` | 88 | - | - | - |
| `release-process` | 1,690 | - | - | - |
| `release-rolling-ridley` | 196 | - | - | - |
| `release-schedule` | 443 | - | - | - |
| `release-team-repository` | 713 | - | - | - |
| `release-timeline` | 306 | - | - | - |
| `release-track` | 1,192 | - | - | - |
| `releases` | 802 | - | - | - |
| `releasing-a-package` | 164 | - | - | - |
| `reviewing-a-pr` | 921 | - | - | - |
| `rhel-development-setup` | 905 | - | - | - |
| `rhel-install-binary` | 743 | - | - | - |
| `rhel-install-rpms` | 647 | - | - | - |
| `rmw-implementations` | 92 | - | - | - |
| `roadmap` | 318 | - | - | - |
| `ros-2-ides` | 1,296 | - | - | - |
| `ros-2-mirrors` | 485 | - | - | - |
| `ros2-tracing-trace-and-analyze` | 849 | - | - | - |
| `rosbag-with-ros1-bridge` | 864 | - | - | - |
| `roscon-content` | 4,006 | - | - | - |
| `rosdep` | 1,432 | - | - | - |
| `run-2-nodes-in-single-or-separate-docker-containers` | 267 | - | - | - |
| `rviz-custom-display` | 1,675 | - | - | - |
| `rviz-custom-panel` | 1,339 | - | - | - |
| `rviz-main` | 46 | - | very short (46 words) | - |
| `rviz-user-guide` | 2,890 | - | - | - |
| `security-main` | 27 | - | very short (27 words) | - |
| `security-on-two` | 379 | - | - | - |
| `service-introspection` | 1,187 | - | - | - |
| `setting-up-simulation-webots-advanced` | 1,877 | - | - | - |
| `setting-up-simulation-webots-basic` | 3,187 | - | - | - |
| `setup-ros-2-with-vscode-and-docker-container` | 866 | - | - | - |
| `simulation-gazebo` | 25 | - | very short (25 words) | - |
| `simulation-main` | 79 | - | - | - |
| `simulation-mvsim` | 96 | - | - | - |
| `simulation-reset-handler` | 829 | - | - | - |
| `simulation-supervisor` | 737 | - | - | - |
| `simulation-webots` | 51 | - | - | - |
| `single-package-define-and-use-interface` | 1,575 | - | - | - |
| `snapshot-repository` | 1,225 | - | - | - |
| `source-control-best-practices` | 745 | - | - | - |
| `subsequent-releases` | 976 | - | - | - |
| `supplementing-custom-rosdep-keys` | 975 | - | - | - |
| `supported-platforms` | 700 | - | - | - |
| `sync-vs-async` | 834 | - | - | - |
| `testing` | 620 | - | - | - |
| `testing-main` | 871 | - | - | - |
| `tf2-main` | 310 | - | - | - |
| `the-keystore` | 1,572 | - | - | - |
| `the-ros2-project` | 56 | - | - | - |
| `time-travel-with-tf2-cpp` | 704 | - | - | - |
| `topic-statistics-tutorial` | 1,217 | - | - | - |
| `tutorials` | 477 | - | - | - |
| `tutorials-advanced` | 96 | - | - | - |
| `tutorials-intermediate` | 71 | - | - | - |
| `ubuntu-development-setup` | 1,019 | - | - | - |
| `ubuntu-install-binary` | 819 | - | - | - |
| `ubuntu-install-debs` | 761 | - | - | - |
| `understanding-ros2-actions` | 1,490 | - | - | - |
| `understanding-ros2-nodes` | 843 | - | - | - |
| `understanding-ros2-parameters` | 870 | - | - | - |
| `understanding-ros2-services` | 1,374 | - | - | - |
| `understanding-ros2-topics` | 2,360 | - | - | - |
| `urdf-main` | 77 | - | - | - |
| `using-callback-groups` | 2,291 | - | - | - |
| `using-custom-rosdistro` | 684 | - | - | - |
| `using-event-handlers` | 956 | - | - | - |
| `using-node-interfaces-template-class` | 1,010 | - | - | - |
| `using-parameters-in-a-class-cpp` | 1,518 | - | - | - |
| `using-parameters-in-a-class-python` | 1,375 | - | - | - |
| `using-python-packages` | 455 | - | - | - |
| `using-ros1_bridge-jammy-upstream` | 554 | - | - | - |
| `using-ros2-launch-for-large-projects` | 3,024 | - | - | - |
| `using-ros2-param` | 563 | - | - | - |
| `using-rqt-console` | 702 | - | - | - |
| `using-stamped-datatypes-with-tf2-ros-messagefilter` | 2,394 | - | - | - |
| `using-substitutions` | 2,507 | - | - | - |
| `using-urdf-with-robot-state-publisher-cpp` | 1,094 | - | - | - |
| `using-urdf-with-robot-state-publisher-py` | 876 | - | - | - |
| `using-variants` | 380 | - | - | - |
| `using-xacro-to-clean-up-a-urdf-file` | 1,232 | - | - | - |
| `visualizing-data-and-teleoperating-with-phantom-bridge` | 11 | - | very short (11 words) | - |
| `visualizing-ros-2-data-with-foxglove-studio` | 947 | - | - | - |
| `wait-for-acknowledgment` | 507 | - | - | - |
| `webots-installation-ubuntu` | 518 | - | - | - |
| `windows-development-setup` | 1,185 | - | - | - |
| `windows-install-binary` | 735 | - | - | - |
| `windows-tips-and-tricks` | 1,538 | - | - | - |
| `working-with-eclipse-cyclonedds` | 241 | - | - | - |
| `working-with-eprosima-fast-dds` | 173 | - | - | - |
| `working-with-gurumnetworks-gurumdds` | 308 | - | - | - |
| `working-with-multiple-rmw-implementations` | 1,053 | - | - | - |
| `working-with-rti-connext-dds` | 623 | - | - | - |
| `working-with-zenoh` | 310 | - | - | - |
| `writing-a-composable-node` | 464 | - | - | - |
| `writing-a-simple-cpp-publisher-and-subscriber` | 1,885 | - | - | - |
| `writing-a-simple-cpp-service-and-client` | 1,484 | - | - | - |
| `writing-a-simple-py-publisher-and-subscriber` | 1,682 | - | - | - |
| `writing-a-simple-py-service-and-client` | 1,380 | - | - | - |
| `writing-a-tf2-broadcaster-cpp` | 1,815 | - | - | - |
| `writing-a-tf2-broadcaster-py` | 1,724 | - | - | - |
| `writing-a-tf2-listener-cpp` | 1,543 | - | - | - |
| `writing-a-tf2-listener-py` | 1,184 | - | - | - |
| `writing-a-tf2-static-broadcaster-cpp` | 1,693 | - | - | - |
| `writing-a-tf2-static-broadcaster-py` | 1,647 | - | - | - |
| `writing-an-action-server-client-cpp` | 2,476 | - | - | - |

## Not added in the last run

Nothing was left out.

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
