#!/usr/bin/env python3
"""Writes the neighborhood guide sources into src/pages/ from the data below.

Edit the text here, run this script, then run build.py.
Washington Park is hand-written in src/pages/washington-park.html.
"""
import json
from pathlib import Path

OUT = Path(__file__).parent / "pages"
UPDATED = "2026-10-31"
TODO = '<span class="todo">Chris: confirm or reword</span>'

HOODS = {
"platt-park": dict(
    name="Platt Park",
    title="Living in Platt Park, Denver | Neighborhood Guide",
    description="Living in Platt Park, Denver: South Pearl Street, bungalows and Denver Squares, light rail, schools and honest pros and cons from local agent Chris Nowakiwsky of RE/MAX Professionals.",
    lede="Craftsman bungalows and Denver Squares a few blocks from South Pearl Street, one of Denver's best neighborhood main streets. Here's who it fits and what to know before you buy.",
    glance=[("Best For", "Walkers, young families, first move-up"),
            ("Homes", "Bungalows, Denver Squares, new infill"),
            ("Boundaries", "Broadway to Downing, Mississippi to Evans"),
            ("Getting Around", "Louisiana–Pearl light rail, I-25")],
    take="If you want to walk to dinner on a Tuesday night and still have a backyard, Platt Park is hard to beat. South Pearl is the reason people fall for it.",
    life_title="Life Revolves Around South Pearl Street",
    life=[("South Pearl Street", "A few blocks of independent restaurants, coffee shops, bars and small stores run through the middle of the neighborhood. On Sundays the South Pearl Street Farmers Market takes over the street, and the neighborhood hosts seasonal events like Oktoberfest and Winterfest."),
          ("The Park and Library", "James H. Platt Park, at South Pearl Street and Florida Avenue, gives the neighborhood its name. It holds a recreation center, a playground and the Decker Branch Library, a 1913 Carnegie library that is still in use."),
          ("The Homes", "Most homes date from about 1900 to 1930: Craftsman bungalows, brick Denver Squares, Victorian gable-fronts and a few Spanish Revivals. Modern infill homes and duplexes with rooftop decks sit between them on many blocks."),
          ("Getting Around", "The Louisiana–Pearl light rail station sits just north of the neighborhood, a short ride from downtown. I-25 is a few blocks north, and Washington Park is a few blocks east.")],
    loves=["South Pearl Street within walking distance",
           "Light rail to downtown without a car",
           "Character homes on tree-lined blocks",
           "Washington Park and Old South Gaylord nearby"],
    know=["Lots are often narrow, and garages are usually detached and off the alley",
          "Older homes need a careful sewer scope and electrical check",
          "Street parking near Pearl gets tight during events",
          "A new build and an original bungalow can sell far apart on the same block"],
    faq=[("Is Platt Park a Good Place to Live?", "For buyers who want a walkable neighborhood with a real main street, yes. South Pearl Street, the light rail and Washington Park are all close. The trade-offs are smaller lots, older homes that need careful inspections, and event-day crowds near Pearl."),
         ("Where Is Platt Park in Denver?", "Platt Park is in south-central Denver, roughly between Broadway and Downing Street from Mississippi Avenue south to Evans Avenue. Washington Park is just to the northeast."),
         ("Is It Platt Park or Platte Park?", "Platt Park. The neighborhood is named for James H. Platt Park at its center. It's often misspelled Platte, after the river and the street, which are in other parts of the city."),
         ("Which Schools Serve Platt Park?", "Denver Public Schools serving the area include McKinley-Thatcher Elementary, Grant Beacon Middle School and South High School. Boundaries vary by address, so always confirm a specific home's assigned schools with DPS.")],
    nearby=["washington-park", "bonnie-brae", "cory-merrill"],
    legal="School assignments change; confirm with Denver Public Schools.",
),
"bonnie-brae": dict(
    name="Bonnie Brae",
    title="Living in Bonnie Brae, Denver | Neighborhood Guide",
    description="Living in Bonnie Brae, Denver: a 1920s planned neighborhood of curving streets, period homes, Bonnie Brae Park and the tavern, with honest pros and cons from local agent Chris Nowakiwsky.",
    lede="A 1920s planned neighborhood of curving streets, stone entry pillars and an oval park, tucked between Washington Park and Cherry Creek.",
    glance=[("Best For", "Move-up families who want quiet streets"),
            ("Homes", "1920s–1950s period homes and newer custom builds"),
            ("Where", "East of University Blvd, near Washington Park"),
            ("Getting Around", "University Blvd, minutes to Cherry Creek")],
    take="Bonnie Brae feels tucked away. The curving streets slow traffic down, and most of the people you pass are walking dogs or pushing strollers.",
    life_title="A Neighborhood Designed to Feel Like a Village",
    life=[("A Planned Neighborhood", "In the early 1920s, George Olinger bought farmland southeast of downtown and hired landscape architects S. R. DeBoer and Walter Pesman. They skipped the city grid and laid out curving streets that follow the land. Building began in 1923, stalled when Olinger's company went bankrupt, and picked up again in the late 1930s."),
          ("Bonnie Brae Park", "At the center is an oval park with mature trees, flowering shrubs, an open play field and stone steps. It's the neighborhood's front lawn."),
          ("The Homes", "More than 700 homes line the curving streets: period homes from the 1920s and 1930s, post-war houses with modernist touches, and newer custom homes built where older ones were replaced. Most blocks still feel historic."),
          ("Shops and Food", "Stone pillars mark the entrances where Kentucky and Tennessee avenues meet University Boulevard. Right there are the Bonnie Brae Tavern, open since 1934, and Bonnie Brae Ice Cream. Washington Park and Old South Gaylord Street are a short walk west.")],
    loves=["Curving, low-traffic streets",
           "Bonnie Brae Park at the center",
           "Walkable to Washington Park and Old South Gaylord",
           "Ten minutes or less to Cherry Creek"],
    know=["Homes rarely come up for sale, so be ready when one does",
          "Older homes need careful sewer, roof and electrical checks",
          "New custom homes are changing the look of some blocks",
          "Most market data lumps Bonnie Brae in with Belcaro"],
    faq=[("Where Is Bonnie Brae in Denver?", "Bonnie Brae sits just east of University Boulevard, between Washington Park and Cherry Creek. Its stone entry pillars stand where Kentucky and Tennessee avenues meet University."),
         ("Is Bonnie Brae Part of Belcaro?", "Most of it, officially. Denver counts much of Bonnie Brae inside its Belcaro statistical neighborhood, so city figures and many market reports combine the two. Locals and buyers still treat Bonnie Brae as its own neighborhood."),
         ("Why Are Bonnie Brae's Streets Curved?", "The neighborhood was designed in the 1920s by landscape architects S. R. DeBoer and Walter Pesman, who rejected the city's grid in favor of curving streets that follow the natural slope of the land."),
         ("Is Bonnie Brae a Good Place to Live?", "For buyers who want a quiet, established neighborhood close to Washington Park and Cherry Creek, it's one of Denver's most sought-after. The trade-offs are limited inventory and the upkeep that comes with older homes.")],
    nearby=["washington-park", "belcaro", "cory-merrill"],
    legal="",
),
"belcaro": dict(
    name="Belcaro",
    title="Living in Belcaro, Denver | Neighborhood Guide",
    description="Living in Belcaro, Denver: large lots, ranch homes and custom builds between Washington Park and Cherry Creek, the Cherry Creek Trail, and honest pros and cons from local agent Chris Nowakiwsky.",
    lede="Larger lots, sprawling ranch homes and newer custom builds between Washington Park and Cherry Creek, with the Cherry Creek Trail along the northern edge.",
    glance=[("Best For", "Move-up and luxury buyers who want space"),
            ("Homes", "Large ranches and custom homes on bigger lots"),
            ("Boundaries", "University to Colorado Blvd, Cherry Creek to Tennessee"),
            ("Getting Around", "Colorado Blvd, University Blvd, Cherry Creek Trail")],
    take="Belcaro is where people go when they want a big lot without leaving the city. Cherry Creek is five minutes away, and you still get a real backyard.",
    life_title="Space in the Middle of the City",
    life=[("The Name", "Belcaro takes its name from the mansion of Lawrence C. Phipps, a U.S. senator from Colorado in the 1920s, who called his estate Belcaro and developed much of the neighborhood. Today it's better known as the Phipps Mansion."),
          ("The Homes", "Large ranch-style homes on generous, tree-lined lots set the tone, mixed with newer custom homes. The Polo Grounds, a gated community, fills part of the northern section. Bonnie Brae's curving streets fall mostly within Belcaro's official borders."),
          ("The Outdoors", "The Cherry Creek Trail runs along the neighborhood's northern edge, a paved path that stretches about 40 miles from downtown Denver to Franktown. Washington Park is a short drive or bike ride west."),
          ("Shops and Food", "There's little retail inside the neighborhood. Cherry Creek North's shops and restaurants are minutes north, and Bonnie Brae Ice Cream, the Bonnie Brae Tavern and Campus Lounge are close by along University Boulevard.")],
    loves=["Some of the largest lots in central Denver",
           "Quiet, established streets",
           "Minutes from Cherry Creek North",
           "The Cherry Creek Trail at the edge of the neighborhood"],
    know=["One of Denver's most expensive neighborhoods",
          "Many ranch homes need updating, so budget for renovation",
          "Few shops or restaurants within walking distance",
          "Traffic and noise along Colorado Boulevard on the east edge"],
    faq=[("Where Is Belcaro in Denver?", "Belcaro is bounded by Cherry Creek and Exposition Avenue on the north, Colorado Boulevard on the east, Tennessee Avenue on the south and University Boulevard on the west, between Washington Park and Cherry Creek."),
         ("Is Belcaro Expensive?", "Yes. In 5280 Magazine's 2025 neighborhood rankings, Belcaro's average sale price was close to $2 million, behind only Country Club and Southmoor Park. Prices range widely between original ranch homes and new custom builds."),
         ("What Is the Polo Grounds?", "The Polo Grounds is a gated community in the northern part of Belcaro, with large homes on private streets near Cherry Creek."),
         ("Is Bonnie Brae Part of Belcaro?", "Mostly. Denver's official Belcaro neighborhood includes much of Bonnie Brae, though buyers and locals treat Bonnie Brae as its own area.")],
    nearby=["bonnie-brae", "cory-merrill", "washington-park"],
    legal="",
),
"cory-merrill": dict(
    name="Cory-Merrill",
    title="Living in Cory-Merrill, Denver | Neighborhood Guide",
    description="Living in Cory-Merrill, Denver: quiet streets east of Washington Park, two neighborhood schools, post-war ranches and new custom homes, with honest pros and cons from local agent Chris Nowakiwsky.",
    lede="Quiet streets just east of Washington Park, named for its two neighborhood schools, where post-war ranches are giving way to new custom homes.",
    glance=[("Best For", "Families who want newer homes near Wash Park"),
            ("Homes", "Post-war ranches, bungalows and new custom builds"),
            ("Where", "Between University and Colorado boulevards"),
            ("Getting Around", "Quick access to I-25 and Colorado Blvd")],
    take="Cory-Merrill is where a lot of families land when they want a newer home and a neighborhood school, but don't want to leave the Wash Park area.",
    life_title="A Family Neighborhood Close to Everything",
    life=[("The Name", "The neighborhood is named for its two Denver public schools, Cory Elementary and Merrill Middle School. For many buyers, those schools are the reason to look here."),
          ("The Homes", "Many of the original homes were small single-story houses built for returning World War II veterans. A lot of them have been replaced by large contemporary homes, while brick ranches and bungalows remain on many blocks."),
          ("Shops and Food", "Cory-Merrill is mostly residential. There are a few restaurants and shops along its edges, and Cherry Creek's shopping is a short drive north."),
          ("Getting Around", "Washington Park is just to the west. I-25 and Colorado Boulevard put downtown, Cherry Creek and the Tech Center within easy reach.")],
    loves=["Two neighborhood schools",
           "More newer construction than most central neighborhoods",
           "Close to Washington Park",
           "Easy commute to downtown and the Tech Center"],
    know=["Little you can walk to for dinner or coffee",
          "Large new homes sit next to small originals",
          "Colorado Boulevard is busy along the east edge",
          "Prices have climbed quickly in recent years"],
    faq=[("Why Is It Called Cory-Merrill?", "It's named for Cory Elementary and Merrill Middle School, the two Denver public schools in the neighborhood."),
         ("Is Cory-Merrill Good for Families?", "It's one of the more family-oriented neighborhoods in central Denver, with neighborhood schools, quiet streets and Washington Park nearby. It's mostly residential, so you'll drive for most errands."),
         ("What Kind of Homes Are in Cory-Merrill?", "A mix of post-war ranches and bungalows and large new custom homes. Many original homes have been replaced, so new construction is easier to find here than in neighborhoods like Platt Park or Washington Park."),
         ("Which Schools Serve Cory-Merrill?", "Cory Elementary and Merrill Middle School are in the neighborhood. School boundaries vary by address, so confirm a specific home's assigned schools with Denver Public Schools.")],
    nearby=["washington-park", "belcaro", "bonnie-brae"],
    legal="School assignments change; confirm with Denver Public Schools.",
),
"south-park-hill": dict(
    name="South Park Hill",
    title="Living in South Park Hill, Denver | Neighborhood Guide",
    description="Living in South Park Hill, Denver: tree-lined parkways, classic brick homes, City Park next door and an easy airport run, with honest pros and cons from local agent Chris Nowakiwsky.",
    lede="Wide, tree-lined parkways and classic early-1900s brick homes on the east side of the city, with City Park, the zoo and the museum next door.",
    glance=[("Best For", "Families and anyone who flies often"),
            ("Homes", "Early-1900s brick homes in many styles"),
            ("Boundaries", "Colorado Blvd to Quebec, Colfax to 23rd Ave"),
            ("Getting Around", "Colorado Blvd, Colfax, quick drive to DIA")],
    take="South Park Hill has the big trees and old brick homes people love about central Denver, and it's the easiest of my neighborhoods to get to the airport from.",
    life_title="Parkways, Porches and City Park Next Door",
    life=[("A Planned Suburb in the City", "Park Hill got its name in 1887, when Baron Alois von Winckler platted land just east of City Park. Early rules required 40-foot setbacks and homes far more expensive than the Denver average, which is why the streets feel so wide and green today. Denver annexed the area in 1903."),
          ("The Streets", "Montview Boulevard is the neighborhood's grand street, lined with towering trees and big older homes. Smaller pockets of shops and restaurants sit along Kearney Street, 23rd Avenue and Colfax."),
          ("City Park Next Door", "City Park, Denver's largest park, borders the neighborhood to the west. It holds the Denver Zoo, the Denver Museum of Nature & Science and a golf course."),
          ("Getting Around", "Downtown is an easy commute, and quiet streets with bike lanes make cycling popular. Being on the east side also makes it one of the quicker central neighborhoods to drive to Denver International Airport.")],
    loves=["Wide parkways and mature trees",
           "City Park, the zoo and the museum next door",
           "A strong neighborhood feel with families of all ages",
           "A shorter drive to the airport"],
    know=["Colfax on the south edge is busier and more commercial",
          "Older homes need careful inspections",
          "Farther from south Denver and the Tech Center",
          "Homes on Montview and the parkways carry a premium"],
    faq=[("Where Is South Park Hill?", "South Park Hill is on Denver's east side, bounded roughly by Colorado Boulevard on the west, 23rd Avenue on the north, Quebec Street on the east and Colfax Avenue on the south. City Park is just to the west."),
         ("How Did Park Hill Get Its Name?", "In 1887, Baron Alois von Winckler platted about 32 blocks just east of City Park and called the development Park Hill. Denver annexed the area in 1903."),
         ("Is South Park Hill a Good Place to Live?", "For buyers who want classic homes, tree-lined streets and City Park nearby, yes. It's also convenient to the airport. The trade-offs are older homes and a longer drive to south Denver and the Tech Center."),
         ("Which Schools Serve South Park Hill?", "Park Hill School, a Denver landmark, is a neighborhood elementary school, and East High School sits just west by City Park. Boundaries vary by address, so confirm a specific home's assigned schools with Denver Public Schools.")],
    nearby=["capitol-hill", "washington-park", "platt-park"],
    legal="School assignments change; confirm with Denver Public Schools.",
),
"sloan-lake": dict(
    name="Sloan Lake",
    title="Living in Sloan Lake, Denver | Neighborhood Guide",
    description="Living in Sloan Lake, Denver: the city's second-largest park, a 2.6-mile lake loop, bungalows and new builds, with honest pros and cons from local agent Chris Nowakiwsky of RE/MAX Professionals.",
    lede="A west-side neighborhood wrapped around a 177-acre lake, with a 2.6-mile loop, mountain and skyline views, and a mix of older bungalows and new builds.",
    glance=[("Best For", "Active buyers who want new construction"),
            ("Homes", "1920s–1950s bungalows, new townhomes and custom builds"),
            ("Boundaries", "Sheridan to Raleigh, 17th to 26th Ave"),
            ("Getting Around", "About 4 miles to downtown, Colfax, Sheridan")],
    take="Sloan Lake is the west side's answer to Wash Park: a bigger lake, mountain views from the path, and a lot more new construction.",
    life_title="Life Around the Lake",
    life=[("Sloan's Lake Park", "At about 290 acres, Sloan's Lake Park is Denver's second-largest park after City Park, and its lake covers about 177 acres. A paved loop of roughly 2.6 miles circles the water, with views of the mountains and downtown. Paddleboards and kayaks are common, and the Colorado Dragon Boat Festival comes every summer."),
          ("The Homes", "Bungalows, Tudors and brick cottages from the 1920s to the 1950s mix with modern duplexes, townhomes and custom homes. The former St. Anthony hospital site south of the park has been rebuilt with a condo tower, apartments, shops and restaurants."),
          ("Shops and Food", "New restaurants and shops cluster along the south side near the old hospital site and along West Colfax, with the Highlands' restaurants a short drive east."),
          ("Getting Around", "Downtown is about four miles east. Most residents drive, with bus routes on Colfax and Sheridan and the W Line light rail a short distance south.")],
    loves=["A 177-acre lake and a 2.6-mile loop",
           "Mountain and skyline views",
           "More new construction than most central neighborhoods",
           "Close to downtown and the Highlands"],
    know=["Many new homes are duplexes and townhomes on split lots",
          "Some nearby addresses are in Edgewater or Lakewood, not Denver",
          "Farther from south Denver and the Tech Center",
          "Park events and summer weekends bring crowds and traffic"],
    faq=[("How Big Is Sloan's Lake?", "The lake covers about 177 acres, and Sloan's Lake Park covers about 290 acres, making it Denver's second-largest park after City Park. The paved loop around the lake is about 2.6 miles."),
         ("Is It Sloan Lake or Sloan's Lake?", "Both are used. The park is Sloan's Lake Park, while Denver lists the neighborhood as Sloan Lake. The name comes from Thomas Sloan, who homesteaded the land in the 1860s."),
         ("Is a Home Near Sloan's Lake in Denver?", "Not always. The neighborhood borders the separate cities of Edgewater and Lakewood along Sheridan Boulevard. Taxes, city services and school districts differ, so check which city an address is in."),
         ("Is Sloan Lake a Good Place to Live?", "For buyers who want an active, outdoorsy neighborhood with newer homes close to downtown, yes. The trade-offs are more townhome-style new construction and a longer drive to the south side of the metro.")],
    nearby=["capitol-hill", "south-park-hill", "platt-park"],
    legal="Confirm whether an address is in Denver, Edgewater or Lakewood; taxes, services and schools differ.",
),
"greenwood-village": dict(
    name="Greenwood Village",
    title="Living in Greenwood Village, CO | Neighborhood Guide",
    description="Living in Greenwood Village, Colorado: estate lots, Cherry Creek schools, the High Line Canal trail and a short commute to the Tech Center, with honest pros and cons from local agent Chris Nowakiwsky.",
    lede="A separate city just south of Denver with estate lots, mid-century ranches, Cherry Creek schools and the Denver Tech Center inside its limits.",
    glance=[("Best For", "Families who want space and Cherry Creek schools"),
            ("Homes", "Estates, ranches, newer custom homes and condos"),
            ("Where", "South of Denver along I-25, Arapahoe County"),
            ("Getting Around", "I-25, I-225, light rail through the Tech Center")],
    take="Greenwood Village is for families who want space and Cherry Creek schools but still want to be 20 minutes from downtown and five minutes from work at the Tech Center.",
    life_title="Room to Spread Out, Close to Work",
    life=[("A City of Its Own", "Greenwood Village is its own city of roughly 15,000 people across about 8 square miles in Arapahoe County. The Denver Tech Center sits inside its limits, which is why many residents have short commutes."),
          ("The Outdoors", "The city maintains more than 180 acres of parks and about 276 acres of open space, including Westlands Park and the Marjorie Perry Nature Preserve. The High Line Canal Trail winds through on a natural-surface path, and there are equestrian trails and parks too."),
          ("The Homes", "Housing ranges from gated estates on multi-acre lots to mid-century ranches and newer custom homes, with condos and townhomes near the Tech Center and its light rail stations."),
          ("Schools", "Most of Greenwood Village is in the Cherry Creek School District, including Cherry Creek High School. Some neighborhoods are served by Littleton Public Schools depending on which side of Belleview Avenue they're on, so check by address.")],
    loves=["Larger lots and estate properties",
           "Cherry Creek School District for most addresses",
           "Short commute to the Tech Center",
           "Trails, open space and equestrian areas"],
    know=["Mostly car-dependent for daily errands",
          "Some addresses are in Littleton schools or unincorporated Arapahoe County",
          "Farther from downtown's restaurants and nightlife",
          "Estate homes can carry high maintenance costs"],
    faq=[("Is Greenwood Village Part of Denver?", "No. Greenwood Village is a separate city in Arapahoe County, just south of Denver along I-25. It's about 20 to 30 minutes from downtown Denver by car."),
         ("What School District Is Greenwood Village In?", "Most of Greenwood Village is in the Cherry Creek School District. Some neighborhoods are served by Littleton Public Schools depending on which side of Belleview Avenue they're on, so always confirm by address."),
         ("Is Greenwood Village a Good Place to Live?", "For families who want space, well-regarded schools and a short commute to the Tech Center, it's one of the metro's most popular choices. It's quieter and more car-dependent than central Denver."),
         ("Is Every Greenwood Village Address in City Limits?", "No. Some pockets with Greenwood Village mailing addresses are unincorporated Arapahoe County, with different taxes and services. Check before you buy.")],
    nearby=["belcaro", "cory-merrill", "washington-park"],
    legal="Confirm city limits and school district by address.",
),
"capitol-hill": dict(
    name="Capitol Hill",
    title="Buying in Capitol Hill, Denver | Condo and Neighborhood Guide",
    description="Buying a condo or townhome in Capitol Hill, Denver: historic buildings, HOA questions to ask, parking and what to know before you buy, from local owner and agent Chris Nowakiwsky.",
    lede="Denver's densest, most historic neighborhood: mansions turned condos, classic brick apartment buildings and townhomes, steps from the Capitol and Cheesman Park.",
    glance=[("Best For", "First-time buyers, downsizers, investors"),
            ("Homes", "Condos, townhomes and historic buildings"),
            ("Boundaries", "Broadway to Downing, 7th Ave to Colfax"),
            ("Getting Around", "Walkable, bikeable, buses on Colfax")],
    take="I own a townhome in Capitol Hill, so I know these buildings from the owner's side: the HOA meetings, the parking, and the questions to ask before you buy.",
    life_title="City Living With a Lot of History",
    life=[("A Neighborhood of Mansions and Apartments", "Denver's wealthy families built mansions here in the late 1800s. After the Silver Crash of 1893, building shifted to apartments, and historic buildings like the Colonnade, Alta Court and the Hamilton still stand. Many mansions are now offices or condos."),
          ("Landmarks", "The Colorado State Capitol, the Molly Brown House Museum, the Governor's Residence and the Cathedral of St. John in the Wilderness are all here. Cheesman Park sits just east, and many residents consider it part of the neighborhood."),
          ("The Homes", "Most homes are condos and apartments in buildings from the early 1900s, with some townhomes and newer condo buildings. Capitol Hill is Denver's most densely populated neighborhood, with about 16,700 residents in 2020."),
          ("Getting Around", "Almost everything is walkable. Colfax Avenue on the north edge has frequent buses, restaurants and music venues, and downtown is a short walk or bike ride west.")],
    loves=["One of Denver's most affordable ways into homeownership",
           "Walk to restaurants, parks, downtown and Cheesman Park",
           "Historic buildings with real character",
           "Strong rental demand for future landlords"],
    know=["Many older buildings have no off-street parking",
          "HOA dues, reserves and special assessments vary widely",
          "Some buildings aren't approved for FHA or VA loans",
          "Colfax brings nightlife noise to the north edge"],
    faq=[("Is Capitol Hill a Good Place to Buy a Condo?", "For first-time buyers and downsizers who want to walk everywhere, it's one of Denver's best options. The key is the building: review the HOA's budget, reserves, insurance and any planned assessments before you commit."),
         ("What Should I Check Before Buying a Condo in Denver?", "Ask for the HOA's budget, reserve study, meeting minutes, insurance and rules on rentals and pets. Find out whether any special assessments are planned, whether parking is deeded or assigned, and whether the building is approved for FHA or VA loans if you need one."),
         ("Is Cheesman Park Part of Capitol Hill?", "Officially, no. Denver treats Cheesman Park as its own neighborhood just east of Capitol Hill, but many residents consider the two one area."),
         ("Where Is Capitol Hill in Denver?", "Capitol Hill sits just east of downtown, bounded by Broadway on the west, Downing Street on the east, 7th Avenue on the south and Colfax Avenue on the north.")],
    nearby=["south-park-hill", "platt-park", "washington-park"],
    legal="",
),
}

# REcolorado closed sales, Nov 1, 2025 to Oct 31, 2026, pulled Oct 31, 2026.
# (subdivision search, single-family n / median / $psf, attached n / median / $psf)
MARKET = {
    "washington-park": ("Washington Park", (141, 1450000, 551), (28, 488750, 434)),
    "platt-park": ("Platt Park or Platte Park", (119, 985000, 483), (9, 830000, 462)),
    "bonnie-brae": ("Bonnie Brae", (39, 1915000, 535), (0, None, None)),
    "belcaro": ("Belcaro", (12, 2675000, 574), (0, None, None)),
    "cory-merrill": ("Cory-Merrill", (63, 1225000, 442), (0, None, None)),
    "south-park-hill": ("South Park Hill", (58, 1012500, 423), (0, None, None)),
    "sloan-lake": ("Sloan Lake, Sloans Lake or Sloan's Lake (Denver addresses)", (123, 1040000, 463), (67, 645000, 436)),
    "greenwood-village": (None, (144, 1972500, 427), (46, 646000, 351)),
    "capitol-hill": ("Capitol Hill", (11, 975000, 424), (87, 295000, 343)),
}


def money(v):
    if v >= 1e6:
        return f"${int(v / 1e4 + 0.5) / 100:.2f}M".replace(".00M", "M")
    return f"${v:,.0f}"


def market_rows(slug):
    _, sfr, att = MARKET[slug]
    rows = []
    for label, (n, med, psf) in (("Single-family", sfr), ("Townhome and condo", att)):
        if n >= 5:
            rows.append(f'<tr><td>{label}</td><td class="num">{money(med)}</td><td class="num">${psf:,}</td><td class="num">{n}</td></tr>')
        elif n > 0:
            rows.append(f'<tr><td>{label}</td><td class="num" colspan="3">Too few sales to report ({n})</td></tr>')
    return "\n            ".join(rows)


def market_source(slug):
    sub = MARKET[slug][0]
    scope = "in the City of Greenwood Village" if sub is None else f"with the subdivision listed as {sub}"
    return f"Closed sales from November 2025 through October 2026 {scope}. Source: REcolorado MLS. Deemed reliable but not guaranteed."


def typical(slug):
    _, sfr, att = MARKET[slug]
    if slug == "capitol-hill":
        return f"About {money(att[1])} for a condo or townhome"
    return f"About {money(sfr[1])} for a single-family home"

BLURBS = {
    "washington-park": "Two lakes, a 2.6-mile loop, and Denver's most loved park.",
    "platt-park": "Bungalows a few blocks from South Pearl Street.",
    "bonnie-brae": "Curving streets and a 1920s village feel.",
    "belcaro": "Larger lots and ranch homes near Cherry Creek.",
    "cory-merrill": "Neighborhood schools and newer homes near Wash Park.",
    "south-park-hill": "Wide parkways and classic brick homes.",
    "sloan-lake": "A big lake, mountain views and new builds on the west side.",
    "greenwood-village": "Space, trails and Cherry Creek schools.",
    "capitol-hill": "Condos and townhomes, the city's best first step.",
}
NAMES = {"washington-park": "Washington Park", **{k: v["name"] for k, v in HOODS.items()}}


def page(slug, h):
    meta = {
        "title": h["title"],
        "headline": f"Living in {h['name']}" + (", Colorado" if slug == "greenwood-village" else ", Denver"),
        "description": h["description"],
        "type": "article",
        "place": f"{h['name']}, " + ("Colorado" if slug == "greenwood-village" else "Denver, Colorado"),
        "nav": "neighborhoods",
        "published": UPDATED,
        "updated": UPDATED,
        "crumbs": [["Home", "index"], ["Neighborhoods", "neighborhoods"], [h["name"], None]],
        "legal_extra": h["legal"],
        "valuation": {
            "eyebrow": f"Own in {h['name']}?",
            "heading": "See What Your Home Would Sell For Now",
            "text": "Online estimates miss what makes a home in this neighborhood different. Send your address and I'll run a real valuation from recent nearby sales.",
        },
    }
    glance = "\n".join(f"      <div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in h["glance"])
    life = "\n".join(f"        <div>\n          <h2>{t}</h2>\n          <p>{p}</p>\n        </div>" for t, p in h["life"])
    loves = "\n".join(f"          <li>{x}</li>" for x in h["loves"])
    know = "\n".join(f"          <li>{x}</li>" for x in h["know"])
    faq = "\n".join(
        f"        <details{' open' if i == 0 else ''}>\n          <summary>{q}</summary>\n          <p>{a}</p>\n        </details>"
        for i, (q, a) in enumerate(h["faq"]))
    nearby = "\n".join(
        f'        <a class="hood" href="{{{{link:{n}}}}}"><strong>{NAMES[n]}</strong><span>{BLURBS[n]}</span></a>'
        for n in h["nearby"])
    return f'''<!--meta
{json.dumps(meta, indent=1)}
-->
  <section class="page-hero-band"><div class="wrap page-hero">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="{{{{link:index}}}}">Home</a><span aria-hidden="true">/</span><a href="{{{{link:neighborhoods}}}}">Neighborhoods</a><span aria-hidden="true">/</span><span>{h['name']}</span></nav>
    <h1>Living in {h['name']}</h1>
    <p class="lede">{h['lede']}</p>
  </div></section>

  <div class="wrap">
    <dl class="glance">
{glance}
      <div><dt>Typical Price</dt><dd>{typical(slug)}</dd></div>
    </dl>
  </div>

  <section class="band">
    <div class="wrap">
      <figure class="take" style="margin:0">
        <img src="{{{{asset:chris-portrait.jpg}}}}" alt="Chris Nowakiwsky" width="96" height="96">
        <div>
          <blockquote>“{h['take']}”</blockquote>
          <figcaption>Chris Nowakiwsky, Broker Associate · {TODO}</figcaption>
        </div>
      </figure>
    </div>
  </section>

  <section class="band tint">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">Life Here</p>
        <h2>{h['life_title']}</h2>
      </div>
      <div class="two-col">
{life}
      </div>
    </div>
  </section>

  <section class="band">
    <div class="wrap two-col">
      <div>
        <p class="eyebrow">Why People Love It</p>
        <ul class="ticks">
{loves}
        </ul>
      </div>
      <div>
        <p class="eyebrow">What to Know First</p>
        <ul class="ticks con">
{know}
        </ul>
      </div>
    </div>
  </section>

  <section class="band tint">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">Market Snapshot</p>
        <h2>What Homes Are Selling For</h2>
        <p class="lede">Median sold prices over the last 12 months, from REcolorado.</p>
      </div>
      <div class="table-wrap">
        <table>
          <thead><tr><th>Home Type</th><th class="num">Median Sold Price</th><th class="num">Median Price per Sq Ft</th><th class="num">Sales, Last 12 Months</th></tr></thead>
          <tbody>
            {market_rows(slug)}
          </tbody>
        </table>
      </div>
      <p class="source">{market_source(slug)}</p>
    </div>
  </section>

  <section class="band">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">Questions Buyers Ask</p>
        <h2>{h['name']} FAQ</h2>
      </div>
      <div class="faq">
{faq}
      </div>
    </div>
  </section>

  <section class="band tint">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">Nearby</p>
        <h2>Also Worth a Look</h2>
      </div>
      <div class="hoods">
{nearby}
      </div>
    </div>
  </section>

  {{{{valuation}}}}
'''


if __name__ == "__main__":
    for slug, h in HOODS.items():
        (OUT / f"{slug}.html").write_text(page(slug, h))
    print("wrote", len(HOODS), "neighborhood pages")
