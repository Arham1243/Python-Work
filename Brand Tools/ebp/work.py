import pyperclip

titles = [
    "Increased Book Sales",
    "Expanded Reader Base",
    "Enhanced Author Branding",
    "Increased Author Visibility",
    "Improved Online Presence",
    "Engaged and Loyal Fanbase",
    "Data-Driven Decision Making",
]

paras = [
    "Throw out the genre rulebook! We'll blend unexpected genres to create a fresh, irresistible reading experience. Imagine historical romance meets post-apocalyptic thriller or cozy mystery with a dash of cyberpunk. Surprise readers and dominate new audiences.",
    "Forget passive reading. We'll craft choose-your-own-adventure paths, augmented reality experiences, and interactive social media campaigns that turn readers into active participants in your story. They won't just read, they'll live it.",
    "Forget one-size-fits-all marketing. We'll create exclusive micro-communities of superfans around your book. Think niche online forums, curated influencer partnerships, and personalized reader rewards. Cultivate your most ardent champions and let them shout your praises to the world.",
    "Forget 500-page tomes. We'll release your book in bite-sized, addictive chapters, igniting a cliffhanger frenzy across platforms. Imagine weekly downloads, social media anticipation, and a constant stream of reader buzz keeping your title trending.",
    "Embrace the future! We'll use cutting-edge AI to personalize your book based on reader preferences. Imagine interactive characters adapting to user choices, storylines branching in real-time, and a truly unique reading experience for everyone.",
    "Think beyond bookstores. We'll partner with international platforms, translation teams, and cultural influencers to catapult your book onto the global stage. Imagine your name trending in foreign languages, book tours across continents, and a truly international bestseller phenomenon.",
    "Forget passive reading; let's ignite a visual wildfire! We'll spark a fan art contest with unique prompts and hashtags, creating a social media explosion of artistic interpretations of your book.  Imagine stunning illustrations, cosplay creations, and animation tributes flooding the internet, captivating new audiences and igniting word-of-mouth virality. ",
]

all_cards = ""
for i, title in enumerate(titles):
    title = titles[i]
    para = paras[i]
    code = f"""
<div class="col-sm-4">
  <div class="work_box_sec wow fadeIn" data-wow-duration=".6s" data-wow-delay="0.2s">
    <span>{i+1}</span>
    <h4>{title}</h4>
    <p>{para}</p>
  </div>
</div>
"""
    all_cards += code

pyperclip.copy(all_cards)
