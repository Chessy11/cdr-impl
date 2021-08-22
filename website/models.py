"""
Creatable pages used in CodeRed CMS.
"""
from modelcluster.fields import ParentalKey
from coderedcms.forms import CoderedFormField
from coderedcms.models import (
    CoderedArticlePage,
    CoderedArticleIndexPage,
    CoderedEmail,
    CoderedFormPage,
    CoderedWebPage
)


class ArticlePage(CoderedArticlePage):
    """
    Article, suitable for news or blog content.
    """
    class Meta:
        verbose_name = 'Article'
        ordering = ['-first_published_at']

    # Only allow this page to be created beneath an ArticleIndexPage.
    parent_page_types = ['website.ArticleIndexPage']

    template = 'coderedcms/pages/article_page.html'
    search_template = 'coderedcms/pages/article_page.search.html'


class ArticleIndexPage(CoderedArticleIndexPage):
    """
    Shows a list of article sub-pages.
    """
    class Meta:
        verbose_name = 'Article Landing Page'

    # Override to specify custom index ordering choice/default.
    index_query_pagemodel = 'website.ArticlePage'

    # Only allow ArticlePages beneath this page.
    subpage_types = ['website.ArticlePage']

    template = 'coderedcms/pages/article_index_page.html'


class FormPage(CoderedFormPage):
    """
    A page with an html <form>.
    """
    class Meta:
        verbose_name = 'Form'

    template = 'coderedcms/pages/form_page.html'


class FormPageField(CoderedFormField):
    """
    A field that links to a FormPage.
    """
    class Meta:
        ordering = ['sort_order']

    page = ParentalKey('FormPage', related_name='form_fields')


class FormConfirmEmail(CoderedEmail):
    """
    Sends a confirmation email after submitting a FormPage.
    """
    page = ParentalKey('FormPage', related_name='confirmation_emails')


class WebPage(CoderedWebPage):
    """
    General use page with featureful streamfield and SEO attributes.
    """
    class Meta:
        verbose_name = 'Web Page'

    template = 'coderedcms/pages/web_page.html'

class HomePage(CoderedWebPage):
    
    class Meta:
        verbose_name = "Home Landing Page"

    index_query_pagemodel = "website.HomePage"

    subpage_type = ["website.HomePage"]

    template = "website/pages/home_page.html"



class AboutPage(CoderedWebPage):
    
    class Meta:
        verbose_name = "About Page"

    index_query_pagemodel = "website.AboutPage"

    subpage_type = ["website.AboutPage"]

    template = "coderedcms/pages/about_page.html"



class Services(CoderedWebPage):
    
    class Meta:
        verbose_name = "Services Page"

    index_query_pagemodel = "website.Services"

    subpage_type = ["website.Services"]

    template = "coderedcms/pages/services.html"



class Contact(CoderedWebPage):
    
    class Meta:
        verbose_name = "Contact Page"

    index_query_pagemodel = "website.Contact"

    subpage_type = ["website.Contact"]

    template = "coderedcms/pages/contact.html"



