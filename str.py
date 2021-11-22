import streamlit as st
import time

def main():
    # タイトル
    st.title('ローンシミュレーター')
    # 純粋なテキスト
    st.text('ローンの借入額と返済年月から月々の返済額を計算します。\nボーナス併用有無、頭金有無からお選びいただけます。')
    
    #金額入力
    borrow = float(st.number_input('ご希望の借入金額を入力して下さい（万円）'))
    if not 1 <= borrow <= 3000:
        st.error('1~3000万円の範囲でローンの検討をして下さい')
        
    #利息入力
    bank = float(st.slider('年利率は何%ですか(%)',0.10,25.0,8.0,0.1))
    if borrow < 10 and bank >= 20: 
        st.info('利息が非常に高いので検討が必要です。')
    elif 10 <= borrow < 100 and bank >= 18: 
        st.info('利息が非常に高いので検討が必要です。')
    elif 100 <= borrow and bank >= 15: 
        st.info('利息が非常に高いので検討が必要です。')
    bank = bank/100
        
    #支払い回数入力
    time = float(st.slider('何回払いですか',3,600,24,1))
    time_y = (time - time%12)/12
    time_hy = (time - time%6)/6
    
    #頭金の有無
    dep = st.selectbox('頭金有り/無しを選択して下さい',('有り','無し'))
    if dep == '有り':
        deposit = float(st.number_input('頭金の金額を入力して下さい（万円）'))
        if deposit >  borrow:
            st.error('頭金の金額がローン金額を越えています。')

    #ボーナスの有無
    bonus = st.selectbox('ボーナス払いの有無選択して下さい',('有り','無し'))
    if bonus == '有り':
        bonus_value = float(st.number_input('ボーナス払いの金額を入力して下さい（万円）'))
        bonus_time = st.selectbox('ボーナスは年何回ですか',('1','2'))
        if bonus_time == '2':
            if bonus_value*2 + deposit >  borrow:
                st.error('ボーナス払いの金額と頭金の合計がローン金額を越えています。')
        if bonus_value >  borrow:
            st.error('ボーナス払いの金額がローン金額を越えています。')
        if dep =='有り':  
            if bonus_value + deposit >  borrow:  
                st.write('ボーナスと頭金の加算額がローン金額を越えています。')

    left_column, right_column = st.columns(2)
    button = left_column.button('計算結果の表示')
    #計算          total = borrow + borrow*bank*time/12
    if borrow > 0:
        total = borrow        
        #頭金有り
        if dep == '有り':
            total = total - deposit   
            
        total = total + total*bank*time/12
        
        #ボーナス併用あり
        if bonus == '有り':
            if bonus_time == '1':
                total = total - bonus_value*time_y
            elif bonus_time == '2'
                total = total - bonus_value*time_hy
        
        monthly = total/time
        if button:
            st.write('毎月のお支払い金額は','{:.2f}'.format(monthly),'万円です')
    
if __name__ == '__main__':
    main()
