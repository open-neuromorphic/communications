# ⚡ Initiative: Zero to Silicon (Z2S)

**Accountable Fellows:** @beffiong1, @aMarcireau, @eljoserass, @neural-loop
**Status:** IN PROGRESS
**GitHub Tracker:** [Issue #146](https://github.com/open-neuromorphic/communications/issues/146)

---

## 🎯 Objective
Zero to Silicon (Z2S) is a step-by-step educational pipeline designed to take software engineers, students, and researchers from zero hardware background to simulating a digital spiking neuron chip.

All materials produced in this initiative are released as **Open Educational Resources (OER)** under CC-BY/MIT licenses.

---

## 🏗️ Course Architecture (NMA-Style Format)
*Note: This initiative has transitioned from a legacy 6-week live webinar format to a highly scalable, asynchronous structure modeled after Neuromatch Academy (NMA).*

The curriculum relies on:
1. **Pre-recorded "Concept" Videos:** Short (10-15 minute) videos from domain experts introducing the theory.
2. **Google Colab Notebooks:** Hands-on tutorials that require **zero local installation**.
3. **Async Discord Support:** Community-driven problem-solving in dedicated Discord channels.

### 🛠️ The Toolchain (Cloud-Native)
To remove friction and operating system dependencies, the entire Z2S toolchain runs directly inside the browser using Google Colab:
- **Python Prototyping:** `snnTorch`, `NumPy`, `Matplotlib`
- **Hardware Description:** `Verilog` (written inline via `%%file` magic commands)
- **Simulation & Linting:** `Verilator` and `Icarus Verilog` (installed via `apt-get` in Colab)
- **Waveform Visualization:** CSV/VCD parsing rendered directly in Matplotlib.

---

## 📂 Directory Contents & Source of Truth

This directory acts as the single source of truth for the curriculum specification. Before writing Jupyter Notebooks, the curriculum is mapped out here in Markdown.

| File | Description |
| :--- | :--- |
| 🗺️ **[course_architecture.md](./course_architecture.md)** | The master syllabus. Maps the course modules (W1D1 to W1D5), learning objectives, and structural flow. |
| 💻 **[colab_exercises.md](./colab_exercises.md)** | The raw technical requirements, code stubs, and problem sets that will be converted into the student-facing Colab Notebooks. |
| 🧑‍🏫 **[facilitator_guide.md](./facilitator_guide.md)** | The grading rubrics, common pitfalls, and guide for ONM volunteers assisting students asynchronously in Discord. |

---

## 🚀 Current Roadmap & Next Steps

1. **Content Scaffolding (Current Phase):** Translating the Markdown specifications in this directory into executable `jupyter-book` formats.
2. **Colab Pipeline Testing:** Validating the `Verilator` execution pipeline inside the sandbox Colab environment.
3. **Speaker Video Sourcing:** Reaching out to external experts to record the 15-minute conceptual introductions for each module.
4. **Beta Launch:** Releasing the first modules to a targeted group of ONM community members for stress testing.