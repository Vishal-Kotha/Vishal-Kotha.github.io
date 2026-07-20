---
title: "Spectroscopy & Surface Science"
category: "instrumentation"
date: 2024-01-01
cover:
    image: "/images/icon-spectroscopy.jpg"
    alt: "XPS Analysis"
description: "Unraveling surface oxidation states and reaction kinetics via XPS, EDS, and Impedance Spectroscopy."
weight: 5
---

### The Surface is the Stage
In electrocatalysis, the bulk formula doesn't matter as much as the surface state. To understand *why* my K-substituted Perovskites outperformed standard catalysts, I had to probe the top few nanometers of the material.

**1. X-Ray Photoelectron Spectroscopy (XPS)**
* **The Query:** Did Potassium substitution actually change the manganese oxidation state?
* **The Analysis:** I performed high-resolution deconvolution of the **Mn 2p** spectra.
* **The Finding:** The spectra revealed a shift in the $Mn^{3+}/Mn^{4+}$ ratio. The incorporation of $K^+$ created significant **$Mn^{4+}$ surface defects**, which act as the primary active sites for oxygen adsorption during the ORR process.

**2. Electrochemical Impedance Spectroscopy (EIS)**
* **The Query:** Is the catalyst inherently faster, or just more conductive?
* **The Analysis:** I modeled the Nyquist plots using a Randles equivalent circuit.
* **The Finding:** The K-substituted samples showed a drastically reduced **Charge Transfer Resistance ($R_{ct}$)** compared to the pristine sample, confirming faster electron transfer kinetics at the electrode-electrolyte interface.

### Visual Methodology
<div class="project-grid">
    <figure>
        <a href="/images/icon-spectroscopy.jpg" class="lightbox-trigger" data-caption="<strong>XPS Deconvolution:</strong> High-resolution Mn 2p spectrum showing the coexistence of Mn3+ and Mn4+ states.">
            <img src="/images/icon-spectroscopy.jpg" alt="XPS Spectra" style="height: 250px; object-fit: cover; width: 100%;">
        </a>
        <figcaption>Figure 1: Deconvoluted XPS spectra revealing surface oxidation states.</figcaption>
    </figure>
    <figure>
        <a href="/images/exp-weizmann1.jpg" class="lightbox-trigger" data-caption="<strong>Kinetics:</strong> Nyquist plots derived from EIS, showing reduced arc radius (lower resistance) for the doped catalyst.">
            <img src="/images/exp-weizmann1.jpg" alt="EIS Data" style="height: 250px; object-fit: cover; width: 100%;">
        </a>
        <figcaption>Figure 2: Reaction Kinetics (EIS)</figcaption>
    </figure>
</div>

---

### 📜 Source & Citation

<div class="citation-block">
    <p><strong>Note:</strong> Data derived from the author's doctoral research. Citation:</p>
    <span class="citation-text">
        Kotha, V. (2022). Tailoring Transition Metal Perovskite Oxides via Low-Temperature Hydrothermal Routes as Potential Candidates for Catalytic Applications [Doctoral dissertation, IIT Bombay].
    </span>
    <div style="margin-top: 15px;">
        <button class="btn-cite" onclick="window.copyCitation('Kotha, V. (2022). Tailoring Transition Metal Perovskite Oxides via Low-Temperature Hydrothermal Routes as Potential Candidates for Catalytic Applications [Doctoral dissertation, IIT Bombay].')">
            Copy Citation
        </button>
    </div>
</div>