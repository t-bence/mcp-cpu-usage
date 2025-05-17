import os

from databricks.sdk import WorkspaceClient
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("SecretServer")


@mcp.tool()
def get_secret_number() -> int:
    """Returns a predefined secret number."""
    return 13


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
        return "\n".join(
            f"{cluster.cluster_name}: {cluster.state.value}"
            for cluster in self.client.clusters.list()
        )

    def list_jobs(self) -> str:
        return "\n".join(
            f"{job.settings.name}: {job}" for job in self.client.jobs.list()
        )

    def current_user(self) -> str:
        return self.client.current_user.me().user_name


@mcp.tool(description="Returns a list of catalogs the user can access")
def list_accessible_catalogs() -> str:
    return WorkspaceConnection().list_catalogs()
