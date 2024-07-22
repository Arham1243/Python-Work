import pyperclip

titles = [
    "Long-Term Strategy and Goal Setting",
    "Building and nurturing a community",
    "Content Marketing with Depth and Impact",
    "Paid Advertising with Strategic Focus",
    "Public Relations and Media Outreach",
    "Data Analysis and Continuous Improvement",
    "Building a Sustainable Partnership",
]

paras = [
    "Instead of chasing temporary peaks, we will help you define a year-long vision for lasting success. Whether you aim for bestseller status, a loyal readership, or a strong author brand, we'll guide you toward the summit of your goals. By setting clear objectives and mapping out a strategic plan, we ensure that your marketing efforts align with your long-term vision. Together, we'll establish milestones, track progress, and make necessary adjustments along the way, keeping you on the path to sustained success in the literary world.",
    "Success isn't a solo climb. We understand the importance of building a vibrant community around your work, where readers not only consume but actively engage. Through our tailored strategies, we'll help you create and nurture a community of passionate fans who are invested in your writing journey. From interactive social media campaigns to virtual events and author Q&As, we'll encourage meaningful interactions and foster a sense of connection. By cultivating a loyal following, you'll not only gain support and word-of-mouth promotion but also build a strong foundation for long-term success.",
    "In the ever-evolving literary landscape, standing out requires more than just a captivating book. Our team specializes in crafting evergreen content that goes beyond traditional promotion. We'll develop thought-provoking blog posts, engaging multimedia experiences, and strategic partnerships that solidify your position in the literary world. By creating content with depth and impact, we'll expand your reach, diversify your appeal, and leave a lasting impression on readers. Whether it's through informative articles, captivating videos, or collaborations with influencers, we'll help you build a strong author brand that resonates long after readers finish the final page.",
    "In the vast digital landscape, reaching your target audience requires a strategic approach. Our team will invest in laser-focused adventures, utilizing data as your compass to identify and engage ideal reader demographics. By leveraging various advertising platforms and techniques, we'll help you embrace new formats, experiment with different strategies, and conquer the digital wilderness. From targeted social media campaigns to display ads and paid search, we'll ensure that your message reaches receptive audiences who are most likely to connect with your book. With a strategic focus on paid advertising, we'll maximize your visibility and drive meaningful engagement.",
    "Navigating the media landscape is crucial for gaining recognition and exposure as an author. Our team excels in forging powerful partnerships, crafting compelling press kits, and pitching your story with precision. We'll help you secure valuable media coverage in relevant publications, both online and offline, that reach your target audience. From interviews and features to book reviews and guest blogging opportunities, we'll strategically position your book to generate buzz and enhance your author brand. With our expertise in public relations and media outreach, we'll leverage editorial wind currents to propel your literary ascent and amplify your presence in the industry.",
    "In the world of marketing, knowledge is power. That's why we prioritize data analysis to drive decision-making and continuous improvement. Our team will track and analyze key performance metrics, such as website traffic, engagement rates, and conversion rates, to gain valuable insights into the effectiveness of your marketing efforts. By understanding what works and what doesn't, we'll adapt your strategy, refine your approach, and conquer new horizons in book marketing. With a data-driven approach, we ensure that your marketing efforts remain efficient, impactful, and aligned with your overall goals.",
    "At Monthly Marketing Made Easy, we believe in building a sustainable partnership with our clients. We stand beside you, showcasing the ongoing value we deliver and customizing strategies to fit your unique needs. Through open communication and unwavering support, we navigate the literary terrain together, year after year. Our dedicated team is committed to understanding your goals, staying up-to-date with industry trends, and evolving our strategies to meet your changing needs. With a long-term perspective and a collaborative approach, we'll work tirelessly to help you achieve lasting success in the competitive world of publishing.",
]

all_cards = ""
for i, title in enumerate(titles):
    title = titles[i]
    para = paras[i]
    code = f"""
<div class="col-sm-4">
    <div class="services_box">
        <div class="sercices_head_main">
            <div class="services_icon">
                <img data-src="assets/images/service-icons/1.png" class="img-fluid lazy" alt="Ghost Book Writing">
            </div>
            <div class="services_head">
                <h3>{title}</h3>
            </div>
        </div>

        <div class="services_content scroll-block">
            <p>
            {para}
            </p>
        </div>
    </div>
</div>
"""
    all_cards += code

pyperclip.copy(all_cards)
