# Prompt Playbook — VisionGenAI

Purpose: This document captures the prompt engineering patterns used in the VisionGenAI project. It includes reusable templates, few-shot examples, and practical guidance for grounded, production-safe LLM responses.

## General guidance
- Be explicit about the expected output format.
- Ask for structured JSON when outputs must be processed downstream.
- Require sources or retrieval references when using RAG.
- Prefer low temperature for deterministic outputs.
- Provide a clear system role to reduce ambiguity.

## Prompt template: structured incident summary
System:
> You are a concise visual analyst. Return JSON with keys: summary, people, actions, evidence. Do not include extra text.

User:
> Image: <image>
> Documents: <retrieved_documents>
> Question: "Summarize the incident shown in the image. Provide only valid JSON."

### Example output
```json
{
  "summary": "Two people are arguing near a loading dock while pointing toward equipment. No visible injuries were detected.",
  "people": [
    {"name": "person_1", "confidence": 0.92},
    {"name": "person_2", "confidence": 0.88}
  ],
  "actions": [
    {"action": "pointing", "confidence": 0.91}
  ],
  "evidence": [
    {"source": "docA.pdf#page2", "excerpt": "Witness statement: 'Person pointing at the pallet.'"}
  ]
}
```

## Prompt template: RAG-based question answering
System:
> You are an evidence-first assistant. Use only the retrieved context. If the answer is uncertain, say so and cite the limited evidence.

User:
> Based on the image and the supported documents, who is responsible for the equipment at the scene? Answer in 2-3 sentences and include a source list.

## Prompt template: image captioning for business workflows
System:
> Describe the image in concise business terms. Focus on objects, people, actions, and any unusual events. Return the output as plain text in 2-3 sentences.

User:
> Analyze the image and summarize key operational information.

## Prompt tuning recommendations
- Temperature: 0.0–0.2 for structured outputs and factual responses
- Max tokens: tune based on use case, typically 256–512 for JSON responses
- Top-p: around 0.95 for general summarization
- Use system prompts to enforce format and evidence requirements

## Few-shot prompting strategy
Use 2-3 high-quality examples when the task is not obvious:
- Example 1: summarization of a warehouse scene
- Example 2: extracting entities and actions from an image
- Example 3: answering a grounded question using retrieved documents

## Testing prompts
- Validate schema compliance using automated JSON checks
- Test ambiguous images and low-confidence retrieval cases
- Check for hallucinations by requiring sentence-level evidence references

## Production guidance
- Keep prompts modular and version-controlled
- Separate context retrieval instructions from task instructions
- Log prompt versions and model versions for reproducibility
- Evaluate prompts with human reviewers and retrieval metrics
