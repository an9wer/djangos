from .field_options import *
from .relationship_fields import *
from .meta_options import *
from .aggregation import *
from .field_types import *


"""
(How can I see the raw SQL queries Django is running?)
[https://docs.djangoproject.com/en/1.11/faq/models/#how-can-i-see-the-raw-sql-queries-django-is-running]

1.  connection.queries is only available if DEBUG is True. 

        >>> from django.db import connection
        >>> connection.queries
        [{'sql': 'SELECT polls_polls.id, polls_polls.question, polls_polls.pub_date FROM polls_polls',
        'time': '0.002'}]

    it’s a list of dictionaries in order of query execution. Each dictionary has the following:

        ``sql`` -- The raw SQL statement
        ``time`` -- How long the statement took to execute, in seconds.

    If you are using multiple databases, you can use the same interface on 
    each member of the connections dictionary:

        >>> from django.db import connections
        >>> connections['my_db_alias'].queries

    If you need to clear the query list manually at any point in your functions,
    just call reset_queries(), like this:

        >>> from django.db import reset_queries
        >>> reset_queries()

2.  使用 QuerySet.query 来获取该 QuerySet 的 SQL 语句

"""
