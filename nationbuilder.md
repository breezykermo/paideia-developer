# [www.paideia-institute.org](http://www.paideiainstitute.org/): Nationbuilder Website
Paideia's website is not just a description of the institute for publicity's purpose--many of Paideia's program applications, donations, and internal classical tours management is handled through the website's backend, which runs on [Nationbuilder](http://nationbuilder.com/). Form submissions are managed through [123ContactForms](https://www.123contactform.com), and payments are handled through either [Paypal](http://paypal.com/) or [Stripe](https://stripe.com/it).

#### Technologies

 - [Liquid](http://liquidmarkup.org/) templating language
 - [Sass](http://sass-lang.com/) styling sheets
 - HTML, CSS and some JavaScript.
 - [Nationbuilder APIs](http://nationbuilder.com/api_documentation)

 Nationbuilder is a pretty sophisticated platform for non-profit organizations, which makes your job as a developer very happy. Almost all of the site's functionality is pre-packaged, including the content management system, money handling, the blog engine, and the people tracking system. Your primary responsibility as a developer is to tweak configuration and styling, rather than to actually build out any functionality.

 Once you log into through the [admin portal](https://paideiainstitute.nationbuilder.com/admin/streams/activity), you'll see the splash page for the admin interface.

 ![Admin splash](/media/admin-splash.png)

 There's a lot to see here, but luckily as a developer you are really only interested in the 'Website' tab on the top. Nationbuilder allows organizations to manage multiple websites through one admin portal, but we at Paideia just have the one website, 'The Paideia Institute'.

 Once you click through, you'll be brought to a list of all the pages on the current site. Click on some of the pages, and get a feel for how they look in the backend; each page has topbar with tabs such as 'Content', 'Settings', and 'Subpages'.

 ![Home page backend](/media/home-page.png)

 Most of these titles are fairly self-explanatory, and if anything seems obscure there is plenty of [documentation online](http://nationbuilder.com/docs) that can explain some of the finer points.

 Of these headings, the 'Template' section is the most relevant for you as a developer. The template is a document written in [Liquid markup](https://shopify.github.io/liquid/), and this template determines what the HTML page that the user loads on the Paideia website will look like. What the template does is interpolate values from the Nationbuilder backend into an HTML document. Therefore, when something is changed in the Nationbuilder backend (i.e., someone's personal profile gets updated), the site will change as well. For example, our [people page](http://www.paideiainstitute.org/people) pulls all profiles from the Nationbuilder backend that have a Staff tag, and creates a clickable picture for each. This is specified in the [people page template](https://paideiainstitute.nationbuilder.com/admin/sites/1/pages/21/template) (NB: profiles in Nationbuilder syntax are called 'directory listings'. The line 16 liquid code, `for signup in page.directory.listings` is the line of code that loops through profiles).

 There are several different types of page in Nationbuilder, such as Basic pages, Directory pages and Donation pages. Each page allows you to access the information in the Nationbuilder backend in slightly different ways, and has different configuration settings in the content management system. For example, our primary [donation page](https://paideiainstitute.nationbuilder.com/admin/sites/1/pages/4/activities) has two tabs for settings in the backend, one that configures standard page settings, and another that configures Donation page specific settings. I would suggest reading through the docs online to get a feel for what these different types of pages can do.

 Besides configuring pages and tweaking the way they read values from the backend, the other mode in which you'll be editing Nationbuilder is through [its stylesheets](https://paideiainstitute.nationbuilder.com/admin/sites/1/themes/557af32c2213932c75000001/attachments/page_templates). Nationbuilder uses [Sass](http://sass-lang.com/) stylesheets, which is esentially CSS with a couple of handy extra features. The stylesheets effect the entire site, and are part of a particular theme.

 The theme the Paideia site uses is called 'Dodici Venerdi', which is a theme I wrote in 2015. It is separated into a bunch of different fragments, which sometimes make it hard to know where exactly relevant styles are located. Also, because of the way CSS '[cascades](http://stackoverflow.com/questions/1043001/what-is-the-meaning-of-cascading-in-css)', it is sometimes the case that even when you find the right class, it doesn't affect your HTML in the way you expect it to. Just some things to be aware of.

 Hopefully this is enough information to get you started with Nationbuilder. The best place to start is with practice; play around with the backend, create pages (make sure they are unlisted or hidden, so that they don't show up on the live site!), and generally get a feel for things. Be careful not to mess with preexisting content, as *the backend is linked to the live site*; if you delete a page or make some other adjustment it **will** modify the live site.

 Hit me up on Slack or via email, kermode@paideia-institute.org, if you have any questions.
