# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## プロジェクト概要

「ベクトル検索実践入門」書籍のサンプルコードリポジトリ。12章分のベクトル検索実装例とAmazon Science ESCIデータセット（Gitサブモジュール）を含む。

## 開発コマンド

### Docker Compose での実行（推奨）

```bash
# セットアップ
cd code
git submodule update --init --recursive
docker compose up -d

# スクリプト実行
docker compose exec workspace /code/ch01_data_preparation.py

# または script ディレクトリのシェルスクリプトを使用
./script/ch01/docker_exec.sh

# サービス停止
docker compose down
```

### GPU対応

```bash
git apply docker-compose.yaml.gpu.patch
docker compose up -d
```

### ローカル実行（uv使用）

```bash
uv sync                    # 依存関係インストール（ルートに.venvが作成される）
uv run python code/ch01_data_preparation.py
```

### フォーマット

```bash
uv run ruff format code/
```

## アーキテクチャ

```
./
├── pyproject.toml          # workspace root設定
├── uv.lock                 # 依存関係ロックファイル
├── .venv/                  # 仮想環境（ルートに配置、IDE補完用）
├── .python-version         # Pythonバージョン指定
└── code/
    ├── ch*.py              # 章別サンプルコード（メイン実装）
    ├── script/ch*/         # 章別シェルスクリプト（docker_exec_*.sh）
    ├── output/ch*/         # 章別出力例
    ├── esci-data/          # ESCIデータセット（Gitサブモジュール）
    ├── tmp/                # 一時ファイル（モデル、キャッシュ）
    ├── pyproject.toml      # パッケージ依存関係設定（workspace member）
    ├── requirements.txt    # 章別依存関係一覧
    └── docker-compose.yaml # workspace + OpenSearch環境
```

## Docker Compose サービス

- **workspace**: Python実行環境（/codeにマウント）
- **opensearch**: ベクトル検索エンジン（ポート9200、第3章以降で使用）

## 主要ライブラリ

| 章 | ライブラリ |
|----|-----------|
| 1章 | pandas, pyarrow, fastparquet |
| 2章 | transformers, sentence-transformers |
| 3章 | faiss-cpu, opensearch-py |
| 5章 | sentencepiece, fugashi, datasets, accelerate |
| 11章 | xgboost |

## 注意事項

- Python 3.14以上が必要（ローカル実行時）
- Dockerイメージは Python 3.12 ベース
- ESCIデータセットはGitサブモジュールとして管理（初回クローン後に `git submodule update --init --recursive` が必要）
