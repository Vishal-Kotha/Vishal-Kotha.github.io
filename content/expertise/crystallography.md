---
title: "Crystallography & Diffraction"
category: "instrumentation"
date: 2024-01-01
cover:
    image: "/images/icon-diffraction.jpg"
    alt: "XRD Analysis"
description: "SAED pattern indexing for precise crystal phase identification."
weight: 6
---

### Solving the Crystal Puzzle
Synthesizing a material is only half the battle; proving its structure is the other. In my work on **Lanthanum Perovskites**, distinguishing between the rhombohedral ($R\bar{3}c$) and cubic ($Pm\bar{3}m$) phases is critical, as they have nearly identical diffraction fingerprints.

**Technique: Rietveld Refinement**
Standard XRD matching is insufficient for complex doping studies. I employed **Rietveld Refinement** (using FullProf suite) to fit the entire diffraction profile.
* **Process:** I refined lattice parameters, atomic positions, and occupancy factors.
* **Result:** For my **K-substituted $LaMnO_3$**, the refinement confirmed a symmetry breaking from Rhombohedral to **Cubic**, induced by the larger ionic radius of Potassium in the A-site.
* **Precision:** Achieved a Goodness of Fit ($\chi^2$) close to 1, confirming the atomic model matched the experimental reality.

### Visual Methodology
<div class="project-grid">
    <figure>
        <a href="/images/action-xrd.jpg" class="lightbox-trigger" data-caption="<strong>The Data:</strong> Powder X-ray diffraction patterns of hydrothermally synthesized perovskites.">
            <img src="/images/action-xrd.jpg" alt="XRD Patterns" style="height: 250px; object-fit: cover; width: 100%;">
        </a>
        <figcaption>Figure 1: Diffraction Data (Rietveld Refinement)</figcaption>
    </figure>
    <figure>
        <a href="/images/icon-diffraction.jpg" class="lightbox-trigger" data-caption="<strong>The Model:</strong> Rietveld refinement plot showing the experimental data (dots), calculated model (line), and the difference curve.">
            <img src="/images/icon-diffraction.jpg" alt="Rietveld Refinement" style="height: 250px; object-fit: cover; width: 100%;">
        </a>
        <figcaption>Figure 2: SAED pattern indexing</figcaption>
    </figure>
</div>

---
### 📜 Source & Citation

<div class="citation-block">
    <p><strong>Note:</strong> Structural data derived from the author's doctoral research. Citation:</p>
    <span class="citation-text">
        Kotha, V. (2022). Tailoring Transition Metal Perovskite Oxides via Low-Temperature Hydrothermal Routes as Potential Candidates for Catalytic Applications [Doctoral dissertation, IIT Bombay].
    </span>
</div>