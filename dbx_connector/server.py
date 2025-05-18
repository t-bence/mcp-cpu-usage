from databricks.sdk import WorkspaceClient
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("SecretServer")


class WorkspaceConnection:
    def __init__(self):
        load_dotenv()
        # Login works automatically with the correct environment variable names
        self.client = WorkspaceClient()

    def list_catalogs(self) -> str:
        return "\n".join(
            catalog.name for catalog in self.client.catalogs.list(include_browse=False)
        )

    def list_clusters(self) -> str:
        cluster_details = [
            f"{cluster.cluster_name}: {cluster.state.value}"
            for cluster in self.client.clusters.list()
        ]
        if not cluster_details:
            return "No clusters found."
        return "\n".join(cluster_details)

    def list_jobs(self) -> str:
        job_details = [f"{job.settings.name}: {job}" for job in self.client.jobs.list()]
        if not job_details:
            return "No jobs found."
        return "\n".join(job_details)

    def current_username(self) -> str:
        return self.client.current_user.me().user_name


@mcp.tool(description="Returns the list of catalogs the user can access")
def list_accessible_catalogs() -> str:
    return WorkspaceConnection().list_catalogs()


@mcp.tool(description="Returns the list of clusters the user can access")
def list_accessible_clusters() -> str:
    return WorkspaceConnection().list_clusters()


@mcp.tool(description="Returns the list of jobs the user can access")
def list_accessible_jobs() -> str:
    return WorkspaceConnection().list_jobs()


@mcp.tool(description="Return the user's username in the workspace")
def get_username() -> str:
    return WorkspaceConnection().current_username()
