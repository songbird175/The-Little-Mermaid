iterations = 3**7
Ucount = 0
Secount = 0
Scount = 0
Ecount = 0
Tcount = 0
Acount = 0

for number in range(0, iterations):
	number += 1

	working_file = open("The_Little_Mermaid_Rewrite_%s" % str(number), "w")

	if number % 3 == 1:
		u2_she = "she"
		u2_She = "She"
		u2_her = "her"
		u2_herm = "her"
		herself = "herself"
		u_girl = "girl"
		Ucount += 1

		if Ucount % 3 == 1:
			u_she = "she"
			u_She = "She"
			u_her = "her"
			witch = "witch"
			Witch = "Witch"
			Ursula = "Ursula"
			Secount += 1

			if Secount % 3 == 1:
				se_he = "she"
				se_his = "her"
				Sebastian = "Sandy"
				Scount += 1

				if Scount % 3 == 1:
					sc_His = "Her"
					sc_he = "she"
					sc_He = "She"
					sc_him = "her"
					sc_his = "her"
					Ecount += 1

					if Ecount % 3 == 1:
						e_His = "Her"
						e_he = "she"
						e_He = "She"
						e_him = "her"
						e_his = "her"
						e_His = "Her"
						man = "woman"
						himself = "herself"
						prince = "princess"
						Prince = "Princess"
						Eric = "Erica"
						Tcount += 1

						if Tcount % 3 == 1:
							t_His = "Her"
							t_he = "she"
							t_He = "She"
							t_him = "her"
							t_his = "her"
							father = "mother"
							Father = "Mother"
							king = "queen"
							King = "Queen"
							Acount += 1

							if Acount % 3 == 1:
								a_she = "she"
								a_She = "She"
								a_her = "her"
								a_herm = "her"
								Her = "Her"
								daughter = "daughter"
								girl = "girl"
								mermaid = "mermaid"
								Mermaid = "Mermaid"
							elif Acount % 3 == 2:
								a_she = "he"
								a_She = "He"
								a_her = "his"
								a_herm = "him"
								Her = "His"
								daughter = "son"
								girl = "boy"
								mermaid = "merman"
								Mermaid = "Merman"
							elif Acount % 3 == 0:
								a_she = "they"
								a_She = "They"
								a_her = "their"
								a_herm = "them"
								Her = "Their"
								daughter = "child"
								girl = "person"
								mermaid = "merperson"
								Mermaid = "Merperson"

						elif Tcount % 3 == 2:
							t_His = "His"
							t_he = "he"
							t_He = "He"
							t_him = "him"
							t_his = "his"
							father = "father"
							Father = "Father"
							king = "king"
							King = "King"
						elif Tcount % 3 == 0:
							t_His = "Their"
							t_he = "they"
							t_He = "They"
							t_him = "them"
							t_his = "their"
							father = "baba"
							Father = "Baba"
							king = ""
							King = ""

						elif Ecount % 3 == 2:
							e_His = "His"
							e_he = "he"
							e_He = "He"
							e_him = "him"
							e_his = "his"
							e_His = "His"
							man = "man"
							himself = "himself"
							prince = "prince"
							Prince = "Prince"
							Eric = "Eric"
						elif Ecount % 3 == 0:
							e_His = "Their"
							e_he = "they"
							e_He = "They"
							e_him = "them"
							e_his = "their"
							e_His = "Their"
							man = "human"
							himself = "theirself"
							prince = "human"
							Prince = ""
							Eric = "Eric"


				elif Scount % 3 == 2:
					sc_His = "His"
					sc_he = "he"
					sc_He = "He"
					sc_him = "him"
					sc_his = "his"
				elif Scount % 3 == 0:
					sc_His = "Their"
					sc_he = "they"
					sc_He = "They"
					sc_him = "them"
					sc_his = "their"

			elif Secount % 3 == 2:
				se_he = "he"
				se_his = "his"
				Sebastian = "Sebastian"
			elif Secount % 3 == 0:
				se_he = "they"
				se_his = "their"
				Sebastian = "Sebastian"

		elif Ucount % 3 == 2:
			u_she = "he"
			u_She = "He"
			u_her = "his"
			witch = "wizard"
			Witch = "Wizard"
			Ursula = "Ursus"
		elif Ucount % 3 == 0:
			u_she = "they"
			u_She = "They"
			u_her = "their"
			witch = "witch"
			Witch = "Witch"
			Ursula = "Ursula"

	elif number % 3 == 2:
		u2_she = "he"
		u2_She = "He"
		u2_her = "his"
		u2_herm = "him"
		herself = "himself"
		u_girl = "boy"
	elif number % 3 == 0:
		u2_she = "they"
		u2_She = "They"
		u2_her = "their"
		u2_herm = "them"
		herself = "theirself"
		u_girl = "human"

	story = ["Far beneath the ocean waves, in the land of the merpeople, lived a lovely young ", mermaid, " named Ariel. ", Her,
	" home was an undersea palace. Although it was quite magnificent, ", a_she, " hardly ever spent time there. ", a_She, " preferred to go exploring with ", a_herm,
	" little friend Flounder, the fish.\nAriel loved to collect objects from the world above the sea. ", a_She,
	" and Flounder would swim in and out of sunken ships, picking up whatever caught the Little ", Mermaid, "\'s fancy.\n\nAriel\'s ", father, ", ", King,
	" Triton, ruled the undersea kingdom. ", t_He, " was very proud of Ariel\'s many gifts, especially ", a_her, " beautiful singing voice. ", t_He,
	" had arranged to give a special concert to show ", t_his, " ", daughter,
	"\'s wonderful talent to all the merfolk.\nAriel\'s sisters sang to begin the concert. Then they sang a special song to introduce Ariel.\nBut Ariel wasn\'t there!\nTriton was not pleased. How could Ariel have forgotten to show up for ",
	a_her, " own debut?\n\nAs usual, Ariel was off exploring. ", a_She, " had found a sunken ship to play in and had forgotten all about the concert. By the time ",
	a_she, " returned home, the guests had left. Triton was so angry that ", t_he, " ordered ", Sebastian, ", a crab who was ", t_his,
	" court composer, to follow Ariel and keep ", a_herm, " out of trouble.\n\nLater that day, Ariel slipped away again, with ", Sebastian,
	" following close behind. ", a_She, " hadn\'t gone far when a huge shadow darkened the waters above.\n\"It\'s a ship!\" ", a_she,
	" gasped with delight.\n\nAriel swam to the surface to get a closer look. There were humans on board! One of them was very handsome. Ariel heard the others call ",
	e_him, " ", Prince, " ", Eric, ".\n\nBut as Ariel watched, a sudden storm took them all by surprise. To ", a_her,
	" horror, the ship began to sink. Most of the people on board were able to climb safely into a lifeboat. But the handsome young ", prince,
	" was hit by a falling spar and thrown into the churning water.\n\nAriel knew that humans could not live under the sea. ", a_She, " had to save the unconscious ",
	prince, ". There was no time to lose!\n\nAriel darted through the waves to the ", prince, " as ", a_her, " friend, Scuttle, watched anxiously.\n\nUsing all ",
	a_her, " strength, Ariel dragged the young ", prince, " to shore. Scuttle was waiting for them. The silly bird put ", sc_his, " ear close to ", Eric,
	"\'s boot!\n\"Sorry, Ariel, I can\'t make out a heartbeat,\" said Scuttle.\n\nAriel placed ", a_her, " head on the ", prince, "\'s chest.\n\"Oh, ", e_he,
	" is breathing, Scuttle!\" ", a_she, " cried.\n", a_She, " was so happy that ", a_she, " began to sing to the ", prince,
	". At the sound of Ariel\'s lovely voice, ", Eric, "\'s eyelids began to flutter.\n\n\"", e_He,
	"\'s going to be all right,\" Ariel said gratefully. \"Now I\'d better get back before ", Father, " finds out I\'ve left.\"\nWhen the ", prince, " opened ",
	e_his, " eyes, all ", e_he, " saw was ", e_his, " faithful dog, Max, running up to ", e_him, ".\n\nAriel returned home, but ", a_she,
	" couldn\'t forget the human ", prince, ". As ", a_she, " sat thinking about ", e_him, ", two evil eels named Flotsam and Jetsam watched ", a_herm,
	" with their cunning eyes.\n\n\"Come with us,\" they coaxed sweetly. \"We know someone who can help you.\"\nAriel followed the slippery eels. Before ",
	a_she, "knew it, they were inside the deep, dark cave of ", Ursula, ", the Sea ", Witch, "!\n\n", Ursula, " knew how much Ariel missed ", Eric, ". ", u_She,
	" told the young ", mermaid, " that ", u_she, " could help ", a_herm, " visit ", e_him, " - for a price!\n\n\"I will make you human so you can visit your young ",
	man, ",\" ", Ursula, " said. \"But you must get ", e_him,
	" to fall in love and kiss you before the sun sets on the third day. If you fail, you will turn back into a ", mermaid,
	" and return to the sea as my slave!\"\nThen ", Ursula, " laughed wickedly. \"Oh, and one other thing. You must leave your voice with me!\"\n\nPoor Ariel! ",
	a_She, " would have done anything to see the young ", prince, " again. So ", a_she, " signed the agreement! Then the evil ", witch,
	" locked Ariel\'s beautiful voice inside a magic seashell that ", u_she, " wore around ", u_her, " neck.\n\nFlounder and ", Sebastian,
	" watched in amazement as ", Ursula, "\'s magic powers changed Ariel into a human ", girl, ". Suddenly Ariel could no longer live underwater. Luckily, ", a_her,
	" two friends rushed ", a_herm, " up to the surface so ", a_she, " could breathe.\n", Ursula, " cackled with glee. ", u_She,
	" intended to make sure Ariel did not get ", a_her,
	" kiss!\n\nOnce Ariel was safe on the beach, Scuttle said, \"There\'s something different about you, Ariel. I just can\'t put my foot on it.\"\nAriel showed ",
	sc_him, " ", a_her, " two legs. ", a_She, " wanted to tell Scuttle about what had happened. But since ", Ursula, " had taken ", a_her, " voice, ", Sebastian,
	" had to explain.\n\nWhen Ariel tried to stand, ", a_she, " found that balancing on ", a_her,
	" new legs was harder than it looked. \"You can do it,\" said Scuttle. \"Just watch me.\"\n", Sebastian, " shook ", se_his,
	" head in disbelief. \"How am I going to tell the ", king, " about this?\" ", se_he, " wondered.\n\nMeanwhile, ", Eric,
	" had not forgotten about the mystery person who had saved ", e_his, " life. Although ", e_he, " hadn\'t seen ", a_herm, ", ", e_he,
	" had fallen in love with ", a_her, " wonderful voice. ", Eric, " would have given ", e_his, " entire kingdom to find ", a_herm, "! Then, as ", e_he,
	" was walking with Max, ", e_he, " saw Ariel on the beach.\n\"Have we met before?\" ", Eric, " asked, ", e_his, " heart skipping a beat. But ", e_his,
	" hopes were soon dashed when ", e_he, " found that Ariel could not speak. ", a_She, " can\'t be the one, ", e_he, " thought.\n\nStill, the ", prince,
	" felt sorry for Ariel, so ", e_he, " brought ", a_herm, " to ", e_his, " castle. ", e_His, " servants fed ", a_herm, " and gave ", a_herm,
	" nice clothes to wear.\n\nThe next day, the ", prince, " took Ariel for a coach ride through ", e_his, " kingdom. \"", a_She, "\'s so lovely,\" ", Eric,
	" said to ", himself, ". \"If only ", a_she, " were the ", girl, " I\'ve been searching for!\"\n\nThe next day, the ", prince,
	" took Ariel for a boat ride.\nThere isn\'t much time, thought Ariel. If ", e_he, " doesn\'t kiss me soon, I will become ", Ursula,
	"\'s slave.\nAlthough Ariel didn\'t know it, the ", prince, " was falling in love and was just about to kiss ", a_herm,
	".\n\nBut Flotsam and Jetsam had been watching them. They tipped the boat over and sent the young couple tumbling into the water before Ariel could get ",
	a_her, " kiss!\n\n", Ursula, " had been watching the couple in ", u_her, " magic bubble. ", u_She, " decided to trick ", Eric, " so Ariel would never get ",
	a_her, " kiss. The ", witch, " transformed ", herself, " into a beautiful ", u_girl, ".\nWith Ariel\'s voice locked inside the seashell necklace, ", Ursula,
	" would sound just like ", Eric, "\'s true love!\n\nThe following day, as ", Ursula,
	" walked along the beach, the sound of Ariel\'s beautiful voice filled the air. ", Eric, " could hardly believe ", e_his, " ears! The person who had saved ",
	e_his, " life had finally come back to ", e_him, "!\nQuickly, the Sea ", Witch, " put a spell on ", Eric, ", and ", e_he,
	" decided to marry ", u2_herm, " right away.\n\n", Ursula, "\'s nasty trick had worked. ", u2_She, " and ", Eric, " were to be married on ", e_his,
	" ship that very day!\nIn ", u2_her, " cabin, ", Ursula, " laughed as ", u2_she, " looked at ", u2_her, " true reflection in the mirror. Luckily, Scuttle saw ",
	Ursula, "\'s real reflection, too.\n\nScuttle and Flounder rushed off to find Ariel and tell ", a_herm, " all about the Sea ", Witch,
	"\'s latest trick.\n\"Don\'t worry, Ariel. We\'ll help you!\" said Scuttle, as Flounder pulled ", a_herm,
	" out to the ship. Then Scuttle flew to the ship.\n\nWith the help of sea lions, pelicans, and other birds, Scuttle stopped the wedding. As Ariel climbed over the railing, the birds tore at ",
	Ursula, "\'s clothing and pulled ", u2_her, " hair. The seashell fell from ", Ursula, "\'s neck. When it broke, Ariel\'s voice returned to ", a_herm,
	" instantly. Ariel called out to warn the ", prince, ".\n\nThen ", Eric, " knew ", e_he,
	" had been tricked. But time had run out. The sun had started to set, and Ariel was already turning back into a ", mermaid,
	".\n\"You belong to me now!\" gloated ", Ursula, ", who had turned back into ", u_her, " mean, ugly self. ", u_She,
	" grabbed Ariel and slithered into the sea.\n\nBut ", Eric, " was not about to let Ariel slip away this time! Grabbing a harpoon, ", e_he,
	" dived into the sea and hurled it at the Sea ", Witch, "!\n\nThat made ", Ursula, " angrier than ever! ", u_She, " transformed ", herself,
	" into a huge monster and tried to crush poor Ariel and the ", prince, " with ", u_her, " black tentacles.\n", Eric, " clutched the Little ", Mermaid,
	" to ", e_him, ", trying to protect ", a_herm, " from the ", witch, "\'s fury.\n\n", Eric, " knew ", e_he,
	" had to do something, and fast! Climbing aboard a ship that ", Ursula, "\'s angry thrashing had raised from the bottom of the sea, ", e_he,
	" grabbed the wheel. ", e_He, " aimed the ship\'s prow at ", Ursula, " and sailed full speed ahead! As the boat struck the ", witch, ", ", u_she,
	" let out a terrible scream. Then ", u_she, " was gone.\n\nEveryone was glad the Sea ", Witch,
	" was gone, but Ariel was still unhappy. Even Triton could see that ", t_his, " ", daughter, " was truly in love. So, using ", t_his, " magic powers, ", t_he,
	" granted Ariel ", a_her, " dearest wish - ", t_he, " made ", a_herm, " human again.\n\nTriton watched as ", Eric,
	" and Ariel walked back to the castle.\n\"I\'m going to miss ", a_herm, ",\" ", King, " Triton said to ", Sebastian,
	", \"but I know they\'ll be happy.\"\nSoon after that, ", Eric,
	" and Ariel were married in a splendid shipboard wedding with all the merpeople looking on. And just as ", King,
	" Triton had predicted, they lived happily ever after!\n"]


	working_file.write("\nVersion %s" % number + "\n")
	working_file.write("\nAriel: %s," % a_she + " Triton: %s," % t_he + " Eric: %s," % e_he + " Scuttle: %s," % sc_he + " Sebastian: %s," % se_he 
		+ " Ursula: %s," % u_she + " Transformed Ursula: %s\n" % u2_she + "\n\n")
	working_file.write("".join(story))
	working_file.close()