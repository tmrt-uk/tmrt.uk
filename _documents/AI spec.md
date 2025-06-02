---
layout: document
title: "Document Format Guide"
subtitle: "Template and Guidelines for Creating Healthcare Technology Documentation"
date: 2025-06-01
author: "Darwinist Team"
tags: ["Documentation", "Template", "AI Guidelines", "Healthcare Technology"]
category: "Documentation Guidelines"
featured: false
toc: true
hide: true
excerpt: "Comprehensive guide for AI systems on how to format healthcare technology documents using Jekyll markdown, including YAML front matter, heading structure, content organization, and style conventions used in the Darwinist documentation collection."
---

# Document Format Guide

This guide explains how to structure and format healthcare technology documents for the Darwinist collection using Jekyll markdown.

---

## YAML Front Matter

Every document must begin with YAML front matter enclosed in triple dashes (`---`). This metadata controls how Jekyll processes and displays the document:

```yaml
---
layout: document
title: "Primary Document Title"
subtitle: "Explanatory subtitle"
date: 2025-06-01
author: "Darwinist Team"
tags: ["Tag1", "Tag2", "Tag3"]
category: "Category Name"
featured: true
toc: true
hidden: false
excerpt: "Brief summary..."
---
```

**YAML Field Guidelines:**
- **title:** Use title case, be specific and descriptive
- **subtitle:** Explain the document's purpose or scope
- **tags:** Include 3-7 relevant keywords (healthcare tech, product names, standards)
- **category:** Use consistent categories like "Healthcare Technology", "Medical AI Solutions", "Healthcare Infrastructure"
- **excerpt:** Write a compelling 1-2 sentence summary highlighting key benefits, metrics, or unique value

---

## Markdown Heading Structure

Use ATX-style headings with proper hierarchy:

- `#` Main Title (H1) – Use sparingly, mainly for document title
- `##` Major Section (H2) – Primary content divisions
- `###` Subsection (H3) – Secondary topics
- `####` Details (H4) – Specific points
- `#####` Minor Points (H5) – Rarely used
- `######` Smallest (H6) – Avoid if possible

**Heading Best Practices:**
- Start with H2 for main content sections (H1 reserved for document title)
- Maintain logical hierarchy (don't skip levels)
- Use descriptive, scannable headings
- Include keywords relevant to healthcare/technology context

---

## Content Formatting

**Emphasis and Strong Text**
- *Italics for emphasis*
- **Bold for strong importance**
- ***Bold and italic for critical points***

**Lists**
- Use unordered lists for features, benefits, and capabilities:
  - Primary point
  - Secondary point
    - Nested sub-point
    - Another sub-point
- Use ordered lists for processes, steps, and phases:
  1. First step
  2. Second step
  3. Third step

**Code and Technical Elements**
- Use `inline code` for technical terms, file names, and commands.
- Use code blocks for longer technical content, configurations, or examples.

**Links**
- [External link text](https://example.com)
- [This AI Spec Document]({% link _documents/AI spec.md %})

**Blockquotes**
- Use for important quotes, key statistics, or highlighted information:
  > This is a blockquote for emphasis.

---

## Document Structure Pattern

Most healthcare technology documents follow this structure:

- **Executive Summary or Overview:**  
  Brief introduction explaining what the technology/solution does and its primary value proposition.

- **Key Features/Capabilities:**  
  - List main functionalities as bullet points.
  - Use numbered lists for processes.
  - Use clear headings for comparisons.

- **Technical Specifications:**  
  - System requirements
  - Integration capabilities
  - Standards compliance
  - Architecture details

- **Use Cases/Applications:**  
  - Real-world scenarios where the solution provides value.
  - Organize by healthcare setting, clinical specialty, or workflow type.

- **Benefits/Outcomes:**  
  - List quantified results, metrics, and qualitative improvements.
  - Include clinical outcomes, operational efficiency, cost savings, and user satisfaction.

- **Implementation/Deployment:**  
  - Setup requirements
  - Integration process
  - Training needs
  - Support available

- **Compliance/Security:**  
  - Regulatory certifications
  - Data protection measures
  - Healthcare standards compliance
  - Audit capabilities

- **Conclusion:**  
  - Summary of key value propositions and call to action.

---

## Writing Style Guidelines

**Tone and Voice**
- Professional but accessible: Avoid overly technical jargon without explanation.
- Confident and authoritative: Present information as factual and well-researched.
- Solution-focused: Emphasize benefits and outcomes for healthcare organizations.
- UK healthcare context: Reference NHS, NICE, CQC, and UK regulations where relevant.

**Technical Writing Best Practices**
- Define acronyms on first use: "Electronic Health Record (EHR)"
- Use active voice when possible.
- Include specific metrics and quantified benefits.
- Provide context for technical capabilities (why they matter clinically).
- Use consistent terminology throughout.

**Healthcare-Specific Considerations**
- Reference relevant UK healthcare standards (HL7 FHIR, DICOM, etc.)
- Include regulatory compliance information (CE marking, MHRA approval, etc.)
- Mention integration with common NHS systems.
- Address clinical workflow implications.
- Consider different user types (clinicians, IT staff, administrators).

---

## Special Formatting Elements

**Callout Boxes (using blockquotes with formatting)**
> **Key Benefit:** This solution reduces diagnostic time by 70% while improving accuracy.

**Feature Lists with Icons**
- ✅ **FHIR Compliant:** Native support for healthcare interoperability standards
- ❌ **Legacy Compatible:** Works with existing PACS and HIS systems
- 🔒 **Secure:** End-to-end encryption and GDPR compliance

**Comparison Points**
- Instead of tables, use clear bullet points or headings to compare features, capabilities, or approaches.

---

## Common Document Categories

- "Healthcare Technology": General health IT solutions
- "Medical AI Solutions": AI-powered diagnostic and clinical tools
- "Healthcare Infrastructure": Core systems like PACS, imaging networks
- "Healthcare Standards": Documentation about FHIR, DICOM, HL7
- "Healthcare Policy": Analysis of regulations, procurement, strategy
- "Medical Imaging Solutions": Radiology and imaging-specific tools
- "Healthcare Education": Training and certification frameworks

---

## SEO and Discoverability

- Include relevant keywords naturally in headings and content.
- Use descriptive link text.
- Structure content for scanning (headings, lists, blockquotes).
- Include quantified benefits and outcomes.
- Reference popular healthcare technology terms and standards.

---

## File Naming Convention

Files should use descriptive names with spaces and proper capitalization, for example:
- `Product Name Technical Brief.md`
- `Healthcare Standard Implementation Guide.md`
- `Clinical AI Solution Overview.md`

---