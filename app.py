from flask import Flask, render_template

app = Flask(__name__)

# --- 路由設定 ---

# 1. 首頁 (Dashboard)
@app.route('/')
def index():
    return render_template('index.html', page_title="首頁 - 健康數據總覽")

# 2. 紀錄頁 (Record) - 輸入每日數據
@app.route('/record')
def record():
    return render_template('record.html', page_title="紀錄 - 每日習慣")

# 3. 計畫頁 (Plan) - 飲食規劃與營養建議
@app.route('/plan')
def plan():
    return render_template('plan.html', page_title="計畫 - 飲食與減重")

# 4. 圖表頁 (Charts) - 視覺化統計
@app.route('/charts')
def charts():
    return render_template('charts.html', page_title="統計 - 健康圖表")

# 5. 個人設定頁 (Profile) - 新增功能！
@app.route('/profile')
def profile():
    return render_template('profile.html', page_title="設定 - 個人目標")

# 6. 關於頁 (About) - 團隊介紹
@app.route('/about')
def about():
    return render_template('about.html', page_title="關於 - 給我滿分團隊")

if __name__ == '__main__':
    app.run(debug=True)