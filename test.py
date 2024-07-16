import re                                                  # 导入正则表达式模块

def get_numeric(input_string):                             # 定义函数
  match = re.findall(r'\d+\.\d{0,2}|\d+', input_string)    # 使用正则表达式查找所有匹配的数字部分
  if match:                                                # 如果有匹配结果
    num_str = match[0]                                     # 获取第一个匹配结果
    if '.' not in num_str:                                 # 如果数字字符串中没有小数点
      num_str += '.00'                                     # 在后面添加 ".00"
    else:
      num_str_split = num_str.split('.')                   #  如果有小数点,按小数点分割数字字符串
      if len(num_str_split[1]) > 2:                        # 如果小数部分长度大于 2
        num_str = num_str_split[0] + '.' + num_str_split[1][:2] # 截取小数部分为前 2 位，并与整数部分重新组合
    return num_str                                         # 返回处理后的数字字符串  
  return ''                                                # 如果没有匹配结果，返回空字符串

