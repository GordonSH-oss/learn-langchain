#!/bin/bash
# 清除所有 Git 历史记录并强制推送到远程

set -e

REPO_PATH="/Users/admin/Workspace@RongCloud/For-learning/learn-langchain-langgraph"
cd "$REPO_PATH"

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${RED}🚨 警告：此操作将删除所有 Git 历史记录！${NC}"
echo ""
echo -e "${YELLOW}此操作将：${NC}"
echo "1. 删除所有现有的 Git 历史"
echo "2. 创建一个全新的初始 commit"
echo "3. 强制推送到远程仓库（覆盖所有历史）"
echo ""
echo -e "${RED}⚠️  这将永久删除所有 commit 历史！${NC}"
echo ""

read -p "确认继续？(yes/no): " confirm

if [ "$confirm" != "yes" ]; then
    echo "已取消操作"
    exit 0
fi

# 检查是否是 git 仓库
if [ -d ".git" ]; then
    echo -e "${BLUE}检测到现有 Git 仓库，删除历史...${NC}"
    
    # 获取远程仓库信息（如果有）
    REMOTE_URL=$(git remote get-url origin 2>/dev/null || echo "")
    REMOTE_BRANCH=$(git branch --show-current 2>/dev/null || echo "main")
    
    # 删除 .git 目录
    rm -rf .git
    echo -e "${GREEN}✅ 已删除现有 Git 历史${NC}"
else
    echo -e "${BLUE}未检测到 Git 仓库，将创建新仓库${NC}"
    REMOTE_URL=""
    REMOTE_BRANCH="main"
fi

# 初始化新的 Git 仓库
echo -e "${GREEN}初始化新的 Git 仓库...${NC}"
git init

# 设置默认分支为 main
git branch -M main

# 添加所有文件
echo -e "${GREEN}添加所有文件...${NC}"
git add .

# 创建初始 commit
echo -e "${GREEN}创建初始 commit...${NC}"
git commit -m "Initial commit - cleared all history"

# 如果有远程仓库，添加并强制推送
if [ -n "$REMOTE_URL" ]; then
    echo -e "${GREEN}添加远程仓库: ${REMOTE_URL}${NC}"
    git remote add origin "$REMOTE_URL"
    
    echo -e "${YELLOW}准备强制推送到远程...${NC}"
    echo -e "${RED}⚠️  这将覆盖远程仓库的所有历史！${NC}"
    read -p "确认推送到远程？(yes/no): " push_confirm
    
    if [ "$push_confirm" == "yes" ]; then
        echo -e "${GREEN}强制推送所有分支...${NC}"
        git push -f origin main
        
        echo -e "${GREEN}强制推送所有标签（如果有）...${NC}"
        git push -f origin --tags 2>/dev/null || echo "没有标签需要推送"
        
        echo -e "${GREEN}✅ 已强制推送到远程${NC}"
    else
        echo -e "${YELLOW}已跳过远程推送${NC}"
        echo "你可以稍后手动执行："
        echo "  git remote add origin <your-remote-url>"
        echo "  git push -f origin main"
    fi
else
    echo -e "${YELLOW}未找到远程仓库配置${NC}"
    echo ""
    read -p "是否要添加远程仓库？(yes/no): " add_remote
    
    if [ "$add_remote" == "yes" ]; then
        read -p "请输入远程仓库 URL: " remote_url
        if [ -n "$remote_url" ]; then
            git remote add origin "$remote_url"
            
            echo -e "${YELLOW}准备强制推送到远程...${NC}"
            read -p "确认推送？(yes/no): " push_confirm
            
            if [ "$push_confirm" == "yes" ]; then
                git push -f origin main
                echo -e "${GREEN}✅ 已推送到远程${NC}"
            fi
        fi
    fi
fi

echo ""
echo -e "${BLUE}═══════════════════════════════════════${NC}"
echo -e "${GREEN}✅ 操作完成！${NC}"
echo -e "${BLUE}═══════════════════════════════════════${NC}"
echo ""
echo -e "${GREEN}当前状态：${NC}"
echo "- Git 历史已清除"
echo "- 创建了新的初始 commit"
if [ -n "$REMOTE_URL" ] || [ -n "$(git remote -v 2>/dev/null)" ]; then
    echo "- 已推送到远程仓库"
fi
echo ""
echo -e "${YELLOW}⚠️  重要提醒：${NC}"
echo "1. 所有团队成员需要重新克隆仓库"
echo "2. 或者执行: git fetch origin && git reset --hard origin/main"
echo ""

