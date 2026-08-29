# Zero to Silicon
## Facilitator Guide, Grading Rubrics & Solution Keys
**Executive Committee & Facilitator Edition | Open Neuromorphic | Summer 2026**

---

## 1. Facilitation Philosophy & Community Workflow

Zero to Silicon is designed as an encouraging, low-friction entry point into neuromorphic hardware engineering. Facilitation takes place asynchronously in the Discord `#zero-to-silicon` forum threads and during informal co-working sessions in `🔊 Z2S Working Lounge`.

### Key Facilitator Guidelines
1. **Connect Artifacts Across Modules:** Always frame feedback around the pipeline. If a participant has an issue in `W1D4` (Verilog), check their `W1D3` (Logic Map) and `W1D2` (Python) parameters.
2. **Prioritize Browser-First Troubleshooting:** All exercises run in Google Colab. Avoid asking students to install local EDA packages unless they specifically request advanced local workflows.
3. **Encourage Iterative Check-ins:** Use a lightweight "Pass / Needs Revision" review standard on Discord rather than intimidating academic letter grades.

---

## 2. Module Rubrics & Solution Keys

---

### Module 1 (`W1D1`) — Biological & Conceptual Foundations

#### Part A: Anatomy (20 pts)
* **All 6 functional regions present (12 pts):** Dendrites, Soma, Axon Hillock, Axon, Synapse, Membrane.
* **Accurate functional placement (5 pts):** Threshold trigger labeled at the axon hillock/soma junction, not on dendrites.
* **Clarity (3 pts):** Legible diagram or digital drawing.

#### Part B: Qualitative Voltage Trace (30 pts)
* **Key phases identified (20 pts):** Resting baseline ($V_{reset}$), integration curve, horizontal threshold ($V_{th}$), instantaneous spike, refractory reset.
* **Two full cycles depicted (5 pts):** Demonstrates understanding of repeatable integration cycles.
* **Qualitative accuracy (5 pts):** Convex exponential trajectory, not a purely straight linear line.

#### Part C: Conceptual Questions (50 pts)
* **Q1 (15 pts) — The Leak:** Full marks for explaining that the leak represents passive ion diffusion through resting channels pulling $V$ toward $V_{reset}$. Without a leak, the neuron becomes a perfect accumulator with infinite memory of past inputs.
* **Q2 (15 pts) — Neuromorphic Bridge:** Full marks for linking biological sparsity or event-driven signaling to reduced static/dynamic power dissipation in digital hardware.
* **Q3 (20 pts) — Current Doubling:** Full marks for noting: (a) Inter-spike interval decreases (faster firing), (b) Spike amplitude remains unchanged (all-or-none digital event), and (c) Integration slope becomes steeper.

---

### Module 2 (`W1D2`) — Python LIF Reference Modeling

#### Part A: Python Class Implementation (50 pts)

```python
import numpy as np

class LIFNeuron:
    def __init__(self, tau=20.0, V_th=-55.0, V_reset=-70.0, dt=0.5):
        self.tau = tau
        self.V_th = V_th
        self.V_reset = V_reset
        self.dt = dt
        self.V = V_reset

    def step(self, I_in):
        # Discrete-time Euler update rule
        dV = (self.dt / self.tau) * (-(self.V - self.V_reset) + I_in)
        self.V += dV

        if self.V >= self.V_th:
            spike = 1
            self.V = self.V_reset
        else:
            spike = 0

        return self.V, spike

    def reset_state(self):
        self.V = self.V_reset
```

* **Mathematical correctness (20 pts):** Correct formulation of discrete decay and current injection.
* **Threshold & reset logic (15 pts):** Returns spike flag and correctly resets membrane state.
* **State persistence (10 pts):** Membrane state persists across sequential calls to `step()`.
* **Clean interface (5 pts):** Matches required arguments and return signatures.

#### Part B: Plots (30 pts)
* Single-current trace plotted with threshold line (10 pts).
* Multi-current traces ($I \in \{1.0, 2.0, 4.0\}$) on shared axes with legend (10 pts).
* Matches qualitative expectations from Module 1 (10 pts).

#### Part C: Analytical Questions (20 pts)
* **Q1 (10 pts):** Identifies non-linear compression in $f\text{-}I$ curve caused by the leak opposing incoming current as $V$ approaches threshold.
* **Q2 (10 pts):** Recognizes that removing the leak results in a non-decaying perfect integrator.

---

### Module 3 (`W1D3`) — Digital Logic Mapping & Bit-Width Analysis

#### Part A: Logic Mapping Key (40 pts)
* `V >= V_th` $\rightarrow$ Digital Comparator (8 pts).
* `V = V_reset` on spike $\rightarrow$ Multiplexer / MUX (8 pts).
* `return spike` $\rightarrow$ Output single-bit register/wire (8 pts).
* State retention $\rightarrow$ D Flip-Flop register bank (8 pts).
* Correct identification of subtractor and accumulator adders (8 pts).

#### Part B: Block Diagram (30 pts)
* All 5 components correctly identified (15 pts).
* Signal routing accurate (`I_in` into adder, comparator driving MUX select) (10 pts).
* Clock and synchronous reset clearly wired to register (5 pts).

#### Part C: Quantization & Bit-Shift Analysis (30 pts)
* **Q1 (15 pts) — Bit Width:** Range $= 40\,\text{mV}$, resolution $= 0.1\,\text{mV} \rightarrow \text{Steps} = 400$. $N = \lceil\log_2(400)\rceil = 9$ bits minimum for integer state; full marks for reasonable fixed-point allocations ($12$ to $16$ bits total).
* **Q2 (15 pts) — Bit-Shift Approximation:** $\frac{\Delta t}{\tau} = \frac{0.5}{20} = 0.025$. Nearest power-of-2 shift is $\frac{1}{32} = 0.03125$ (`>> 5`). Error: $\frac{0.03125 - 0.025}{0.025} = +25\%$. The hardware neuron will leak faster and fire slightly faster than the software model.

---

### Module 4 (`W1D4`) — Verilog Hardware Description

#### Part A: RTL Implementation (`lif_neuron.v`) (60 pts)

```verilog
`timescale 1ns / 1ps

module lif_neuron #(
    parameter WIDTH   = 16,
    parameter V_TH    = 16'd3800,
    parameter V_RESET = 16'd0,
    parameter TAU_INV = 5
) (
    input  wire              clk,
    input  wire              rst,
    input  wire [WIDTH-1:0]  I_in,
    output reg  [WIDTH-1:0]  V_out,
    output reg               spike
);

    reg [WIDTH-1:0] V_mem;

    always @(posedge clk) begin
        if (rst) begin
            V_mem <= V_RESET;
            V_out <= V_RESET;
            spike <= 1'b0;
        end else begin
            if (V_mem >= V_TH) begin
                spike <= 1'b1;
                V_mem <= V_RESET;
                V_out <= V_RESET;
            end else begin
                spike <= 1'b0;
                V_mem <= V_mem + I_in - ((V_mem - V_RESET) >> TAU_INV);
                V_out <= V_mem;
            end
        end
    end

endmodule
```

* Synthesizable sequential architecture (20 pts).
* Correct non-blocking (`<=`) assignments inside clocked block (15 pts).
* Parameterized bit-width and threshold registers (15 pts).
* Synchronous reset handling (10 pts).

#### Part B: Lint Check (20 pts)
* Clean execution under `verilator --lint-only -Wall` with zero warnings (20 pts). ($-5$ pts per unresolved width or blocking assignment warning).

#### Part C: Conceptual Questions (20 pts)
* **Q1 (10 pts):** `reg` holds state across clock edges (flip-flop memory), while `wire` is continuous combinational routing.
* **Q2 (10 pts):** Blocking (`=`) executes sequentially, creating race conditions and unintended combinational latches in hardware simulation.

---

### Module 5 (`W1D5`) — Simulation & Parity Verification

#### Part A: Testbench Execution (40 pts)
* Successful compilation and execution of `tb_lif_neuron.cpp` / Python testbench in Colab (20 pts).
* Clean `wave.csv` or `.vcd` trace generated (20 pts).

#### Part B: Waveform Visualization (30 pts)
* Matplotlib waveform plot displaying `clk`, `rst`, `I_in`, `V_out`, and `spike` (15 pts).
* Measured Inter-Spike Interval (ISI) in clock cycles (15 pts).

#### Part C: Hardware vs. Software Parity (30 pts)
* Correct measurement of hardware ISI (~180–220 clock cycles) and Python ISI (~240 timesteps) (10 pts).
* Correct calculation of percentage discrepancy ($\approx 20\text{–}25\%$) (10 pts).
* Correct attribution of error to the $\frac{1}{32}$ bit-shift decay approximation and quantization (10 pts).