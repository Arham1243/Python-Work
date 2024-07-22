<div class="upper-strip py-2">
        <div class="container">
            <div class="row aos-init aos-animate" data-aos="slide-right"  data-aos-duration="2000">
                <div class="col-lg-9">
                    <ul class="upper-left d-flex align-items-center p-0 m-0">
                        <li>
                            <a href="javascript:void(0)"><i class="fa-regular fa-envelope"></i>rbhealthcaresolutions19@gmail.com</a>
                        </li>
                        <li>
                            <a href="javascript:void(0)"><i class="fa-solid fa-phone"></i> +1 647-638-8276</a>
                        </li>
                        <li>
                            <p class="mb-0">
                                <i class="fa-regular fa-clock"></i> Open 24hours
                            </p>
                        </li>
                    </ul>
                </div>
                <div class="col-lg-3">
                    <ul class="upper-right d-flex align-items-center p-0 m-0">
                        <li>
                            <a href="javascript:void(0)"><i class="fa-brands fa-facebook"></i></a>
                        </li>
                        <li>
                            <a href="javascript:void(0)"><i class="fa-brands fa-instagram"></i></a>
                        </li>
                        <li>
                            <a href="javascript:void(0)"><i class="fa-brands fa-twitter"></i></a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
    <!-- heder starts here -->
    <header class="aos-init aos-animate" data-aos="slide-right"  data-aos-duration="2000">
        <div class="container py-2">
            <div class="row align-items-center">
                <div class="col-lg-2">
                    <div class="header-logo">
                        <a href="{{ route("index") }}">
                        <img src="{{ asset("images/logo.png") }}" alt="" />
                        </a>
                    </div>
                </div>
                <div class="col-lg-7">
                    <nav>
                        <ul class="header-list d-flex align-items-center p-0 m-0">
                            <li><a href="{{ route("index") }}">Home</a></li>
                            <li><a href="{{ route("aboutus") }}">About</a></li>
                            <li><a href="{{ route("services") }}">Services</a></li>
                            <li><a href="{{ route("opportunity") }}">Opportunities</a></li>
                            <li><a href="{{ route("post-job") }}">Post A Job</a></li>
                            <li><a href="{{ route("testimonials") }}">Testimonials</a></li>
                            <li><a href="{{ route("contactus") }}">Contact</a></li>
                        </ul>
                    </nav>
                </div>
                <div class="col-lg-3 d-flex justify-content-between">
                    <ul class="sign-list d-flex align-items-center p-0 m-0">
                        <li>
                            <div class="dropdown">
                                <button class="btn  dropdown-toggle" type="button" data-bs-toggle="dropdown"
                                    aria-expanded="false">
                                    Sign up
                                </button>
                                <ul class="dropdown-menu">
                                    <li><a class="dropdown-item" href="{{ route("applicant") }}">Applicants</a></li>
                                    <li>
                                        <a class="dropdown-item" href="{{ route("employer") }}">Employer</a>
                                    </li>

                                </ul>
                            </div>
                        </li>
                        <li><a href="{{ route("login") }}" class="login-btn">Login</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </header>