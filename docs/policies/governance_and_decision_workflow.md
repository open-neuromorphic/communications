# Policy Proposal: Governance Documentation and Decision Workflow

## 1. Purpose & Scope
Following the mandates of the 2026 Annual General Meeting (AGM) to adopt a flattened Executive Committee structure, Open Neuromorphic (ONM) requires a transparent, version-controlled, and auditable process for formalizing organizational decisions.

This policy defines the official workflow for proposing, debating, and ratifying policies, roles, and Charter amendments. The `open-neuromorphic/communications` GitHub repository serves as the official system of record for all ONM governance.

## 2. System of Record Structure
To maintain an organized and accessible history of operations, documentation must be filed in the appropriate directories within the `communications` repository:

*   **Organizational Charter:** The root-level `docs/ONM-Organisational-Charter.md` is the supreme governing document.
*   **Official Policies:** Operational rules, standards, and community guidelines are stored in `docs/policies/` (e.g., Sponsorship Policy, Code of Conduct, this document).
*   **Roles & Responsibilities:** Volunteer and Executive portfolios are documented in the `docs/initiatives/in-progress/` directory. Each initiative or operational portfolio must include a `README.md` defining the objectives and accountable parties, alongside any relevant operational playbooks.
*   **Operational Task Tracking:** The repository's **Issue Queue** is utilized for tracking day-to-day operations, task delegation, and public discussion of pending actions.

## 3. Decision Making & Voting via Pull Requests
To ensure that all strategic decisions are public, auditable, and collaborative, ONM utilizes GitHub Pull Requests (PRs) as our formal voting mechanism.

### 3.1. The PR Voting Process
When a new policy, role definition, or charter amendment is proposed, it must be submitted as a Pull Request.

*   **Scope & Focus:** To maintain clear discussions and accurate voting, each Pull Request must focus on a single, distinct proposal or conceptual change. Mixing unrelated policy updates or amendments into a single PR is strongly discouraged.
*   **The Submitter's Role:** The EC member who opens the Pull Request is implicitly recorded as voting "Approve" (in favor) of their proposal. The submitter owns the proposal and is responsible for facilitating the discussion, addressing concerns, and committing updates based on peer feedback.
*   **Discussion:** Debate and refinement of the proposal take place in the PR comments.
*   **Voting:** The formal casting of a vote by other EC members is executed via GitHub's "Pull Request Review" feature.
    *   **Approve:** Represents a "Yes" vote.
    *   **Request Changes:** Represents an objection or a request for revision.
*   **Auditability:** Once a PR meets the required approval threshold (defined below), merging the PR acts as the official ratification of the decision. The Git history serves as the public decision log.

### 3.2. Approval Thresholds
Different types of updates require different levels of consensus, reflecting the flat authority model. While a 2/3 majority is the operational baseline, **the ultimate goal is always full consensus (3/3 approval) among the Executive Committee (EC)**.

1.  **Minor Edits (Typos, Formatting, Broken Links):**
    *   Do not require formal review. Can be merged directly by any Executive Committee member to maintain repository hygiene.
2.  **Operational & Policy Adjustments (Non-Charter):**
    *   **Baseline & Full Participation Requirement:** A 2/3 majority of the Executive Committee is required to pass a proposal. However, a Pull Request **cannot be merged until 100% of the EC (3/3 input) has registered a response**. Since the PR submitter is assumed to be in favor, they must secure an "Approve" from a second member, *and* wait for the third member to provide input (Approve, Abstain, Veto, or Timeout) before merging.
    *   **Handling Objections & Abstentions:** In the spirit of consensus, if an EC member disagrees with a proposal or is unavailable, the following mechanisms fulfill their required input:
        *   **Explicit Abstention:** The member explicitly states they are withholding approval but not blocking the vote, allowing the 2/3 majority to enact the decision.
        *   **Implicit Abstention (Timeout):** If an EC member does not respond to a formal PR review request within two weeks (14 days), their inaction is automatically treated as an abstention so that operational velocity is not blocked. This timeout fulfills their required input.
        *   **Request Changes:** The member formally objects via a "Request Changes" review. This pauses the PR, prompting the submitter and approvers to work collaboratively on modifications to address the stated concerns. **Once the requested modifications are pushed to the PR, the 14-day timeout clock restarts.** If the objecting member does not re-review within that new 14-day window, it is treated as an implicit abstention.
        *   **Veto & Escalate:** If modifications fail to resolve the issue and a stalemate is reached, the holdout member may exercise a "veto." This blocks the PR from being merged by the EC's 2/3 majority and escalates the matter to the **voting members** (the advisory group of active Fellows) for broader discussion and final resolution.
3.  **Strategic Consensus & Charter Amendments:**
    *   Requires a formal vote by the voting members as outlined in the Charter.
    *   *Execution:* The EC will finalize the exact wording via a PR. Once the EC aligns, the proposal is presented to the voting members (via email or General Meeting). Upon receiving a majority/quorum vote from the voting members, the PR is merged into the `main` branch, officially updating the Charter.

## 4. Interaction with Discord Communications
While Discord is ONM's primary platform for real-time collaboration and community building, it is highly ephemeral.

*   **Informal Consensus:** Preliminary decision-making often occurs in Discord chats. Explicit confirmations or the use of the thumbs-up emoji (`👍`) by Executive Committee members constitutes an informal agreement.
*   **Formalization:** For any decision that alters policies, roles, or the Charter, this informal Discord consensus **must** be translated into a formal GitHub PR. The Discord chat link should be referenced in the PR description to provide historical context.

## 5. Process for Implementing the 2026 AGM Charter Mandate
To smoothly transition to the new flat Executive Committee structure agreed upon at the last AGM, the current EC will follow this workflow:

1.  **Drafting:** The proposed text for the new *ONM Organisational Charter* will be submitted as a Pull Request to the `communications` repo.
2.  **EC Alignment:** The current EC members will use the PR review process to suggest edits, debate clauses, and ultimately approve the finalized text.
3.  **Voting Member Ratification:** Once the EC approves the PR, the draft will be circulated to the voting members for a formal vote.
4.  **Enactment:** Upon a successful vote by the voting members, the PR will be merged, and the new flat structure will immediately take effect.