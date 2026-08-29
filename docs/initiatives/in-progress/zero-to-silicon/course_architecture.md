# Zero to Silicon (Z2S)
## Build Your Own Spiking Digital Hardware
**Curriculum Architecture & Syllabus Specification | Open Neuromorphic**

---

## 1. Curriculum Overview

**Zero to Silicon (Z2S)** is a self-paced, open-access educational track designed to guide software engineers, students, and computational researchers from zero hardware background to designing, coding, and simulating a synthesizable digital spiking neuron chip.

The curriculum is structured as a **cloud-native, asynchronous program modeled after Neuromatch Academy (NMA)**. Every module runs directly inside Google Colab without requiring local EDA tool installations, supported by short modular concept videos and asynchronous Discord co-working spaces.

* **Format:** Modular Asynchronous Curriculum (Pre-recorded Concept Videos + Interactive Google Colab Notebooks + Discord Co-Working).
* **Target Audience:** Software engineers, neuroscientists, ML researchers, and students with basic Python knowledge and no prior hardware engineering background.
* **Curriculum Scope:** 5 Core Modules (`W1D1` through `W1D5`).
* **License:** Open Educational Resources (OER) under **CC-BY-SA 4.0** (content) and **MIT** (code).
* **Primary Platform:** `open-neuromorphic/course-content` (JupyterBook / Google Colab) + Discord (`#zero-to-silicon` & `🔊 Z2S Working Lounge`).

---

## 2. Pedagogical Architecture

Each module is structured around three core learning components:

```
                  MODULAR NMA-STYLE LEARNING CYCLE

┌────────────────────────┐      ┌────────────────────────┐      ┌────────────────────────┐
│  1. Micro-Lecture      │ ──►  │  2. Interactive Colab  │ ──►  │  3. Async Discord Lab  │
│  (10–15 min Video)     │      │  (Zero-Install Code)   │      │  (Co-Working & Feedback)│
└────────────────────────┘      └────────────────────────┘      └────────────────────────┘
```

1. **Pre-Recorded Micro-Lectures (10–15 mins):** Focused conceptual walkthroughs by domain experts explaining theoretical foundations, hardware bridges, and design tradeoffs.
2. **Interactive Google Colab Notebooks:** Browser-based hands-on tutorials with inline exercises. All hardware tools (`verilator`, `iverilog`) install on-demand in the Colab container.
3. **Artifact-Driven Progression:** Every module produces a tangible artifact (e.g., a Python reference class, a gate mapping table, a lint-clean Verilog module, or a simulation waveform). Each artifact forms the exact design input for the subsequent module.
4. **Asynchronous Community Co-Working:** Hands-on peer support via Discord voice lounges and weekly async show-and-tell threads.

---

## 3. The 5-Module Syllabus

```
                THE ZERO TO SILICON ARTIFACT PIPELINE

[ W1D1: Biology & Math ] ──► [ W1D2: Python Reference ] ──► [ W1D3: Logic Mapping ]
Voltage Trace Spec           LIFNeuron Class               Gate & Bit-Width Plan
│
▼
[ Capstone Parity Check ] ◄── [ W1D5: Simulation/Waves ] ◄── [ W1D4: Verilog RTL ]
HW vs SW % Error             Waveform Plots                Synthesizable Module
```

| Module | Title | Primary Artifact Produced | Technical Stack |
| :--- | :--- | :--- | :--- |
| **W1D1** | **Biological & Conceptual Foundations** | Annotated neuron diagram + voltage trace | Python, NumPy, Matplotlib |
| **W1D2** | **Python LIF Reference Modeling** | `lif_neuron.py` reference class + f-I curves | Python, NumPy, Matplotlib |
| **W1D3** | **Digital Logic & Bit-Width Analysis** | Logic mapping table + block diagram + bit analysis | Markdown, Digital Logic Schematics |
| **W1D4** | **Verilog Hardware Description** | Synthesizable, lint-clean `lif_neuron.v` | Verilog, Verilator (Colab inline) |
| **W1D5** | **Verilator Simulation & Waveform Co-Design** | Testbench verification + Matplotlib waveform | C++/Python Testbench, Verilator, Matplotlib |

---

### Module Details

#### Module 1 (`W1D1`) — Biological & Conceptual Foundations
* **Lead Contributors:** Rayane Rocha (`@peppermintcollie`), Bells
* **Objective:** Establish the biophysical intuitions and mathematical vocabulary that govern neuromorphic engineering. Participants understand why leaky integration and discrete spike events provide extreme energy efficiency over traditional architectures.
* **Topics Covered:**
  * Neurons as dynamical systems: membrane potential ($V$), resting potential ($V_{reset}$), leak conductance, threshold ($V_{th}$).
  * Biophysical action potentials vs. the Leaky Integrate-and-Fire (LIF) abstraction (why hardware builds LIF instead of Hodgkin-Huxley).
  * Synaptic transmission: temporal summation, coincidence detection, and excitation/inhibition (E/I) balance.
  * The Neuromorphic Bridge: mapping sparsity, asynchrony, and event-driven communication (AER) to silicon constraints.
* **Colab Tutorial:** `tutorials/W1D1_NeuronFoundations/W1D1_Tutorial1.ipynb`

---

#### Module 2 (`W1D2`) — Python LIF Reference Modeling
* **Lead Contributors:** Erastus Toe (`@e_aurelius`), Jose Antonio (`@eljoserass`)
* **Objective:** Implement the discrete-time LIF mathematical model from scratch in pure Python/NumPy without high-level ML frameworks. This code acts as the golden reference model for all downstream hardware verification.
* **Topics Covered:**
  * Discrete-time Euler integration of the LIF differential equation: $\Delta V = \frac{\Delta t}{\tau} (-(V - V_{reset}) + I_{in})$.
  * State update, threshold crossing detection, and instantaneous reset mechanics.
  * Simulating subthreshold integration vs. regular firing across variable current inputs ($I_{in}$).
  * Generating frequency-current ($f\text{-}I$) response curves.
* **Colab Tutorial:** `tutorials/W1D2_PythonLIFPrototyping/W1D2_Tutorial1.ipynb`

---

#### Module 3 (`W1D3`) — Digital Logic Mapping & Bit-Width Analysis
* **Lead Contributors:** Erastus Toe (`@e_aurelius`), Jose Antonio (`@eljoserass`)
* **Objective:** Translate Python mathematical operations into digital hardware building blocks (registers, adders, subtractors, comparators, and multiplexers) and resolve hardware quantization constraints.
* **Topics Covered:**
  * Mapping software lines to digital logic primitives (e.g., `if V >= V_th` $\rightarrow$ comparator + multiplexer).
  * Fixed-point arithmetic and integer offsets (eliminating negative voltage representations).
  * Bit-width budget analysis: calculating necessary register widths for dynamic range and precision.
  * Hardware optimization: replacing expensive multipliers with power-of-2 bit-shift approximations for decay factor $\frac{\Delta t}{\tau}$.
* **Colab Tutorial:** `tutorials/W1D3_DigitalLogicMapping/W1D3_Tutorial1.ipynb`

---

#### Module 4 (`W1D4`) — Verilog Hardware Description & Linting
* **Lead Contributors:** Erastus Toe (`@e_aurelius`), Jose Antonio (`@eljoserass`)
* **Objective:** Formalize a written hardware specification (`lif_chip_spec.md`) and implement it as a synthesizable, parameterized Verilog module directly inside Google Colab.
* **Topics Covered:**
  * Writing a formal port table, register definition, and cycle-by-cycle behavioral specification.
  * Verilog syntax fundamentals: `module`, `wire`, `reg`, parameters, and sequential `always @(posedge clk)` blocks.
  * Non-blocking assignments (`<=`) and race-condition prevention.
  * Cloud-native static linting: executing `verilator --lint-only -Wall` directly inside Colab cells.
* **Colab Tutorial:** `tutorials/W1D4_VerilogHardwareDesign/W1D4_Tutorial1.ipynb`

---

#### Module 5 (`W1D5`) — Verilator Simulation & Waveform Co-Design
* **Lead Contributors:** Jose Antonio (`@eljoserass`), Erastus Toe (`@e_aurelius`)
* **Objective:** Compile the Verilog module into a cycle-accurate C++/Python simulation harness, capture execution waveforms, and verify hardware-software parity against the Module 2 reference model.
* **Topics Covered:**
  * Setting up automated compilation pipelines with Verilator inside Colab.
  * Writing testbench stimuli (clock generation, synchronous reset assertion, constant current injection).
  * In-browser waveform rendering: parsing simulation output (`.vcd`/`.csv`) and plotting digital waveforms using Matplotlib.
  * Co-design verification: measuring the hardware Inter-Spike Interval (ISI) and calculating percentage discrepancy against the Python reference model.
* **Colab Tutorial:** `tutorials/W1D5_HardwareVerification/W1D5_Tutorial1.ipynb`

---

## 4. Repository Structure & Toolchain

All curriculum materials reside in the `open-neuromorphic/course-content` repository:

```text
open-neuromorphic/course-content/
├── book/                           # JupyterBook configuration and site build
│   ├── _config.yml
│   └── _toc.yml
├── tutorials/
│   ├── materials.yml               # NMA Course Master Manifest
│   ├── templates/                  # Standardized notebook authoring templates
│   │   └── tutorial_template.ipynb
│   ├── sandboxes/                  # Experimental prototype notebooks
│   │   └── sandbox_z2s_demo.ipynb
│   ├── W1D1_NeuronFoundations/     # Module 1
│   │   ├── README.md
│   │   ├── W1D1_Intro.ipynb
│   │   └── W1D1_Tutorial1.ipynb
│   ├── W1D2_PythonLIFPrototyping/  # Module 2
│   │   ├── README.md
│   │   ├── W1D2_Intro.ipynb
│   │   └── W1D2_Tutorial1.ipynb
│   ├── W1D3_DigitalLogicMapping/   # Module 3
│   │   ├── README.md
│   │   ├── W1D3_Intro.ipynb
│   │   └── W1D3_Tutorial1.ipynb
│   ├── W1D4_VerilogHardwareDesign/ # Module 4
│   │   ├── README.md
│   │   ├── W1D4_Intro.ipynb
│   │   └── W1D4_Tutorial1.ipynb
│   └── W1D5_HardwareVerification/  # Module 5
│       ├── README.md
│       ├── W1D5_Intro.ipynb
│       └── W1D5_Tutorial1.ipynb
```

---

## 5. Cloud-Native Toolchain Integration

To ensure zero installation friction across operating systems (Windows, macOS, Linux), the entire toolchain runs inside the Colab environment:

```python
# 1. Automated Toolchain Installation (Header Cell)
!apt-get update -yq > /dev/null
!apt-get install -y verilator verilog > /dev/null

# 2. Inline Hardware Description
%%file lif_neuron.v
module lif_neuron #(parameter WIDTH = 16) (...);
  // Synthesizable RTL
endmodule

# 3. In-Notebook Compilation & Execution
!verilator --lint-only -Wall lif_neuron.v
!verilator -Wall --cc --exe --build tb_lif_neuron.cpp lif_neuron.v
!./obj_dir/Vlif_neuron

# 4. Inline Waveform Visualization
import matplotlib.pyplot as plt
import pandas as pd
# Render digital signal traces directly in notebook outputs
```
