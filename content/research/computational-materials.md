---
title: "Computational Materials Science: Boron Carbide"
date: 2016-06-01
description: "Ab-initio DFT calculations on the failure mechanisms of bulletproof armor."
tags: ["DFT", "Python", "Simulation"]
cover:
    image: "/images/boron-carbide.jpg"
    alt: "Boron Carbide"
    relative: false
weight: 4
---

### The Mystery of Boron Carbide
Boron Carbide ($B_4C$) is used in bulletproof jackets due to its hardness (30 GPa). However, it fails unexpectedly under high-velocity impact.

<div class="figure-container">
    <img src="/images/boron-carbide.jpg" alt="Rhombohedral Structure" class="figure-img">
    <p class="figure-caption">
        <strong>Figure 1:</strong> The Rhombohedral unit cell structure of Boron Carbide ($B_4C$).
    </p>
</div>

### Methodology
During my M.Sc., I utilized **Density Functional Theory (DFT)** codes (VASP, Gaussian) to model the atomic bonding and identify structural weaknesses.

<div class="figure-container">
    <img src="/images/vasp-model.jpg" alt="VASP Model" class="figure-img">
    <p class="figure-caption">
        <strong>Figure 2:</strong> Electron density mapping generated using VASP.
    </p>
</div>

### Discovery
* **Bonding Analysis:** Identified that specific weak B-B bonds in the inter-polyhedral chains cause structural collapse under high pressure.

<div class="figure-container">
    <img src="/images/crack-plane.jpg" alt="Crack Plane Analysis" class="figure-img">
    <p class="figure-caption">
        <strong>Figure 3:</strong> Visualization of the crack plane propagation in the crystal lattice.
    </p>
</div>

* **Data Engineering:** Implemented Python and SQL scripts for efficient bookkeeping of simulation results and literature data.

---
### 💻 Open Source Contribution
I have open-sourced the Python scripts used for plotting the XRD data and automating the VASP log parsing.

<div style="margin-top: 20px;">
    <a href="https://github.com/vishalkotha" target="_blank" class="btn-cite" style="border: 2px solid var(--primary-color); color: var(--primary-color) !important;">
        View Code on GitHub ↗
    </a>
</div>