print("-"*50)
b=input("输入网址：")
print("-"*50,"\n","By Harder\n")
print("\n"*5)
a="<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><msg serviceID=\"1\" templateID=\"1\" action=\"plugin\" actionData=\"AppCmd://OpenContactInfouin=0\" a_actionData=\"mqqapi://card/show_pslcard?src_type=internal&amp;source=sharecard&amp;version=1&amp;uin=\" i_actionData=\"mqqapi://card/show_pslcard?src_type=internal&amp;source=sharecard&amp;version=1&amp;uin=\" brief=\"[特别关心]男神\" sourceMsgId=\"0\" url=\"\" flag=\"0\" adverSign=\"0\" multiMsgFlag=\"0\"><item layout=\"5\"><picture cover=\"%s\" w=\"0\" h=\"0\" /><title size=\"25\" color=\"FF0000\"></title></item><item layout=\"0\"><hr hidden=\"false\" style=\"0\" /><title size=\"28\" color=\"FF0000\">腾讯认证男神</title></item><source name=\"官方认证\" icon=\"http://url.cn/JS8oE7\" action=\"\" appid=\"0\" /></msg>"%(b)
print(a)
print("\n"*5)

