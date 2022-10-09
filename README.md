<h1 align="center">Welcome to mock-buddy-slide-server 👋</h1>
<p>
  <a href="#" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
</p>

> This repo contains slide processing service (microservice) for [Mock-buddy](https://github.com/Karthick47v2/mock-buddy) application, uses Flask to build RESTful APIs, you can see project description [here](https://github.com/Karthick47v2/mock-buddy). This service is deployed on Heroku.

A slide is a single page projected on a screen, usually built on the premise of a title, body, and figures or tables and includes both what is shown and what is spoken about that slide. This system will analyze Google Slide and give report about fine details of how to design a slide for optimal effect—such as the design elements that allow slides to convey meaningful information, to keep the audience engaged and informed, and to deliver the information intended and in the time frame allowed.

Workflow is,

1. Check for spelling and grammatical errors
2. Check slide violates rules of effective presenation.

- ### Spelling and Grammatical erros

  System will analyze presentation slide and report errors found along with suggestions with the help of [LanguageTool](https://languagetool.org/).

- ### Evaluate effectiveness of presentation

  System will analyze presentation slide for number of slides, words per slide, shapes and pictures per slide and so on. Then give feedback about which things needs to be optimized.

## Prerequisite

- Java JDK 8 or newer (To launch LanguageTool server)
- Python 3.7 or newer

## Install

```
pip install -r requirements.txt
```

## Usage

```
python3 app.py
```

## Author

👤 **Karthick T. Sharma**

- Github: [@Karthick47v2](https://github.com/Karthick47v2)
- LinkedIn: [@Karthick47](https://linkedin.com/in/Karthick47)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/Karthick47v2/mock-buddy-slide-server/issues).

## Show your support

Give a ⭐️ if this project helped you!
