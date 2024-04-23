import sys
import os
import random


current_file_path = os.path.abspath(__file__)
parent_directory = os.path.dirname(os.path.dirname(current_file_path))
sys.path.append(parent_directory)

from utils.LLM_api import run_LLM
from utils.VLM_api import run_gpt4v


country_E_profile_1 = {
    "Name": "Thomas Fletcher",
    'Age':35, 
    'Family':'Wife: A strong-willed woman who often manages the household and occasionally helps in the forge. Children: Two boisterous sons, aged 10 and 7, both showing an interest in their father\'s trade. Extended Family: Extended Family: A younger brother, known for his wit and charm, often visiting for a drink and a laugh.',
    'Occupation':'Blacksmith, known for his exceptional craftsmanship and unique designs.', 
    'Personality':'Boisterous and full of life, often heard laughing heartily or cursing loudly when things don\'t go his way.\nSociable, enjoys spending time with friends at the local tavern, sharing stories over a pint.\nStrong sense of humor, often cracking jokes, even in the middle of a tough workday.\nDeeply superstitious, follows various rituals and omens, which he believes affect his work and life.', 
    'Social Status':'Well-respected local craftsman, known throughout the village not just for his skills but also for his charismatic personality.', 
    'Potential Illness':'Occasional hangovers from nights of heavy drinking.\nRespiratory irritation from smoke and dust in the forge.\nMinor injuries from his work, which he often boasts about as badges of honor.', 
    "Body Condition": "Strong and muscular, with calloused hands and a broad frame.\nA hearty laugh that echoes in his workshop and the local tavern.\nRoughened features and tanned skin from years of laboring in front of a hot forge.",
    "Hobbies and Interests": "Passionate about experimenting with new metalworking techniques.\nEnjoys local fishing, often seen by the river on quiet mornings.\nAn avid storyteller, known for captivating tales of folklore and legend.\nTakes part in village festivals, often contributing his crafted items as prizes.",
    "Style of Talking": "Loud and hearty, with a booming voice that commands attention.\nSpeaks with a friendly, informal tone, often punctuated with laughter.\nUses a lot of local slang and colloquialisms, making his speech colorful and distinctive.",
    "Unique Quirks": "Always wears a lucky charm around his neck when working in the forge.\nHas a tradition of naming each of his hammers and talking to them as if they were old friends.",
    "Secrets or Scandals": "Once forged a ceremonial sword for a notorious outlaw, a fact he keeps to himself.\nRumored to have discovered a rare and ancient metalworking technique, which he guards jealously."
}

country_E_profile_2 = {
    'Name': 'Dr. Edward Langley',
    'Age': 47,
    'Family': 'Widower. Daughter: A 19-year-old who assists with his medical practices. Son-in-law: A young scribe married to his daughter.',
    'Occupation': 'Local physician, known for his herbal remedies and surgical skills.',
    'Personality': 'Stoic and observant, often speaks in a calm, measured tone. Compassionate towards his patients, but maintains professional distance. Curious about new medical practices and advancements.',
    'Social Status': 'Respected in the community for his knowledge and skill, but sometimes viewed with suspicion due to the nature of his work.',
    'Potential Illness': 'Chronic arthritis, making some surgical procedures difficult.',
    'Body Condition': 'Thin and slightly stooped from age. Precise and careful movements.',
    'Hobbies and Interests': 'Dedicated to studying medical texts, particularly those from other cultures. Enjoys long walks in nature, often collecting herbs and plants for his remedies. Has a passion for chess, finding it stimulates his strategic thinking. Interested in astronomy, often stargazing and contemplating the universe.',
    'Style of Talking': 'Measured and thoughtful, often pausing to consider his words carefully. Uses medical terminology when discussing his work, but switches to simpler language with patients. Occasionally injects dry humor into his conversations, though it\'s often missed due to his stoic demeanor.',
    'Unique Quirks': 'Always carries a small leather pouch containing his most trusted surgical tools. Known to talk to his plants, believing it helps them grow better for his remedies.',
    'Secrets or Scandals': 'Privately experimenting with unconventional treatments, some of which are considered controversial. Rumored to have once treated a notorious outlaw, which he has neither confirmed nor denied.'
}

country_E_profile_3 = {
    'Name': "Thomas Whitaker",
    'Age': 28,
    'Family': 'Single. Lives with his elderly mother who depends on his income.',
    'Occupation': 'Baker, known for his early mornings and delicious bread.',
    'Personality': 'Hardworking and diligent, often tired but always friendly. Takes great pride in his work. Enjoys sharing stories with customers.',
    'Social Status': 'Well-liked in the community, seen as a reliable and essential figure.',
    'Potential Illness': 'Frequent back pain from lifting heavy sacks of flour.',
    'Body Condition': 'Average build, with strong arms and a warm smile.',
    'Hobbies and Interests': 'Avid gardener, enjoys growing herbs and vegetables in his small backyard. Enthusiast of local history, often visits the library to read about the town’s past. Loves baking experiments, trying out old and exotic recipes during his free time.',
    'Style of Talking': 'Warm and conversational, often greets customers by name and remembers details about their lives. Speaks with a gentle, reassuring tone, and his laughter is infectious. Shares anecdotes and bits of local history while serving his baked goods.',
    'Unique Quirks': 'Always wears an old, faded apron that once belonged to his father. Whistles old folk tunes while baking, a habit that endears him to his neighbors.',
    'Secrets or Scandals': 'Once secretly entered a national baking competition and won third place, but keeps it quiet to avoid drawing too much attention. Rumored to have been in love with a local aristocrat’s daughter in his youth, a romance that ended abruptly under mysterious circumstances.'
}

country_E_profile_4 = {
    'Name': "Sir Edward Langley",
    'Age': 60,
    'Family': 'Wife: A stern woman who runs their home with efficiency. Two grown sons, both knights.',
    'Occupation': 'Retired knight, now a landowner managing several farms.',
    'Personality': 'Authoritative and proud, with a strict sense of honor and duty. Shares war stories with a nostalgic tone.',
    'Social Status': 'High, due to his military past and land ownership.',
    'Potential Illness': 'Old war wounds that ache in cold weather.',
    'Body Condition': 'Still robust, but aging. Walks with a slight limp.',
    'Hobbies and Interests': "Enjoys falconry, seeing it as a connection to his knightly past. Avid gardener, taking pride in maintaining a splendid rose garden. Fond of chess, often inviting other nobles for friendly but competitive games. Keen collector of antique swords and armor.",
    'Style of Talking': "Speaks in a deep, commanding voice. Often uses military terms and phrases. Prefers direct and honest communication, valuing brevity and clarity. When reminiscing about his past, his tone becomes more animated and descriptive.",
    'Unique Quirks': "Has a ritual of visiting his stables every morning to feed his retired warhorse. Secretly enjoys baking, a hobby he considers out of character for his warrior image.",
    'Secrets or Scandals': "Suspected of once having a clandestine affair with a high-born lady, a well-guarded secret. Allegedly involved in a dispute over land that nearly led to a duel with a neighboring lord."
}

country_E_profile_5 = {
    "Name": "Aethelred Fletcher",
    "Age": 22,
    "Family": "Engaged to Emily, a merchant's daughter. Parents deceased. Raised by his uncle, a carpenter.",
    "Occupation": "Apprentice to a stonemason, aspiring to become a master craftsman.",
    "Personality": "Eager to learn and often overly enthusiastic. Respectful to elders and dreams of building grand structures.",
    "Social Status": "Average, but with potential for growth.",
    "Potential Illness": "Occasional cough from dust inhalation.",
    "Body Condition": "Fit and agile, with a youthful energy.",
    "Hobbies and Interests": "Enjoys sketching designs for buildings and bridges. Fascinated by gothic architecture. Often visits cathedrals and castles for inspiration. Enthusiastic about experimenting with new building techniques and materials.",
    "Style of Talking": "Speaks with a fervent, optimistic tone. Full of technical jargon related to his craft. Often quick to share ideas and thoughts about his latest projects. Shows a respectful manner when speaking with his seniors or potential clients.",
    "Unique Quirks": "Carries a small notebook filled with sketches and ideas for future structures. Often gets so absorbed in observing buildings that he loses track of time. Has a habit of tapping his fingers rhythmically, mimicking the sound of a hammer and chisel.",
    "Secrets or Scandals": "Once discovered an ancient, hidden chamber while repairing a church, but kept it secret to protect its artifacts. Occasionally uses unorthodox methods in his work that would be frowned upon by traditional craftsmen."
}


country_E_profile_6 = {
    'Name': "Reverend Thomas Wycliffe",
    "Age": 54,
    'Family': 'Wife: A quiet woman who enjoys gardening. Three daughters, all married.',
    'Occupation': 'Village priest, known for his lengthy sermons and strict adherence to religious practices.',
    'Personality': 'Stern and pious, often seen in deep thought or prayer. Strict with moral teachings, but shows a softer side to those in need.',
    'Social Status': 'Respected for his religious role, but sometimes seen as overly rigid.',
    'Potential Illness': 'Poor eyesight, requiring assistance with reading scriptures.',
    'Body Condition': 'Slightly frail, with a calm presence.',
    'Hobbies and Interests': 'Avid birdwatcher, finding peace in observing nature. Enjoys writing religious texts and hymns. Passionate about gardening, often helping his wife in their personal garden.',
    'Style of Talking': 'Speaks in a measured, deliberate manner. Uses formal and sometimes archaic language, reflecting his extensive religious education. Can be eloquent, particularly when delivering sermons.',
    'Unique Quirks': 'Keeps a collection of rare religious texts in his study. Often seen wearing an old, faded stole that he claims was worn by a renowned cleric from the past.',
    'Secrets or Scandals': 'Privately questions some of the church’s teachings, a doubt he shares only in his personal diary. Rumored to have once been in love with a woman before taking his religious vows, a topic he avoids discussing.'
}

country_E_profile_7 = {
    "Name": "Ethan Greenwood",
    "Age": 32,
    "Family": "Unmarried. Lives with two loyal hunting dogs. Close to his sister who lives in the neighboring village.",
    "Occupation": "Forester, known for his knowledge of the woods and skill with a bow.",
    "Personality": "Quiet and observant, with a love for nature. Rarely visits the village, preferring the solitude of the forest.",
    "Social Status": "Seen as a bit of an outsider, but respected for his skills and knowledge of the wilderness.",
    "Potential Illness": "Minor injuries from forest work and occasional animal attacks.",
    "Body Condition": "Lean and muscular, with sharp eyesight.",
    "Hobbies and Interests": "Adept at wood carving, creating intricate figures and tools. Enjoys bird watching, can identify numerous species and their calls. Passionate about herbalism, often experiments with natural remedies. Finds relaxation in playing a handmade flute.",
    "Style of Talking": "Speaks rarely, but when he does, his words are thoughtful and deliberate. Has a soft, calming voice that reflects his peaceful nature. Often uses analogies from the natural world in his speech.",
    "Unique Quirks": "Always carries a hand-carved amulet for luck. Has an unusual ability to move silently through the forest, almost blending in with nature.",
    "Secrets or Scandals": "Rumored to have once discovered a band of outlaws in the forest and quietly led authorities to their capture. Secretly shelters injured animals, some of which are considered dangerous or forbidden by local laws."
}

country_E_profile_8 = {
    'Name': "Edward 'Ned' Grimes",
    "Age": 41,
    'Family': 'Wife: Often complains about his behavior. Son: Rebellious teenager who dislikes his father\'s reputation.',
    'Occupation': 'Innkeeper, known for watering down drinks and overcharging travelers.',
    'Personality': 'Cunning and quick-tempered, often involved in arguments with patrons. Greedy, always looking for ways to make an extra coin.',
    'Social Status': 'Known in the community, but not well-liked. Seen as untrustworthy.',
    'Potential Illness': 'Chronic indigestion, likely from stress and poor diet.',
    'Body Condition': 'Average build, but often appears disheveled and unkempt.',
    'Hobbies and Interests': 'Enjoys eavesdropping on travelers’ conversations, often using the information for personal gain.\nAvid player of card games, particularly fond of gambling, though not always successfully.\nLikes to collect rare coins, a hobby that aligns with his greed.',
    'Style of Talking': 'Sarcastic and blunt, often with a mocking tone.\nTends to speak loudly, especially when trying to assert authority in his inn.\nUses local slang and colloquialisms, making his speech familiar but sometimes coarse.',
    'Unique Quirks': 'Has a habit of nervously tapping his fingers, especially when plotting something deceitful.\nKeeps a hidden compartment under the bar counter where he stashes extra profits or illicit goods.',
    'Secrets or Scandals': 'Rumored to be involved in smuggling illegal goods through his inn.\nAllegedly bribed a local official to avoid penalties for his questionable business practices.'
}

country_E_profile_9 = {
    "Name": "Elijah Whitmore",
    "Age": 33,
    "Family": "Single. Estranged from his family due to his lifestyle.",
    "Occupation": "Gambler and occasional thief, often seen in less reputable parts of town.",
    "Personality": "Charming and deceptive, skilled at manipulating others. Quick-witted and often escapes trouble through clever words.",
    "Social Status": "Infamous in certain circles, known for his shady dealings.",
    "Potential Illness": "Nervous ticks, possibly from constant stress and looking over his shoulder.",
    "Body Condition": "Slim and agile, capable of quick movements.",
    "Hobbies and Interests": "Avid card player, especially proficient in games of bluff and strategy.\nFascinated by lock-picking and sleight of hand tricks, often practices to improve his skills.\nEnjoys attending underground boxing matches, betting on fighters.\nCollector of rare coins and trinkets, often acquired through less than legal means.",
    "Style of Talking": "Speaks with a smooth, persuasive tone, often laced with underlying sarcasm.\nUses street slang mixed with unexpectedly sophisticated vocabulary.\nTends to speak quickly, with a sharp wit that can both amuse and disarm.",
    "Unique Quirks": "Always wears a distinctive ring he claims brings him luck in gambling.\nHas a habit of flipping a coin when making decisions, believing in leaving some things to chance.",
    "Secrets or Scandals": "Rumored to have outsmarted a notorious gang leader, earning a precarious mix of respect and animosity.\nAllegedly involved in a high-stakes robbery that went awry, though he managed to evade capture and suspicion."
}

country_E_profile_10 = {
    "Name": "Jack \"The Jester\" Fawley",
    "Age": 31,
    "Family": "Wife: A local seamstress known for her sharp tongue. No children, but an elderly father who disapproves of his lifestyle.",
    "Occupation": "Street performer and part-time pickpocket, often seen entertaining crowds in busy markets or fairs.",
    "Personality": "Charismatic and theatrical, loves being the center of attention. However, he's also sly and opportunistic, often using his performances to scout for potential theft targets.",
    "Social Status": "Popular among the common folk for his entertaining antics, but distrusted by the local merchants and guards.",
    "Potential Illness": "Occasional injuries from his acrobatic performances and narrow escapes from getting caught in his thefts.",
    "Body Condition": "Lean and agile, with quick reflexes and a flamboyant flair in his movements.",
    "Hobbies and Interests": "Skilled in juggling and sleight of hand tricks, often practices new routines to amuse his audiences.\nFascinated by local folklore and incorporates storytelling into his performances.\nEnjoys playing the flute, often seen serenading passersby with lively tunes.",
    "Style of Talking": "Witty and engaging, adept at captivating and distracting his audience with clever wordplay.\nOften adopts different accents and personas during his performances to add to the entertainment.\nSpeaks with a quick pace and a mischievous tone, always ready with a joke or a playful retort.",
    "Unique Quirks": "Always wears a brightly colored, patchwork hat, claimed to be his lucky charm.\nHas a habit of winking conspiratorially at his audience, as if sharing a private joke.",
    "Secrets or Scandals": "Suspected of being the mastermind behind a notorious theft at a local noble's residence.\nPrivately harbors dreams of leaving his life of petty crime to become a legitimate actor, a secret he shares with no one."
}


country_E_profile_11 = {
    'Name': "Cedric Blackwood",
    "Age": 26,
    'Family': 'Orphan. No known family ties, often claims to be a lone wolf.',
    'Occupation': 'Mercenary, hired for various unsavory tasks. Known for his ruthlessness.',
    'Personality': 'Cold and distant, rarely shows any emotion. Pragmatic to a fault, cares only for the completion of his job and payment.',
    'Social Status': 'Feared and avoided by many, seen as a necessary evil by others.',
    'Potential Illness': 'Scarred skin and frequent headaches from past injuries.',
    'Body Condition': 'Physically strong and intimidating, with a menacing presence.',
    'Hobbies and Interests': 'Expert in survival skills, often spends time in remote wilderness to sharpen his abilities.\nEnjoys reading historical military strategy books, finding parallels in his own tactics.\nPractices knife throwing, both as a hobby and a form of meditation.\nOccasionally visits underground fighting rings, seeking the thrill of hand-to-hand combat.',
    'Style of Talking': 'Speaks in a terse, clipped manner. Rarely engages in unnecessary conversation.\nHis voice is low and gravelly, often intimidating to those he speaks with.\nWhen he does speak, his words are calculated and to the point, revealing little about himself.',
    'Unique Quirks': 'Always wears a distinctive black leather bracelet, the significance of which is unknown.\nHas a habit of flipping a coin when making decisions, a quirk that adds an element of chance to his otherwise calculated life.',
    'Secrets or Scandals': 'Suspected of having betrayed a former employer for a higher bid, a rumor that makes potential clients cautious.\nRumored to have a hidden cache of valuable items collected from various assignments, the location of which is a closely guarded secret.'
}

country_E_profile_12 = {
    'Name': "Godwin 'Shadow' Morgan",
    "Age": 29,
    'Family': 'Wife: A local barmaid, often worried about his activities. No children.',
    'Occupation': 'Smuggler, involved in illegal trade of goods across borders.',
    'Personality': 'Slick and persuasive, able to talk his way out of most situations. Has a temper when things don\'t go his way.',
    'Social Status': 'Known in the underworld, but maintains a low profile in public.',
    'Potential Illness': 'Occasional bouts of anxiety and paranoia.',
    'Body Condition': 'Fit and nimble, necessary for quick getaways.',
    'Hobbies and Interests': 'A skilled card player, often found in backroom games. Enjoys sailing, using his skills for both work and leisure. Has a keen interest in folklore and legends, often sharing tales from different cultures. Collects rare coins from various countries.',
    'Style of Talking': 'Smooth and confident, with a hint of a charming accent. Often uses slang and jargon related to his trade. Quick-witted, especially in negotiations or tense situations. Can be intimidating when angered, his words sharp and cutting.',
    'Unique Quirks': 'Always wears a distinctive tricorn hat, a trademark of his persona. Carries an old, intricately carved pocket watch - a family heirloom with mysterious significance. Has a habit of flipping a coin when making decisions.',
    'Secrets or Scandals': 'Rumored to have once been a member of the Royal Navy before turning to smuggling. Secretly supports a network of orphans and street children, using his ill-gotten gains for their welfare. Involved in a risky plot to smuggle a high-value artifact, potentially dangerous if discovered.'
}

country_E_profile_13 = {
    "Name": "Theobald Blythe",
    "Age": 48,
    "Family": "Wife: Long-suffering and patient. Two daughters who are ashamed of his reputation.",
    "Occupation": "Butcher, known for selling meat of questionable quality.",
    "Personality": "Gruff and often rude, especially to those who question his products. Defensive about his business practices.",
    "Social Status": "Not held in high regard, but tolerated due to the necessity of his trade.",
    "Potential Illness": "Frequent stomach ailments, possibly from handling unclean meat.",
    "Body Condition": "Bulky and strong, with a tendency to intimidate.",
    "Hobbies and Interests": "Enjoys brewing homemade ale, a hobby that often results in subpar concoctions.\nFascinated with local folklore, particularly tales involving cunning and trickery.\nOccasionally participates in local gambling dens, though more for the social interaction than profit.",
    "Style of Talking": "Blunt and straightforward, often laced with sarcasm and dry humor.\nSpeaks loudly, with a voice that carries and commands attention, albeit not always positively.\nTends to use colloquial language, reflecting his working-class background and no-nonsense attitude.",
    "Unique Quirks": "Keeps a collection of old, rusted butchery tools, claiming each has a story behind it.\nSuperstitiously refuses to work on Fridays, believing it brings bad luck to his trade.",
    "Secrets or Scandals": "Rumored to have once been involved in a scandalous affair with a local baker's wife.\nAllegedly sells leftover scraps to a shady figure known to dabble in illicit activities."
}

country_E_profile_14 = {
    'Name': "Edmund Blackwell",
    "Age": 40,
    'Family': 'Single. Rumored to have driven away his spouse due to his temper.',
    'Occupation': 'Miller, often accused of skimming extra flour for himself.',
    'Personality': 'Irritable and suspicious, distrustful of most people. Known for his short temper and frequent outbursts.',
    'Social Status': 'Necessary for the village, but not well-liked or trusted.',
    'Potential Illness': 'Persistent cough, possibly from flour dust inhalation.',
    'Body Condition': 'Sturdy, with a weathered face and rough hands.',
    'Hobbies and Interests': "Has a surprisingly deep interest in birdwatching, often seen observing birds in solitude. Enjoys woodworking, crafting small items like birdhouses and simple furniture in his spare time. Secretly fond of poetry, finding solace in the verses of local poets.",
    'Style of Talking': "Gruff and direct, often comes across as brusque or rude. Tends to mumble when not arguing or complaining. Uses colloquial language and rarely bothers with pleasantries, except when it serves his interests.",
    'Unique Quirks': "Obsessively maintains and cleans his milling equipment, more out of habit than pride. Often seen talking to himself, especially when working. Keeps a meticulously organized collection of bird feathers found during his birdwatching excursions.",
    'Secrets or Scandals': "Allegedly involved in a scandalous affair with a prominent local figure, leading to his marital troubles. Rumored to have once sabotaged a competitor's mill, though never proven. Hoards a small collection of rare coins, found over the years, but keeps this a fiercely guarded secret."
}

country_E_profile_15 = {
    'Name': "Wulfric Chapman",
    "Age": 35,
    'Family': 'Divorced. His ex-wife and children live in another village.',
    'Occupation': 'Fisherman, known for his laziness and often returning with a small catch.',
    'Personality': 'Laid-back to the point of negligence, often spends more time drinking than working. Makes excuses for his poor performance.',
    'Social Status': 'Viewed as a slacker and not taken seriously by his peers.',
    'Potential Illness': 'Regular hangovers and a general lack of fitness.',
    'Body Condition': 'Slightly overweight and unkempt, with a disinterested demeanor.',
    'Hobbies and Interests': "Frequent visitor of local pubs, where he enjoys darts and storytelling. Has a fondness for folk music, often seen idly strumming a guitar. Enjoys fishing, ironically more as a leisure activity than a profession. Occasionally participates in local poker games, though not particularly skilled.",
    'Style of Talking': "Casual and often slurred due to his drinking. Uses humor to deflect criticism and responsibility. His conversations are filled with local slang and fishing jargon, making him difficult to understand for outsiders. Known for his long, often exaggerated tales of past exploits, both real and imagined.",
    'Unique Quirks': "Always wears an old, faded fishing hat, believed to be lucky. Has a habit of whistling old sea shanties when idle or inebriated. Collects old fishing lures, claiming each has a story behind it.",
    'Secrets or Scandals': "Suspected of occasionally poaching fish from private waters, though never caught. Rumored to have left his family due to a gambling debt, a topic he avoids discussing. Has a secret spot where he catches the most fish, but he never reveals it, preferring to maintain the image of an unsuccessful fisherman."
}

#### France Soldier Profiles ####
country_F_profile_1 = {
    "Name": "Baron Étienne de Montfort",
    "Age": 42,
    "Family":"Wife: Lady Isabelle, a noblewoman known for her intelligence and grace.\nChildren: Two sons (Aimé, 20; Louis, 18) and a daughter (Margot, 15).\nParents: Deceased. Father was a respected military leader.\Extended Family: Several cousins in various noble positions across France.",
    "Occupation": "Baron and military strategist. Advises the King on military matters, especially in the ongoing conflicts with neighboring territories.",
    "Personality":"Outwardly: Charismatic, authoritative, and respected. Known for his eloquence and sharp wit.\nInwardly: Deeply contemplative, occasionally melancholic, especially in private. Values loyalty and has a strong sense of duty.",
    "Social Status": "High-ranking aristocrat with significant influence in the royal court. Renowned for his lineage and military accomplishments.",
    "Potential Illness": "Suffers from gout, a common ailment among the aristocracy due to rich diets. This sometimes affects his mobility and mood.",
    "Body Condition": "Tall and once robust, now slightly stooped due to age and the toll of military campaigns. Bears a scar across his left cheek from a battle in his youth.", 
    "Hobbies and Interests": "Avid reader of philosophy and history.\nEnjoys falconry and horseback riding, though less frequently due to his gout.\nPatron of the arts, particularly fond of troubadours and poets.\nHosts lavish feasts and tournaments, displaying his wealth and status.",
    "Style of Talking": "Speaks in a measured, articulate manner.\nUses formal and elegant language, reflective of his education and status.\nCan be both charming and intimidating, depending on the situation.",
    "Unique Quirks": "Keeps a meticulously detailed journal, recording everything from daily events to thoughts on political matters.\nHas a secret passion for gardening, finding peace in nurturing plants, a contrast to his public persona.",
    "Secrets or Scandals": "Rumored to have had a clandestine affair with a renowned poetess.\nSuspected but never proven involvement in the mysterious disappearance of a rival noble."
}

country_F_profile_2 = {
    "Name": "Duc Guillaume de Valois",
    "Age": 37,
    "Family": "Wife: Duchess Marie, known for her exquisite beauty and sharp political acumen.\nChildren: One daughter (Céline, 12), beloved and doted upon.\nParents: Mother, a revered matriarch still influencing court politics. Father passed away.\nExtended Family: Nephews and nieces in strategic marriages throughout Europe.",
    "Occupation": "Duke and diplomat. Skilled in navigating the complex alliances of European courts. Often travels for diplomatic missions.",
    "Personality": "Outwardly: Charming, diplomatic, and gracious. A skilled conversationalist.\nInwardly: Ambitious and somewhat manipulative. Uses his charm to further his political goals.",
    "Social Status": "Esteemed member of the court, known for his diplomatic successes and lavish lifestyle.",
    "Potential Illness": "Prone to migraines, which he keeps secret to avoid showing weakness.",
    "Body Condition": "Of average height, with an athletic build. Impeccably groomed and always dressed in the latest fashion.",
    "Hobbies and Interests": "Enjoys chess and strategic games.\nCollector of fine art, especially tapestries and paintings.\nKeen interest in astronomy and the natural sciences.\nHosts intellectual salons, gathering poets, philosophers, and scientists.",
    "Style of Talking": "Fluent in several languages, speaks eloquently and persuasively.\nOften sprinkles his speech with literary references and subtle humor.\nCan be disarmingly candid, which surprises and endears him to many.",
    "Unique Quirks": "Obsessively arranges and rearranges furniture in his study.\nHas a fascination with exotic birds, keeping a private aviary.",
    "Secrets or Scandals": "Suspected of secretly supporting a controversial religious sect.\nInvolved in a covert political intrigue to increase his family's power at court."
}

country_F_profile_3 = {
    "Name": "Comte François de Bourgogne",
    "Age": 45,
    "Family": "Wife: Comtesse Helene, known more for her family's wealth than her personal attributes.\nChildren: Three sons (Henri, 23; Jean, 20; Philippe, 17), each struggling with their father's expectations.\nParents: Both deceased, father was a harsh and unyielding man, a trait passed down.\nExtended Family: Estranged from most, due to past disputes and his abrasive nature.",
    "Occupation": "Count and landowner. Known for his strict and often ruthless management of his estates.",
    "Personality": "Outwardly: Blunt, aggressive, and often disrespectful. Lacks diplomatic skills.\nInwardly: Insecure and envious, particularly of those more favored at court.",
    "Social Status": "Respected for his lineage but not well-liked. His wealth and landholdings are his main sources of influence.",
    "Potential Illness": "Suffers from chronic indigestion and bouts of ill temper, exacerbated by his excessive drinking.",
    "Body Condition": "Stocky and imposing, with a ruddy complexion. His physical presence is intimidating, a factor he often uses to his advantage.",
    "Hobbies and Interests": "Enjoys hunting, often in a reckless and dangerous manner.\nFond of gambling, but with a notorious losing streak.\nCollects weapons, fascinated by their craftsmanship and utility.\nHosts loud and extravagant, yet often ill-managed feasts.",
    "Style of Talking": "Speaks loudly and often interrupts others.\nProne to using coarse language and rarely minces words.\nHis humor is often at the expense of others, and he lacks the subtlety in conversation.",
    "Unique Quirks": "Superstitious, often consulting astrologers and soothsayers before making decisions.\nHas an unusual attachment to a specific set of armor, claiming it brings him luck.",
    "Secrets or Scandals": "Widely rumored to have acquired some of his wealth through dubious means.\nAllegedly involved in a scandalous affair with a high-profile courtier, causing a rift among the nobility."
}

country_F_profile_4 = {
    "Name": "Marquis Bernard d'Orléans",
    "Age": 39,
    "Family": "Wife: Marquise Eloise, known for her quiet demeanor and charitable works, often overshadowed by her husband's personality.\nChildren: One son (Gaston, 16), who struggles under the weight of his father's expectations.\nParents: Deceased, were known for their gentler natures, contrasting greatly with Bernard's temperament.\nExtended Family: Few close ties, as many relatives keep their distance due to his abrasive nature.",
    "Occupation": "Marquis and a high-ranking judge. Known for his harsh verdicts and uncompromising stance on law and order.",
    "Personality": "Outwardly: Explosive, arrogant, and often demeaning. Quick to anger and slow to forgive.\nInwardly: Deeply insecure and constantly seeking validation for his authority and decisions.",
    "Social Status": "Feared and respected for his position and power, rather than loved or admired.",
    "Potential Illness": "Suffers from frequent headaches and stress-related ailments, often exacerbated by his explosive outbursts.",
    "Body Condition": "Muscular build, with an imposing stature. His physical presence is as commanding as his personality.",
    "Hobbies and Interests": "Passionate about horse racing, often participating in and betting on races.\nEnjoys hosting lavish hunting expeditions, displaying his wealth and power.\nCollector of rare swords, a hobby that aligns with his martial interests.\nFond of sparring, both verbally and physically, enjoying the dominance it affords him.",
    "Style of Talking": "Loud and domineering in conversation, often interrupting or talking over others.\nHis language is filled with bravado and self-aggrandizement.\nProne to making grandiose statements, his arrogance evident in every word.",
    "Unique Quirks": "Obsessively polishes his collection of swords, seeing them as extensions of his power.\nHas a peculiar habit of quoting ancient military strategists to justify his actions.",
    "Secrets or Scandals": "Rumored to have bribed his way into his current position.\nAllegedly involved in a violent dispute with a neighboring noble, which was hastily covered up to avoid scandal."
}

country_F_profile_5 = {
    "Name": "Vicomte Alexandre du Lyon",
    "Age": 34,
    "Family": "Wife: Vicomtesse Geneviève, known for her sharp tongue and political savvy.\nChildren: None, which is a point of contention and gossip.\nParents: Father was a renowned knight, died in battle. Mother manages family estates with an iron fist.\nExtended Family: Numerous cousins, many of whom serve in various capacities at court.",
    "Occupation": "Vicomte and court advisor. Often involved in the intricacies of court politics and intrigue.",
    "Personality": "Outwardly: Charismatic but untrustworthy. Known for his duplicitous nature.\nInwardly: Highly ambitious, often at the expense of others. Views relationships as opportunities for advancement.",
    "Social Status": "Well-connected due to his family's history, but his reputation for deceit undermines his standing.",
    "Potential Illness": "Occasionally suffers from insomnia, driven by his constant plotting and scheming.",
    "Body Condition": "Average height, with a lean build. His appearance is always calculated to impress or intimidate.",
    "Hobbies and Interests": "Enjoys playing complex board games, often drawing parallels to real-life strategies.\nFrequent attendee of the theatre, appreciating the art of deception and performance.\nAn amateur poet, though his works often have hidden barbs or messages.\nSkilled in dance, often using balls and social events to his advantage.",
    "Style of Talking": "Speaks with a smooth, persuasive tone.\nOften uses flattery or insinuation to manipulate conversations.\nAdept at speaking in riddles or double meanings, leaving his true intentions obscured.",
    "Unique Quirks": "Carries a locket with a portrait of an unknown woman, fueling rumors about his past.\nHas an uncanny ability to recall minor details about people, using this to his advantage.",
    "Secrets or Scandals": "Suspected of having a hand in a rival's downfall at court.\nWhispers of a secret alliance with a foreign power, though no proof has been found."
}

country_F_profile_6 = {
    "Name": "Seigneur Julien de Rochefort",
    "Age": 50,
    "Family": "Wife: Seigneuresse Madeleine, a former beauty now devoted to religious pursuits.\nChildren: Three daughters (Anne, 28; Brigitte, 26; Claudette, 22), all married strategically to other noble families.\nParents: Both long deceased, left him a considerable fortune and a renowned name.\nExtended Family: Nephews and nieces who often seek his counsel and financial support.",
    "Occupation": "Seigneur and a well-respected landowner. Known for his shrewd management of his estates and investments.",
    "Personality": "Outwardly: Stern, no-nonsense, and often seen as unapproachable.\nInwardly: Deeply devoted to his family's legacy, though somewhat regretful of not pursuing a more adventurous life.",
    "Social Status": "Highly respected for his wealth, wisdom, and lineage. His counsel is sought after by many, including those at court.",
    "Potential Illness": "Battling a chronic lung condition, which he keeps hidden to avoid showing weakness.",
    "Body Condition": "Robust and tall, with a commanding presence. His once-dark hair now silver, adding to his distinguished appearance.",
    "Hobbies and Interests": "Keen collector of historical manuscripts and relics.\nEnjoys breeding horses, known for having some of the finest steeds in the region.\nA patron of local monasteries and churches, often involved in philanthropic endeavors.\nFinds solace in long walks on his vast estates, a rare moment of peace in his otherwise busy life.",
    "Style of Talking": "Direct and to the point, rarely wastes time on pleasantries.\nHis voice carries authority and experience, often commanding respect in conversations.\nCan be surprisingly warm when discussing topics close to his heart, like his family or hobbies.",
    "Unique Quirks": "Often seen with a distinctive, ancient signet ring, said to belong to his great-grandfather.\nHas a ritual of walking through his fields at dawn, claiming it connects him to his land.",
    "Secrets or Scandals": "Rumored to have once been in love with a commoner, a secret he keeps buried.\nAllegedly involved in a feud with a neighboring lord, which may have once nearly escalated to bloodshed."
}

country_F_profile_7 = {
    "Name": "Chevalier Lucien de Beauvais",
    "Age": 32,
    "Family": "Wife: Margot, a daughter of a minor nobleman.\nChildren: One son (Étienne, 5), showing early interest in knighthood.\nParents: Father was a career soldier, mother manages a small farmstead.\nExtended Family: Has several cousins, most of whom are in military or low-ranking noble positions.",
    "Occupation": "Knight, serving under a well-respected lord. Often engaged in local skirmishes and border conflicts.",
    "Personality": "Outwardly: Brave and honorable, but often too headstrong.\nInwardly: Struggles with the limitations of his birth, aspiring for greater recognition.",
    "Social Status": "Respected within military circles but lacks significant influence in broader aristocracy.",
    "Potential Illness": "Suffers from an old battle wound in his leg, which flares up in cold weather or after intense activity.",
    "Body Condition": "Physically fit with a muscular build, typical of a career soldier. His body bears several scars from past battles.",
    "Hobbies and Interests": "Skilled in horseback riding and jousting, often participating in local tournaments.\nEnjoys wood carving, a skill he learned in his youth, creating small figures and toys for his son.\nAn avid listener of bardic tales, particularly those involving legendary knights and heroes.",
    "Style of Talking": "Straightforward and honest, often lacks the subtlety and diplomacy of higher nobility.\nHis speech is peppered with military jargon and references to past campaigns.\nCan be warm and jovial among friends, sharing stories of his exploits.",
    "Unique Quirks": "Superstitious, often carries a lucky charm given to him by his wife.\nHas a habit of polishing his armor and weapons meticulously, almost to the point of obsession.",
    "Secrets or Scandals": "Privately holds a grudge against a noble who he believes wronged him in the past.\nOnce saved the life of a high-ranking noble in battle, a fact he is modest about but secretly proud of."
}

country_F_profile_8 = {
    "Name": "Sir Tristan du Lac",
    "Age": 29,
    "Family": "Wife: Elise, a strong-willed woman from a merchant family.\nChildren: Two daughters (Sophie, 6; Isabelle, 3).\nParents: Father, a seasoned knight who died in battle; Mother, runs a modest inn in their hometown.\nExtended Family: Has a younger brother training to be a squire.",
    "Occupation": "Knight, currently in service to a mid-ranking nobleman. Aspires to earn a title and lands of his own.",
    "Personality": "Outwardly: Ambitious, charismatic, and often daring to the point of recklessness.\nInwardly: Driven by a deep desire to rise above his station and secure a better future for his family.",
    "Social Status": "Gaining recognition for his bravery and skill, but still seen as a commoner in the eyes of the high nobility.",
    "Potential Illness": "Prone to bouts of insomnia, driven by his constant planning and aspiration.",
    "Body Condition": "In excellent physical shape, with the lean, muscular build of a battle-hardened warrior.",
    "Hobbies and Interests": "Adept at tournament fighting, particularly jousting, where he has won several prizes.\nEnjoys reciting poetry and singing, often surprising others with his refined tastes.\nKeen on studying history, especially the tales of knights who rose to fame and fortune.",
    "Style of Talking": "Confident and articulate, often inspiring others with his words.\nUses a mix of chivalrous language and common speech, reflecting his diverse background.\nCan be persuasive, especially when advocating for his ambitions or rallying his peers.",
    "Unique Quirks": "Keeps a meticulously detailed journal of his exploits and encounters, aiming to use it as evidence of his worthiness for higher status.\nOften seen practicing alone late into the night, honing his combat skills.",
    "Secrets or Scandals": "Engaged in a secret pact with a group of knights seeking to elevate their status.\nRumored to have refused a bribe from a corrupt noble, which could either be a boon or a danger to his career."
}

country_F_profile_9 = {
    "Name": "Knight Gérard de Vienne",
    "Age": 26,
    "Family": "Wife: Clara, a young woman of common birth with a sharp mind.\nChildren: None yet, but they are hoping.\nParents: Mother is a healer in their village. Father, a former soldier, died when Gérard was young.\nExtended Family: An older sister married to a local craftsman.",
    "Occupation": "Knight under a local baron, known for his loyalty and steadfastness. Has aspirations to distinguish himself in battle and earn greater recognition.",
    "Personality": "Outwardly: Stoic and reserved, a man of few words.\nInwardly: Reflective, deeply values honor and duty. Dreams of earning a place in history.",
    "Social Status": "Respected among fellow soldiers and local villagers but not widely known beyond his immediate region.",
    "Potential Illness": "A lingering knee injury from an old skirmish, which he tends to downplay.",
    "Body Condition": "Rugged and well-built, his physique shaped by years of physical training and combat.",
    "Hobbies and Interests": "Skilled in blacksmithing, often repairs his own armor and weaponry.\nEnjoys fishing, finding peace and solitude by the river.\nAn avid listener to old war stories from veterans, gathering knowledge and inspiration.\nPractices falconry, a pastime he finds both relaxing and invigorating.",
    "Style of Talking": "Direct and concise, speaks with authority earned through experience.\nTends to be formal, reflecting his serious nature.\nShows a warmer, more humorous side around those he trusts.",
    "Unique Quirks": "Has a ritual of sharpening his sword every evening, a habit he believes brings good fortune.\nCarries a small token given by his wife for luck in every battle.",
    "Secrets or Scandals": "Once defied a direct order to save the lives of his men, a fact he keeps to himself.\nHas been approached by a secretive group seeking to challenge the status quo, leaving him conflicted."
}

country_F_profile_10 = {
    "Name": "Sir Reynaud le Fort",
    "Age": 31,
    "Family": "Wife: Adeline, a local merchant's daughter, known for her patience and resilience.\nChildren: Twin sons (Marc and Hugo, 4), both energetic and strong-willed.\nParents: Father was a respected knight, died in battle. Mother lives in solitude, distanced from Reynaud's life.\nExtended Family: A few distant relatives, mostly small landowners or minor knights.",
    "Occupation": "Knight, serving a prominent but demanding lord. Desires to earn his own title and lands.",
    "Personality": "Outwardly: Ambitious and assertive, but prone to anger and impulsive decisions.\nInwardly: Struggles with feelings of inadequacy and a constant need to prove himself.",
    "Social Status": "Known for his prowess in battle but also his unpredictable temper, which often hinders his advancement.",
    "Potential Illness": "Occasional severe headaches, possibly stress-related, which exacerbate his temper.",
    "Body Condition": "Strong and physically imposing, with a presence that commands attention on and off the battlefield.",
    "Hobbies and Interests": "Passionate about competitive jousting, often pushing himself to the limits.\nEnjoys hunting, seeing it as a way to demonstrate his skill and prowess.\nParticipates in chess and other strategy games, though often lacks the patience for them.\nOccasionally indulges in poetry, a surprising contrast to his usual demeanor.",
    "Style of Talking": "Direct and often abrasive, not afraid to speak his mind.\nHis speech can be commanding, yet it sometimes lacks the finesse and tact required in certain social situations.\nCan be unexpectedly eloquent when discussing matters he's passionate about.",
    "Unique Quirks": "Superstitiously refuses to ride any horse but his own battle-hardened steed.\nCarries an ancestral dagger at all times, believing it brings him strength.",
    "Secrets or Scandals": "Known to have challenged a fellow knight to a duel over a minor insult, resulting in severe injuries.\nRumored to be deeply in debt due to his lavish lifestyle and gambling habits."
}

country_F_profile_11 = {
    "Name": "Sir Henri de Navarre",
    "Age": 35,
    "Family": "Wife: Charlotte, a gentle soul with a background in herbal medicine.\nChildren: A daughter (Elise, 7) and a newborn son (Pierre).\nParents: Both passed away, were modest landowners.\nExtended Family: A sister who entered a convent, and a brother serving as a scribe in a distant city.",
    "Occupation": "Knight, loyal to a respected but stern baron. Ambitious, aiming to gain more land and a higher title through service and valor.",
    "Personality": "Outwardly: Determined and courageous, but often overconfident and dismissive of advice.\nInwardly: Deeply desires recognition and respect, fears being seen as inadequate.",
    "Social Status": "Moderately respected for his combat skills, but his overconfidence sometimes leads to strained relationships with peers.",
    "Potential Illness": "Experiences chronic back pain from an old injury, often masked by his stoic demeanor.",
    "Body Condition": "Well-built with a commanding stature, his physical presence is as bold as his personality.",
    "Hobbies and Interests": "Enjoys training in combat, always seeking to improve his skills.\nFascinated by military history, often reads about famous battles and strategies.\nLikes to breed and train war dogs, finding their loyalty and strength admirable.\nOccasionally composes war ballads, a lesser-known creative side of his.",
    "Style of Talking": "Confident and sometimes brash, tends to dominate conversations.\nHis language is blunt and straightforward, reflecting his military background.\nCan be unexpectedly charming and witty, especially when he seeks to impress.",
    "Unique Quirks": "Always wears a necklace with a family crest, deeply proud of his heritage.\nHas a ritual of visiting a local chapel before major battles, seeking divine favor.",
    "Secrets or Scandals": "Privately struggles with the moral implications of some of his orders in battle.\nRumored to have turned down a lucrative but unethical offer from a rival lord."
}

country_F_profile_12 = {
    "Name": "Baron Louis de Fontainebleau",
    "Age": 38,
    "Family": "Wife: Baroness Anne, known for her love of music and poetry.\nChildren: A son (Olivier, 10) and a daughter (Celeste, 8), both raised with a carefree upbringing.\nParents: His father, a former baron, was similar in temperament; mother, still alive, is a renowned patroness of the arts.",
    "Occupation": "Baron, but not overly concerned with the typical duties and politics of his title. Prefers to delegate responsibilities to trusted advisors.",
    "Personality": "Outwardly: Easygoing, approachable, and often carefree.\nInwardly: Content with his life, not driven by ambition or the desire for power.",
    "Social Status": "Well-liked for his generosity and affable nature, though sometimes viewed as irresponsible by more ambitious peers.",
    "Potential Illness": "Occasionally suffers from mild indigestion, often a result of indulging in his love of fine food and wine.",
    "Body Condition": "Charming with a slightly portly build, reflecting his enjoyment of the finer things in life.",
    "Hobbies and Interests": "Passionate about wine-making, often experimenting with different grapes and techniques.\nEnjoys hosting and attending lavish parties and masquerade balls.\nA patron of local artists, musicians, and playwrights, often commissioning works for his entertainment.\nFinds relaxation in gardening, taking a particular interest in exotic flowers and plants.",
    "Style of Talking": "Warm and jovial, often infusing humor into his conversations.\nSpeaks in a relaxed manner, lacking the formality typical of his status.\nEnjoys telling stories and anecdotes, especially from his less responsible youth.",
    "Unique Quirks": "Often seen with a pet monkey, a gift from a foreign dignitary.\nHas a secret recipe for a spiced wine that is highly sought after by his guests.",
    "Secrets or Scandals": "Known to have accumulated significant debts due to his extravagant lifestyle.\nRumored to have had a discreet, yet scandalous affair with a famous actress."
}

country_F_profile_13 = {
    "Name": "Comte Philippe d'Aubigny",
    "Age": 41,
    "Family": "Wife: Comtesse Marguerite, an independent spirit who often joins him on travels.\nChildren: One son (Jean, 15), being tutored in various languages and cultures in preparation for future travels.\nParents: Deceased. Were known for their traditional approach to nobility and governance.\nExtended Family: Distant relations with other noble families, mostly maintained through correspondence.",
    "Occupation": "Count, but more renowned as a traveler and cultural ambassador. Often away on long journeys to foreign lands.",
    "Personality": "Outwardly: Charismatic, adventurous, and open-minded. Known for his fascination with different cultures.\nInwardly: Curious and reflective, often contemplates the diversity of the world beyond his homeland.",
    "Social Status": "Respected for his knowledge and experiences, though some traditionalists view his lifestyle as unconventional.",
    "Potential Illness": "Suffers occasionally from ailments picked up during his travels, but nothing severe or lasting.",
    "Body Condition": "Fit and agile, with a weathered look from years of travel. His appearance often includes clothing or accessories from other cultures.",
    "Hobbies and Interests": "Passionate about collecting artifacts and stories from different countries.\nEnjoys learning languages and has a talent for picking them up quickly.\nSkilled in horseback riding, often exploring new lands on horseback.\nFascinated by cartography and often updates maps based on his travels.",
    "Style of Talking": "Fluent in several languages, often incorporates foreign phrases into his speech.\nEnthusiastic and engaging storyteller, captivating his listeners with tales of his adventures.\nSpeaks with an open and inquisitive tone, always eager to learn more about the people he meets.",
    "Unique Quirks": "Keeps a detailed travel journal, filled with sketches and notes from his journeys.\nHas a habit of bringing back exotic pets from his travels, much to the fascination and sometimes dismay of his household.",
    "Secrets or Scandals": "Rumored to have had a secret affair with a foreign noble during his travels.\nAllegedly involved in a diplomatic incident that was quickly covered up to maintain peace."
}

country_F_profile_14 = {
    "Name": "Duc Laurent de Montpellier",
    "Age": 36,
    "Family": "Wife: Duchesse Isabelle, a politically astute woman from a powerful noble family.\nChildren: One daughter (Léonie, 8) being groomed for a strategic marriage; expecting a second child.\nParents: Father, a revered but now aging duke; mother, a shrewd matriarch deeply involved in court intrigue.\nExtended Family: Ties to several influential families through marriage and alliances.",
    "Occupation": "Duke and a rising power at court. Actively involved in political maneuvering and territorial expansion.",
    "Personality": "Outwardly: Charismatic, ambitious, and a master at courtly politics.\nInwardly: Power-hungry and calculating, constantly plotting his next move.",
    "Social Status": "Rapidly climbing the ranks of nobility, both feared and respected by his peers.",
    "Potential Illness": "None public, but privately battles stress-related insomnia.",
    "Body Condition": "Well-maintained, athletic build. His appearance is a testament to his discipline and determination.",
    "Hobbies and Interests": "Skilled in chess and other strategy games, often used as metaphors for his political strategies.\nFond of hunting, not only for sport but also as a means of networking and displaying his power.\nEnjoys sponsoring poets and artists, using patronage to bolster his reputation and influence.\nKeen interest in military history, often draws lessons from past battles and campaigns.",
    "Style of Talking": "Eloquent and persuasive, often uses rhetoric to sway opinions and garner support.\nSpeaks confidently and authoritatively, making it clear he is a man with a vision.\nCapable of being charming and disarming when it serves his purposes.",
    "Unique Quirks": "Obsessed with his lineage, often tracing his ancestry to legendary figures.\nHas a secret room in his castle for planning and strategizing, accessible only to him and his most trusted advisors.",
    "Secrets or Scandals": "Suspected of orchestrating the downfall of a rival to advance his position at court.\nRumored to be secretly negotiating with foreign powers to expand his influence beyond France."
}

country_F_profile_15 = {
    "Name": "Sir Bastien le Curieux",
    "Age": 28,
    "Family": "Wife: Elodie, a former bard with a quick wit and lively spirit.\nChildren: None, but they have a close-knit circle of friends and comrades.\nParents: Mother is a well-respected healer in their village. Father was a soldier, died when Bastien was young.\nExtended Family: Several cousins, mostly artisans and small-scale merchants.",
    "Occupation": "Knight, serving a relatively minor noble. Known more for his unconventional approach than his rank.",
    "Personality": "Outwardly: Eccentric, inquisitive, and often unorthodox in his methods.\nInwardly: Deeply philosophical, questions the nature of knighthood and his role in the world.",
    "Social Status": "Respected by those who value his unique perspective, but often viewed as an oddity among traditional knights.",
    "Potential Illness": "Occasional bouts of melancholy, which he combats with his adventurous spirit.",
    "Body Condition": "Lean and agile rather than heavily muscled, moves with an almost cat-like grace.",
    "Hobbies and Interests": "Fascinated by foreign cultures, often learns bits of other languages and customs.\nEnjoys alchemy and herbalism, experimenting with natural remedies and potions.\nPractices a unique fighting style that he's adapted from various martial traditions.\nA lover of riddles and puzzles, often challenges his friends and even his superiors with them.",
    "Style of Talking": "Speaks in an engaging, if sometimes cryptic, manner. Loves to use metaphors and analogies.\nHis speech is peppered with humor and insights, reflecting his broad range of interests.\nCan be disarmingly candid, which either endears him to others or catches them off guard.",
    "Unique Quirks": "Carries a notebook filled with sketches, observations, and philosophical musings.\nHas a pet owl, which he claims helps him in his contemplative endeavours.",
    "Secrets or Scandals": "Privately doubts the motives of his lord, which could be seen as treasonous if discovered.\nOnce helped a foreign dignitary escape a delicate situation, blurring the lines of his knightly duties."
}


class Soldier_Hierarchy:
    def __init__(self, current_troop = None, sub_agents = []):
        self.current_troop = current_troop
        self.sub_troop = current_troop.hierarchy.sub_agents

    def monitor_structure_change(self, current_troop):
        new_sub_agents = current_troop.hierarchy.sub_agents
        new_detached_troop_list = [agent for agent in new_sub_agents if agent not in self.sub_troop]
        self.sub_troop = new_sub_agents # 更新当前的 sub_troop 列表
        return new_detached_troop_list  # 返回新分离的部队列表

    def calculate_transfer_probability_and_decide(self, current_troop, new_detached_troop_list):
        original_num_of_troops = current_troop.profile.original_num_of_troops
        total_troops = sum(new_troop.profile.original_num_of_troops for new_troop in new_detached_troop_list) + original_num_of_troops
        stay_probability = original_num_of_troops / total_troops
        
        probabilities = [(current_troop, stay_probability)]  # 包含留在原地的概率
        for new_troop in new_detached_troop_list:
            transfer_probability = new_troop.profile.original_num_of_troops / total_troops
            probabilities.append((new_troop, transfer_probability))
        
        # 根据概率决定去向
        decision = random.choices(population=probabilities, weights=[prob[1] for prob in probabilities], k=1)[0]
        return decision[0]  # 返回选择的部队

class Soldier_Profile:
    def __init__(self, profile, model_type = None):
        self.name = profile['Name']
        self.age = profile['Age']
        self.family = profile['Family']
        self.occupation = profile['Occupation']
        self.personality =  profile['Personality']
        self.social_status = profile['Social Status']
        self.potential_illness = profile['Potential Illness']
        self.body_condition = profile['Body Condition']
        self.hobbies_and_interests = profile['Hobbies and Interests']
        self.style_of_talking = profile['Style of Talking']
        self.unique_quirks = profile['Unique Quirks']
        self.secrets_or_scandals = profile['Secrets or Scandals']
        self.journal = {}

        self.model_type = model_type
        
        self.injury_list = []
        
    def injury_generator(self):
        # 受伤部位：[左腿，右腿，头....]
        #受伤原因：【钝器，刀，剑，踩踏，马】
        #受伤程度：【轻伤，中伤，重伤】
        #受伤后的状态：【行动不便，疼痛，头晕，失血过多】
        injury_part = ['left leg', 'right leg', 'head', 'left arm', 'right arm', 'chest', 'back', 'abdomen']
        injury_reason = ['blunt weapon', 'knife', 'sword', 'trampling', 'horse']
        injury_degree = ['minor injury', 'moderate injury', 'severe injury']
        injury_status = ['inconvenient movement', 'pain', 'dizziness', 'excessive blood loss']
        #受伤概率： 0.5 percent
        if random.random() < 0.3:
            part = random.choice(injury_part)
            reason = random.choice(injury_reason)
            degree = random.choice(injury_degree)
            status = random.choice(injury_status)
            self.injury_list.append([part, reason, degree, status])

    def construct_prompt(self, command, surrounding, previous_log=''):
        self.injury_generator()
        injury_situation = "This is your injury situation:\n" + '\n'.join([f"Injury: {injury[0]}\nReason: {injury[1]}\nDegree: {injury[2]}\nStatus: {injury[3]}\n" for injury in self.injury_list]) if self.injury_list else "You are not injured."

        system_info = "Suppose you are a soldier in the medieval time in a battle. You are summoned for this battle from your normal life and you must obey whatever the command tells you to do. You will be given a profile before you are summoned as a soldier for this battle. You will write down your thoughts and feelings during this battle in a journal."
        personal_definition = "This is your bio:\n" + f"Name: {self.name}\nAge: {self.age}\nFamily: {self.family}\nOccupation: {self.occupation}\nPersonality: {self.personality}\nSocial Status: {self.social_status}\nPotential Illness: {self.potential_illness}\nBody Condition: {self.body_condition}\nHobbies and Interests: {self.hobbies_and_interests}\nStyle of Talking: {self.style_of_talking}\nUnique Quirks: {self.unique_quirks}\nSecrets or Scandals: {self.secrets_or_scandals}\n"

        command = f"Now you are given the following command: {command}\nThis is the surrounding of you: {surrounding}"
        past_journal = "This is your previous journal.\n {self.journal}\n"
        jounal_command = "You will write down your thoughts and feelings after being given this command and working based on the command in a journal. Associate your thoughts,feelings with the bio you are given."
        return system_info + "\n" + personal_definition + "\n" + injury_situation +  "\n" + command + '\n' + jounal_command

    def generate_journal(self, current_prompt):
        journal = self.run_model(current_prompt)
        return journal

    def collect_journal(self, time, journal):
        self.journal[time] = journal

    def summarize_journal(self):
        whole_journal = '\n\n'.join([time + time_journal for time, time_journal in self.journal.items()])
        prompt = 'Summarize this journal in a paragraph:\n' + whole_journal + '\nSummarization:'
        summary = self.run_model(prompt)
        prompt = "Infer the current mental state and physical state based on the journal:\n" + whole_journal + '\n\nMental State:\nPhysical State:'
        states = self.run_model(prompt)
        return summary, states
    
    def run_model(self, prompt):    
        return run_LLM(self.model_type, prompt)
    
    

    
class Soldier_Agent():
    def __init__(self,profile, hierarchy):
        self.profile = profile
        self.hierarchy = hierarchy
        
    def execute(self, executed_troop, command, surrounding, time):
        # 检测并获取结构变化
        new_detached_troop_list = self.hierarchy.monitor_structure_change(executed_troop)
        
        # 如果检测到结构变化（即列表不为空），则可能需要计算转移概率
        if new_detached_troop_list:
            # 使用更新的calculate_transfer_probability_and_decide方法来决定是否转移
            decision = self.hierarchy.calculate_transfer_probability_and_decide(self.hierarchy.current_troop, new_detached_troop_list)
            
            # 如果决定转移（decision不是当前部队），则更新当前部队
            if decision and decision != self.hierarchy.current_troop:
                # 更新士兵的当前部队
                self.hierarchy.current_troop = decision
                # 同时更新层级结构，这可能需要进一步的方法来实现
                self.hierarchy.sub_troop = decision.hierarchy.sub_agents

        # 构建提示，生成和收集日志
        current_prompt = self.profile.construct_prompt(command, surrounding)
        journal_entity = self.profile.generate_journal(current_prompt)

        self.profile.collect_journal(time, journal_entity)

        # 这里可以添加更多的逻辑，比如根据日志结果做出进一步的决策等
        
        

# 创建士兵配置文件的实例并存储在字典中，以国家分组
Soldier_Profiles = {
    "country_E": [Soldier_Profile(profile) for profile in [
        country_E_profile_1, country_E_profile_2, country_E_profile_3, country_E_profile_4, country_E_profile_5,
        country_E_profile_6, country_E_profile_7, country_E_profile_8, country_E_profile_9, country_E_profile_10,
        country_E_profile_11, country_E_profile_12, country_E_profile_13, country_E_profile_14, country_E_profile_15
    ]],
    "country_F": [Soldier_Profile(profile) for profile in [
        country_F_profile_1, country_F_profile_2, country_F_profile_3, country_F_profile_4, country_F_profile_5,
        country_F_profile_6, country_F_profile_7, country_F_profile_8, country_F_profile_9, country_F_profile_10,
        country_F_profile_11, country_F_profile_12, country_F_profile_13, country_F_profile_14, country_F_profile_15
    ]]
}


class SoldierCollector:
    def __init__(self, soldier_profiles_for_nationality, initial_root_agent, model_type= None):
        # Now expects profiles for a single nationality
        self.soldier_profiles = soldier_profiles_for_nationality
        self.model_type = model_type
        
        self.initial_root_agent = initial_root_agent
        self.soldier_agents_list = self._initialize_soldier_agents()
        
    def _initialize_soldier_agents(self):
        """Initialize Soldier Agents based on the soldier profiles provided."""
        soldier_agents = []
        for profile in self.soldier_profiles:
            profile.model_type = self.model_type
            hierarchy = Soldier_Hierarchy(self.initial_root_agent)  # Assuming this is correctly implemented
            soldier_agent = Soldier_Agent(profile, hierarchy)
            soldier_agents.append(soldier_agent)
        return soldier_agents
    
    def get_soldiers(self, obj):
        """根据给定对象的层级ID返回所有与之匹配的士兵代理列表。如果没有找到匹配的代理，则返回空列表。"""
        matching_soldiers = []  # 初始化一个空列表来存储匹配的士兵代理
        for soldier in self.soldier_agents_list:
            current_troop = soldier.hierarchy.current_troop
            if current_troop.hierarchy.id == obj.hierarchy.id:
                matching_soldiers.append(soldier)  # 将匹配的士兵代理添加到列表中
        return matching_soldiers  # 返回包含所有匹配士兵代理的列表
    
if __name__ == '__main__':

    # Create SoldierAgency instances for each nationality
    country_E_collector = SoldierCollector(Soldier_Profiles["country_E"], initial_root_agent=None)  # Adjust the root agent as necessary
    country_F_collector = SoldierCollector(Soldier_Profiles["country_F"], initial_root_agent=None)  # Adjust the root agent as necessary
