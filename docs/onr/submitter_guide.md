# ONM Research Initiative — Submitter's Guide

Welcome to the ONM Research Initiative! This guide outlines how to submit your work for review and inclusion in the ONM Community Peer Review Program.

#### Submissions are accepted on a rolling basis

---

## What Can You Submit?

We welcome open-source neuromorphic projects of all kinds, including but not limited to:

- Research codebases (e.g., SNN models, simulators, benchmarks)
- Datasets and dataset preparation pipelines
- Educational tools, tutorials, and documentation
- Hardware support libraries and FPGA/ASIC interfaces
- Analysis tools, visualization, and measurement utilities

Submissions may take the form of:
- **Git repositories** containing software and documentation  
- **Jupyter notebooks** with code, figures, and narrative explanations  
- **IEEE-formatted papers** (PDF)  
- **Technical whitepapers** or overview documents (PDF or web-hosted)  

Your project must satisfy Open Neuromorphics [Definition of Open](../policies/open-definition.md)

We especially encourage well-documented Jupyter notebooks that walk through core functionality, demonstrate reproducibility, or explain concepts interactively.  Also, please try to submit source files of figures if possible.

---

## How to Submit

### Prerequisites

**All authors must have existing OpenReview profiles** before submitting. If you don't have one:
1. Create an account at [OpenReview.net](https://openreview.net/)
2. Complete your profile with your name, email, and affiliations
3. Ensure your profile ID follows the format `~FirstName_LastName1` (e.g., `~Jane_Doe1`)

### Submission Process

Submit your work through OpenReview using the official ONM Research submission form.  
🔗 [OpenReview ONR Submission Portal](https://openreview.net/)

You will be required to provide the following information:

#### 1. **Title** *(required)*
- **Type**: Text field
- **Max length**: 250 characters
- **Supports**: TeX formulas using `$…$` for inline or `$$…$$` for display math
- **Example**: `Efficient Spiking Neural Networks for $\mathcal{O}(n)$ Classification`

#### 2. **Abstract** *(required)*
- **Type**: Textarea
- **Max length**: 5000 characters
- **Supports**: TeX formulas for mathematical notation
- **Tip**: Clearly summarize your contribution, methods, and key findings

#### 3. **Authors** *(required)*
- **Type**: Comma-separated list
- **Format**: `FirstName LastName, FirstName LastName`
- **Note**: This field is hidden and not publicly displayed
- **Example**: `Jane Doe, John Smith, Alice Johnson`

#### 4. **Author IDs** *(required)*
- **Type**: Comma-separated list of OpenReview profile IDs
- **Format**: Must match the pattern `~.*` (e.g., `~Jane_Doe1`)
- **Must map to**: Valid OpenReview profiles
- **Example**: `~Jane_Doe1, ~John_Smith2, ~Alice_Johnson1`
- **Important**: The order must match the author list above

#### 5. **PDF** *(required)*
- **Type**: File upload
- **Format**: `.pdf` only
- **Max size**: 50 MB
- **Requirements**: 
  - Must include title, authors, abstract, and references
  - Should be well-formatted and readable
  - Ensure proper anonymization if required by submission guidelines

#### 6. **Submission Length** *(required)*
- **Type**: Single choice
- **Options**:
  - `Regular submission (≤12 pages of main content)` — for papers with up to 12 pages of main content (excluding references and appendices)
  - `Long submission (>12 pages)` — for papers exceeding 12 pages of main content
- **Note**: Choose based on your main content length; references and appendices are not counted

#### 7. **Supplementary Material** *(optional)*
- **Type**: File upload
- **Formats**: `.zip` or `.pdf`
- **Max size**: 100 MB
- **Requirements**:
  - Must be anonymized
  - Must be self-contained (do not rely on external links)
  - Visible to reviewers and public
- **May include**: Code, datasets, additional figures, extended proofs, demo videos
- **Tip**: Organize ZIP files with a clear directory structure and include a README

#### 8. **Previous ONR Submission URL** *(optional)*
- **Type**: Text field
- **Format**: Must match `https://openreview.net/forum?id=.*`
- **When to use**: If this is a revision of a previously submitted work
- **Example**: `https://openreview.net/forum?id=abc123xyz`

#### 9. **Changes Since Last Submission** *(optional)*
- **Type**: Textarea
- **Supports**: Markdown and TeX formulas
- **When to use**: Required if you provided a previous submission URL
- **Tip**: Be specific about what changed (e.g., "Added experiments on dataset X", "Revised Section 3 based on reviewer feedback")

#### 10. **Competing Interests** *(required)*
- **Type**: Textarea
- **Purpose**: Disclose any conflicts of interest
- **Format**: Free text
- **If none**: Enter `N/A`
- **Examples of competing interests**:
  - Employment or consulting relationships with organizations related to the submission
  - Financial interests in companies related to the work
  - Personal relationships with potential reviewers

#### 11. **Human Subjects Reporting** *(required)*
- **Type**: Textarea
- **Purpose**: Disclose if your research involved human subjects
- **If not applicable**: Enter `N/A`
- **If applicable**: Provide:
  - IRB approval information
  - Consent procedures
  - Data privacy measures
  - Compliance with ethical guidelines

### After Submission

Your submission will be reviewed by a panel of 3–5 ONM volunteer reviewers. You'll receive confirmation and an estimated timeline for decisions.

---

## Review Criteria

Projects are evaluated based on:
- **Openness**: Is the project license-compatible and open to contributions?
- **Impact & Utility**: Does the project address significant challenges in the field of Neuromorphic Computing?
- **Clarity**: Is the project well-implemented, well-documented, and easy to navigate?
- **Documentation**: Are setup and usage instructions complete and usable?
- **Reproducibility**: Can reviewers run or verify the work easily?
- **Technical Quality**: Is the work rigorous, correct, and useful to others?

---

## Outcomes

We expect to provide decisions by a month after submission.

After review:
- If **approved**, your project will receive:
  - **For software projects:** An "ONM Community Approved" badge (for your README)
  - **For papers:** A listing in the ONM Research Registry
  - Potential to lead talks and workshops through ONM's website, Discord, and social media

- If **not yet approved**, you'll receive actionable feedback and may revise and resubmit.

---

## Questions?

Join us on the [ONM Discord](https://discord.gg/3dbSPeAZkk)! or email: [contact@open-neuromorphic.org](mailto:contact@open-neuromorphic.org)

We look forward to seeing your work!
