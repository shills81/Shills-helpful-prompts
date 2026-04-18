# Write a Prompt for Image or Video Generation

**Use case:** Write high-quality generation prompts for Midjourney, DALL-E, Stable Diffusion, Veo, Sora, Runway, or similar tools.
**Works with:** Claude (any version)

---

Write a [MIDJOURNEY / DALL-E / STABLE DIFFUSION / VEO / SORA / RUNWAY] prompt for [DESCRIBE THE SUBJECT OR SCENE].

- Style: [AESTHETIC REFERENCE, e.g. cinematic, painterly, photorealistic, lo-fi]
- Lighting: [DESCRIBE]
- Composition: [DESCRIBE FRAMING, ANGLE, PERSPECTIVE]
- Mood: [DESCRIBE THE EMOTIONAL TONE]
- Negative prompts (if the tool supports them): [WHAT TO AVOID]

Output 3 variations: one literal, one interpretive, one experimental.

**Tool-specific notes:**
- Midjourney: responds well to style references (`--style`), aspect ratios (`--ar`), and quality flags (`--q`)
- Veo / Sora: needs explicit motion description — what moves, how, at what speed
- Runway: responds well to cinematography language (lens type, camera movement, depth of field)
- DALL-E: benefits from detailed scene descriptions over abstract style references
- Stable Diffusion: negative prompts matter more here than in other tools
