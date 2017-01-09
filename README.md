Welcome to Vericant!
===================

This project is used for Front End/Design/Architecture layouts for new, upcoming features for the Vericant site and its included technologies. The original Front-End development framework was developed using Python's Django/Jinja frameworks intertwined with Bootstrap 3. All design preparations for 2017 and beyond, including this prototype project will be built using the Zurb Foundation front-end
framework. The source code is compiled using a mixture of NPM and Gulp commands which will output a simple, static HTML site.

Although this is a static design framework, this prototype platform will be set up according to a classic MVC (Model-View-Controller) pattern as much as possible - this will allow easy replication and integration with pre-existing Vericant systems and frameworks.

Most of the UI is separated into modular view components. The data is primarily stored in YAML files in order to avoid requiring any sort of back-end database infrastructure. That said, any changes to the data - the site will need to be re-compiled and deployed. There is no real controller logic except using Handlebars to render certain views and elementary logic handles during the compilation process (if-else statements, etc.).

Getting Started
---------------

Development Application Dependencies:
+ You will need to have the following items installed on your local machine to handle setting up this framework correctly.


    Nodejs - www.nodejs.org - Version 6, **NOT VERSION 7**
    Git - www.git-scm.com - Git for the command line

> RE: GIT Installation - Would recommend installing "optional command line tools" in order to bring Linux-like BASH command line functionality to Windows.



+ Once these items are installed, you will need to use Node Package Manager (npm) to install certain dependencies globally to the system. You will need to run an elevated command prompt *(Right click when running command prompt in windows, choosing "Run As Administrator")*


      $ npm install -g gulp
      $ npm install -g foundation-cli

+  Clone the repository in a location of your choosing. After cloning the repository - you will need to install the node dev-dependency modules. Do this by navigating to the root of the repo:


    $ git clone https://github.com/vericant/vericant-prototyping.git
    $ cd vericant-prototyping/
    $ git checkout dev

    $ npm install

+  NPM will install the following important dependencies used for further
    development of this framework:


    gulp (and various gulp dependencies): "^3.9.0"
        // Compiles src to dist

    foundation-sites: "^6.3.0"
        // Foundation Front End Framework

    object-fit-images: "^2.5.3"
        // Imagizer that sets images to fit or fill their div

    panini: "^1.0.0"
        // Handlebars and compilation tool

<center>*Most other devDependencies are for gulp compilation - some may be depreciated in later releases*


+  There are two primary gulp tasks that can be used:


    $ gulp build
        // Compiles the SRC code and distributes it into a newly cleaned DIST

    $ gulp development
        // Compiles and sets WATCH to continue re-compiling as one actively makes changes

Source Code Hierarchy
---------------------

The Vericant Prototyping repository is composed primarily of source code files that are then
compiled using gulp into a distribution that should then be uploaded to a web
server. The /src folder has 6 primary sub-directories:

| src           |          |                                                                                                                                                                                                                                   |
|---------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \|            | assets   | Composed of mostly static files, such as fonts, images, and other various resources; also contains the JS and SCSS folders that are compiled into a single app.css/app.js                                                         |
| \|            | data     | YAML files that serve as the site “data”. These files are similar to JSON objects and are integrated into the views using {{handlebars}} syntax.                                                                                  |
| \|            | helpers  | Additional JS that is **NOT** used for the site, but used to assist in the compilation process; most current helpers extend the handlebars language to include more complex controller functions used during the site compilation |
| \|            | layouts  | default.html - Used to define the page \<head\> and other global elements such as headers and footers                                                                                                                             |
| \|            | pages    | Individual HTML pages placed in the {{body}} of the default.html; Currently comprised of index - about - app - contact.                                                                                                           |
| \|            | partials | Partial HTML snippets organized primarily as “ui-modules”. Some are generated for certain page-specific use; inline SVG elements are also stored here                                                                             |
| node\_modules |          | Created during npm install to contain necessary development modules/code.                                                                                                                                                         |
| dist          |          | Compiled from SRC to prepare site for hosting                                                                                                                                                                                     |
| resources     |          | UI/Design resources. *To be removed...*                                                                                                                                                                                           |



### SASS File Implementation Overview

The SCSS files located in /src/assets are the core design components for both
Foundation framework and the B • OUT Website design.

The SCSS **Root Directory** contains the following configuration files:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
app.scss
    // Imports mixins, settings.scss, font configurations, foundation, and custom SCSS components

settings.scss
    // Required by Foundation Framework. Declares variables used throughout Foundation's SCSS style sheets. Some are preconfigured with new customs for B•OUT, however most are untouched.

mixins.scss
    // New SASS scripting methods for easier CSS compilation

fonts.scss
    // Pretty self-explanatory...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The SCSS **Components Directory** contains mostly files attributed to overall
layout and design paradigms. The most important files to review include:
*\_typography.scss*, *\_layout.scss*, and *\_general.scss*.

The SCSS **Vericant Directory** includes styles specifically set up for Vericant.
There are *ui-modules* which match their corresponding HTML partials; *pages*
which are custom styles set up for specific page layouts (mostly just the
homepage); and *global* which are styles for header, footers, and other global
components used throughout the site.

### JS File Implementation Overview

*Incomplete*
