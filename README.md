# DAA-Project
The de Bruijn graph is a fundamental concept in bioinformatics and graph theory, commonly used in genome assembly. It represents overlaps between substrings of a DNA sequence. The de Bruijn graph construction is a crucial step in genome assembly algorithms, particularly for short-read sequencing data.

Here's a brief overview of the problem statement and the initial data you will work with:

### Problem Statement:
Given a set of DNA sequences (reads), the goal is to reconstruct the original DNA sequence (genome) from which the reads were derived. This process is known as genome assembly. The de Bruijn graph method is a popular approach for solving this problem, as it efficiently represents the overlaps between reads.

### Initial Data:
1. **DNA Sequences (Reads):** You will be provided with a collection of short DNA sequences obtained from sequencing technology, such as Illumina sequencing. These reads are typically short fragments of the original genome.
   
2. **Read Length:** The length of each read will be known, denoted as \(k\). For example, for Illumina sequencing, typical read lengths range from 50 to 300 base pairs.

### Approach:
The de Bruijn graph method constructs a directed graph where nodes represent sequences of length \(k-1\) (k-mers) and edges represent overlaps between adjacent k-mers. The de Bruijn graph provides a compact representation of the overlaps between reads, facilitating the assembly process.

Here's a high-level overview of the algorithm using de Bruijn graph construction:

1. **K-merization:** Break each read into overlapping k-mers of length \(k\).
   
2. **Graph Construction:** Build a directed graph (de Bruijn graph) where nodes represent k-mers and edges represent overlaps between adjacent k-mers.

3. **Graph Traversal:** Traverse the de Bruijn graph to reconstruct the original genome. This step involves finding an Eulerian path or Eulerian cycle in the graph.

4. **Genome Reconstruction:** Assemble the genome by concatenating the k-mers along the Eulerian path or cycle.

### Example:
Suppose you have the following DNA reads:
- ATGCG
- CGTGT
- TGGTA
- GTATT

And the read length \(k\) is 3 (i.e., \(k = 3\)). 

You would first generate k-mers from the reads:
- ATG, TGC, GCG
- CGT, GTG, TGT
- TGG, GGT, GTA
- GTA, TAT, ATT

Then, you construct the de Bruijn graph using these k-mers and find an Eulerian path or cycle in the graph to reconstruct the genome.
