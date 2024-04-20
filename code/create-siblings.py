# %%
import datalad.api as dl 
import os
from configparser import ConfigParser

# %%
dry_run_status = False

# %%
os.chdir("/home/pranav/work/pranavmishra90/courses")
print(os.getcwd())

# %%
# Load tokens from the secrets fle
parser = ConfigParser()

_ = parser.read('./code/token.secrets')

os.environ['github'] = parser.get('github', 'github-token')
github = parser.get('github', 'github-token')
gin_token = parser.get('gin', 'gin-token')

# %%
# Superdataset
repository_name = "courses"

# %%
# GitHub public

dl.create_sibling_github(
    reponame=repository_name,
	# dataset=public_paths,
    recursive=True,
    recursion_limit=1,
    name="origin",
    existing="reconfigure",
	credential='github',
    access_protocol="ssh",
    publish_depends=None,
    private=False, # PUBLIC repository
    description="Courses superdataset: pranavmishra90/courses",
    dry_run=dry_run_status,
)

# %%
# GitHub private

repository_name = "courses-enrolled"

os.chdir("./enrolled")


dl.create_sibling_github(
    reponame=repository_name,
    recursive=True,
    recursion_limit=1,
    name="origin",
    existing="reconfigure",
	credential='github',
    access_protocol="ssh",
    publish_depends=None,
    private=True, # Private
    description="Courses superdataset: pranavmishra90/courses",
    dry_run=dry_run_status,
)


# %%
# Done