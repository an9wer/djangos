from .uniquetogether import UniqueTogetherModel, NullUniqueTogetherModel
from .db_table import DbTableModel
from .proxy import ProxyModel, ExtraProxyModel


"""
Model metadata is “anything that’s not a field”, such as ordering options
(ordering), database table name (db_table), or human-readable singular and
plural names (verbose_name and verbose_name_plural). None are required, and
adding class Meta to a model is completely optional.

"""
