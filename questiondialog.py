import tkinter.messagebox as mb
import requests, sys, webbrowser, bs4

title = mb.askyesno("最初に", "今から10のクイズを出します。\nちゃんと答えてね。")
result = 0


def questionA():
    q1 = mb.askyesno("１つ目", "点滴の成分は砂糖水と同じである")
    if q1 == False:
        return 1
    q2 = mb.askyesno("2つ目", "人口が5人しかいない国がある")
    if q2 == False:
        return 1
    googling("人口が5人の国")
    q3 = mb.askyesno("3つ目", "キリンの睡眠時間は人間より長い")
    if q3 == True:
        return 1
    q4 = mb.askyesno("4つ目","豚は人間より早く走ることができる")
    if q4 == False:
        return 1
    q5 = mb.askyesno("5つ目","ビリヤードの和名は送球である")
    if q5 == True:
        return 1
    else:
        return 2



def googling(str):
    res = requests.get('http://google.com/search?q=' + ''.join(str))
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, features="html.parser")
    link_elems = soup.select('.r a')
    webbrowser.open('http://google.com' + link_elems[0].get('href'))
    return


if title == True:
    result = questionA()
else:
    mb.showinfo("NO", "帰れ")

if result == 1:
    mb.showinfo("残念", "君はもっと勉強が必要だ。\n出直して来なさい。")
elif result == 2:
    mb.showinfo("おめでとう", "クリアおめでとう！")
