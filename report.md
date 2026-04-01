Report: Client Meeting Follow-up Email Generator

# 1. Business Use Case
The objective of this project is to automate the post-meeting follow up process for sales representatives or account managers.
*   **Target Users:** Sales personnel.
*   **Inputs:** Unstructured meeting notes, client names, and action items.
*   **Outputs:** Professionally formatted, friendly-toned follow-up emails.
*   **Value:**  Reduces the time spent manually drafting repetitive emails, ensures consistency in brand voice, and prevents key next steps from being overlooked.

## 2. Model Selection
I selected Gemini 2.5 Flash.
* **Rationale:** It boasts fast generation speeds and a strong capacity for understanding long contexts, making it ideally suited for business writing tasks that demand both rapid responses and logical clarity.

## 3. Prompt Iteration and Improvement Comparison (Baseline vs. Final Design)
Through two major iterations of the prompt, the system's performance saw significant improvement:
* **Initial Version (Baseline):** The AI-generated emails had a somewhat stiff tone; furthermore, in Case 4 and Case 5, the AI ​​failed to utilize structured lists, resulting in a mediocre reading experience.
* **Final Version (Final Design):**
* I enforced the use of bullet points, rendering the emails exceptionally easy to read. 
* I introduced an "anti-hallucination rule": Addressing the vague "security compliance framework" mentioned in Case 3, I strictly prohibited the AI ​​from making wild guesses. Instead, it was instructed to politely ask the client for clarification (for example, "Could you please confirm if we were discussing SOC2 or ISO?"). This significantly enhanced the tool's reliability in a business context.

## 4. System Limitations
Currently, this prototype may still require human review when processing extremely complex legal clauses or meeting notes involving multiple parties. Additionally, since it lacks access to external CRM systems, all contextual information must be manually input by the user; this could become a bottleneck when handling clients on a massive scale.

## 5. Deployment Recommendation
I recommend deploying this workflow as an "Internal Drafting Assistant."
**Conditions:** The AI ​​must be strictly prohibited from automatically sending emails directly. All generated content must undergo a final human review and refinement by a sales representative before being sent out. Provided this "human-AI collaboration" workflow is in place, the system can vastly improve team efficiency.
