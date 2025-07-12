# 環境変数の読み込み（.envファイルからAPIキーなどを取得）
from dotenv import load_dotenv
load_dotenv()

# LangChainライブラリからChatOpenAIとメッセージ型をインポート
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# OpenAI GPT-4o-miniモデルを使用したLLMインスタンスを作成
# temperature=0で出力の一貫性を高める
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

# Streamlit Webアプリケーションフレームワークをインポート
import streamlit as st

def get_expert_response(input_message: str, selected_sport: str) -> str:
    """
    スポーツの専門家からの回答を取得する関数
    
    Args:
        input_message (str): ユーザーからの相談内容
        selected_sport (str): 選択されたスポーツ（野球、サッカー、テニス）
    
    Returns:
        str: 専門家からの回答
    """
    # 入力メッセージが空の場合はエラーメッセージを返す
    if not input_message:
        return "相談内容を入力してください。"
    
    # スポーツごとのシステムメッセージを辞書で管理
    # システムメッセージはAIの役割や専門性を定義する
    sport_systems = {
        "野球": "あなたは優秀な野球の専門家です。",
        "サッカー": "あなたは優秀なサッカーの専門家です。",
        "テニス": "あなたは優秀なテニスの専門家です。"
    }
    
    # 選択されたスポーツに対応するシステムメッセージを取得
    # 該当しない場合はデフォルトメッセージを使用
    system_content = sport_systems.get(selected_sport, "あなたは優秀なスポーツの専門家です。")
    
    # LLMに送信するメッセージリストを作成
    # SystemMessage: AIの役割を定義
    # HumanMessage: ユーザーからの質問内容
    messages = [
        SystemMessage(content=system_content),
        HumanMessage(content=input_message),
    ]
    
    # LLMにメッセージを送信して回答を取得
    try:
        response = llm(messages)
        return response.content
    except Exception as e:
        # エラーが発生した場合はエラーメッセージを返す
        return f"エラーが発生しました: {str(e)}"

# =============================================================================
# Streamlit Webアプリケーションのメイン部分
# =============================================================================

# Webページの基本設定（タイトル、アイコン、レイアウト）
st.set_page_config(page_title="スポーツの専門家に相談するWebアプリ",
                   page_icon=":sports_medal:", layout="wide")

# アプリケーションのメインタイトルを表示
st.title("スポーツの専門家に相談するWebアプリ")

# =============================================================================
# アプリケーションの概要と操作方法を表示
# =============================================================================

# アプリケーションの概要を説明
st.markdown("""
### 📝 アプリケーションの概要
このWebアプリでは、**野球・サッカー・テニス**の各分野における専門家のAIとチャットができます。  
各スポーツに特化した知識を持つAIが、あなたの質問や相談に詳しく回答します。

### 🔧 使い方
1. **専門家を選択**: 下のラジオボタンから相談したいスポーツを選んでください
2. **質問を入力**: テキストボックスに質問や相談したい内容を入力してください
3. **実行ボタンをクリック**: 「実行」ボタンを押すと、選択した分野の専門家AIが回答します

### ⚡ 質問例
- **野球**: 「バッティングフォームを改善したい」「投球のコントロールを良くする方法は？」
- **サッカー**: 「ドリブル技術を向上させたい」「守備の基本を教えて」
- **テニス**: 「サーブのスピードを上げたい」「バックハンドの打ち方のコツは？」
""")

# 区切り線を表示してUIを見やすくする
st.divider()

# ラジオボタンで専門家（スポーツ）を選択
# ユーザーは野球、サッカー、テニスの中から1つを選択
selected_item = st.radio(
    "🏆 相談する専門家を選択してください",
    ["野球", "サッカー", "テニス"],
    help="質問したいスポーツ分野を選んでください"
)

# テキスト入力フィールドでユーザーからの相談内容を受け取る
input_message = st.text_input(
    label="💬 専門家に相談する内容を入力してください",
    placeholder="例：バッティングフォームを改善したい",
    help="具体的な質問や相談内容を入力してください"
)

# 選択されたスポーツに応じて説明文を表示
with st.container():
    if selected_item == "野球":
        st.info("⚾ **野球の専門家** が選択されています。バッティング、ピッチング、守備など野球に関するあらゆる質問にお答えします。")
    elif selected_item == "サッカー":
        st.info("⚽ **サッカーの専門家** が選択されています。ドリブル、シュート、戦術などサッカーに関するあらゆる質問にお答えします。")
    else:
        st.info("🎾 **テニスの専門家** が選択されています。サーブ、ストローク、戦略などテニスに関するあらゆる質問にお答えします。")

# 「実行」ボタンが押された時の処理
if st.button("🚀 実行", type="primary", help="選択した専門家に質問を送信します"):
    # 区切り線を表示して結果セクションを分ける
    st.divider()
    
    # 入力内容がある場合のみ処理を実行
    if input_message:
        # 相談内容の確認メッセージを表示
        with st.container():
            st.write(f"**{selected_item}の専門家**に以下の内容で相談しています...")
            with st.expander("📋 相談内容を確認", expanded=True):
                st.write(input_message)
        
        # プログレスバーとスピナーで処理中であることを示す
        with st.spinner(f'{selected_item}の専門家が回答を準備中です...'):
            # 作成した関数を呼び出してLLMからの回答を取得
            response = get_expert_response(input_message, selected_item)
        
        # エラーメッセージの場合は赤色で表示
        if response.startswith("エラーが発生しました") or response == "相談内容を入力してください。":
            st.error("❌ " + response)
        else:
            # 正常な回答の場合は専門家の回答として表示
            st.success(f"✅ {selected_item}の専門家からの回答が届きました！")
            with st.container():
                st.markdown("### 🎯 専門家の回答")
                st.markdown(f"""
                <div style="background-color: #f0f8ff; padding: 20px; border-radius: 10px; border-left: 5px solid #1f77b4;">
                {response}
                </div>
                """, unsafe_allow_html=True)
    else:
        # 入力が空の場合はエラーメッセージを表示
        st.error("⚠️ 相談内容を入力してください。")
