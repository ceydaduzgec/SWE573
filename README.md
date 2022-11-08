
<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/ceydaduzgec/SWE573">
    <img src="images/boun.png" alt="Logo" width="380" height="200">
  </a>

<h3 align="center">SWE 573 Software Development Practice</h3>

  <p align="center">
    Boğaziçi University Fall'22 Software Development Course Project
    <br />
    <a href="https://github.com/ceydaduzgec/SWE573/wiki"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/ceydaduzgec/SWE573">View Demo</a>
    ·
    <a href="https://github.com/ceydaduzgec/SWE573/issues/new">Report Bug</a>
    ·
    <a href="https://github.com/ceydaduzgec/SWE573/issues/new">Request Feature</a>
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
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
This projects is for the SWE 573 Software Development Practice course of Boğaziçi University on Fall'22 and supervised by [Suzan Uskudarlı](https://github.com/uskudarli). It will be updated each week in order to reflect projects process which is divided into 3 Milestones. You can find out more about it on the [wiki](https://github.com/ceydaduzgec/SWE573/wiki).

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [![Django][Django-image]][Django-url]
* [![React][React.js]][React-url]

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* Download Docker from [here](https://www.docker.com/products/docker-desktop/)


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/ceydaduzgec/SWE573.git
   ```
2. Open project with your favorite code editor and a new terminal.
   ```sh
   cd sole_project
   ```
3. Run Docker infastructure. 
   ```sh
   source tools/run_development.sh
   ```
4. Migrate the database.
  ```python
  python manage.py migrate
  ```

5. Collect static.
  ```python
  python manage.py collectstatic`
  ```

6. (Optional) Create a super user for admin panel.
  ```python
  python manage.py createsuperuser`
  ```

7. Run the server.
  ```python
  python manage.py runserver 0:8000`
  ```

<p align="right">(<a href="#top">back to top</a>)</p>

### Linting
Each commit must be linted. Pre-commit is currently configured for flake8, isort and black. So, please install the pre-commit linter hook by running the following command from the terminal you use `git`:

```
pip install pre-commit
pre-commit install
```
To manually run all pre-commit hooks on a repository:
```
pre-commit run --all-files
```
To update versions of pre-commit hooks to the latest version automatically:
```
pre-commit autoupdate
```


<!-- ROADMAP -->
## Roadmap

- [ ] Milestone 1
- [ ] Milestone 2
- [ ] Milestone 3

See the [open issues](https://github.com/ceydaduzgec/SWE573/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "Type: Enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/SWE573`)
3. Commit your Changes (`git commit -m 'Add some NewFeature'`)
4. Push to the Branch (`git push origin feature/SWE573`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Ceyda Düzgeç - cduzgec@gmail.com

Project Link: [https://github.com/ceydaduzgec/SWE573](https://github.com/ceydaduzgec/SWE573)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Suzan Uskudarlı](https://github.com/uskudarli)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/ceydaduzgec/SWE573.svg?style=for-the-badge
[contributors-url]: https://github.com/ceydaduzgec/SWE573/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ceydaduzgec/SWE573.svg?style=for-the-badge
[forks-url]: https://github.com/ceydaduzgec/SWE573/network/members
[stars-shield]: https://img.shields.io/github/stars/ceydaduzgec/SWE573.svg?style=for-the-badge
[stars-url]: https://github.com/ceydaduzgec/SWE573/stargazers
[issues-shield]: https://img.shields.io/github/issues/ceydaduzgec/SWE573.svg?style=for-the-badge
[issues-url]: https://github.com/ceydaduzgec/SWE573/issues
[license-shield]: https://img.shields.io/github/license/ceydaduzgec/SWE573.svg?style=for-the-badge
[license-url]: https://github.com/ceydaduzgec/SWE573/LICENSE.txt

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/ceydaduzgec/
[product-screenshot]: images/screenshot.png

[Django-image]: https://img.shields.io/badge/Django-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[Django-url]: https://nextjs.org/

[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
