import os
import subprocess
import sys
import webbrowser

def run_command(command, check=True):
    try:
        # Run command and capture output
        result = subprocess.run(command, shell=True, text=True, capture_output=True, check=check)
        return True, result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return False, e.stderr.strip()

def main():
    print("🚀 Welcome to the Groww FAQ AI Bot GitHub Uploader!")
    print("====================================================")
    
    username = "akanakshajaiswalwork"
    repo_name = "groww-faq-ai-bot"
    
    # 1. Check if git is installed
    git_installed, _ = run_command("git --version", check=False)
    if not git_installed:
        print("❌ Error: Git is not installed on your system. Please install Git first.")
        sys.exit(1)
        
    # 2. Check if it's a git repo
    if not os.path.exists(".git"):
        print("📁 Initializing git repository...")
        run_command("git init")
    else:
        print("✅ Git repository already initialized.")

    # 3. Add all files
    print("📦 Staging files for commit...")
    run_command("git add .")
    
    # 4. Commit files
    # Check if there is anything to commit
    _, status_out = run_command("git status --porcelain")
    if status_out:
        print("💾 Committing files...")
        run_command('git commit -m "Initial commit - Groww FAQ AI Bot"')
    else:
        print("✅ No new changes to commit.")

    # Set branch to main
    run_command("git branch -M main")

    # 5. Check if GitHub CLI is installed and logged in
    gh_installed, _ = run_command("gh --version", check=False)
    gh_auth = False
    if gh_installed:
        gh_auth, auth_status = run_command("gh auth status", check=False)
        
    repo_created = False
    
    if gh_installed and gh_auth:
        print("🤖 GitHub CLI (gh) detected and authenticated!")
        print(f"Creating repository '{repo_name}' on GitHub under username '{username}'...")
        # Create repo using gh CLI
        success, out = run_command(f"gh repo create {username}/{repo_name} --public --source=. --push", check=False)
        if success:
            print("🎉 Repository successfully created and pushed to GitHub!")
            repo_created = True
        else:
            if "already exists" in out or "already exists" in out.lower():
                print(f"ℹ️ Repository '{repo_name}' already exists on GitHub. Trying to set remote and push...")
            else:
                print(f"⚠️ Warning: GitHub CLI failed to create the repository. Error: {out}")
    
    if not repo_created:
        # Check if remote origin already exists
        _, remote_out = run_command("git remote get-url origin", check=False)
        
        target_remote = f"https://github.com/{username}/{repo_name}.git"
        
        if not remote_out:
            print(f"🔗 Setting remote origin to: {target_remote}")
            run_command(f"git remote add origin {target_remote}")
        else:
            if remote_out != target_remote:
                print(f"🔄 Updating remote origin to: {target_remote}")
                run_command(f"git remote set-url origin {target_remote}")
        
        print("\n🌐 Opening browser to create the repository on GitHub...")
        print(f"Please click 'Create repository' on the page that opens.")
        print(f"URL: https://github.com/new?name={repo_name}")
        
        # Open browser to create new repo
        webbrowser.open(f"https://github.com/new?name={repo_name}")
        
        input("\nPress [ENTER] AFTER you have successfully created the repository on GitHub web interface to push your code...")
        
        print("📤 Pushing code to GitHub...")
        push_success, push_err = run_command("git push -u origin main", check=False)
        if push_success:
            print("🎉 Code pushed successfully!")
        else:
            print(f"❌ Failed to push. Error:\n{push_err}")
            print("\n💡 Troubleshooting tips:")
            print("1. Make sure you created the repo with the exact name 'groww-faq-ai-bot'.")
            print("2. Ensure your local machine is authenticated with GitHub (e.g. SSH key or Personal Access Token).")
            print("3. If you created the repo with a README or License on GitHub, pull first: git pull origin main --rebase")
            sys.exit(1)

    print("\n✅ Setup complete! You can now check your repository at:")
    print(f"🔗 https://github.com/{username}/{repo_name}")
    print("\nNext step: To deploy this on Streamlit, go to https://share.streamlit.io/, connect this repository, and set your GROQ_API_KEY in the Secrets section!")

if __name__ == "__main__":
    main()
