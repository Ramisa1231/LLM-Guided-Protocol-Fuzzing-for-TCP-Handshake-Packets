# LLM-Guided-Protocol-Fuzzing-for-TCP-Handshake-Packets
evaluates whether large language models can understand and fuzz TCP handshakes. The project studies grammar inference, hex dump parsing, packet generation under mutation, and state-aware next-packet prediction using real Wireshark TCP traffic


This project evaluates whether Large Language Models (LLMs) can understand, parse, generate, and reason about **TCP handshake packets** for protocol fuzzing and state inference.  
The study is conducted by a single researcher and uses **real TCP traffic captured via Wireshark**.

---

## 📁 Repository Structure

```text
.
├── ground_truth_grammar/
│   ├── SYN.json
│   ├── SYNACK.json
│   └── ACK.json
│
├── tcp_server.py
├── tcp_client.py
│
├── data/
│   ├── handshake.pcap
│   ├── handshake_packets.txt
│   ├── handshake_hex.txt
│   └── ground_truth.txt
│
├── task1a/
├── task1b/
├── task2/
├── task3/
│
└── README.md

```
## 🔹 Task 1a — TCP Packet Grammar Inference

### Goal
Evaluate whether an LLM can infer structured TCP packet grammars for handshake packets.

### Setup
Create a folder called `ground_truth_grammar/` containing grammar definitions for
`SYN.json`, `SYNACK.json`, and `ACK.json`.

```bash
ground_truth_grammar/
```

Add three ground truth grammar files:
```text
.
├── ground_truth_grammar/
│   ├── SYN.json
│   ├── SYNACK.json
│   └── ACK.json
```
Each JSON file defines the expected structure and fields of the corresponding TCP packet type.
These grammars are used as ground truth for evaluating LLM-generated grammars.




##🔹 Task 1b — TCP Hex Dump Parsing
### Goal
Evaluate whether an LLM can parse raw TCP hex dumps and extract correct header fields and values.

This task uses real TCP traffic captured locally.

### Setup
#### 🔧 Step 1: Run TCP Server and Client
Start the TCP server:

```bash
python tcp_server.py
```
Start the TCP client in a separate terminal:
```bash
python tcp_client.py
```

This generates a real TCP handshake on localhost:12345.

#### 🔧 Step 2: Capture Traffic Using tshark (Windows CMD)

##### 1️⃣ Capture packets to PCAP
```cmd

"C:\Program Files\Wireshark\tshark.exe" ^
-i 7 ^
-a duration:30 ^
-f "tcp port 12345" ^
-w "C:\pathto\handshake.pcap"
```
##### 2️⃣ Extract column-wise TCP header fields
```cmd
"C:\Program Files\Wireshark\tshark.exe" ^
-r "C:\Users\ramif\OneDrive\Desktop\SEMESTER 4\Mobile and Wireless\DATA2\handshake.pcap" ^
-T fields ^
-E separator=, ^
-e frame.number ^
-e tcp.srcport ^
-e tcp.dstport ^
-e tcp.seq ^
-e tcp.ack ^
-e tcp.hdr_len ^
-e tcp.flags ^
-e tcp.flags.syn ^
-e tcp.flags.ack ^
-e tcp.window_size_value ^
-e tcp.checksum ^
-e tcp.urgent_pointer ^
-e tcp.options ^
-e tcp.payload ^
> "C:\pathto\handshake_packets.txt"
```
#####3️⃣ Extract raw TCP hex dump
```cmd

"C:\Program Files\Wireshark\tshark.exe" ^
-r "C:\Users\ramif\OneDrive\Desktop\SEMESTER 4\Mobile and Wireless\DATA2\handshake.pcap" ^
-x ^
> "C:\Users\ramif\OneDrive\Desktop\SEMESTER 4\Mobile and Wireless\DATA2\handshake_hex.txt"
```
#####4️⃣ Extract full ground truth (Wireshark-style)
```cmd

"C:\pProgram Files\Wireshark\tshark.exe" ^
-r "C:\pathto\handshake.pcap" ^
> "C:\pathto\ground_truth.txt"
```
####📂 Files Produced
```text
| File                    | Purpose                         |
| ----------------------- | ------------------------------- |
| `handshake.pcap`        | Raw packet capture              |
| `handshake_packets.txt` | Column-wise TCP header values   |
| `handshake_hex.txt`     | Raw TCP hex dump                |
| `ground_truth.txt`      | Human-readable TCP ground truth |
```

These files are converted into CSV format and reused in Tasks 1b, 2, and 3.

##🔹 Task 2 — ACK Packet Generation from Mutated Inputs
###Goal
Evaluate whether LLMs can generate a valid ACK packet hex dump given:

A mutated SYN packet

A mutated SYN-ACK packet

Evaluation Metrics
Valid packet type generation

Missing packet type rate

Hallucination rate

Relative packet position correctness

🔹 Task 3 — TCP State Transition Prediction
Goal
Evaluate whether LLMs can infer stateful TCP behavior.

Given:

The current TCP state

The current packet hex dump

The LLM is asked to generate the next packet in the handshake.

Outcomes
Successful state transition

Partial state transition

Unsuccessful state transition

Hallucination

🧪 Models Evaluated
GPT-3.5-Turbo

GPT-4.1

Each task is evaluated using:

Baseline prompting

One-shot + Chain-of-Thought prompting

