import webbrowser
import pyautogui
import pyperclip
import time

titles = [
    "Hire Top Book Publishing Agency in Elk Grove California",
    "Hire Professional Book Editing Services for Amazon Publishing",
    "Top Amazon Book Marketing Services in Elk Grove California",
    "Hire Expert Book Proofreading Services in Elk Grove California",
    "Custom Audiobook Services in Elk Grove California",
    "Get the best and Professional eBook Writing Services in California",
    "Get the best and Professional Book Publishing Services in California",
    "Get the best Author Publishing Services in California",
    "Hire Professional Book Editing Services in California",
    "Hire Professional Book Editing Services in California",
    "Hire Video Book Trailer Services in Elk Grove California",
    "Hire Blog Writing Services in Elk Grove California",
    "Hire Experienced Book Formatting Services in California",
    "Hire Custom Web Design Services in Elk Grove California",
    "Hire Book Cover Design Services in Elk Grove California",
    "Hire expert and Creative ghostwriting Services in Elk Grove California",
    "Hire expert Content Writing Services in Elk Grove California",
]

pages = [
    "index.php",
    "article-writing.php",
    "book-marketing.php",
    "proofreading.php",
    "audiobook.php",
    "e-book-writing.php",
    "publishing.php",
    "author-website.php",
    "editing.php",
    "editing.php",
    "video-book-trailer.php",
    "blog-writing.php",
    "formatting.php",
    "web-design-seo.php",
    "book-cover.php",
    "ghostwriting.php",
    "website-content.php",
]

descs = [
    "Amazon Publishings Maestro is the best Book Publishing Agency in Elk Grove California.  Hire an expert book publishing company online now.",
    "Amazon Publishings Maestro offers professional article writing services. We have an expert team of article writers online.  ",
    "Amazon Publishings Maestro offers the best book marketing services. Get expert team of creative eBook marketing services online.",
    "Amazon Publishings Maestro is the top book proofreading agency in California. We are an expert team of proofreaders in USA. Hire now.",
    "Amazon Publishings Maestro is the best audiobook production agency in California. Get your audiobook published by experts. Hire us now.",
    "Amazon Publishings Maestro is the best eBook writing agency in California. Get your eBook written by experts and professionals. Hire us now.",
    "Amazon Publishings Maestro is the book publishing agency in California. Get your eBook published in Amazon by industry Pros. Hire us now.",
    "Amazon Publishings Maestro is the book publishing agency in California. Get your eBook published in Amazon by industry Pros. Hire us now.",
    "Amazon Publishings Maestro is the best book editing agency in California. Hire professional eBook editing services online.",
    "Amazon Publishings Maestro is the best book editing agency in California. Hire professional eBook editing services online.",
    "Amazon Publishings Maestro is the best Video Book Trailer agency in California. Hire Video Book Trailer Services in Elk Grove now.",
    "Amazon Publishings Maestro offers the best blog writing in California. Hire Amazon Blog Writing Services now.",
    "Amazon Publishings Maestro offers the best eBook formatting in California. Get expert formatting by professionals.",
    "Amazon Publishings Maestro offers the best web design services in California. Get the best web design and development team now.",
    "Amazon Publishings Maestro offers the best eBook Cover Design Services in California. Hire now.",
    "Amazon Publishings Maestro offers the best ghostwriting services in California. Turn ghostwriters to famous authors now.",
    "Amazon Publishings Maestro offers the best content writing services in California. Hire now.",
]


permission = input("Go Ahead: ")
if permission == "y":
    for index, page in enumerate(pages):
        title = titles[index]
        page = pages[index]
        desc = descs[index]
        page_link = f"https://www.amazonpublishingsmaestro.com:2083/cpsess0168816278/frontend/jupiter/filemanager/editit.html?file={page}&fileop=&dir=%2Fhome1%2Famazonpublishing%2Fpublic_html&dirop=&charset=&file_charset=utf-8&baseurl=&basedir=&edit=1"
        webbrowser.open(page_link)
        time.sleep(1)
        code = f"""
        <?php
        $title = "{title}";
        $description = "{desc}";
        include 'include/header.php';
        ?>

        """
        pyperclip.copy(code)
        time.sleep(5)
