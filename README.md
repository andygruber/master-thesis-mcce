# Modernizing Developer Workflows: Embracing Containerization in Legacy Software Development

Master's thesis submitted in partial fulfillment of the requirements for the degree **Master of Science in Engineering** in the Master's Program **Cloud Computing Engineering** at **Hochschule Burgenland** (University of Applied Sciences Burgenland, Eisenstadt, Austria).

**Author:** DI (FH) Andreas Gruber, MA
**Supervisor:** Kevin Horvath, BSc, MSc
**Date:** February 2026

## Abstract

Legacy software development environments pose significant challenges by limiting developer productivity and undermining build reproducibility.
Traditional setups rely on manually configured workstations, leading to configuration drift and the well-known "works on my machine" problem.

This thesis investigates whether containerization can modernize development workflows for long-standing native software projects without requiring fundamental changes to the existing codebase.
Controlled experiments are conducted on an industrial C++ software system with decades of accumulated complexity, comparing containerized environments with native and virtualized approaches.
The evaluation focuses on build performance, resource utilization, and the efficiency and reproducibility of environment provisioning.

### Key Findings

- **95% reduction in toolchain switching time** - from 12.9 minutes to 37.5 seconds
- **35–72% faster filesystem-intensive workloads** with Linux-based containers compared to Windows-native environments
- **Up to 89% reduction in total build time** with compiler caching in optimized containerized workflows
- **Near-zero overhead** for native Linux containers compared to bare-metal execution

## PDF Download

The compiled thesis PDF is available from the [Releases](https://github.com/andygruber/master-thesis-mcce/releases) page.

## Repository Structure

```
main.tex                  # Primary document file
00_preamble/              # Document class, packages, formatting
01_data/                  # Thesis metadata, version info
A_FrontMatter/            # Title page, acknowledgements, abstracts
B_Chapters/               # Thesis chapters (01–08)
C_BackMatter/             # Bibliography, acronyms, appendix
figures/                  # Images and diagrams
references.bib            # Bibliography database
.github/workflows/        # GitHub Actions for automated LaTeX compilation
```

## Build System

The thesis is compiled automatically via **GitHub Actions** using a containerized TeXLive distribution (`xu-cheng/latex-action@v2`).
The workflow is triggered on pushes, pull requests, and releases.
Release builds attach the compiled PDF to the GitHub release.

## Template

This thesis was written using the [FH-Burgenland-MasterThesis](https://github.com/andygruber/FH-Burgenland-MasterThesis) LaTeX template.

## License

This repository contains the source of a submitted academic thesis.
You are welcome to use it as a reference, but please respect academic integrity guidelines and cite appropriately if you build upon this work.
