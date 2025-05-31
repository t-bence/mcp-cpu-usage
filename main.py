from dbx_connector.server import (
    get_username,
    list_accessible_clusters,
    list_accessible_jobs,
)

if __name__ == "__main__":
    print(list_accessible_clusters())
    print(list_accessible_jobs())
    print(get_username())
