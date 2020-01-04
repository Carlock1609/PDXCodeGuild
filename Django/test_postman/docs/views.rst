Custom views
============

The simplest way to access to the default standard views of Postman is to include the provided URLconf module.
This can be done in the root URLconf of the site::

    path('messages/', include('postman.urls', namespace='postman')),

If you want customized views, make a copy of the original module to another location (for example, your main
application or the project root), reference it in the root URLconf, and tune the parameters in the view calls.

Example::

    # in mysite/urls.py
    # ...
    path('messages/', include('mysite.postman_urls', namespace='postman')),

::

    # in mysite/postman_urls.py
    # ...
    # from postman.views import ...
    # ...
    urlpatterns = [
        # ...
        # re_path(… ✂ …View.as_view(... add parameters here ...),… ✂ …
        # ...
    ]

.. _styles:

styles
------
Here is a sample of some CSS rules, usable for :file:`postman/views.html`::

    .pm_message.pm_deleted             { text-decoration: line-through; }
    .pm_message.pm_deleted .pm_body    { display: none; }
    .pm_message.pm_archived            { font-style: italic; color: grey; }
    .pm_message.pm_unread .pm_subject  { font-weight: bolder; }
    .pm_message.pm_pending .pm_header  { background-color: #FFC; }
    .pm_message.pm_rejected .pm_header { background-color: #FDD; }

These rules are provided with the application, as an example, in a static file (See :ref:`static files`).

forms
-----

You can replace the default forms in views.

Examples::

    urlpatterns = [
        # ...
        re_path(r'… ✂ …',
            WriteView.as_view(form_classes=(MyCustomWriteForm, MyCustomAnonymousWriteForm)),
            name='write'),
        re_path(r'… ✂ …',
            ReplyView.as_view(form_class=MyCustomFullReplyForm),
            name='reply'),
        re_path(r'… ✂ …',
            MessageView.as_view(form_class=MyCustomQuickReplyForm),
            name='view'),
        # ...
    ]

templates
---------

You can replace the default template name in all views.

Example::

    urlpatterns = [
        # ...
        re_path(r'… ✂ …',
            MessageView.as_view(template_name='my_custom_view.html'),
            name='view'),
        # ...
    ]

after submission
----------------

You can supersede the default view where to return to, after a successful submission.

The default algorithm is:

#. Return where you came from
#. If it cannot be known, fall back to the inbox view
#. But if the submission view has a ``success_url`` parameter, use it preferably
#. In all cases, a ``next`` parameter in the query string has higher precedence

The parameter ``success_url`` is available to these views:

* ``WriteView``
* ``ReplyView``
* ``ArchiveView``
* ``DeleteView``
* ``UndeleteView``

Example::

    urlpatterns = [
        # ...
        re_path(r'… ✂ …',
            ReplyView.as_view(success_url='postman:inbox'), name='reply'),
        # ...
    ]

Example::

    <a href="{% url 'postman:reply' reply_to_pk %}?next={{ next_url|urlencode }}">Reply</a>

reply formatters
----------------

You can replace the default formatters used for replying.

Examples::

    def format_subject(subject):
        return "Re_ " + subject

    def format_body(sender, body):
        return "{0} _ {1}".format(sender, body)

    urlpatterns = [
        # ...
        re_path(r'… ✂ …',
            ReplyView.as_view(formatters=(format_subject, format_body)),
            name='reply'),
        re_path(r'… ✂ …',
            MessageView.as_view(formatters=(format_subject, format_body)),
            name='view'),
        # ...
    ]

See also:

* the ``POSTMAN_QUICKREPLY_QUOTE_BODY`` setting in :ref:`optional_settings`
