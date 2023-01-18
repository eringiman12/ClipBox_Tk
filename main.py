import tkinter as tk
from tkinter import messagebox
import pyperclip

class Application(tk.Frame):

    def __init__(self, master = None):
        super().__init__(master)
        
        # ウィンドウタイトル
        self.master.title("Entryの作成") 
        # ウィンドウサイズ(幅x高さ)
        self.master.geometry("400x400")    
      
        # 表示する値
        self.entry_text = tk.StringVar() 
        
        # 左辺取り除く   
        self.entry_text2 = tk.StringVar() 
        
        # 区切り値  
        self.entry_text3 = tk.StringVar()  
        
                
        #ラベルWidgetを生成
        label = tk.Label(self.master, text = "変換対象文字列") 
        #ラベルを配置
        label.place(relx=0, rely=0.01, relheight=0.06, relwidth=0.3)
        
        # Entry（テクストボックス）の作成
        entry = tk.Entry(self.master,
               justify = tk.LEFT, # tk.RIGHT:右寄せ、tk.LEFT:左寄せ、tk.CENTER:中央寄せ
               textvariable = self.entry_text # 表示する値
            )
        
        entry.place(relx=0.01, rely=0.07, relheight=0.5, relwidth=0.97) 

          #ラベルWidgetを生成
        label2 = tk.Label(self.master, text = "以降取得") 
        #ラベルを配置
        label2.place(relx=0.2, rely=0.6, relheight=0.06, relwidth=0.4)
        
        # 左辺取り除く 
        entry2 = tk.Entry(self.master,
               width = 5,         # ウィジェットの幅（文字数で指定）
               justify = tk.LEFT, # tk.RIGHT:右寄せ、tk.LEFT:左寄せ、tk.CENTER:中央寄せ
               textvariable = self.entry_text2 # 表示する値
            )
        entry2.place(relx=0.01, rely=0.6, relheight=0.06, relwidth=0.3)
        
        # 区切り文字列ラベル
        label3 = tk.Label(self.master, text = "区切り文字列") 
        #ラベルを配置
        label3.place(relx=0.23, rely=0.7, relheight=0.06, relwidth=0.4)
        
        # 区切り文字列入力
        entry3 = tk.Entry(self.master,
               width = 20,         # ウィジェットの幅（文字数で指定）
               justify = tk.LEFT, # tk.RIGHT:右寄せ、tk.LEFT:左寄せ、tk.CENTER:中央寄せ
               textvariable = self.entry_text3 # 表示する値
            )
        entry3.place(relx=0.01, rely=0.7, relheight=0.06, relwidth=0.3)
        
        # ボタンの作成
        btn_input = tk.Button(self.master, text = "入力", command = self.btn_input_click)
        btn_input.place(relx=0.01, rely=0.8, relheight=0.06, relwidth=0.13)

        btn_clear = tk.Button(self.master, text = "クリア", command = self.btn_clear_click)
        btn_clear.place(relx=0.15, rely=0.8, relheight=0.06, relwidth=0.13)

    def btn_input_click(self):
        # 各エリアリスト  
        Area_List = [
           self.entry_text.get(),  #　メインエリアの入力値
           self.entry_text2.get(), #　左辺エリア値
         #   self.entry_text3.get(),  #　右辺エリア値
           self.entry_text3.get()  #　分割値
        ]
        
        # 空を含むか   
        Bol = self.Val_Chk(Area_List)
        
        if Bol:
            # 入力リストで変換文字列、分割対象文字列を格納
            A_List = Area_List[0].split(Area_List[2])
            rep_val = ""
            
            # 切り取り以降対象文字列
            target = Area_List[1]
            
            # 入力リスト対象ループ
            for a_val in A_List:
               # 値が空以外
               if a_val != "":
                  # 値のインデックス取得
                  idx = a_val.find(target)
                  # 文字列の切り取り
                  r = a_val[idx+1:] 
                  
                  # クリップボードにコピペ対象変数
                  if rep_val != "":
                     rep_val += "," + r
                  else:
                     rep_val = r
            
            # クリップボードにコピペ
            pyperclip.copy(rep_val)
         
        else:
            messagebox.showinfo("","入力値に空が含まれてます。\n入力ボックスは、すべて入力してください。")
    
    def Val_Chk(self,Area_List):
       # 空判定  
       em = True
       
       # 空を含むか判定   
       for a in Area_List:
           if a == "":
              em = False
              break
        
       return em
           
    def btn_clear_click(self):
        self.entry_text.set("")
        self.entry_text2.set("")
        self.entry_text3.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master = root)
    app.mainloop()
    
