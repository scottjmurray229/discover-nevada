#!/usr/bin/env python3
"""Nevada Tier 3 quality pass — adds affiliatePicks, scottTips, immersive-break-inline, AEO ledes"""
import os, re

BASE = "C:/Users/scott/Documents/discover-nevada/src/content/destinations"

BOOKING = "https://www.booking.com/region/us/nevada.html?aid=2778866"
GYG = "https://www.getyourguide.com/?partner_id=IVN6IQ3"
AMAZON = "https://www.amazon.com/s?k=nevada+travel&tag=discovermore-20"

DESTINATIONS = {
    "las-vegas": {
        "aeo": "Las Vegas is the most visited city in the United States — a 24-hour entertainment machine built in the Mojave Desert, with the most concentrated collection of hotel rooms, fine dining restaurants, live entertainment, and casino gaming in the world. Beyond the Strip's spectacle, it's also a 30-minute drive from Red Rock Canyon and Valley of Fire, some of Nevada's most dramatic outdoor landscapes.",
        "gradient": "linear-gradient(135deg, #7c3aed, #be185d, #f59e0b)",
        "video_title": "Las Vegas: The Strip Never Sleeps",
        "video_text": "Neon, casinos, and the desert just beyond.",
        "affiliatePicks": [
            {"name": "The Venetian Las Vegas", "type": "hotel", "url": "https://www.booking.com/hotel/us/venetian-resort-las-vegas.html?aid=2778866", "description": "The Strip's most iconic resort — enormous rooms (all suites), gondola rides, and central location.", "priceRange": "$$$"},
            {"name": "Las Vegas Strip Walking Tour", "type": "tour", "url": f"{GYG}&q=Las+Vegas+Strip+tour", "description": "Guided Strip walking tour covering casino history, architecture, and insider tips.", "priceRange": "$"},
            {"name": "Red Rock Canyon and Valley of Fire Day Tour", "type": "tour", "url": f"{GYG}&q=Red+Rock+Canyon+Valley+of+Fire+tour", "description": "Full-day guided tour covering both Red Rock Canyon and Valley of Fire from Las Vegas.", "priceRange": "$$"},
        ],
        "scottTips": {
            "logistics": "Las Vegas is the entry point for road trips to Zion (2.5 hrs), Bryce Canyon (4 hrs), and the Grand Canyon South Rim (4 hrs). Harry Reid International Airport has direct flights from virtually every major US city and many international hubs. The Strip has a free tram system connecting some resorts.",
            "bestTime": "March–April and October–November. Spring and fall temperatures are in the 70s–80s°F — comfortable for walking the Strip and outdoor day trips. Summer (June–September) regularly hits 110°F+ — outdoor activities are extremely limited.",
            "gettingAround": "Car rental for day trips to Red Rock Canyon and Valley of Fire. Las Vegas Monorail connects mid-Strip resorts. Walking is viable for the central Strip (4 miles round trip from Mandalay Bay to the Stratosphere). Uber/Lyft are cheap and abundant.",
            "money": "The Strip casinos are designed to separate you from money at every opportunity. Budget for accommodation, meals, entertainment, and some gambling separately. A $50 entertainment budget can go fast; a $200 budget can provide a full evening. Off-Strip hotels are dramatically cheaper. Food courts in casinos offer surprisingly good value.",
            "safety": "Las Vegas is generally safe on the Strip and Fremont Street. Watch for pickpockets in crowds. Downtown off Fremont Street has higher crime rates — stay aware. Extreme heat in summer is a genuine safety risk — carry water and don't underestimate desert temperatures.",
            "packing": "Comfortable walking shoes for the long Strip distances. Layers — casinos are heavily air-conditioned year-round (cold) while outdoors is hot. Sun protection for any outdoor time.",
            "localCulture": "Las Vegas runs on tips — dealers, servers, valets, housekeeping. Budget accordingly. The 24-hour culture means some restaurants and bars never close. Buffets are largely extinct now (pandemic casualties) — the food scene has upgraded to celebrity chef restaurants and good casual spots."
        },
    },
    "valley-of-fire": {
        "aeo": "Valley of Fire State Park is Nevada's most spectacular natural landscape — 40,000 acres of ancient red and orange Aztec sandstone formations east of Las Vegas, with elephant rocks, arch formations, and some of the best-preserved petroglyphs in the Southwest. It's only 55 miles from the Strip and wildly undervisited by comparison to its neighbors.",
        "gradient": "linear-gradient(135deg, #dc2626, #ea580c, #f59e0b)",
        "video_title": "Valley of Fire: Nevada's Red Secret",
        "video_text": "50 miles from Vegas. Feels like another planet.",
        "affiliatePicks": [
            {"name": "Las Vegas Hotels — Valley of Fire Day Trip Base", "type": "hotel", "url": f"{BOOKING}&ss=Las+Vegas+NV", "description": "Las Vegas is the logical base for Valley of Fire — only 55 miles away.", "priceRange": "$$"},
            {"name": "Valley of Fire Guided Photography Tour", "type": "tour", "url": f"{GYG}&q=Valley+of+Fire+tour", "description": "Small-group guided tour of Valley of Fire's best formations and petroglyph sites.", "priceRange": "$$"},
            {"name": "Red Rock Canyon and Valley of Fire Combo", "type": "tour", "url": f"{GYG}&q=Red+Rock+Canyon+Valley+of+Fire+day+trip", "description": "Full day covering both Nevada parks from Las Vegas.", "priceRange": "$$"},
        ],
        "scottTips": {
            "logistics": "Valley of Fire is 55 miles northeast of Las Vegas via I-15 and NV-169. $15/vehicle Nevada resident, $20 non-resident. No gas stations in the park — fill up before entering. The visitor center has water and maps.",
            "bestTime": "October–April. Summer temperatures reach 120°F — dangerous for hiking and not recommended. Winter is mild (60–70°F) and often has the park to yourself. Spring wildflowers (February–April) add color to the red rock.",
            "gettingAround": "Drive the main park road (15 miles) and stop at all marked pullouts. White Domes Road takes you to the best petroglyphs and arch formations. A standard sedan handles all paved park roads. Dirt side roads require 4WD.",
            "money": "$20 non-resident vehicle entry. No shuttle — you need a car. Easily combined with a Lake Mead visit for a full day trip from Las Vegas.",
            "safety": "Summer heat is lethal — serious. The park's red and orange rock absorbs and radiates heat aggressively. Even in spring, start hikes by 7am and be off exposed trails by 10am on warm days. Carry 2 liters minimum per person.",
            "packing": "More water than you think you need. Sun hat and sunscreen. Camera — the red formations in low morning/evening light are extraordinary. Closed-toe shoes for rocky terrain.",
            "localCulture": "Valley of Fire has a long Ancestral Puebloans and Anasazi history — the petroglyphs at Atlatl Rock and Mouse's Tank are genuine cultural heritage sites, not just scenic photos. Read the visitor center exhibits for context."
        },
    },
    "red-rock-canyon": {
        "aeo": "Red Rock Canyon National Conservation Area is a world-class rock climbing and hiking destination 17 miles west of Las Vegas — a 13-mile scenic loop through dramatic red and white Calico Hills sandstone formations, with over 2,000 climbing routes and hiking trails that bear no resemblance to anything on the Strip. It's the best reason to rent a car in Las Vegas even if you're not an outdoor person.",
        "gradient": "linear-gradient(135deg, #dc2626, #ea580c, #78716c)",
        "video_title": "Red Rock Canyon: Vegas's Backyard Wilderness",
        "video_text": "World-class climbing 17 miles from the Strip.",
        "affiliatePicks": [
            {"name": "Red Rock Canyon Guided Rock Climbing", "type": "tour", "url": f"{GYG}&q=Red+Rock+Canyon+rock+climbing", "description": "Introductory rock climbing lesson with guide on Red Rock's beginner routes.", "priceRange": "$$"},
            {"name": "Red Rock Canyon Hiking Tour", "type": "tour", "url": f"{GYG}&q=Red+Rock+Canyon+hiking+tour", "description": "Guided half-day hike through the Calico Hills and canyon narrows.", "priceRange": "$"},
            {"name": "Black Diamond Climbing Shoes", "type": "activity", "url": f"{AMAZON}&k=rock+climbing+shoes+beginner", "description": "Entry-level climbing shoes for Red Rock's sandstone routes.", "priceRange": "$$"},
        ],
        "scottTips": {
            "logistics": "Red Rock Canyon is 17 miles west of Las Vegas via Charleston Boulevard (SR-159). $15/vehicle timed entry required — reserve on Recreation.gov in advance during peak season (Sept–May). Entry available 6am–8pm (gates close at sunset).",
            "bestTime": "September–May. Summer heat (100°F+) makes hiking dangerous. October–April is ideal — comfortable temperatures for hiking and prime climbing season. Spring (March–April) has wildflowers.",
            "gettingAround": "The 13-mile one-way scenic loop drive is the main access — drive it clockwise, stopping at marked pullouts and trailheads. No loop exit until you complete the circuit. Many trailheads accessible from side roads before the loop entrance.",
            "money": "$15/vehicle timed entry. One of the best outdoor values near any major US city — equivalent experiences in Sedona or Moab require much longer drives.",
            "safety": "Stay on marked trails — the desert shrub can obscure cliffs. Rattlesnakes are present March–October — watch where you step and sit. Flash floods are possible in canyon areas after rain.",
            "packing": "Hiking boots or trail runners for sandstone. 2+ liters water per person. Sun protection. Binoculars for spotting climbers on the walls.",
            "localCulture": "Red Rock Canyon has a serious climbing culture that is distinct from the Vegas scene. The Spring Mountain Ranch State Park (adjacent, free) preserves a historic ranch and offers flat easy walks. The Desert Willow gift shop at the visitor center has good local guides and maps."
        },
    },
    "lake-tahoe": {
        "aeo": "Lake Tahoe is North America's largest alpine lake — a 22-mile-long, 12-mile-wide jewel of crystal-clear blue water sitting at 6,225 feet on the Nevada-California border. It's surrounded by ski resorts in winter (Heavenly, Northstar, Palisades Tahoe), hiking and mountain biking trails in summer, and has a calm, uncrowded South Lake Tahoe casino strip for those who want Nevada gaming with a mountain lake backdrop.",
        "gradient": "linear-gradient(135deg, #0369a1, #0ea5e9, #166534)",
        "video_title": "Lake Tahoe: Alpine Perfection",
        "video_text": "Crystal-clear water, ski resorts, and year-round mountain life.",
        "affiliatePicks": [
            {"name": "Edgewood Tahoe Resort", "type": "hotel", "url": "https://www.booking.com/hotel/us/edgewood-tahoe.html?aid=2778866", "description": "The premier South Shore resort — lakefront, golf, spa, and exceptional service.", "priceRange": "$$$$"},
            {"name": "Heavenly Mountain Ski Resort Lift Tickets", "type": "activity", "url": f"{GYG}&q=Heavenly+Ski+Resort+Tahoe", "description": "Book ski passes for Heavenly — the largest Tahoe resort with Nevada and California terrain.", "priceRange": "$$$"},
            {"name": "Lake Tahoe Sunset Kayak Tour", "type": "tour", "url": f"{GYG}&q=Lake+Tahoe+kayak+tour", "description": "Guided kayak tour on the crystal-clear lake with Emerald Bay views.", "priceRange": "$$"},
        ],
        "scottTips": {
            "logistics": "Lake Tahoe straddles Nevada and California — the Nevada side has South Lake Tahoe casinos and Incline Village. Reno is 1 hour north (nearest major airport). Sacramento is 2 hours west. San Francisco is 3.5 hours. I-80 through Donner Pass is the main route from the Bay Area.",
            "bestTime": "December–March for skiing. June–September for lake recreation (swimming, kayaking, hiking, mountain biking). July–August is peak season with significant crowds. Spring and fall offer fewer crowds and excellent hiking.",
            "gettingAround": "Car essential — Lake Tahoe is 72 miles of shoreline. The Tahoe Area Regional Transit (TART) bus runs along the lake in summer but is limited. South Lake Tahoe has a casino shuttle. Drive the full lake loop (72 miles) for the complete perspective.",
            "money": "Lake Tahoe is expensive in peak seasons. Ski resort lodging runs $300–600+/night at slope-side options. Summer cabin rentals are competitive with hotels. South Lake Tahoe casino hotels offer better value than resort lodging.",
            "safety": "Altitude sickness possible at 6,225 feet — some visitors feel it. I-80 through Donner Pass closes occasionally in major storms. Chain controls required frequently in winter — rent a car with AWD or carry chains.",
            "packing": "Full ski or snowboard gear in winter. Layers for the dramatic temperature swings (hot days, cold nights). Sun protection — UV is intense at altitude over reflective water. Waterproof jacket for lake activities.",
            "localCulture": "Lake Tahoe has a strong summer camp and cabin rental culture — families return for generations. The Nevada side (Crystal Bay, Incline Village) is quieter and more residential than the California South Shore casino strip. Cal-Neva Resort on the state line has a legendary history (Frank Sinatra ownership)."
        },
    },
    "reno": {
        "aeo": "Reno is Nevada's second city — a mid-size gambling and entertainment city 4 hours from San Francisco and 30 minutes from Lake Tahoe, reinventing itself as an outdoor adventure hub and tech industry satellite. The Reno-Tahoe International Airport is an excellent gateway for the northern Nevada and Lake Tahoe region, and the Truckee River runs right through downtown.",
        "gradient": "linear-gradient(135deg, #1e40af, #7c3aed, #dc2626)",
        "video_title": "Reno: The Biggest Little City",
        "video_text": "Lake Tahoe 30 minutes west. The desert 30 minutes east. Reno in between.",
        "affiliatePicks": [
            {"name": "Whitney Peak Hotel Reno", "type": "hotel", "url": "https://www.booking.com/hotel/us/whitney-peak-reno.html?aid=2778866", "description": "Non-gaming boutique hotel in downtown Reno with an outdoor climbing wall on the exterior.", "priceRange": "$$"},
            {"name": "Reno River Walk and Craft Brewery Tour", "type": "tour", "url": f"{GYG}&q=Reno+Nevada+tour", "description": "Guided walking tour of Reno's arts district, river walk, and craft brewery scene.", "priceRange": "$"},
            {"name": "Virginia City Historic Tour from Reno", "type": "tour", "url": f"{GYG}&q=Virginia+City+Nevada+tour", "description": "Day trip from Reno to the preserved silver mining boomtown of Virginia City.", "priceRange": "$"},
        ],
        "scottTips": {
            "logistics": "Reno-Tahoe International Airport (RNO) has direct flights from 30+ cities — excellent gateway for both Lake Tahoe and northern Nevada. Downtown is compact and walkable. I-80 west takes you to Truckee and Lake Tahoe in 30 minutes.",
            "bestTime": "June–October for Reno itself and lake access. December–March if skiing at Lake Tahoe is the primary goal. The Burning Man festival (late August/early September) transforms the region — Black Rock City is 100 miles north.",
            "gettingAround": "Car essential for Lake Tahoe and regional exploration. Downtown Reno is walkable. The Sierra Nevada ski resorts (Mt. Rose, Heavenly) are accessible by car.",
            "money": "Reno casino hotels are dramatically cheaper than Las Vegas Strip equivalents. Mid-range options run $80–150/night. Food and entertainment are similarly affordable. Good value city for Nevada gambling with outdoor access.",
            "safety": "Downtown Reno has active casino areas that are safe, and a homeless population concentrated near the river — standard urban awareness applies. The Truckee River corridor and arts district are safe and active.",
            "packing": "Layers for the altitude and temperature swings. Outdoor gear if Tahoe hiking or skiing is on the agenda.",
            "localCulture": "Reno has reinvented itself with a strong arts community (the Nevada Museum of Art is genuinely excellent), a craft beer scene, and Tesla's Gigafactory and other tech companies moving in. It's a more complex city than its gambling-town reputation suggests. The Reno Arch ('The Biggest Little City in the World') is a fun photo op."
        },
    },
    "great-basin": {
        "aeo": "Great Basin National Park in eastern Nevada is one of the most remote and least-visited national parks in the contiguous United States — a dramatic landscape of ancient bristlecone pines, a marble cave system, glacier-carved peaks topping 13,000 feet, and some of the darkest skies in America. It's 5 hours from Las Vegas and 4 hours from Salt Lake City.",
        "gradient": "linear-gradient(135deg, #1e40af, #166534, #1c1917)",
        "video_title": "Great Basin: America's Forgotten Park",
        "video_text": "The darkest skies in the lower 48. Ancient trees. Marble caves.",
        "affiliatePicks": [
            {"name": "Border Inn Baker NV", "type": "hotel", "url": f"{BOOKING}&ss=Baker+NV", "description": "The only lodging near the park in Baker — modest but the right base for stargazing.", "priceRange": "$"},
            {"name": "Great Basin Lehman Caves Tour", "type": "tour", "url": f"{GYG}&q=Lehman+Caves+Great+Basin", "description": "Book ranger-led cave tours at Lehman Caves in advance — spots sell out.", "priceRange": "$"},
            {"name": "Celestron StarSense Explorer Telescope", "type": "activity", "url": f"{AMAZON}&k=portable+telescope+stargazing", "description": "Portable telescope for Great Basin's extraordinary dark skies — Gold Tier IDA Dark Sky Park.", "priceRange": "$$"},
        ],
        "scottTips": {
            "logistics": "Great Basin is on US-50 (the Loneliest Road in America) in eastern Nevada. Baker, NV (the gateway town) has minimal services — fill gas in Ely (68 miles west) or Delta, UT (100 miles east). Lehman Caves tours are the primary structured activity — book on Recreation.gov.",
            "bestTime": "June–October for summit hiking and cave tours. Wheeler Peak (13,063 ft) is accessible July–September. Winter closes high elevation roads. Spring has good wildflowers at lower elevations.",
            "gettingAround": "Car essential — no public transportation exists within 200 miles. The Wheeler Peak Scenic Drive (12 miles) accesses the high country. Lehman Caves visitor center is at 6,825 feet.",
            "money": "Free park entry (no entrance fee). Lehman Caves tours are $12–18/adult depending on tour length. The cheapest major national park experience in the US. Baker has one restaurant and one motel.",
            "safety": "Remote location — inform someone of your itinerary before backcountry travel. Wheeler Peak summit (13,063 ft) requires altitude awareness. Lightning risk above treeline July–August.",
            "packing": "Food and water for multiple days — services are extremely limited. Stargazing equipment (the park is a Gold-Tier International Dark Sky Park). Warm layers — temperatures drop significantly at elevation even in summer.",
            "localCulture": "The ancient bristlecone pines on Wheeler Peak's glacial cirque are among the oldest living organisms on Earth — some over 4,000 years old. This is one of the genuinely extraordinary natural phenomena in the American West, rarely visited. The solitude here is profound."
        },
    },
    "carson-city": {
        "aeo": "Carson City is Nevada's capital — a small, historic city of 55,000 in the Carson Valley at the foot of the Sierra Nevada, 30 miles from Lake Tahoe and 30 miles from Reno. It's the gateway to Lake Tahoe's East Shore, has a well-preserved Victorian downtown, and offers a quieter base than Reno for exploring the northern Nevada region.",
        "gradient": "linear-gradient(135deg, #166534, #1e40af, #78716c)",
        "video_title": "Carson City: Nevada's Quiet Capital",
        "video_text": "Sierra Nevada foothills, Lake Tahoe nearby, and a state capital that surprises.",
        "affiliatePicks": [
            {"name": "Carson City Hotels", "type": "hotel", "url": f"{BOOKING}&ss=Carson+City+NV", "description": "Several mid-range hotels in downtown Carson City. Good value base for Tahoe/Reno trips.", "priceRange": "$$"},
            {"name": "Nevada State Museum Carson City", "type": "activity", "url": f"{GYG}&q=Carson+City+Nevada+tour", "description": "The state museum in the historic US Mint building — Nevada's best history museum.", "priceRange": "$"},
            {"name": "Lake Tahoe East Shore Drive", "type": "activity", "url": f"{GYG}&q=Lake+Tahoe+East+Shore", "description": "Scenic drive from Carson City to Sand Harbor and Crystal Bay on Tahoe's Nevada shore.", "priceRange": "$"},
        ],
        "scottTips": {
            "logistics": "Carson City is equidistant from Lake Tahoe (30 miles via US-50) and Reno (30 miles via US-395). Reno-Tahoe Airport is the nearest major airport. Small enough to drive through comfortably; has all services.",
            "bestTime": "Year-round. Summer for Lake Tahoe access and hiking in the Sierra. Winter for Tahoe skiing from a less expensive base than South Lake Tahoe.",
            "gettingAround": "Car essential. The Lake Tahoe East Shore (Nevada side) is accessible via SR-28 from Carson City — Incline Village, Sand Harbor, and Crystal Bay are all along this route.",
            "money": "Carson City lodging is significantly cheaper than South Lake Tahoe or Reno casino hotels. Good budget base for the region.",
            "safety": "Standard mid-size city safety. Highway 50 west to Lake Tahoe has steep grades and sharp curves — drive carefully, especially in winter.",
            "packing": "Layers for Sierra foothills temperature swings. Camera for the Capitol building and historic downtown.",
            "localCulture": "The Nevada State Museum is in the restored US Mint building — Carson City was the site of the Carson City Mint from 1870 to 1893. The museum has the original coin press and Nevada silver and gold specimens. Worth two hours."
        },
    },
    "henderson": {
        "aeo": "Henderson is Las Vegas's largest suburb — a planned city of 320,000 that's developed its own identity separate from the Strip, with the Clark County Wetlands Park (the most-visited county park in Nevada), Lake Las Vegas resort community, and a growing dining and arts scene. It's also the base for Hoover Dam day trips and Valley of Fire.",
        "gradient": "linear-gradient(135deg, #0369a1, #166534, #dc2626)",
        "video_title": "Henderson: Beyond the Strip",
        "video_text": "The other side of Las Vegas Valley — wetlands, lakes, and real neighborhoods.",
        "affiliatePicks": [
            {"name": "Lake Las Vegas Resort Hotels", "type": "hotel", "url": f"{BOOKING}&ss=Henderson+NV", "description": "Lake Las Vegas has luxury resort options on a private lake — quieter than the Strip.", "priceRange": "$$$"},
            {"name": "Hoover Dam Guided Tour from Henderson", "type": "tour", "url": f"{GYG}&q=Hoover+Dam+tour+Las+Vegas", "description": "Guided Hoover Dam and Lake Mead tour — accessible from Henderson in 30 minutes.", "priceRange": "$$"},
            {"name": "Clark County Wetlands Park Birding Walk", "type": "activity", "url": f"{GYG}&q=Henderson+Nevada+nature", "description": "Guided birding walk through the Clark County Wetlands — over 100 species recorded.", "priceRange": "$"},
        ],
        "scottTips": {
            "logistics": "Henderson is southeast of Las Vegas, 15-20 minutes from the Strip via I-215. Hoover Dam and Lake Mead are 30 minutes east via US-93/95. Boulder City (where Hoover Dam is) is a 25-minute drive.",
            "bestTime": "October–April. Summer heat (110°F+) is severe — the Wetlands Park and Lake Mead activities are dangerous at midday in July–August. The wetlands are excellent for birdwatching year-round but especially during spring and fall migration.",
            "gettingAround": "Car essential. Henderson has limited public transit. The I-215 beltway makes Strip access straightforward.",
            "money": "Henderson hotel rates run $80–180/night — significantly less than comparable Strip options. Good base for budget-conscious visitors who still want Vegas access.",
            "safety": "Henderson is one of Nevada's safest cities. Desert heat is the primary safety concern in summer.",
            "packing": "Sun protection and water for any outdoor activities. Binoculars for the Wetlands Park birding.",
            "localCulture": "Henderson has its own dining and arts scene centered on Water Street and the Galleria area — not as developed as Las Vegas proper but improving. The Ethel M Chocolate Factory tour is a popular local attraction with a cactus garden."
        },
    },
    "boulder-city": {
        "aeo": "Boulder City is the company town that built Hoover Dam — the only city in Nevada without gambling (it was prohibited during construction to keep workers sober and productive). The historic downtown preserves the 1930s dam-era architecture, and Hoover Dam itself is 8 miles east — one of the most impressive engineering achievements of the 20th century.",
        "gradient": "linear-gradient(135deg, #78716c, #1e40af, #166534)",
        "video_title": "Boulder City: Gateway to Hoover Dam",
        "video_text": "The town that built the dam. No casinos allowed.",
        "affiliatePicks": [
            {"name": "Boulder City Hotels", "type": "hotel", "url": f"{BOOKING}&ss=Boulder+City+NV", "description": "Small hotel options in historic Boulder City — quiet and characterful base for Hoover Dam.", "priceRange": "$"},
            {"name": "Hoover Dam Interior Tour", "type": "tour", "url": f"{GYG}&q=Hoover+Dam+interior+tour", "description": "Book the Powerplant Tour or Hoover Dam Tour for access to the tunnels and generators.", "priceRange": "$$"},
            {"name": "Colorado River Kayaking Hoover Dam", "type": "tour", "url": f"{GYG}&q=Colorado+River+kayaking+Hoover+Dam", "description": "Kayak or raft below Hoover Dam through Black Canyon — stunning geology.", "priceRange": "$$"},
        ],
        "scottTips": {
            "logistics": "Boulder City is 26 miles southeast of Las Vegas via US-93. Hoover Dam is 8 miles further east. Allow 3-4 hours for the dam visit including the tour. Lake Mead National Recreation Area begins just east of the dam.",
            "bestTime": "October–April. Summer heat at the dam (100°F+) is intense. The Colorado River below the dam is cooler and shaded — kayaking is feasible earlier in the day even in summer.",
            "gettingAround": "Car required from Las Vegas. Parking is plentiful at the Boulder City trailheads and the dam visitor center.",
            "money": "$30 for the Hoover Dam Tour, $15 for Powerplant Tour. The walkway across the dam and the Mike O'Callaghan–Pat Tillman Memorial Bridge overlook are free. Colorado River kayaking runs $70–120/person.",
            "safety": "The dam visitor area is well-managed. The Colorado River kayak through Black Canyon requires a guide — the currents below the dam are managed and calm but disorienting for beginners.",
            "packing": "Sun protection for the exposed dam walk. Comfortable shoes for tours. Water — the desert heat at Hoover Dam is unrelenting.",
            "localCulture": "Boulder City has a genuine small-town character uncommon in the Las Vegas metro. The Boulder City/Hoover Dam Museum on Nevada Way is worth an hour for context. The downtown has antique shops, cafes, and a distinctly non-Vegas atmosphere."
        },
    },
    "virginia-city": {
        "aeo": "Virginia City is Nevada's best-preserved silver boomtown — a National Historic Landmark on the side of Mount Davidson with Victorian-era saloons, boardwalk storefronts, the Piper's Opera House, and operating mine tours. It's 25 miles southeast of Reno and preserves the look and atmosphere of the Comstock Lode era (1859–1898) better than any other Western mining town.",
        "gradient": "linear-gradient(135deg, #92400e, #78716c, #1e40af)",
        "video_title": "Virginia City: The Comstock Lives",
        "video_text": "Silver boom, Mark Twain, and the Old West. Mostly intact.",
        "affiliatePicks": [
            {"name": "Gold Hill Hotel Virginia City", "type": "hotel", "url": f"{BOOKING}&ss=Virginia+City+NV", "description": "Nevada's oldest operating hotel (1859) in nearby Gold Hill. Atmospheric and historic.", "priceRange": "$$"},
            {"name": "Virginia City Mine Tour", "type": "tour", "url": f"{GYG}&q=Virginia+City+Nevada+mine+tour", "description": "Underground mine tour through the original Comstock Lode shafts.", "priceRange": "$"},
            {"name": "Virginia City Historic District Walking Tour", "type": "tour", "url": f"{GYG}&q=Virginia+City+Nevada+walking+tour", "description": "Guided walking tour of C Street, the opera house, and Mark Twain historical sites.", "priceRange": "$"},
        ],
        "scottTips": {
            "logistics": "Virginia City is 25 miles southeast of Reno via US-395 south and SR-341. The mountain road (SR-341) has steep grades and tight switchbacks — take it slowly. The town itself is on a steep hillside; walking is on slopes.",
            "bestTime": "May–October. Winter brings snow and some attractions close. Summer weekends are the busiest but the weather is ideal. Shoulder season (May–June, September–October) has fewer crowds.",
            "gettingAround": "Drive up, park on C Street, and walk the main commercial district. C Street is the main drag — boardwalks, saloons, shops, and museum buildings.",
            "money": "Mine tours run $8–15. Most museums and historic buildings charge modest entry fees. Virginia City overall is an affordable day trip from Reno.",
            "safety": "The mountain road up SR-341 requires care — tight switchbacks and steep grades. Take your time driving. The mine tours are well-maintained and safe.",
            "packing": "Comfortable walking shoes for the hilly terrain. A jacket even in summer — Virginia City sits at 6,200 feet and cools quickly after sunset.",
            "localCulture": "Virginia City has genuine history rather than manufactured Western theme-park atmosphere. Mark Twain worked as a reporter at the Territorial Enterprise here before his fame (the building is preserved). The Four Mile Flats cemetery contains the graves of many original Comstock-era residents. The town's history of labor strikes, fires, and boom-bust cycles is told well in the local museums."
        },
    },
}


def process_file(filepath, slug, data):
    """Add affiliatePicks content, scottTips, immersive-break-inline, and AEO to existing files."""
    content = open(filepath, 'r', encoding='utf-8').read()

    # Replace empty affiliatePicks: [] with real picks
    affiliatePicks_yaml = "affiliatePicks:\n"
    for pick in data.get("affiliatePicks", []):
        affiliatePicks_yaml += f"""  - name: "{pick['name']}"
    type: {pick['type']}
    url: "{pick['url']}"
    description: "{pick['description']}"
    priceRange: "{pick['priceRange']}"
"""

    if "affiliatePicks: []" in content:
        content = content.replace("affiliatePicks: []", affiliatePicks_yaml.rstrip())

    # Add scottTips before contentStatus
    scottTips = data.get("scottTips", {})
    if "scottTips:" not in content:
        scottTips_yaml = f"""scottTips:
  logistics: "{scottTips.get('logistics', '').replace('"', "'")}"
  bestTime: "{scottTips.get('bestTime', '').replace('"', "'")}"
  gettingAround: "{scottTips.get('gettingAround', '').replace('"', "'")}"
  money: "{scottTips.get('money', '').replace('"', "'")}"
  safety: "{scottTips.get('safety', '').replace('"', "'")}"
  packing: "{scottTips.get('packing', '').replace('"', "'")}"
  localCulture: "{scottTips.get('localCulture', '').replace('"', "'")}"
"""
        content = content.replace('contentStatus: "published"', scottTips_yaml + 'contentStatus: "published"')

    # Add immersive-break-inline and AEO after first body paragraph
    if "immersive-break-inline" not in content:
        video_block = f"""<div class="immersive-break-inline">
  <video autoplay muted loop playsinline preload="metadata">
    <source src="/videos/destinations/{slug}-hero.mp4" type="video/mp4" />
  </video>
  <div class="ib-gradient" style="background: {data['gradient']};"></div>
  <div class="ib-content">
    <div class="ib-title">{data['video_title']}</div>
    <p class="ib-text">{data['video_text']}</p>
  </div>
</div>"""

        lines = content.split('\n')
        fm_count = 0
        fm_end = -1
        for i, line in enumerate(lines):
            if line.strip() == '---':
                fm_count += 1
                if fm_count == 2:
                    fm_end = i
                    break

        if fm_end >= 0:
            body_lines = lines[fm_end+1:]
            first_para_end = -1
            in_para = False
            for j, bl in enumerate(body_lines):
                if bl.strip() and not in_para:
                    in_para = True
                elif not bl.strip() and in_para:
                    first_para_end = j
                    break

            if first_para_end >= 0:
                aeo_text = data.get("aeo", "")
                new_body_lines = []
                if aeo_text:
                    new_body_lines.append(aeo_text)
                    new_body_lines.append("")
                new_body_lines.extend(body_lines[:first_para_end])
                new_body_lines.append("")
                new_body_lines.append(video_block)
                new_body_lines.append("")
                new_body_lines.extend(body_lines[first_para_end:])
                content = '\n'.join(lines[:fm_end+1]) + '\n' + '\n'.join(new_body_lines)

    open(filepath, 'w', encoding='utf-8').write(content)
    print(f"Done {slug}")


for slug, data in DESTINATIONS.items():
    filepath = f"{BASE}/{slug}.md"
    if not os.path.exists(filepath):
        print(f"SKIP {slug} — not found")
        continue
    content = open(filepath, 'r', encoding='utf-8').read()
    if "scottTips:" in content:
        print(f"SKIP {slug} — already has Tier 3")
        continue
    process_file(filepath, slug, data)

print("Nevada Tier 3 complete")
