from databricks.sdk import WorkspaceClient
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("DatabricksServer")

load_dotenv()


@mcp.tool(description="Returns the list of clusters the user can access")
def list_accessible_clusters() -> str:
    client = WorkspaceClient()
    cluster_details = [
        f"{cluster.cluster_name}: {cluster.state.value}"
        for cluster in client.clusters.list()
    ]
    if not cluster_details:
        return "No clusters found."
    return "\n".join(["The list of clusters the user has access to:"] + cluster_details)


@mcp.tool(description="Returns the list of jobs the user can access")
def list_accessible_jobs() -> str:
    client = WorkspaceClient()
    job_details = [f"{job.settings.name}: {job}" for job in client.jobs.list()]
    if not job_details:
        return "No jobs found."
    return "\n".join(job_details)


@mcp.tool(description="Return the user's username in the workspace")
def get_username() -> str:
    client = WorkspaceClient()
    return client.current_user.me().user_name
