// Shared destination coordinates — single source of truth
// Used by plan page + companion app + generate-itinerary API.

export const DESTINATION_COORDS: Record<string, { lat: number; lng: number; label: string }> = {
  'las-vegas': { lat: 36.1699, lng: -115.1398, label: 'Las Vegas' },
  reno: { lat: 39.5296, lng: -119.8138, label: 'Reno' },
  'lake-tahoe': { lat: 39.0968, lng: -120.0324, label: 'Lake Tahoe' },
  'valley-of-fire': { lat: 36.4412, lng: -114.5131, label: 'Valley of Fire' },
  'red-rock-canyon': { lat: 36.1355, lng: -115.4289, label: 'Red Rock Canyon' },
  'great-basin': { lat: 38.9833, lng: -114.3000, label: 'Great Basin' },
  'virginia-city': { lat: 39.3096, lng: -119.6497, label: 'Virginia City' },
  henderson: { lat: 36.0395, lng: -114.9817, label: 'Henderson' },
  'boulder-city': { lat: 35.9789, lng: -114.8322, label: 'Boulder City' },
  'carson-city': { lat: 39.1638, lng: -119.7674, label: 'Carson City' },
};
