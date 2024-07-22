import re
import pyperclip

with open('ebp/content.php', 'r') as f:
    content = f.read()

# Extracting H1 heading
banner_heading_match = re.search(r'H1:(.*?)(?=\s*Paragraph:|$)', content, re.DOTALL)
banner_heading = banner_heading_match.group(1).strip() if banner_heading_match else None

# Extracting first paragraph for banner
banner_para_match = re.search(r'Paragraph:(.*?)\n\n', content, re.DOTALL)
banner_para = banner_para_match.group(1).strip() if banner_para_match else None

# Extracting H2 heading and paragraph for about 1
about1_match = re.search(r'H2:(.*?)(?=\nParagraph:|$)', content, re.DOTALL)
about1_heading = about1_match.group(1).strip() if about1_match else None

about1_para_match = re.search(r'Paragraph:(.*?)(?=\n\n|$)', content[about1_match.end():], re.DOTALL)
about1_para = about1_para_match.group(1).strip() if about1_para_match else None

# Extracting H2 heading and paragraph for about 2 (second occurrence)
about2_match = re.search(r'H2:(.*?)(?=\nParagraph:|$)', content[about1_para_match.end() + about1_match.end():], re.DOTALL)
about2_heading = about2_match.group(1).strip() if about2_match else None

about2_para_match = re.search(r'Paragraph:(.*?)(?=\n\n|$)', content[about1_para_match.end() + about1_match.end() + about2_match.end():], re.DOTALL)
about2_para = about2_para_match.group(1).strip() if about2_para_match else None

# Extracting H2 heading for portfolio (third occurrence)
portfolio_match = re.search(r'H2:(.*?)(?=\nH2:|$)', content[about1_para_match.end() + about1_match.end() + about2_match.end():], re.DOTALL)
portfolio_heading = portfolio_match.group(1).strip().split('\n')[0] if portfolio_match else None


code = f"""
<?php
include 'include/header.php';
?>


<!-- Banner Section Begin -->
<section class="banner___sec__main">
  <div id="demo" class="carousel slide" data-ride="carousel">
    <div class="carousel-inner">
      <div class="carousel-item active">
        <video width="100%" autoplay="" loop="" muted="" playsinline="" id="vid" poster="assets/images/video-poster.jpg" class="banner-video-bg">
          <source src="assets/videos/banner-video-new.mp4" type="video/mp4">
        </video>
        <!-- <img  src='assets/images/main-banner.webp' alt='image' class='imgFluid'> -->

        <div class="carousel-caption">
          <div class="container">
            <div class="row">
              <div class="col-sm-6">
                <div class="banner__content__sec">
                  <h1 class="wow slideInLeft typeingEffect">The Best Book <span class="typed-text"></span><span class="cursor">&nbsp;</span></h1>
                  <h1>
                      
                     {banner_heading}

                </h1>
                  <p>
{banner_para}
                    </p>

                  <div class="banner_btn">
                    <ul>
                      <li><a href="javascript:;"  class="btn_2 open-custom-form">Get Started</a>
                      </li>
                      <li><a href="<?= $telto ?>"><?= $phoneNumber ?></a></li>
                    </ul>
                  </div>
                </div>
              </div>
              <div class="col-sm-6">
                <div class="banner__form__tab">
                  <h3>Get In Touch With <span>Our Expert</span></h3>
                  <?php include 'include/inner-banner-form.php'?>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
<!-- Banner Section End -->


<section class="GotASection">
  <div class="container">
    <div class="row">
      <div class="col-md-3">
        <h3>Hire <?= $brand_name ?> is your <b>ultimate solution</b> to Influence your readers</h3>
      </div>
      <div class="col-md-6">
        <div class="logo-br-slider">
          <div class="logo-bran">
            <div class="logo-img">
              <img src="assets/images/logo-img.png" alt="img" loading="lazy">
            </div>
          </div>
          <div class="logo-bran">
            <div class="logo-img">
              <img src="assets/images/logo-img1.png" alt="img" loading="lazy">
            </div>
          </div>
          <div class="logo-bran">
            <div class="logo-img">
              <img src="assets/images/logo-img2.png" alt="img" loading="lazy">
            </div>
          </div>
          <div class="logo-bran">
            <div class="logo-img">
              <img src="assets/images/logo-img3.png" alt="img" loading="lazy">
            </div>
          </div>
          <div class="logo-bran">
            <div class="logo-img">
              <img src="assets/images/logo-img4.png" alt="img" loading="lazy">
            </div>
          </div>
        </div>
      </div>
      <div class="col-md-3">
        <h4>Got a plot idea?</h4>
        <div class="banner_btn">
          <ul class="d-flex justify-content-center getStarted-btnss">
            <li><a href="javascript:;" onclick="setButtonURL()" class="btn_2">Live Chat</a></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>


<!-- Media Platform Section Begin -->
<section class="media_platform_sec padding_70">
  <div class="container">
    <div class="row align-items-center">

      <div class="col-sm-6">
        <div class="media_left_img wow zoomIn" data-wow-duration=".6s" data-wow-delay="1s">
          <img data-src="assets/images/about.png" alt="ebook writing">
        </div>
      </div>
      <div class="col-sm-6">
        <div class="web_head_Content">
          <h2 class="wow fadeInDown" data-wow-duration=".6s" data-wow-delay="0.5s">
{about1_heading}
            </h2>
          <p class="wow fadeInUp" data-wow-duration=".6s" data-wow-delay="1s">
             {about1_para}

              </p>
        </div>
      </div>
    </div>

  </div>
</section>
<!-- Media Platform Section End -->


<!-- Ghostwriting Section Begin -->
<section class="ghostwriting_sec_main padding_70">
  <div class="container">
    <div class="row">
      <div class="col-sm-6">
        <div class="web_content_sec">
          <h2 class="wow fadeInDown" data-wow-duration=".6s" data-wow-delay="1s">
{about2_heading}


            </h2>
          <p class="wow fadeIn" data-wow-duration=".6s" data-wow-delay="1.5s">
             {about2_para}

            </p>

          <div class="banner_btn">
            <ul>
              <li class="wow fadeInUp" data-wow-duration=".6s" data-wow-delay="1.6s"><a href="<?= $telto ?>"><?= $phoneNumber ?></a></li>
              <li class="wow fadeInUp" data-wow-duration=".6s" data-wow-delay="1.7s"><a href="javascript:;" onclick="setButtonURL()" class="btn_2">Live Chat</a></li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
<!-- Ghostwriting Section End -->



<?php 
$portfolio_heading = "{portfolio_heading}";
include 'include/portfolio.php' ?>

"""


pyperclip.copy(code)