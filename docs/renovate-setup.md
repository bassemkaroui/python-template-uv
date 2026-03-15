# Self-hosted Renovate Setup

This template supports two authentication methods for self-hosted Renovate: **Personal Access Token (PAT)** and **GitHub App**. You choose the method via the `renovate_auth_method` template variable during project generation.

## PAT Authentication (`renovate_auth_method: pat`)

### 1. Create a fine-grained Personal Access Token

1. Go to GitHub **Settings → Developer settings → Personal access tokens → Fine-grained tokens → Generate new token**
2. Set a token name, expiration, and under **Repository access** select the target repo
3. Under **Permissions**, grant the following:

**Repository permissions:**

| Permission        | Access Level   |
| ----------------- | -------------- |
| Commit statuses   | Read and write |
| Contents          | Read and write |
| Dependabot alerts | Read-only      |
| Issues            | Read and write |
| Pull requests     | Read and write |
| Workflows         | Read and write |

**Organization permissions:**

| Permission | Access Level |
| ---------- | ------------ |
| Members    | Read-only    |

4. Click **Generate token** and copy it

### 2. Add the secret to your repository

- **CLI**: `gh secret set RENOVATE_TOKEN` and paste the token when prompted
- **Web UI**: Go to repo **Settings → Secrets and variables → Actions → New repository secret**, name it `RENOVATE_TOKEN`, and paste the token

## GitHub App Authentication (`renovate_auth_method: github_app`)

Using a GitHub App avoids token expiration issues and provides more granular permission control. Additionally, GitHub automatically marks commits authored by a GitHub App as verified, ensuring your commit history shows these changes as authenticated without requiring additional signing.

### 1. Create a GitHub App

1. Go to GitHub **Settings → Developer settings → GitHub Apps → New GitHub App**
2. Set a name (e.g. `renovate-<your-org>`) and homepage URL
3. Under **Webhook**, uncheck **Active** (not needed)
4. Under **Permissions**, grant the following:

**Repository permissions:**

| Permission        | Access Level   |
| ----------------- | -------------- |
| Checks            | Read and write |
| Commit statuses   | Read and write |
| Contents          | Read and write |
| Issues            | Read and write |
| Pull requests     | Read and write |
| Workflows         | Read and write |
| Administration    | Read-only      |
| Dependabot alerts | Read-only      |
| Metadata          | Read-only      |

**Organization permissions:**

| Permission | Access Level |
| ---------- | ------------ |
| Members    | Read-only    |

5. Under **Where can this GitHub App be installed?**, select **Only on this account**
6. Click **Create GitHub App**

### 2. Generate a private key

1. On the App's settings page, scroll to **Private keys**
2. Click **Generate a private key** — a `.pem` file will be downloaded

### 3. Install the App on your repository

1. On the App's settings page, click **Install App** in the sidebar
2. Select your account, then choose your installation scope:
    - **Only select repositories** — pick specific repositories to limit Renovate's scope
    - **All repositories** — if you want Renovate to manage all repositories in your account
3. Click **Install**

### 4. Add the secrets to your repository

You need two secrets:

| Secret                     | Value                                                     |
| -------------------------- | --------------------------------------------------------- |
| `RENOVATE_APP_ID`          | The App ID (found on the App's **General** settings page) |
| `RENOVATE_APP_PRIVATE_KEY` | The full contents of the `.pem` private key file          |

- **CLI**:
    ```bash
    gh secret set RENOVATE_APP_ID
    gh secret set RENOVATE_APP_PRIVATE_KEY < path/to/private-key.pem
    ```
- **Web UI**: Go to repo **Settings → Secrets and variables → Actions → New repository secret** and add each secret
