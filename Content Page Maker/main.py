titles = [
    "BRAND BOOSTER",
    "LEADS WIZARD",
    "SALES NIRVANA",
]

dels = [
    "$498",
    "$998",
    "$1998",
]
news = [
    "$249",
    "$499",
    "$999",
]
perks = [
    """

                            
                            <li>Covers Two Social Media Platforms</li>
                            <li>Over 2500 Likes, Followers Engagements On Social Media</li>
                            <li>Custom Brand Marketing Strategy Creation</li>
                            <li>Indepth Competitor Review</li>
                            <li>Content Plan Creation</li>
                            <li>12 Custom Design Posts Per Month</li>
                            <li>Community Management</li>
                            <li>Custom Monthly Banner Design</li>
                            <li>Existing Page Accounts Optimization</li>
                            <li>Traffic Conversion Tracking Setup With Facebook Pixel Google
                                Analytics</li>
                        
                            """,
    """

                            
                           
    <li>Covers Three Social Media Platforms</li>
    <li>Over 5000 Likes, Followers  Engagements On Social Media</li>
    <li>Custom Brand Marketing Strategy Creation</li>
    <li>FREE Facebook Ad Credit Worth $200</li>
    <li>Lead Form Setup  Optimization</li>
    <li>Facebook  Instagram Shops Setup</li>
    <li>Facebook  Instagram Ads Setup</li>
    <li>LinkedIn Native Ads  Sponsored InMail Setup</li>
    <li>Social Media Pages Moderation</li>
    <li>Indepth Competitor Review</li>
    <li>Content Plan Creation</li>
    <li>16 Custom Design Posts Per Month</li>
    <li>Community Management</li>
    <li>Custom Monthly Banner Design</li>
    <li>Existing Page  Accounts Optimization</li>
    <li>Traffic  Conversion Tracking Setup With Facebook Pixel  Google
        Analytics</li>
                        
                            """,
    """

    <li>Covers Five Social Media Platforms</li>
    <li>Over 10,000 Likes, Followers  Engagements On Social Media</li>
    <li>Advanced Brand Marketing Strategy Creation</li>
    <li>FREE Facebook  Instagram Ad Credit Worth $200</li>
    <li>Lead Form Setup  Optimization</li>
    <li>Facebook  Instagram Shops Setup</li>
    <li>Facebook  Instagram Ads Setup</li>
    <li>LinkedIn Native Ads  Sponsored InMail Setup</li>
    <li>Social Media Pages Moderation</li>
    <li>Indepth Competitor Review</li>
    <li>Content Plan Creation</li>
    <li>16 Custom Design Posts Per Month</li>
    <li>Community Management</li>
    <li>Targeted AB Testing Ad Campaigns</li>
    <li>Custom Monthly Banner Design</li>
    <li>Existing Page  Accounts Optimization</li>
    <li>Traffic  Conversion Tracking Setup With Facebook Pixel  Google
        Analytics</li>
                        
                            """,
]


for i in range(len(titles)):
    title = titles[i].title()
    del_ = dels[i]
    new = news[i]
    perk = perks[i]
    page_name = f"{title}.php"
    page_name = page_name.lower().replace(" ",'-')

    code = f"""



<?php
$title = "{title}";
include 'include/header.php';
?>


<section class="packages_sec_main dark-black">
    <div class="container">
    <div class="row">
            <div class="col-sm-12">
                <div class="heading_packages">
                    <h2>SMM Package</h2>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-xl-4 col-lg-5 col-md-6 col-sm-4">
                <div class="packages_detail_price">
                    <h3>{title}</h3>
                    <div class="cut_price_pck">{del_} ONLY </div>
                    <h4>{new} USD </h4>
                    <div class="packages-card__btns">
                        <a href="javascript:void(0)" data-toggle="modal" data-target="#quickOrder">Order Now</a>
                        <a href="<?php echo $telto ?>">Book a call</a>
                    </div>

                </div>
            </div>
            <div class="col-xl-8 col-lg-7 col-md-6 col-sm-8">
                <div class="packages_list_tab">
                    <div class="pakages_list_head">
                        <h2>Package Includes</h2>
                    </div>

                    <div class="pakages_list_detail">
                        <ul>{perk}</ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<?php include 'include/footer.php'; ?>
    

"""
    with open(page_name,'w') as f:
        f.write(code)