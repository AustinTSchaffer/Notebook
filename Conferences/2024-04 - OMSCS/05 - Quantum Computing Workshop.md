---
tags:
---
# 05 - Quantum Computing Workshop
> By Lakshmi Yendapalli


- Classical Bit: 0 or 1
- Quantum Qubit: Probability distribution over the range of possibilities between 0 and 1
	- "It's simultaneously 0 and 1"
	- Quantum speedup comes from operating on those qbits
- It's all just abstracted concepts.
	- Bits in a computer are a logical construct.
	- Qubits are also a logical construct, based on an underlying quantum particle. We tap into the quantum phenomena through the quantum particle. This is achieved via
		- Trapped Ions
		- Superconnected Qubits
		- Lots of near-0-Kelvin cooling
- "We just write the programs and we just care about the output."
- Best way to represent Qubit operations? linear algebra.
	- $\Psi = \alpha | 0 \rangle + \beta | 1 \rangle$
	- $|0\rangle = [ 1 \space 0 ]$
	- $|1\rangle = [ 0 \space 1 ]$
	- $\Psi = [ \alpha \space \beta ]$
- $\circledcross$ = "Tensor product"
	- Taking the tensor product allows us to combine the results of multiple qubits
- Number of States = 2 ^ (number of Qubits)
	- Example 4-Qubit state: $|0110\rangle$
- Qubits are represented via a vector representation
	- $\theta$ represents the Qubit in a unit-circle space.
	- $\alpha = cos(\theta)$
	- $P(\alpha = 0) = cos^2(\theta)$
	- $\beta = sin(\theta)$
	- $P(\beta = 1) = sin^2(\theta)$
	- https://bloch.kherb.io/
	- The sphere notation is apparently more common, but otherwise describes the same phenomenon.
- "All operations on Qubits are rotations"

## Quantum Gates
- X Gate - Rotates the qubit $180\degree$ in the X axis - Multiply by matrix `((0 1), (1 0))`
- Y Gate - Rotates the qubit in the Y axis - Multiply by matrix `((0, -i), (i, 0))`
- H Gate - Rotates qubit along a 45 degree angle between the X and Z axis - $(1/\sqrt{2}) \times ((1, 1),(1, -1))$ 
- CNOT - Uses a control qubit and a target qubit. The control qubit controls whether the "NOT" operation to the target qubit. `((1,0,0,0), (0,1,0,0), (0,0,0,1), (0,0,1,0))`

## Entanglement
> "Spooky action at a distance."
>
> Einstein - chief dork

- "It's just one of those weird things that quantum particles do."
- "Observing one impacts the other qubit somehow."
- It's possible to entangle 2 qubits, such that observing one, collapsing it to a value, gives 100% certainty that the other qubit has also collapsed to the same value.
- EPR Paradox
	- "There must be something wrong with entanglement as described."
	- "Superposition cannot be observed."
- John Bell designed an experiment to measure superposition.
	- Some inequality which would decide whether particles were not entangled and instead had some hidden property that explains superposition.
	- Experiment was performed by John Clauser, Alain Aspect, Anton Zeilinger
	- Turns out Einstein was wrong.
- Entanglement is correlation, not communication.

## CHSH game

- Alice gets random bit X
- Bob gets random bit Y
- some strategy is applied
- Alice creates output bit A
- Bob creates output bit B
- $X \cdot Y = A \oplus B$
	- "X logical-and Y" should be the same operation as "A exclusive-or B"

| X   | Y   | $X \cdot Y$ |
| --- | --- | ----------- |
| 0   | 0   | 0           |
| 0   | 1   | 0           |
| 1   | 0   | 0           |
| 1   | 1   | 1           |
- Strategy
	- Alice
		- $X=0: \theta = 0$
		- $X = 1: \theta = \pi/4$
	- Bob
		- $Y = 0: \theta = \pi/8$
		 - $Y = 1: \theta = -\pi/8$
 - This strategy results in 85% win probability, compared to the classical probability of 75%.

## Qiskit
- How to do Quantum Computing
	- Design a "circuit" for performing quantum computations
	- Run your circuit against a quantum "simulator" to make sure that everything is working correctly.
	- Run your circuit against a real quantum computer.
- IBM has a Python package/API/service Qiskit
	- You specify a "backend" for performing the qubit operations. The package provides multiple backends for different "simulators" on classical computers, and a separate backend for running the qubit operations in 
	- The IBM-provided-quantum-computers backend is super slow. Your job gets added to a queue. You have to wait for your job to make it through the queue before you get an output.
- Circuit design
	- Define number of qubits
	- define number of "classical registers" (for recording the output)
	- Qiskit uses a different notation from what is in the previous section in this doc.

