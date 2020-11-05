# My logs what changed in forked version of parsifal

## Reminders

* commented out dropbox, mendeley (check out later if it is needed)

## python3 & Django2 adaption checklist

* account_settings (commented out dropbox, mendeley)
* activities
* authentication (commented out dropbox, mendeley in models.py;
    **reset, reset_confirm (deprecated in 2.0) changed to PasswordResetView and PasswordResetConfirmView !!!! (need testing) **
* blog
* core
* help
* library (in views.py added request as first param in message.error; changed unicode() to str())
    ??? usage of SharedFolder from library.forms, but it was not imported
* reviews.conducting (check: for entry in bib_database.entries, no entries field)
* reviews.planning
* reviews.reporting (check: export.py: WD_ALIGN_PARAGRAPH)
    **(export_review_to_docx cant be im
    ported (commented for now) bc 'from lxml import etree' doesnt work)**
* reviews.settings
* reviews
* utils.elsevier

## Bugs appeared after adaption
- [x] Profile pictures


##  deprecated in Django 2.0

* django.core.urlresolvers.reverse  -> django.urls.reverse
* django.core.context_processors.csrf ---> django.template.context_processors.csrf
* {% load staticfiles %} changed to {% load static %} (templates)
* added on_delete to all models and migrations, where missing


## settings.py
* default database change
* email, dropbox settings in both setting.py and .env
* MIDDLEWARE  (+ UpdateCashe, FetchFromCache middlewares)
* TEMPLATE_CONTEXT_PROCESSORS ---> TEMPLATES (default from https://docs.djangoproject.com/en/3.1/topics/templates/ example)
* PROJECT_DIR from Path to os module
* SESSION_ENGINE added

## urls
split up SciLRtool/urls so that it contains only include() function: added urls.py to reviews.settings

# Improvements & Updates

* added admin.py to authentication to track Profiles of users

