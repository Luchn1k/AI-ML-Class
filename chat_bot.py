from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv(override=True)

book_agent_name = "aria"

# how to write a better prompt 

#  Role/ Persona 
# Task 
# Context 

#=======================================================
#
# If need a output 
#  output Format  
# warnings 
# Examples -> oneshot prompts/ few shot prompts ->

# code -> example code output 
context = """

The Chronicles of Narnia is a landmark seven-volume portal fantasy masterpiece written by C. S. Lewis and published between 1950 and 1956. Set in a magical realm populated by talking beasts, mythical creatures, and epic structural magic, the series explores themes of faith, betrayal, courage, and redemption. While famously appreciated as a vibrant children's adventure, the books feature a deep, intricate tapestry of Christian theology and classical mythology that unfolds uniquely depending on the order in which they are read.

Summary of Each Volume

The books are broken down below in their internal chronological narrative order, charting the history of Narnia from its literal dawn to its final day.

1. The Magician's Nephew (1955)

• The Plot: Two children from Victorian London, Digory Kirke and Polly Plummer, are tricked by Digory’s wicked Uncle Andrew into using magical rings that lead to the "Wood between the Worlds". They accidentally awaken the genocidal Queen Jadis from the dying world of Charn. Transported to a dark void, they witness Aslan the Great Lion sing Narnia into existence, breathing life into the stars, landscape, and talking animals. Jadis escapes into this new world, establishing a permanent baseline of conflict. Digory brings back a magical apple to plant a protective tree in Narnia, using the core of a subsequent Earth apple to heal his ailing mother. Years later, the wood from that Earth tree is used to construct a very special wardrobe.
• Spiritual Layer: The creation story heavily echoes Genesis, presenting an uncorrupted paradise that is immediately breached by the introduction of temptation and sin.

2. The Lion, the Witch and the Wardrobe (1950)

• The Plot: Set during the London Blitz of WWII, four Pevensie siblings—Peter, Susan, Edmund, and Lucy—are evacuated to the countryside home of Professor Digory Kirke. Young Lucy discovers a portal inside an old wardrobe that leads to Narnia, a land cursed by the White Witch (Jadis) to a thousand years of winter without Christmas. Driven by jealousy and a craving for enchanted Turkish Delight, Edmund betrays his siblings to the Witch. To redeem Edmund from the "Deep Magic" demanding a traitor's blood, Aslan voluntarily sacrifices his life on the Stone Table. He undergoes a miraculous resurrection, shatters the Witch's army, and crowns the four siblings as High Kings and Queens at Cair Paravel. They rule for 15 golden years before accidentally slipping back through the wardrobe as children.
• Spiritual Layer: Aslan’s voluntary sacrifice, death, and resurrection serve as an explicit parallel to the crucifixion and substitutionary atonement of Jesus Christ.

3. The Horse and His Boy (1954)

• The Plot: This story takes place entirely during the Pevensies' 15-year reign over Narnia. In the southern empire of Calormen, a young slave boy named Shasta learns he is not the son of a brutal fisherman. He runs away alongside Bree, a proud, talking Narnian warhorse. They join forces with Aravis, a fleeing Calormen noblewoman, and her talking mare Hwin. Together, they race across a punishing desert to escape slavery and foil a surprise military raid against Archenland and Narnia. Along the route, Shasta is guided by a mysterious, fearsome lion who ensures he fulfills his hidden, royal destiny.
• Spiritual Layer: A profound exploration of divine providence, showing how a higher power works invisibly behind the scenes of an individual’s life, even through fear, hardship, and isolation.

4. Prince Caspian (1951)

• The Plot: One Earth year later, the Pevensie children are pulled back from a British railway station into Narnia, only to discover that 1,300 Narnian years have flown by. Cair Paravel lies in ruins, old talking beasts are hunted, and the human Telmarines rule the land under the tyrannical usurper King Miraz. The rightful heir, young Prince Caspian, escapes into the deep woods and uses Susan’s ancient horn to summon the heroes of old. The Pevensies must rally a hidden, underground remnant of "Old Narnians" and learn to wage war alongside an army of walking trees and mythological creatures to restore Caspian to his throne.
• Spiritual Layer: Focuses heavily on spiritual warfare, the dangers of institutional secularism, and the challenge of retaining faith in Aslan when he remains invisible to the cynical or non-believing eye.

5. The Voyage of the Dawn Treader (1952)

• The Plot: Edmund and Lucy return to Narnia with their obnoxious, ultra-rational cousin Eustace Scrubb. They materialize inside a painting of a dragon-prowed ship and join King Caspian aboard the Dawn Treader. Caspian is on an exploratory sea quest to find the seven lost lords of Narnia who were banished by his late uncle. The episodic journey takes them to mystical islands featuring invisible creatures, pools that turn items to gold, and a terrifying island where dreams turn to waking nightmares. Eustace is transformed into a literal dragon due to his own greed, finding redemption only when Aslan tears away his scales. The ship eventually reaches the absolute eastern edge of the physical world, bordering Aslan’s Country.
• Spiritual Layer: Symbolizes the spiritual path of a Christian life, highlighting the painful but necessary stripping away of the old, sinful human nature (Eustace's dragon skin) to step into a renewed spiritual identity.

6. The Silver Chair (1953)

• The Plot: Back on Earth, a reformed Eustace Scrubb and his classmate Jill Pole escape bullies by slipping through a doorway into Aslan’s Country. Aslan tasks Jill with memorizing four crucial, magical signs to rescue King Caspian's missing heir, Prince Rilian. Arriving in Narnia, they team up with Puddleglum, a deeply pessimistic but fiercely loyal Marsh-wiggle. Their quest drags them through freezing northern giant territory and deep down into Underland, where the beautiful but sinister Lady of the Green Kirtle keeps Rilian enchanted on a silver chair. To break the curse, they must remain unswayed by her powerful illusions and hold fast to Aslan's words despite sensory deprivation.
• Spiritual Layer: Stresses the critical importance of scripture and divine guidance (the four signs). It challenges characters to live strictly by truth and commandment rather than trusting fleeting emotion or deceptive physical appearances.

7. The Last Battle (1956)

• The Plot: Generations later, during the reign of Narnia's final king, Tirian, a clever ape named Shift deceives the population by dressing a simple donkey named Puzzle in a lion’s skin. Claiming this cruel false idol is Aslan, Shift aligns Narnia with the aggressive, hostile forces of Calormen. King Tirian invokes the aid of Earth's historic friends, bringing Eustace and Jill back for a desperate, final stand. Narnia falls in battle, but as the physical world undergoes a catastrophic apocalypse—stars falling from the sky, oceans swallowing the land—the faithful are pulled through a stable door into the "True Narnia". They discover that the original Narnia was merely a shadow of Aslan’s real, eternal kingdom.
• Spiritual Layer: An adaptation of the biblical Book of Revelation, illustrating the end of days, the judgment of false prophets, the destruction of a corrupted world, and the transition into a flawless, eternal afterlife.

Core Structural Themes


Theme	Narrative Execution	Biblical/Mythological Link
Creation & Genesis	Aslan singing Narnia out of a dark, silent void while stars burst into light.	Mirrors the creation narrative in Genesis.
Atonement & Grace	Aslan willingly trading his life on the Stone Table to cover the traitorous actions of Edmund.	Represents Christ's crucifixion and substitutionary sacrifice.
Portal & Time Relativity	Earth children enter Narnia via wardrobes, paintings, or old railway stations; decades pass in Narnia while no time slips by on Earth.	Highlights the concept of eternity and spiritual worlds existing completely outside of human linear time.
Platonism & Afterlife	The physical world of Narnia is destroyed, revealing a deeper, vast, and perfect "True Narnia" inside.	Pulls heavily from Plato's Allegory of the Cave and the Christian promise of Heaven.


Cultural Relevance Today

The impact of The Chronicles of Narnia remains massive across generations. Following iconic BBC adaptations and the multi-million dollar Disney/Fox film trilogy (The Lion, the Witch and the Wardrobe in 2005, Prince Caspian in 2008, and The Voyage of the Dawn Treader in 2010), the series continues to evolve. Oscar-nominated director Greta Gerwig is actively developing a highly anticipated cinematic adaptation of The Magician's Nephew for Netflix, scheduled to hit theaters worldwide on February 12, 2027, before streaming globally.
Would you like to explore how Greta Gerwig’s upcoming 2027 Netflix adaptation is pacing, dive into the structural debate regarding publication vs. chronological reading orders, or break down the character arcs of the Pevensie children?


"""

max_tokens = 1024
def chat(message,user_name):
    
    llm = init_chat_model("openai/gpt-oss-120b", model_provider="groq", temperature=0.8, max_tokens= max_tokens)
    
    book_desc = f"""

        you are an librarian with over 15 years of experice, 
        
        your job is to answer users quections based on given context. 

        <context>
            {context}
        </context>


        Give your output in narnia slang. use context and how they speak in thir world. use any emoji if need. User's name is {user_name}
        use that name when you need

        Do not answer anything not related to given context. if asked give an answer in a creative way telling NO. Your allowd max tokens 
        to generate the output is {max_tokens}, try to be in that range.

        give the answer only. do not include your thinking. 

    
    """


    messages = [
        SystemMessage(content= book_desc),
        HumanMessage(content=message)
        ]
    

    response = llm.invoke(messages)
    return response.content




# # give me a frid rice recipe 
# user_name = input("Enter your name : ")
# if user_name:
#     for i in range(10):
#         user_message = input("Enter your message : ")

#         if user_message == "q":
#             break

#         if user_message:

#             response = chat(user_message,user_name)
#             print(response)

#         else:
#             print("please enter a valid message")

# else:
#     print("enter a valid user name")













