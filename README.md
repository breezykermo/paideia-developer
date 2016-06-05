#Developer's Guide: The Paideia Institute

What follows is an introduction to the various digital humanities initiatives that are currently warm in Paideia's melting pot. This is the beginning of your adventure and eventual contribution to the wonderful world of Paideia.

## Chromium Dictionary
Chromium Dictionary is a Chrome extension that translates Latin or Greek directly in your webpage. It references the lexical parsers over at [the Perseus Project](http://www.perseus.tufts.edu/hopper/), returning a part of the results each time a user highlights a word in a tab where Chromium has been activated.

#### Technologies

 - ES5 JavaScript, with jQuery.
 - Chrome Extension [Platform APIs](https://developer.chrome.com/extensions/api_index)

Chromium also deals with HTTP requests, the foodstuff of web communication. If you have experience with these things, or you're interested in learning about them, head over to the [Chromium repo on Github](https://github.com/breezykermo/chromium), and follow the instructions on the Readme.

#### Ideas for extension

 - Develop Chromiums for Safari and Firefox.
 - Add the ability to view LSJ and Logeion entries in the right-hand panel.
 - More sophisticated styling, features etc.
 - More detailed lexical parsing/dictionary information. The full-bodied realization of this idea is the (no longer maintained) [Alpheios extension](http://alpheios.net/content/about-alpheios) for Firefox.

## Delphin iOS Reader
Delphin is an iOS reader for the [Delphin Classics](https://archive.org/details/delphinclassics103valp), a series of texts published in the late 18th and early 19th centuries, publications of many great Latin classics replete with commentaries and lemmata, all of which are in Latin. Delphin is designed to render these texts in a cleaner, more readable format, allowing users to tap on words to see associated notes and lemmata, and making sure that all the related notes are rendered on the same page.

The app loads in texts that have been marked up in Delphin XML, and then renders each page by calculating how much associated text (sentences, notes & lemmata) can fit on each page, printing as much content as it can on each page without overflow, so that reading on Delphin 'metaphorizes' the idea of reading a book with pages. It does this by categorizing chunks of associated text as 'sense units', rendering as many sense units on a page until overflow, and then cutting the last sense unit (the one that caused overflow) before rendering the page. Delphin was originally developed for iPad, and has since been adapted to an iPhone's smaller screen, using a scroll view when the iPhone's smaller screen doesn't hold even one sense unit.

#### Technologies

 - Swift
 - [iOS Libraries](https://developer.apple.com/library/ios/navigation/)
 - Xcode, XML parsing.

<small>note: Xcode requires a Mac. Sorry Windows chaps.</small>

Delphin is hosted on Bitbucket as a private repo. If you are interested in working on this, email Lachie (Digital Humanities Fellow 2015-16) at [kermode@paideia-institute.org](mailto:kermode@paideia-institute.org).

#### Ideas for extension

 - Android version of Delphin (using either [Android Studio](http://developer.android.com/tools/studio/index.html), or possibly [React Native](https://facebook.github.io/react-native/docs/android-setup.html) if you have experience with React and ES6 JavaScript.
 - Improved experience for iPhone.
 - Better way of reasoning text on a page than 'sense units'.
 - General improvements, features.

## [www.paideia-institute.org](http://www.paideiainstitute.org/): Nationbuilder Website
Paideia's website is not just a description of the institute for publicity's purpose--many of Paideia's program applications, donations, and internal classical tours management is handled through the website's backend, which runs on [Nationbuilder](http://nationbuilder.com/). Form submissions are managed through [123ContactForms](https://www.123contactform.com), and payments are handled through either [Paypal](http://paypal.com/) or [Stripe](https://stripe.com/it).

#### Technologies

 - [Liquid](http://liquidmarkup.org/) templating language
 - [Sass](http://sass-lang.com/) styling sheets
 - HTML, CSS and some JavaScript.
 - [Nationbuilder APIs](http://nationbuilder.com/api_documentation)

The [Paideia Nationbuilder interface](https://paideiainstitute.nationbuilder.com/admin) requires a username and login. Ask [Jason](mailto:pedicone@paideia-institute.org) to create an account for you, or email [Lachie](mailto:kermode@paideia-institute.org) if Jason isn't available.

See the [Nationbuilder specific docs](/nationbuilder.md) in this repo for more information.

#### Ideas for extension

 - More sophisticated Classical Tour teacher pages, using Liquid templating and Nationbuilder APIs.
 - Better documentation for styling, and how to make changes.


## Web Crawling for R&D
Paideia has a repository of scripts that attempt to scrape American High School registrars for useful information about Latin and Classics teachers, in order to keep our records updated.

#### Technologies

 - Python
 - [Scrapy](http://scrapy.org/), web crawling library

Web scraping is the practice of writing scripts to automatically and 'intelligently' crawl certain websites for interesting information, meaning that it deals in HTTP requests, usually through the Terminal or Command Prompt. If you'd like to work on this project, head over to the [Latin Teachers repository on Github](https://github.com/breezycool/latin-teachers), and follow the instructions in the Readme.

#### Ideas for extension

 - Listed in [notes.md](https://github.com/breezycool/latin-teachers/blob/master/notes.md), at the repo.


## Paideia API
The Paideia API is more of an idea than a reality at the moment. It was scaffolded during the creation of [Chromium](https://chrome.google.com/webstore/detail/chromium-dictionary/plpakagjcfpanojjijfdcjlklffcfdah), while we were brainstorming potential uses of the extension. One idea was to use the extension as a way to read 'footnotes' in specifically curated posts, as part of a larger learning experience. This Paideia API was created as an endpoint where that relevant information might be stored. Eventually, we settled on just using Perseus for Chromium v1, without the Paideia API. However, a Paideia API could be useful in several ways:

 - Exist as an endpoint from which applications like [Delphin](https://itunes.apple.com/gd/app/delphin/id1063055464?mt=8) could download data.
 - Service client applications in the Classics, providing a range of useful services; e.g. simple dictionary translation, lexical parsing, make available Paideia data that might be useful more generally.

#### Technologies

 - [Hapi](http://hapijs.com/), a JavaScript framework for developing API endpoints.
 - ES6 JavaScript
 - [Docker](https://www.docker.com/), for shipping on something like [Elastic Beanstalk](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html)
 - Any other set of technologies in which you are comfortable developing APIs, e.g. [FlaskAPI](http://www.flaskapi.org/), [RailsAPI](http://api.rubyonrails.org/), [ExpressJS](http://expressjs.com/), etc.

If you are interested in working on the Paideia API, you can download the [unfinished boiler code on Github](https://github.com/breezykermo/greek-api), and flesh out your imagination in code.
