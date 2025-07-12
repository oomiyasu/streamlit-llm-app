# スポーツ専門家相談Webアプリ

OpenAI GPT-4o-miniを活用したスポーツ分野の専門家AI相談アプリです。

## 🏅 機能

- **野球・サッカー・テニス**の3つのスポーツ分野に対応
- 各分野に特化したAI専門家との対話
- 直感的で使いやすいWebインターフェース
- リアルタイムでの質問・回答

## 🚀 技術スタック

- **Frontend**: Streamlit
- **AI/LLM**: OpenAI GPT-4o-mini (LangChain経由)
- **Language**: Python
- **環境管理**: python-dotenv

## 📋 必要な環境

- Python 3.8以上
- OpenAI APIキー

## ⚙️ セットアップ

1. リポジトリをクローン
```bash
git clone https://github.com/your-username/streamlit-llm-app.git
cd streamlit-llm-app
```

2. 仮想環境を作成・有効化
```bash
python -m venv env
source env/bin/activate  # macOS/Linux
# または
env\Scripts\activate  # Windows
```

3. 必要なパッケージをインストール
```bash
pip install streamlit langchain-openai python-dotenv
```

4. 環境変数を設定
```bash
# .envファイルを作成し、OpenAI APIキーを設定
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

## 🏃‍♂️ 実行方法

```bash
streamlit run app.py
```

ブラウザで `http://localhost:8501` にアクセスしてアプリを使用できます。

## 💡 使用方法

1. **専門家を選択**: 野球、サッカー、テニスから相談したい分野を選択
2. **質問を入力**: 具体的な質問や相談内容を入力
3. **実行**: ボタンをクリックして専門家からの回答を取得

## 📝 質問例

### 野球
- バッティングフォームを改善したい
- 投球のコントロールを良くする方法は？
- 守備位置の基本を教えて

### サッカー
- ドリブル技術を向上させたい
- 効果的なパス回しの方法は？
- オフサイドルールについて詳しく知りたい

### テニス
- サーブのスピードを上げたい
- バックハンドの打ち方のコツは？
- 試合での戦略について教えて

## 🔧 カスタマイズ

`app.py`の`sport_systems`辞書を編集することで、新しいスポーツ分野を追加したり、既存の専門家の特性を変更できます。

## 📄 ライセンス

このプロジェクトはMITライセンスの下で公開されています。

## 🤝 貢献

プルリクエストや課題報告を歓迎します。貢献する前に、まずイシューを作成して議論することをお勧めします。
