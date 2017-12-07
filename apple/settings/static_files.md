Settings for django.contrib.staticfiles.

-   STATIC_ROOT
-   STATIC_URL
-   STATICFILES_DIRS
-   STATICFILES_STORAGE
-   STATICFILES_FINDERS


### STATIC_ROOT

default: None

-   The absolute path to the directory where collectstatic will collect static
    files for deployment.

        "/var/www/example.com/static/"

    If the staticfiles contrib app is enabled (as in the default project template),
    the `collectstatic` management command will collect static files into this
    directory. 

        python manage.py collectstatic


### STATIC_URL

default: None

-   URL to use when referring to static files located in STATIC_ROOT. 

        "/static/" or "http://static.example.com/"

    If not None, this will be used as the base path for asset definitions
    (the Media class) and the staticfiles app.

    It must end in a slash if set to a non-empty value.


### STATICFILES_DIRS

default: []

-   This setting defines the additional locations the staticfiles app will
    traverse if the FileSystemFinder finder is enabled, e.g. if you use the
    `collectstatic` or `findstatic` management command or use the static file
    serving view.

    This should be set to a list of strings that contain full paths to your
    additional files directory(ies) e.g.:

        STATICFILES_DIRS = [
            "/home/special.polls.com/polls/static",
            "/home/polls.com/polls/static",
            "/opt/webfiles/common",
        ]

    Note that these paths should use Unix-style forward slashes, even on Windows
    (e.g. "C:/Users/user/mysite/extra_static_content").

-   Prefixes (optional)    

    In case you want to refer to files in one of the locations with an additional
    namespace, you can optionally provide a prefix as (prefix, path) tuples, e.g.:

        STATICFILES_DIRS = [
            # ...
            ("downloads", "/opt/webfiles/stats"),
        ]

    For example, assuming you have STATIC_URL set to '/static/', the collectstatic
    management command would collect the “stats” files in a 'downloads' subdirectory
    of STATIC_ROOT.

    This would allow you to refer to the local file '/opt/webfiles/stats/polls_20101022.tar.gz'
    with '/static/downloads/polls_20101022.tar.gz' in your templates, e.g.:

        <a href="{% static "downloads/polls_20101022.tar.gz" %}">


### STATICFILES_STORAGE

Default: 'django.contrib.staticfiles.storage.StaticFilesStorage'

-   The file storage engine to use when collecting static files with the
    collectstatic management command.

    A ready-to-use instance of the storage backend defined in this setting can
    be found at django.contrib.staticfiles.storage.staticfiles_storage.


### STATICFILES_FINDERS

default:

    [
        'django.contrib.staticfiles.finders.FileSystemFinder',      # find in the STATICFILES_DIRS
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',  # find in each app directory
    ]

-   The list of finder backends that know how to find static files in various
    locations.

    The default will find files stored in the STATICFILES_DIRS setting (using
    django.contrib.staticfiles.finders.FileSystemFinder) and in a static subdirectory
    of each app (using django.contrib.staticfiles.finders.AppDirectoriesFinder).
    If multiple files with the same name are present, the first file that is
    found will be used.

    One finder is disabled by default: django.contrib.staticfiles.finders.DefaultStorageFinder.
    If added to your STATICFILES_FINDERS setting, it will look for static files
    in the default file storage as defined by the DEFAULT_FILE_STORAGE setting.

-   Note: When using the AppDirectoriesFinder finder, make sure your apps can be
    found by staticfiles. Simply add the app to the INSTALLED_APPS setting of your site.

---

### Configuring static files

以下操作适合使用在开发/测试环境下(也就是 DEBUG = True)

1.  Make sure that django.contrib.staticfiles is included in your INSTALLED_APPS.

    注意：django.contrib.staticfiles 只有在 DEBUG = True 时帮助获取 static 文件。

2.  In your settings file, define STATIC_URL, for example:

        STATIC_URL = '/static/'

3.  In your templates, either hardcode the url like /static/my_app/example.jpg
    or, preferably, use the static template tag to build the URL for the given
    relative path by using the configured STATICFILES_STORAGE storage (this
    makes it much easier when you want to switch to a content delivery network
    (CDN) for serving static files).

        {% load static %}
        <img src="{% static "my_app/example.jpg" %}" alt="My image"/>

4.  Store your static files in a folder called static in your app. For example
    my_app/static/my_app/example.jpg.

In addition to these configuration steps, you’ll also need to actually serve
the static files. During development, if you use django.contrib.staticfiles,
this will be done automatically by runserver when DEBUG is set to True (see 
django.contrib.staticfiles.views.serve(), this method is grossly inefficient
and probably insecure, so it is unsuitable for production).


### Serving static files in production

The basic outline of putting static files into production is simple: run the
`collectstatic` command when static files change, then arrange for the collected
static files directory (STATIC_ROOT) to be moved to the static file server and
served. Depending on STATICFILES_STORAGE, files may need to be moved to a new
location manually or the post_process method of the Storage class might take
care of that.

#### Serving the site and your static files from the same server

If you want to serve your static files from the same server that’s already
serving your site, the process may look something like:

1.  Push your code up to the deployment server.

2.  On the server, run collectstatic to copy all the static files into STATIC_ROOT.

3.  Configure your web server to serve the files in STATIC_ROOT under the STATIC_URL.


#### Serving static files from a dedicated server

Most larger Django sites use a separate Web server – i.e., one that’s not also
running Django – for serving static files. This server often runs a different
type of web server – faster but less full-featured.

Since your static file server won’t be running Django, you’ll need to modify the
deployment strategy to look something like:

When your static files change, run collectstatic locally. Push your local 
STATIC_ROOT up to the static file server into the directory that’s being 
served. `rsync` is a common choice for this step since it only needs to
transfer the bits of static files that have changed.

#### Serving static files from a cloud service or CDN

Another common tactic is to serve static files from a cloud storage provider
like Amazon’s S3 and/or a CDN (content delivery network). This lets you ignore
the problems of serving static files and can often make for faster-loading Web
pages (especially when using a CDN).

When using these services, the basic workflow would look a bit like the above,
except that instead of using rsync to transfer your static files to the server
you’d need to transfer the static files to the storage provider or CDN.

There’s any number of ways you might do this, but if the provider has an API a
custom file storage backend will make the process incredibly simple. If you’ve
written or are using a 3rd party custom storage backend, you can tell
collectstatic to use it by setting STATICFILES_STORAGE to the storage engine.

For example, if you’ve written an S3 storage backend in myproject.storage.S3Storage
you could use it with:

    STATICFILES_STORAGE = 'myproject.storage.S3Storage'

Once that’s done, all you have to do is run collectstatic and your static files
would be pushed through your storage package up to S3. If you later needed to
switch to a different storage provider, it could be as simple as changing your
STATICFILES_STORAGE setting.
