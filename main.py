from dbx_connector.server import WorkspaceConnection

if __name__ == "__main__":
    print(WorkspaceConnection().list_catalogs())
    print(WorkspaceConnection().list_clusters())
    print(WorkspaceConnection().list_jobs())
    print(WorkspaceConnection().current_user())
