# Maintaining the Spitch Python SDK

Spitch maintains the client, types, and tests directly in this repository. For an API change, update the affected resource and types, the relevant examples in the README or API reference, the HTTP fixtures in `scripts/http-fixtures.json`, and the corresponding resource tests. Preserve existing imports, request headers, and the documented public interface.

## Development

Install Python 3.12, uv 0.8.14 and Node.js 22. Run `./scripts/bootstrap` to install dependencies and `./scripts/ci` to run lint, type checks, tests and clean distribution installation checks. Run `./scripts/test` for the test suite alone. Tests start a loopback server on an ephemeral port.

AWS CodeBuild reports `codebuild/spitch-python-ci` on pull requests to main and pushes to main. Spitch maintainers can approve external fork builds in GitHub. Read logs in the eu-south-2 CodeBuild project `spitch-native-spitch-python-ci`.

## Releasing

1. Update the package version, runtime version and CHANGELOG.md in one PR. Merge after CI passes.
2. Tag the reviewed commit with a stable version, for example `git tag vX.Y.Z <commit>`, then push that tag to origin.
3. Sign in to the GitHub CLI and AWS CLI with read access to this project's builds. Run `./scripts/release vX.Y.Z --dry-run`. It clones the tag, verifies its ancestry, versions, GitHub status and AWS result, and builds and tests the distributions.
4. Configure a package-scoped PyPI token via UV_PUBLISH_TOKEN. Run `./scripts/release vX.Y.Z` to publish, verify registry digests, and create the GitHub release. Retry the same command if an upload or GitHub release step was interrupted. A different digest for an existing file requires maintainer investigation.
