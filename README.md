<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/fo3cus/covid_qr_generator">
    <img src="assets/logo.png" alt="Logo" width="130" height="130">
  </a>

<h3 align="center">NZ COVID QR Sign Generator</h3>

  <p align="center">
    This application will generate a QR code sign based on the design<br /> used in NZ, which allows use of the <a href="https://www.health.govt.nz/our-work/diseases-and-conditions/covid-19-novel-coronavirus/covid-19-resources-and-tools/nz-covid-tracer-app">NZ COVID Tracer</a> app to manually<br /> record our stops at different locations. This facilitates contact tracing<br /> when <a href="https://www.health.govt.nz/our-work/diseases-and-conditions/covid-19-novel-coronavirus/covid-19-health-advice-public/contact-tracing-covid-19/covid-19-contact-tracing-locations-interest">locations of interest</a> become known in your area.
    <br />
    <br />
    <a href="https://github.com/fo3cus/covid_qr_generator/issues">Report Bug</a>
    ·
    <a href="https://github.com/fo3cus/covid_qr_generator/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Road Map</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

![Product Name Screen Shot][product-screenshot]

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

- [Python](https://www.python.org/)
- [tkinter](https://docs.python.org/3/library/tkinter.html)
- [qrcode](https://github.com/lincolnloop/python-qrcode)
- [Pillow](https://pillow.readthedocs.io/en/stable/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple example steps.

All instructions are based on Ubuntu 20.04.

### Prerequisites

Step 1 — Setting Up Python 3

Ubuntu 20.04 and other versions of Debian Linux ship with Python 3 pre-installed. To make sure that our versions are up-to-date, let’s update and upgrade the system with the apt command to work with Ubuntu’s Advanced Packaging Tool:

```sh
sudo apt update
sudo apt -y upgrade
```

The -y flag will confirm that we are agreeing for all items to be installed, but depending on your version of Linux, you may need to confirm additional prompts as your system updates and upgrades.

Once the process is complete, we can check the version of Python 3 that is installed in the system by typing:

```sh
python3 -V
```

You’ll receive output in the terminal window that will let you know the version number. While this number may vary, the output will be similar to this:

```sh
Output
Python 3.8.10
```

To manage software packages for Python, let’s install pip, a tool that will install and manage programming packages we may want to use in our development projects. You can learn more about modules or packages that you can install with pip by reading “How To Import Modules in Python 3.”

```sh
sudo apt install -y python3-pip
```

Python packages can be installed by typing:

```sh
pip3 install package_name
```

For this project you'll need to install pygame.

```sh
pip3 install pygame
```

Also install the tkinter requirement to the system.

```sh
sudo apt install -y python3-tk
```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/fo3cus/covid_qr_generator.git
   ```
2. Install requirements packages
   ```sh
   pip3 install -r requirements.txt
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

Run **main** file from a terminal

```sh
cd <install_path>/covid_qr_generator/

python3 main.py
```

Fill in the fields of the form and click save to generate a PNG image file in the same directory as the application:

> [![Application Usage Screenshot][usage-screenshot]](https://github.com/fo3cus/covid_qr_generator/blob/main/assets/usage_example.png) > [![Sign Sample Image][sample-image]](https://github.com/fo3cus/covid_qr_generator/blob/main/assets/example.png)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADMAP -->

## Roadmap

- [ ] Build and add releases
- [ ] Create wiki
  - [ ] Move prerequisites
  - [ ] Move installation
  - [ ] Move usage

See the [open issues](https://github.com/fo3cus/covid_qr_generator/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

James Rollinson - contact@rollinson.nz

Project Link: [https://github.com/fo3cus/covid_qr_generator](https://github.com/fo3cus/covid_qr_generator)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & assets -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/fo3cus/covid_qr_generator?style=for-the-badge
[contributors-url]: https://github.com/fo3cus/covid_qr_generator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/fo3cus/covid_qr_generator?style=for-the-badge
[forks-url]: https://github.com/fo3cus/covid_qr_generator/network/members
[stars-shield]: https://img.shields.io/github/stars/fo3cus/covid_qr_generator?style=for-the-badge
[stars-url]: https://github.com/fo3cus/covid_qr_generator/stargazers
[issues-shield]: https://img.shields.io/github/issues/fo3cus/covid_qr_generator?style=for-the-badge
[issues-url]: https://github.com/fo3cus/covid_qr_generator/issues
[license-shield]: https://img.shields.io/github/license/fo3cus/covid_qr_generator?style=for-the-badge
[license-url]: https://github.com/fo3cus/covid_qr_generator/blob/main/LICENSE.txt
[product-screenshot]: assets/screenshot.png
[usage-screenshot]: assets/usage_example.png
[sample-image]: assets/example.png
