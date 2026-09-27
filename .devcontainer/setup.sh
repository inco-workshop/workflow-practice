#!/usr/bin/env bash

# Customise the terminal command prompt
printf "export PS1='\\[\\e[3;36m\\]\${PWD#/workspaces/} ->\\[\\e[0m\\] '\n" >> $HOME/.bashrc
export PS1='\[\e[3;36m\]${PWD#/workspaces/} ->\[\e[0m\] '

# Install vim
apt-get update && apt-get install -y vim

cat /usr/local/etc/vscode-dev-containers/first-run-notice.txt


echo "========================================"
echo " Setting up Claude workshop environment"
echo "========================================"


# --------------------------------------------------
# 1. Python packages
# --------------------------------------------------

echo
echo "[1/4] Installing Python packages..."

if [ -f requirements.txt ]; then
    pip install -r requirements.txt
else
    echo "requirements.txt not found, skipping."
fi


# --------------------------------------------------
# 2. uv / uvx
# --------------------------------------------------

echo
echo "[2/4] Installing uv / uvx..."

# 아래 workshop 설정이 $HOME/.local/bin 을 이미 PATH에 추가하므로
# 설치 위치를 거기에 명시적으로 고정하고(installer 기본값은 XDG_BIN_HOME에 좌우됨),
# installer가 rc 파일을 중복으로 건드리지 않게 한다.
export UV_INSTALL_DIR="$HOME/.local/bin"
export UV_NO_MODIFY_PATH=1

curl -fsSL https://astral.sh/uv/install.sh | sh

export PATH="$HOME/.local/bin:$PATH"

uv --version
uvx --version


# --------------------------------------------------
# 3. Claude Code
# --------------------------------------------------

echo
echo "[3/4] Installing Claude Code..."

curl -fsSL https://claude.ai/install.sh | bash


# --------------------------------------------------
# 4. Claude Code wrapper
# --------------------------------------------------

echo
echo "[4/4] Configuring Claude Code..."

CLAUDE_SHELL_CONFIG="$HOME/.claude-workshop.sh"

cat > "$CLAUDE_SHELL_CONFIG" <<'EOF'
# --------------------------------------------------
# Claude Code workshop configuration
# --------------------------------------------------

# Claude Code installer location
export PATH="$HOME/.local/bin:$PATH"


clear_claude_rejected_key() {

    # ~/.claude.json이 없으면 아무것도 하지 않음
    [ -f "$HOME/.claude.json" ] || return 0

    python3 <<'PY'
import json
import os
import tempfile

path = os.path.expanduser("~/.claude.json")

try:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
except (OSError, json.JSONDecodeError):
    raise SystemExit(0)


responses = data.get("customApiKeyResponses")

if not isinstance(responses, dict):
    raise SystemExit(0)


# rejected가 비어 있으면 수정할 필요 없음
if not responses.get("rejected"):
    raise SystemExit(0)


# rejected 기록 초기화
responses["rejected"] = []


# 안전하게 임시 파일을 만든 뒤 교체
directory = os.path.dirname(path)

fd, temp_path = tempfile.mkstemp(
    dir=directory,
    prefix=".claude.json.",
    text=True
)

try:
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    os.replace(temp_path, path)

except Exception:
    try:
        os.remove(temp_path)
    except OSError:
        pass

    raise
PY
}


claude() {

    # 이전에 API Key 사용 질문에서 No를 선택했더라도
    # 다음 실행에서는 다시 선택할 수 있도록 rejected 초기화
    clear_claude_rejected_key

    # 실제 Claude Code 실행
    command claude "$@"
}
EOF


# --------------------------------------------------
# Shell 시작 시 설정 자동 로드
# --------------------------------------------------

SOURCE_LINE='source "$HOME/.claude-workshop.sh"'


# Bash
touch "$HOME/.bashrc"

if ! grep -Fq "$SOURCE_LINE" "$HOME/.bashrc"; then
    echo "$SOURCE_LINE" >> "$HOME/.bashrc"
fi


# Zsh가 존재하면 같이 설정
if [ -f "$HOME/.zshrc" ]; then
    if ! grep -Fq "$SOURCE_LINE" "$HOME/.zshrc"; then
        echo "$SOURCE_LINE" >> "$HOME/.zshrc"
    fi
fi


echo
echo "========================================"
echo " Setup complete!"
echo "========================================"
echo
echo "Open a new terminal and run:"
echo
echo "    claude"
echo
