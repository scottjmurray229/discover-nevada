import type { PackingItem, PackingConfig, GearRecommendation } from './packing-base';

export const NEVADA_ESSENTIALS: PackingItem[] = [
  { id: 'nv-water', name: 'Large Insulated Water Bottle (32oz+)', category: 'destination', description: 'Nevada desert heat regularly hits 110°F June–August. Death Valley holds the world heat record. Dehydration is a genuine emergency risk. 3L minimum on any outdoor activity; 5L for desert hikes.', essential: true, amazonSearchFallback: 'insulated+water+bottle+32oz+64oz+hydration', affiliatePrice: '$20–40' },
  { id: 'nv-sunprotect', name: 'Full Sun Protection (SPF 50 + hat + UPF shirt)', category: 'destination', description: 'Desert UV is extreme — reflected off sand and rock from all angles. Hat, UPF long-sleeved shirt, SPF 50+ sunscreen, and sunglasses are the minimum kit for outdoor Nevada.', essential: true, amazonSearchFallback: 'upf+50+sun+protection+shirt+desert', affiliatePrice: '$30–50' },
  { id: 'nv-layers', name: 'Cold Desert Nights', category: 'destination', description: 'Nevada desert loses heat fast after sunset — a 100°F day becomes a 50°F night. One fleece or light down jacket handles the temperature swing that surprises every visitor.', essential: true, amazonSearchFallback: 'packable+down+jacket+lightweight+travel', affiliatePrice: '$60–100' },
  { id: 'nv-hikeboots', name: 'Hiking Boots / Trail Runners', category: 'destination', description: 'Valley of Fire, Red Rock Canyon, and Great Basin National Park trails are rocky, uneven, and harsh on footwear. Trail runners cover recreational hiking; ankle boots for anything serious.', essential: false, amazonSearchFallback: 'trail+running+shoes+hiking+desert', affiliatePrice: '$80–150' },
];

export const NEVADA_GEAR_RECOMMENDATIONS: GearRecommendation[] = [
  { id: 'gr-nv-water', name: 'Large Insulated Water Bottle (64oz)', reason: 'Nevada desert kills people who underestimate hydration. A 64oz insulated bottle keeps water cool for hours and holds a meaningful supply for treks at Valley of Fire or Red Rock Canyon.', amazonSearchFallback: 'insulated+water+bottle+64oz+hydration+flask', affiliatePrice: '~$35' },
  { id: 'gr-nv-hat', name: 'Wide-Brim Sun Hat (UPF 50)', reason: 'Desert UV hits from above and reflects from below. A wide brim covers your neck and face simultaneously. The single most visible difference between tourists who suffer and those who thrive.', amazonSearchFallback: 'wide+brim+sun+hat+upf+50+outdoor', affiliatePrice: '~$35' },
  { id: 'gr-nv-shirt', name: 'UPF 50 Long-Sleeve Sun Shirt', reason: 'Counterintuitively, covering up in the desert is cooler than bare skin — the fabric wicks sweat and blocks UV simultaneously. The right shirt keeps you cooler than sunscreen alone.', amazonSearchFallback: 'upf+50+long+sleeve+sun+shirt+desert', affiliatePrice: '~$40' },
  { id: 'gr-nv-jacket', name: 'Packable Down Jacket', reason: 'The desert temperature swing is dramatic — 105°F afternoons to 50°F nights. A packable down jacket compresses to nothing in your daypack and comes out when the sun drops.', amazonSearchFallback: 'packable+down+jacket+lightweight+compact', affiliatePrice: '~$70' },
  { id: 'gr-nv-sunglasses', name: 'Polarized Sunglasses (UV400)', reason: 'Desert glare from sand and rock is relentless. Polarized lenses reduce glare dramatically — you\'ll see the trail clearly instead of squinting through reflected UV all day.', amazonSearchFallback: 'polarized+sunglasses+uv400+desert', affiliatePrice: '~$25' },
];

export const NEVADA_CONFIG: PackingConfig = {
  sitePrefix: 'dnv',
  destination: 'Nevada',
  climate: ['desert'],
  currency: 'USD',
  plugType: 'Type A/B',
  plugVoltage: '120V',
  affiliateTag: 'discovermore-20',
  destinationEssentials: NEVADA_ESSENTIALS,
  gearRecommendations: NEVADA_GEAR_RECOMMENDATIONS,
};

export const SITE_CONFIG = NEVADA_CONFIG;

export const NEVADA_PACKING_FAQS = [
  { question: 'What should I pack for Nevada?', answer: 'The desert essentials: a large insulated water bottle (3L minimum for outdoor activities), full sun protection (SPF 50 + UPF shirt + wide-brim hat), and a packable down jacket for the dramatic temperature drop after sunset. For Las Vegas: comfortable walking shoes — the Strip is longer than it looks.' },
  { question: 'How hot does Nevada get?', answer: 'Las Vegas averages 104°F in July; Death Valley holds the world record at 134°F. June through September is brutal outdoors. Plan outdoor activities for early morning before 10am, stay indoors 11am–4pm, and resume at sunset. Spring and fall are the ideal seasons for outdoor Nevada.' },
  { question: 'What power adapter do I need for Nevada?', answer: 'No adapter needed — Nevada uses standard US Type A/B plugs at 120V/60Hz. Everything works as-is.' },
  { question: 'How much water do I need for Nevada hikes?', answer: 'Rangers recommend 1 liter per hour of desert hiking in summer heat. Valley of Fire\'s Wave Cave trail: 2L minimum. Anything in Death Valley in summer: carry at least 4L and don\'t go in the heat of the day. In Las Vegas: the Strip is 2+ miles of walking — even inside casinos it\'s warm. Carry a refillable bottle everywhere.' },
  { question: 'What should I pack for Las Vegas specifically?', answer: 'Comfortable walking shoes (the Strip is deceptively long and full of casino floors), one dressy outfit for shows/clubs, layers for aggressive casino AC, UV protection for the pool, and cash for tips. Las Vegas is walkable if you wear the right shoes — most visitors are surprised how much ground they cover.' },
  { question: 'What should I NOT bring to Nevada?', answer: 'Skip heavy cotton clothing (stays wet with sweat in desert heat), flip-flops for outdoor hiking (wrong shoes for desert terrain), and excessive luggage for Las Vegas (most hotels have excellent amenities). Don\'t bring full water bottles from home — refill everywhere. Do NOT underestimate water needs on any desert trail.' },
];
