# OpenArxiv

A simple python script(hack) to extract latest `Arxiv Papers with Open Source Code` in your favorite topic of interest.
Currently implemented for a combination of Software Engineering(SE) and Machine Learning(ML)/Artificial Intelligence(AI) and results hosted @ [manishshettym/openarxiv](https://manishshettym.github.io/openarxiv.html)

### Credits/References
<img align="right" src="https://miro.medium.com/max/3192/0*SNH9LTObVJWzVtzA" width="40%"></img>
1. `The partnership that made this happen is well chronicled here` - [Link to Medium Release](https://medium.com/paperswithcode/papers-with-code-partners-with-arxiv-ecc362883167) 
2. Arxiv API - [API](https://pypi.org/project/arxiv/)


### To change category of interest:
1. Visit [Line 5, main.py](https://github.com/ManishShettyM/OpenArxiv/blob/6241c46a3649bd19ae024df6dd6f14058c440682/main.py#L5)
2. Apply a combination of sub-category codes using `AND`, `OR`, `ANDNOT` operators as well as parenthesis`()`
3. Refer to the table below for sub-category codes

#### Arxiv Sub-Categories:
<table class="table is-striped">
<thead>
<tr>
<th align="left">Sub Category Code</th>
<th align="left">Sub Category Name</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">astro-ph</td>
<td align="left">Astrophysics</td>
</tr>
<tr>
<td align="left">astro-ph.CO</td>
<td align="left">Cosmology and Nongalactic Astrophysics</td>
</tr>
<tr>
<td align="left">astro-ph.EP</td>
<td align="left">Earth and Planetary Astrophysics</td>
</tr>
<tr>
<td align="left">astro-ph.GA</td>
<td align="left">Astrophysics of Galaxies</td>
</tr>
<tr>
<td align="left">astro-ph.HE</td>
<td align="left">High Energy Astrophysical Phenomena</td>
</tr>
<tr>
<td align="left">astro-ph.IM</td>
<td align="left">Instrumentation and Methods for Astrophysics</td>
</tr>
<tr>
<td align="left">astro-ph.SR</td>
<td align="left">Solar and Stellar Astrophysics</td>
</tr>
<tr>
<td align="left">cond-mat.dis-nn</td>
<td align="left">Disordered Systems and Neural Networks</td>
</tr>
<tr>
<td align="left">cond-mat.mes-hall</td>
<td align="left">Mesoscale and Nanoscale Physics</td>
</tr>
<tr>
<td align="left">cond-mat.mtrl-sci</td>
<td align="left">Materials Science</td>
</tr>
<tr>
<td align="left">cond-mat.other</td>
<td align="left">Other Condensed Matter</td>
</tr>
<tr>
<td align="left">cond-mat.quant-gas</td>
<td align="left">Quantum Gases</td>
</tr>
<tr>
<td align="left">cond-mat.soft</td>
<td align="left">Soft Condensed Matter</td>
</tr>
<tr>
<td align="left">cond-mat.stat-mech</td>
<td align="left">Statistical Mechanics</td>
</tr>
<tr>
<td align="left">cond-mat.str-el</td>
<td align="left">Strongly Correlated Electrons</td>
</tr>
<tr>
<td align="left">cond-mat.supr-con</td>
<td align="left">Superconductivity</td>
</tr>
<tr>
<td align="left">cs.AI</td>
<td align="left">Artificial Intelligence</td>
</tr>
<tr>
<td align="left">cs.AR</td>
<td align="left">Hardware Architecture</td>
</tr>
<tr>
<td align="left">cs.CC</td>
<td align="left">Computational Complexity</td>
</tr>
<tr>
<td align="left">cs.CE</td>
<td align="left">Computational Engineering, Finance, and Science</td>
</tr>
<tr>
<td align="left">cs.CG</td>
<td align="left">Computational Geometry</td>
</tr>
<tr>
<td align="left">cs.CL</td>
<td align="left">Computation and Language</td>
</tr>
<tr>
<td align="left">cs.CR</td>
<td align="left">Cryptography and Security</td>
</tr>
<tr>
<td align="left">cs.CV</td>
<td align="left">Computer Vision and Pattern Recognition</td>
</tr>
<tr>
<td align="left">cs.CY</td>
<td align="left">Computers and Society</td>
</tr>
<tr>
<td align="left">cs.DB</td>
<td align="left">Databases</td>
</tr>
<tr>
<td align="left">cs.DC</td>
<td align="left">Distributed, Parallel, and Cluster Computing</td>
</tr>
<tr>
<td align="left">cs.DL</td>
<td align="left">Digital Libraries</td>
</tr>
<tr>
<td align="left">cs.DM</td>
<td align="left">Discrete Mathematics</td>
</tr>
<tr>
<td align="left">cs.DS</td>
<td align="left">Data Structures and Algorithms</td>
</tr>
<tr>
<td align="left">cs.ET</td>
<td align="left">Emerging Technologies</td>
</tr>
<tr>
<td align="left">cs.FL</td>
<td align="left">Formal Languages and Automata Theory</td>
</tr>
<tr>
<td align="left">cs.GL</td>
<td align="left">General Literature</td>
</tr>
<tr>
<td align="left">cs.GR</td>
<td align="left">Graphics</td>
</tr>
<tr>
<td align="left">cs.GT</td>
<td align="left">Computer Science and Game Theory</td>
</tr>
<tr>
<td align="left">cs.HC</td>
<td align="left">Human-Computer Interaction</td>
</tr>
<tr>
<td align="left">cs.IR</td>
<td align="left">Information Retrieval</td>
</tr>
<tr>
<td align="left">cs.IT</td>
<td align="left">Information Theory</td>
</tr>
<tr>
<td align="left">cs.LG</td>
<td align="left">Learning</td>
</tr>
<tr>
<td align="left">cs.LO</td>
<td align="left">Logic in Computer Science</td>
</tr>
<tr>
<td align="left">cs.MA</td>
<td align="left">Multiagent Systems</td>
</tr>
<tr>
<td align="left">cs.MM</td>
<td align="left">Multimedia</td>
</tr>
<tr>
<td align="left">cs.MS</td>
<td align="left">Mathematical Software</td>
</tr>
<tr>
<td align="left">cs.NA</td>
<td align="left">Numerical Analysis</td>
</tr>
<tr>
<td align="left">cs.NE</td>
<td align="left">Neural and Evolutionary Computing</td>
</tr>
<tr>
<td align="left">cs.NI</td>
<td align="left">Networking and Internet Architecture</td>
</tr>
<tr>
<td align="left">cs.OH</td>
<td align="left">Other Computer Science</td>
</tr>
<tr>
<td align="left">cs.OS</td>
<td align="left">Operating Systems</td>
</tr>
<tr>
<td align="left">cs.PF</td>
<td align="left">Performance</td>
</tr>
<tr>
<td align="left">cs.PL</td>
<td align="left">Programming Languages</td>
</tr>
<tr>
<td align="left">cs.RO</td>
<td align="left">Robotics</td>
</tr>
<tr>
<td align="left">cs.SC</td>
<td align="left">Symbolic Computation</td>
</tr>
<tr>
<td align="left">cs.SD</td>
<td align="left">Sound</td>
</tr>
<tr>
<td align="left">cs.SE</td>
<td align="left">Software Engineering</td>
</tr>
<tr>
<td align="left">cs.SI</td>
<td align="left">Social and Information Networks</td>
</tr>
<tr>
<td align="left">cs.SY</td>
<td align="left">Systems and Control</td>
</tr>
<tr>
<td align="left">econ.EM</td>
<td align="left">Econometrics</td>
</tr>
<tr>
<td align="left">eess.AS</td>
<td align="left">Audio and Speech Processing</td>
</tr>
<tr>
<td align="left">eess.IV</td>
<td align="left">Image and Video Processing</td>
</tr>
<tr>
<td align="left">eess.SP</td>
<td align="left">Signal Processing</td>
</tr>
<tr>
<td align="left">gr-qc</td>
<td align="left">General Relativity and Quantum Cosmology</td>
</tr>
<tr>
<td align="left">hep-ex</td>
<td align="left">High Energy Physics - Experiment</td>
</tr>
<tr>
<td align="left">hep-lat</td>
<td align="left">High Energy Physics - Lattice</td>
</tr>
<tr>
<td align="left">hep-ph</td>
<td align="left">High Energy Physics - Phenomenology</td>
</tr>
<tr>
<td align="left">hep-th</td>
<td align="left">High Energy Physics - Theory</td>
</tr>
<tr>
<td align="left">math.AC</td>
<td align="left">Commutative Algebra</td>
</tr>
<tr>
<td align="left">math.AG</td>
<td align="left">Algebraic Geometry</td>
</tr>
<tr>
<td align="left">math.AP</td>
<td align="left">Analysis of PDEs</td>
</tr>
<tr>
<td align="left">math.AT</td>
<td align="left">Algebraic Topology</td>
</tr>
<tr>
<td align="left">math.CA</td>
<td align="left">Classical Analysis and ODEs</td>
</tr>
<tr>
<td align="left">math.CO</td>
<td align="left">Combinatorics</td>
</tr>
<tr>
<td align="left">math.CT</td>
<td align="left">Category Theory</td>
</tr>
<tr>
<td align="left">math.CV</td>
<td align="left">Complex Variables</td>
</tr>
<tr>
<td align="left">math.DG</td>
<td align="left">Differential Geometry</td>
</tr>
<tr>
<td align="left">math.DS</td>
<td align="left">Dynamical Systems</td>
</tr>
<tr>
<td align="left">math.FA</td>
<td align="left">Functional Analysis</td>
</tr>
<tr>
<td align="left">math.GM</td>
<td align="left">General Mathematics</td>
</tr>
<tr>
<td align="left">math.GN</td>
<td align="left">General Topology</td>
</tr>
<tr>
<td align="left">math.GR</td>
<td align="left">Group Theory</td>
</tr>
<tr>
<td align="left">math.GT</td>
<td align="left">Geometric Topology</td>
</tr>
<tr>
<td align="left">math.HO</td>
<td align="left">History and Overview</td>
</tr>
<tr>
<td align="left">math.IT</td>
<td align="left">Information Theory</td>
</tr>
<tr>
<td align="left">math.KT</td>
<td align="left">K-Theory and Homology</td>
</tr>
<tr>
<td align="left">math.LO</td>
<td align="left">Logic</td>
</tr>
<tr>
<td align="left">math.MG</td>
<td align="left">Metric Geometry</td>
</tr>
<tr>
<td align="left">math.MP</td>
<td align="left">Mathematical Physics</td>
</tr>
<tr>
<td align="left">math.NA</td>
<td align="left">Numerical Analysis</td>
</tr>
<tr>
<td align="left">math.NT</td>
<td align="left">Number Theory</td>
</tr>
<tr>
<td align="left">math.OA</td>
<td align="left">Operator Algebras</td>
</tr>
<tr>
<td align="left">math.OC</td>
<td align="left">Optimization and Control</td>
</tr>
<tr>
<td align="left">math.PR</td>
<td align="left">Probability</td>
</tr>
<tr>
<td align="left">math.QA</td>
<td align="left">Quantum Algebra</td>
</tr>
<tr>
<td align="left">math.RA</td>
<td align="left">Rings and Algebras</td>
</tr>
<tr>
<td align="left">math.RT</td>
<td align="left">Representation Theory</td>
</tr>
<tr>
<td align="left">math.SG</td>
<td align="left">Symplectic Geometry</td>
</tr>
<tr>
<td align="left">math.SP</td>
<td align="left">Spectral Theory</td>
</tr>
<tr>
<td align="left">math.ST</td>
<td align="left">Statistics Theory</td>
</tr>
<tr>
<td align="left">math-ph</td>
<td align="left">Mathematical Physics</td>
</tr>
<tr>
<td align="left">nlin.AO</td>
<td align="left">Adaptation and Self-Organizing Systems</td>
</tr>
<tr>
<td align="left">nlin.CD</td>
<td align="left">Chaotic Dynamics</td>
</tr>
<tr>
<td align="left">nlin.CG</td>
<td align="left">Cellular Automata and Lattice Gases</td>
</tr>
<tr>
<td align="left">nlin.PS</td>
<td align="left">Pattern Formation and Solitons</td>
</tr>
<tr>
<td align="left">nlin.SI</td>
<td align="left">Exactly Solvable and Integrable Systems</td>
</tr>
<tr>
<td align="left">nucl-ex</td>
<td align="left">Nuclear Experiment</td>
</tr>
<tr>
<td align="left">nucl-th</td>
<td align="left">Nuclear Theory</td>
</tr>
<tr>
<td align="left">physics.acc-ph</td>
<td align="left">Accelerator Physics</td>
</tr>
<tr>
<td align="left">physics.ao-ph</td>
<td align="left">Atmospheric and Oceanic Physics</td>
</tr>
<tr>
<td align="left">physics.app-ph</td>
<td align="left">Applied Physics</td>
</tr>
<tr>
<td align="left">physics.atm-clus</td>
<td align="left">Atomic and Molecular Clusters</td>
</tr>
<tr>
<td align="left">physics.atom-ph</td>
<td align="left">Atomic Physics</td>
</tr>
<tr>
<td align="left">physics.bio-ph</td>
<td align="left">Biological Physics</td>
</tr>
<tr>
<td align="left">physics.chem-ph</td>
<td align="left">Chemical Physics</td>
</tr>
<tr>
<td align="left">physics.class-ph</td>
<td align="left">Classical Physics</td>
</tr>
<tr>
<td align="left">physics.comp-ph</td>
<td align="left">Computational Physics</td>
</tr>
<tr>
<td align="left">physics.data-an</td>
<td align="left">Data Analysis, Statistics and Probability</td>
</tr>
<tr>
<td align="left">physics.ed-ph</td>
<td align="left">Physics Education</td>
</tr>
<tr>
<td align="left">physics.flu-dyn</td>
<td align="left">Fluid Dynamics</td>
</tr>
<tr>
<td align="left">physics.gen-ph</td>
<td align="left">General Physics</td>
</tr>
<tr>
<td align="left">physics.geo-ph</td>
<td align="left">Geophysics</td>
</tr>
<tr>
<td align="left">physics.hist-ph</td>
<td align="left">History and Philosophy of Physics</td>
</tr>
<tr>
<td align="left">physics.ins-det</td>
<td align="left">Instrumentation and Detectors</td>
</tr>
<tr>
<td align="left">physics.med-ph</td>
<td align="left">Medical Physics</td>
</tr>
<tr>
<td align="left">physics.optics</td>
<td align="left">Optics</td>
</tr>
<tr>
<td align="left">physics.plasm-ph</td>
<td align="left">Plasma Physics</td>
</tr>
<tr>
<td align="left">physics.pop-ph</td>
<td align="left">Popular Physics</td>
</tr>
<tr>
<td align="left">physics.soc-ph</td>
<td align="left">Physics and Society</td>
</tr>
<tr>
<td align="left">physics.space-ph</td>
<td align="left">Space Physics</td>
</tr>
<tr>
<td align="left">q-bio.BM</td>
<td align="left">Biomolecules</td>
</tr>
<tr>
<td align="left">q-bio.CB</td>
<td align="left">Cell Behavior</td>
</tr>
<tr>
<td align="left">q-bio.GN</td>
<td align="left">Genomics</td>
</tr>
<tr>
<td align="left">q-bio.MN</td>
<td align="left">Molecular Networks</td>
</tr>
<tr>
<td align="left">q-bio.NC</td>
<td align="left">Neurons and Cognition</td>
</tr>
<tr>
<td align="left">q-bio.OT</td>
<td align="left">Other Quantitative Biology</td>
</tr>
<tr>
<td align="left">q-bio.PE</td>
<td align="left">Populations and Evolution</td>
</tr>
<tr>
<td align="left">q-bio.QM</td>
<td align="left">Quantitative Methods</td>
</tr>
<tr>
<td align="left">q-bio.SC</td>
<td align="left">Subcellular Processes</td>
</tr>
<tr>
<td align="left">q-bio.TO</td>
<td align="left">Tissues and Organs</td>
</tr>
<tr>
<td align="left">q-fin.CP</td>
<td align="left">Computational Finance</td>
</tr>
<tr>
<td align="left">q-fin.EC</td>
<td align="left">Economics</td>
</tr>
<tr>
<td align="left">q-fin.GN</td>
<td align="left">General Finance</td>
</tr>
<tr>
<td align="left">q-fin.MF</td>
<td align="left">Mathematical Finance</td>
</tr>
<tr>
<td align="left">q-fin.PM</td>
<td align="left">Portfolio Management</td>
</tr>
<tr>
<td align="left">q-fin.PR</td>
<td align="left">Pricing of Securities</td>
</tr>
<tr>
<td align="left">q-fin.RM</td>
<td align="left">Risk Management</td>
</tr>
<tr>
<td align="left">q-fin.ST</td>
<td align="left">Statistical Finance</td>
</tr>
<tr>
<td align="left">q-fin.TR</td>
<td align="left">Trading and Market Microstructure</td>
</tr>
<tr>
<td align="left">quant-ph</td>
<td align="left">Quantum Physics</td>
</tr>
<tr>
<td align="left">stat.AP</td>
<td align="left">Applications</td>
</tr>
<tr>
<td align="left">stat.CO</td>
<td align="left">Computation</td>
</tr>
<tr>
<td align="left">stat.ME</td>
<td align="left">Methodology</td>
</tr>
<tr>
<td align="left">stat.ML</td>
<td align="left">Machine Learning</td>
</tr>
<tr>
<td align="left">stat.OT</td>
<td align="left">Other Statistics</td>
</tr>
<tr>
<td align="left">stat.TH</td>
<td align="left">Statistics Theory</td>
</tr>
</tbody>
</table>
