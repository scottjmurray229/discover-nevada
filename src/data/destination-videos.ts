/**
 * Shared video map for destination cards.
 * Maps destination slugs to video file paths (preview preferred, hero as fallback).
 * Used by: src/pages/index.astro, src/pages/destinations/index.astro
 */
export const destinationVideoMap: Record<string, string> = {
  // No destination preview videos yet — add as they become available
} as const;
