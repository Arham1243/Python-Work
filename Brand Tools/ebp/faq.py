import pyperclip

titles = [
    "Why should I choose annual marketing over shorter campaigns?",
    "What kind of results should I expect?",
    "Is there a one-size-fits-all plan?",
    "Do you offer consultations to discuss my book and marketing goals?",
    "Can I watch the advancement of my campaign?",
]

paras = [
    "Annual plans offer continuity and build momentum, unlike isolated bursts of promotion. We develop a comprehensive strategy for the year, aligning with your publishing schedule and leveraging seasonal trends for long-term success.",
    "Increased book sales, a more engaged reader base, and broader reach are some potential outcomes. We track key metrics and provide regular reports so that you can see the impact of your investment.",
    "Absolutely not! We customize each plan to your specific book, genre, target audience, and budget. We offer tiered packages and discuss your expectations in detail to create a strategy that perfectly suits your needs.",
    "Absolutely! We believe in personalized service and offer free consultations to understand your vision and make a customized plan that aligns with your goals and budget.",
    "We will provide you with regular reports and updates about your campaign's performance, allowing you to follow your progress and measure the impact of your investment.",
]

all_cards = ""
for i, title in enumerate(titles):
    title = titles[i]
    para = paras[i]
    code = f"""
<div class="card mb-3">
    <div class="card-header" id="inner-question-{i+1}">
        <h5 class="mb-0">
            <button class="btn btn-link text-left w-100 collapsed" data-toggle="collapse" data-target="#inner-answer-{i+1}"
                aria-expanded="false" aria-controls="inner-answer-{i+1}">
                {title}
                <i class="fa fa-minus float-right" aria-hidden="true"></i>
            </button>
        </h5>
    </div>
    <div id="inner-answer-{i+1}" class="collapse" aria-labelledby="inner-question-{i+1}" data-parent="#accordion">
        <div class="card-body">
            {para}
        </div>
    </div>
</div>
"""
    all_cards += code

pyperclip.copy(all_cards)
