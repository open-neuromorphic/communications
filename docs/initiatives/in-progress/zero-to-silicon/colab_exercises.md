# Zero to Silicon
## Interactive Problem Sets & Notebook Specifications
**Participant Edition | Open Neuromorphic | Summer 2026**

*Build one verified artifact per module. By Module 5, your artifacts chain into a complete working hardware simulation.*

---

## The Co-Design Artifact Pipeline

Each module produces a tangible artifact. The artifact produced in one module forms the exact specification and input for the next:

| Module | Task / Focus | Artifact You Produce | Feeds Directly Into |
| :--- | :--- | :--- | :--- |
| **W1D1** | **Biological Foundations** | Annotated neuron sketch + qualitative voltage plot | *W1D2 Python mathematical specification* |
| **W1D2** | **Python LIF Reference** | `lif_neuron.py` class + $f\text{-}I$ curve plot | *W1D3 Digital logic translation source* |
| **W1D3** | **Digital Logic Mapping** | Gate mapping table + bit-width budget | *W1D4 Verilog hardware design target* |
| **W1D4** | **Verilog Hardware RTL** | Synthesizable, lint-clean `lif_neuron.v` | *W1D5 Simulation design-under-test* |
| **W1D5** | **Simulation & Co-Design** | Passing testbench + waveform + parity analysis | *Complete portfolio capstone* |

---

## Task 1 (`W1D1`) — Biological Foundations & Voltage Dynamics
*Module: Biological & Conceptual Foundations | Interactive Colab / Drawing Tool*

**Estimated Time:** 60–90 minutes  
**Environment:** Google Colab / Excalidraw / Drawing Tool  
**Submit to:** Discord `#zero-to-silicon` (Task 1 Thread)

### Background
A biological neuron is a continuous-time dynamical system that integrates synaptic currents across its membrane capacitance, leaks charge through resting ion channels, and emits a discrete, all-or-none action potential when membrane potential reaches threshold. In this task, you specify the biological behaviors that our digital chip must reproduce.

### Part A — Anatomical & Functional Schematic (20 pts)
Create a clean functional schematic of a biological neuron. Label all six core components:
1. **Dendrites:** Synaptic input collection.
2. **Soma:** Continuous somatic charge integration.
3. **Axon Hillock / Trigger Zone:** Action potential initiation site (threshold crossing).
4. **Axon:** Active propagation pathway.
5. **Synaptic Terminal:** Output interface to downstream neurons.
6. **Lipid Bilayer Membrane:** Capacitive boundary maintaining electrical potential difference.

### Part B — Qualitative Voltage Trace (30 pts)
Plot membrane potential ($V$) over time showing at least two full spike cycles. Clearly mark:
* Resting potential ($V_{reset}$).
* Exponential integration trajectory as constant current arrives.
* Firing threshold ($V_{th}$) as a dashed horizontal boundary.
* Instantaneous action potential spike.
* Post-spike refractory reset to baseline.

### Part C — Conceptual Reasoning (50 pts)

* **Question 1 (15 pts):** In 3–4 sentences, explain the physical meaning of the membrane "leak." What would happen to the firing frequency and memory of a neuron if the leak conductance were zero?
* **Question 2 (15 pts):** Choose one of the following biological features and describe in 2–3 sentences how it maps to an architectural advantage in digital silicon:
  * *Sparsity of spiking*
  * *Event-driven (clock-gated) signaling*
  * *Synaptic coincidence detection*
* **Question 3 (20 pts):** If input current ($I_{in}$) is doubled, describe the expected qualitative changes in: (a) Inter-spike interval, (b) Spike amplitude, and (c) Slope of the subthreshold integration curve.

---

## Task 2 (`W1D2`) — Prototyping an LIF Neuron in Python
*Module: Python LIF Reference Modeling | Pure Python + NumPy*

**Estimated Time:** 2 hours  
**Environment:** Google Colab (`W1D2_Tutorial1.ipynb`)  
**Submit to:** GitHub PR / Discord `#zero-to-silicon`

### Background
Before writing hardware description code, you must build a software reference model. Implementing discrete-time Euler integration from first principles ensures you understand the exact mathematical operations your silicon must execute.

### Part A — The `LIFNeuron` Reference Class (50 pts)
Implement a clean `LIFNeuron` class implementing this exact interface:

```python
import numpy as np

class LIFNeuron:
    def __init__(self, tau=20.0, V_th=-55.0, V_reset=-70.0, dt=0.5):
        """
        tau     : Membrane time constant (ms)
        V_th    : Firing threshold (mV)
        V_reset : Reset / resting potential (mV)
        dt      : Integration timestep (ms)
        """
        self.tau = tau
        self.V_th = V_th
        self.V_reset = V_reset
        self.dt = dt
        self.V = V_reset

    def step(self, I_in):
        """
        Executes one timestep of Euler integration:
        dV = (dt / tau) * (-(V - V_reset) + I_in)
        Returns: (V_current, spike_flag)
        """
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

### Part B — Simulation & Firing Response (30 pts)
Instantiate your neuron with parameters $\tau = 20\,\text{ms}$, $V_{th} = -55\,\text{mV}$, $V_{reset} = -70\,\text{mV}$, $\Delta t = 0.5\,\text{ms}$.
1. Run a 500-step simulation with constant current $I_{in} = 2.0\,\text{nA}$ and plot $V(t)$ with the threshold marked.
2. Run multi-current simulations ($I_{in} \in \{1.0, 2.0, 4.0\}\,\text{nA}$) on shared axes with a legend.

### Part C — Analytical Questions (20 pts)
* **Question 1 (10 pts):** Does the spike rate scale linearly with input current? Explain why the leak term causes the $f\text{-}I$ curve to compress at high frequencies.
* **Question 2 (10 pts):** If the leak term is dropped ($\Delta V = \frac{\Delta t}{\tau} I_{in}$), how does the neuron behave mathematically?

---

## Task 3 (`W1D3`) — Digital Logic Mapping & Bit-Width Analysis
*Module: Digital Logic Mapping & Bit-Width Analysis | Markdown / Colab*

**Estimated Time:** 90 minutes  
**Environment:** Google Colab (`W1D3_Tutorial1.ipynb`)  
**Submit to:** `lif_logic_map.md` in repository / Discord

### Background
Hardware executes arithmetic through physical gates and registers. In this task, you map every mathematical operation in `LIFNeuron.step()` to a hardware logic primitive and determine the integer and fractional bit widths required to avoid hardware overflow.

### Part A — Arithmetic Logic Mapping (40 pts)
Complete the digital translation table for every line of `LIFNeuron.step()`:

| Python Operation | Hardware Digital Component | Implementation Notes |
| :--- | :--- | :--- |
| `V - V_reset` | Subtractor | Eliminated if $V_{reset}$ is offset to digital `0` |
| `(dt / tau) * (...)` | Arithmetic Right-Shift | Multipliers are costly; approximate $\frac{\Delta t}{\tau} = \frac{0.5}{20} = \frac{1}{40} \approx \frac{1}{32}$ via `>> 5` |
| `V + dV` | Adder / Accumulator | Intermediate summation register |
| `V >= V_th` | Digital Comparator | Drives multiplexer select line |
| `V = V_reset` | Multiplexer (MUX) | Selects between updated potential and reset value |
| `spike` | Output Register / Wire | Single-bit digital flag, high for 1 clock cycle |
| State retention | D Flip-Flop Register (`V_mem`) | Holds membrane state across clock cycles |

### Part B — Block Diagram (30 pts)
Sketch the digital register-transfer level (RTL) block diagram showing:
* `clk` and synchronous `rst` lines routed to `V_mem`.
* Input current bus `I_in` feeding the arithmetic adder block.
* Comparator checking `V_mem >= V_th` to assert `spike`.
* Multiplexer routing either `V_reset` or `V_mem + dV` back to the register input.

### Part C — Quantization & Bit-Shift Analysis (30 pts)
* **Question 1 (15 pts):** Map the biological range ($V_{reset} = -70\,\text{mV}$ to $V_{th} = -55\,\text{mV}$) into unsigned fixed-point where $-70\,\text{mV} = 0$. For a dynamic range of $40\,\text{mV}$ with $0.1\,\text{mV}$ resolution, calculate the minimum required bit-width ($N = \lceil\log_2(\text{range}/\text{resolution})\rceil$).
* **Question 2 (15 pts):** Calculate the exact percentage error introduced by approximating $\frac{\Delta t}{\tau} = 0.025$ as $\frac{1}{32} = 0.03125$ (right-shift by 5). Will the simulated hardware neuron fire faster or slower than the Python reference model?

---

## Task 4 (`W1D4`) — Verilog Hardware Description
*Module: Verilog Hardware Description & Linting | In-Notebook Verilator*

**Estimated Time:** 2–3 hours  
**Environment:** Google Colab (`W1D4_Tutorial1.ipynb`)  
**Submit to:** Inline cell `lif_neuron.v`

### Background
Using your Task 3 logic map, implement a synthesizable Verilog module. The module runs fixed-point arithmetic using non-blocking sequential logic and passes static lint checks directly in Colab.

### Part A — Verilog Implementation (`lif_neuron.v`) (60 pts)
Write your hardware description module using the template below:

```verilog
%%file lif_neuron.v
`timescale 1ns / 1ps

module lif_neuron #(
    parameter WIDTH   = 16,
    parameter V_TH    = 16'd3800, // Fixed-point mapped threshold
    parameter V_RESET = 16'd0,    // Offset baseline
    parameter TAU_INV = 5         // Right-shift by 5 (~ 1/32 decay)
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
                // Leaky integration with arithmetic right-shift
                V_mem <= V_mem + I_in - ((V_mem - V_RESET) >> TAU_INV);
                V_out <= V_mem;
            end
        end
    end

endmodule
```

### Part B — In-Notebook Lint Check (20 pts)
Execute the Verilator linter cell in Colab and fix all warnings:

```python
!verilator --lint-only -Wall lif_neuron.v
```

*Criteria for Full Marks:* Zero warnings generated under `-Wall`.

### Part C — HDL Conceptual Checks (20 pts)
* **Question 1 (10 pts):** Why must `V_mem` be declared as a `reg` rather than a `wire` in sequential logic?
* **Question 2 (10 pts):** Explain why non-blocking assignments (`<=`) are mandatory inside clocked `always @(posedge clk)` blocks to avoid simulation race conditions.

---

## Task 5 (`W1D5`) — Simulation, Waveforms & Co-Design Verification
*Module: Verilator Simulation & Waveform Co-Design | Colab + Matplotlib*

**Estimated Time:** 2–3 hours  
**Environment:** Google Colab (`W1D5_Tutorial1.ipynb`)  
**Submit to:** Waveform plot + Co-Design Reflection in Discord `#zero-to-silicon`

### Background
In this capstone task, you compile your Verilog module into a cycle-accurate executable, apply testbench stimuli, visualize digital signal waveforms in Matplotlib, and measure the hardware-software parity against your Task 2 Python model.

### Part A — Testbench Execution in Colab (40 pts)
Execute the provided C++/Python testbench in your notebook for 2000 cycles with constant input $I_{in} = 200$:

```cpp
%%file tb_lif_neuron.cpp
#include "Vlif_neuron.h"
#include "verilated.h"
#include <iostream>
#include <fstream>

int main(int argc, char** argv) {
    Verilated::commandArgs(argc, argv);
    Vlif_neuron* top = new Vlif_neuron;

    std::ofstream out("wave.csv");
    out << "cycle,clk,rst,I_in,V_out,spike\n";

    top->clk = 0;
    top->rst = 1;
    top->I_in = 200;

    for (int cycle = 0; cycle < 1000; cycle++) {
        top->clk = !top->clk;
        if (cycle > 4) top->rst = 0;
        top->eval();
        if (top->clk) {
            out << cycle/2 << "," << (int)top->clk << "," << (int)top->rst << "," 
                << top->I_in << "," << top->V_out << "," << (int)top->spike << "\n";
        }
    }
    std::cout << "Simulation complete. Output written to wave.csv\n";
    delete top;
    return 0;
}
```

Compile and run:
```python
!verilator -Wall --cc --exe --build tb_lif_neuron.cpp lif_neuron.v
!./obj_dir/Vlif_neuron
```

### Part B — In-Notebook Waveform Visualization (30 pts)
Parse `wave.csv` and render the digital signal trace directly in Colab:

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("wave.csv")

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
ax1.plot(df["cycle"], df["V_out"], color="navy", label="Hardware V_mem")
ax1.axhline(y=3800, color="crimson", linestyle="--", label="Threshold V_th")
ax1.set_ylabel("Membrane Potential")
ax1.legend(loc="upper right")

ax2.step(df["cycle"], df["spike"], color="red", where="post", label="Spike Output")
ax2.set_ylabel("Digital Spike")
ax2.set_xlabel("Clock Cycle")
ax2.set_ylim(-0.1, 1.1)
ax2.legend(loc="upper right")

plt.suptitle("Zero to Silicon: Hardware Simulation Waveform", fontweight="bold")
plt.show()
```

### Part C — Hardware vs. Software Parity (30 pts)
1. Measure the **Inter-Spike Interval (ISI)** in clock cycles from your hardware waveform.
2. Run your Task 2 Python model using equivalent parameter scaling and compute the software ISI in timesteps.
3. **Written Reflection (150–200 words):**
    * Compare hardware ISI vs. Python ISI. Calculate the percentage discrepancy ($\frac{|\text{ISI}_{HW} - \text{ISI}_{SW}|}{\text{ISI}_{SW}} \times 100$).
    * Explain how the right-shift approximation ($1/32$ vs $1/40$) accounts for this discrepancy.
    * How would you scale this single-neuron module into an array of synaptic cores?

