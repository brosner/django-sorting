from setuptools import setup, find_packages

version = '0.1'

LONG_DESCRIPTION = """
How to use django-sorting
----------------------------

``django-sorting`` allows for easy sorting, and tables headers (<th>) generation
without modifying your views.

There are really 5 steps to setting it up with your projects.

1. List this application in the ``INSTALLED_APPS`` portion of your settings
   file.  Your settings file might look something like::

       INSTALLED_APPS = (
           # ...
           'sorting',
       )

2. Install the sorting middleware. Your settings file might look something
   like::

       MIDDLEWARE_CLASSES = (
           # ...
           'sorting.middleware.SortingMiddleware',
       )

3. If it's not already added in your setup, add the request context processor.
   Note that context processors are set by default implicitly, so to set them
   explicitly, you need to copy and paste this code into your under
   the value TEMPLATE_CONTEXT_PROCESSORS::

        ("django.core.context_processors.auth",
        "django.core.context_processors.debug",
        "django.core.context_processors.i18n",
        "django.core.context_processors.media",
        "django.core.context_processors.request")

4. Add this line at the top of your template to load the sorting tags:

       {% load sorting_tags %}


5. Decide on a variable that you would like to sort, and use the
   autosort tag on that variable before iterating over it.

       {% autosort object_list %}


6. Now, you want to display different headers with links to sort
your objects_list:
    <div class="my_container">
    ...
    <tr>
       <th>{% anchor first_name "First Name" %}</th>
       <th>{% anchor last_name "Last Name" %}</th>
       <th>{% anchor creation_date Creation flojax my_container %}</th>
        ...
    </tr>
    </div>
    The first argument is a field of the objects list, and the second
    one(optional) is a title that would be displayed. The previous
    snippet will be rendered like this:

    <div class="my_container">
    ...
    <tr>
        <th><a href="/path/to/your/view/?sort=first_name" title="First Name">First Name</a></th>
        <th><a href="/path/to/your/view/?sort=last_name" title="Last Name">Last Name</a></th>
        <th><a href="/path/to/your/view/?sort=creation_date" title="Name" class="flojax" rel="my_container">Creation</a></th>
        ...
    </tr>
    </div>

That's it!
"""

setup(
    name='django-sorting',
    version=version,
    description="Like ericflo's django pagination, but this one does the sorting! used with ericflo's pagination, displaying tabular paginated and sortable data is very easy",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='sorting,pagination,django',
    author='directeur',
    url='http://github.com/ericflo/django-sorting/tree/master',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
)