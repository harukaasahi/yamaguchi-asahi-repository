htmlの構造
base.html
home/index.html 最初の画面
account/signup.html 会員登録
registration/login.html ログイン
account/memberinf.html 会員情報確認(ログイン時のみ)
account/changeinfo.html 会員情報変更(ログイン時のみ)
account/comfirm_info.html 会員情報変更の確認(ログイン時のみ)
account/suceed_info.html 会員情報変更の完了



モデル
account/User
  username,email,last_name,first_name
account/Address
  account_number(settings.AUTH_USER_MODELよりForeignkey)
   postcode,prefecture,city,zip,building,room,created_times
