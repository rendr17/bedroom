# Motion Specification

## Philosophy
Motion should feel like game/UI feedback, not a modern marketing landing page.

## Durations
- micro state: 80–140 ms
- menu/window: 140–220 ms
- scene reveal: 250–450 ms
- intro: keep total short; content must not wait on long animation

## Allowed
- hotspot glow/pulse once
- window opacity + slight scale
- quest check animation
- CRT power-on line for optional intro
- subtle ambient light layer movement
- cursor/tooltip feedback

## Avoid
- scroll-jacking
- excessive parallax
- constant CRT distortion
- bounce/spring everywhere
- multi-second unskippable intro

## Reduced motion
When `prefers-reduced-motion: reduce`:
- remove CRT power animation
- remove camera pans/parallax
- reduce transitions to near-instant opacity changes
- preserve state feedback
