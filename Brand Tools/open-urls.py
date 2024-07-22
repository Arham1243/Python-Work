import webbrowser
import time

urls = [
"site:instagram.com 'Hair salon' 'usa'",
"site:instagram.com 'Haircutting salon' 'usa'",
"site:instagram.com 'Hair studio' 'usa'",
"site:instagram.com 'Grooming parlor' 'usa'",
"site:instagram.com 'Haircutting parlor' 'usa'",
"site:instagram.com 'Shaving parlor' 'usa'",
"site:instagram.com 'Men's salon' 'usa'",
"site:instagram.com 'Tonsorial parlor' 'usa'",
"site:instagram.com 'Hairdressing salon' 'usa'",
]

for url in urls:
    time.sleep(0.5)
    webbrowser.open(url)
