---
name: generate-lighting-plot
description: "Use to orchestrate the generation of a complete HTML interactive lighting plot visualizer by coordinating a lighting designer and lighting technician. Ideal for converting cue lists into visual CSS dashboards."
---

# Generate Lighting Plot Workflow

## When to Use
- When compiling a new lighting design visualizer from scratch based on a project brief.
- When transforming a simple text cue list into an interactive HTML stage plot.

## Procedure
1. Review the workspace instructions or prompt user for the specific project constraints (available lights, available colors, stage layout, and piece length).
2. Invoke the `lighting-designer` subagent using the `agent` tool. Send it the cue list and ask it to generate the artistic lighting descriptions.
3. Invoke the `lighting-tech` subagent using the `agent` tool. Feed it the artistic output from the designer, and ask it to generate the technical lighting specification sheet.
4. Absorb the outputs from both agents and step into the role of an Expert Frontend Developer.
5. Generate an HTML file (e.g., `lighting-plot.html`) that visualizes these states using square "stage" `div` elements, CSS gradients, and animations to mimic the requested lighting effects.
6. Build interactive toggle tabs or hover states within the HTML to display the Designer's artistic notes and the Technician's practical specs alongside the visualizer for each cue.
