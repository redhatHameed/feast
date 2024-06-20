import enum
from typing import Any, List, Union

import pandas as pd


class AuthzedAction(enum.Enum):
    """
    To identify the type of action, according to the familiar CRUD terminology.
    """

    ALL = "all"
    READ = "read"
    EDIT = "edit"  # Create-Update-Delete


def assert_permissions(
    resource: Any, actions: Union[AuthzedAction, List[AuthzedAction]]
):
    # Implement your permission assertion logic
    pass


def require_permissions(
    resource: Any, actions: Union[AuthzedAction, List[AuthzedAction]]
):
    def decorator(f):
        def wrapped_function(*args, **kwargs):
            assert_permissions(resource, actions)
            return f(*args, **kwargs)

        return wrapped_function

    return decorator


security_metrics = {
    "Resource": [
        "data-sources",
        "entities",
        "feature-services",
        "feature-views",
        "on-demand-feature-views",
    ],
    "Actions": [
        "READ, EDIT",
        "READ, EDIT",
        "READ, EDIT",
        "READ, EDIT",
        "READ, EDIT",
    ],
    "Function_Name": [
        "list_data_sources",
        "list_entities",
        "list_feature_services",
        "get_feature_view",
        "list_on_demand_feature_views",
    ],
}
df = pd.DataFrame(security_metrics)
# df.to_csv('Feast_Security_Matrix.csv', index=False)

print(df)
