# Input the below 2 values
start_seat_num = 14855
end_seat_num = 14857      # boundary is inclusive

# List of Seat Numbers
seat_numbers = []
for i in range(start_seat_num, end_seat_num+1):
  seat_numbers.append(i)

import requests

url = "http://centres.muhs.edu.in/Vf$ato/JR/MX1/ug_res/res_x1.asp"

rows = []

for seat_number in seat_numbers:

  payload='cr=MBBS&cl=4&sn=' + str(seat_number)
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  
  result = response.text
  name = 'Name of the Student:- ' + result[result.index(":- ",result.index("Name of the Student"))+3:result.index("</p>",result.index("Name of the Student"))]

  college = result[result.index(":- ",result.index("College"))+10:result.index("</p>",result.index("College"))].replace("&nbsp;", " ")

  seat_num = result[result.index(":- ",result.index("Seat No"))+10:result.index("</p>",result.index("Seat No"))].replace("&nbsp;", " ")

  general_med = result[result.index('<td width="12%">',result.index('GENERAL MEDICINE'))+54:result.index("</tr>",result.index('GENERAL MEDICINE'))-26]

  general_surgery = result[result.index('<td width="12%">',result.index('GENERAL SURGERY'))+54:result.index("</tr>",result.index('GENERAL SURGERY'))-26]

  obst_gyna = result[result.index('<td width="12%">',result.index('OBST.'))+54:result.index("</tr>",result.index('OBST.'))-26]

  pediatrics = result[result.index('<b>',result.index('PAEDIATRICS'))+18:result.index("</tr>",result.index('PAEDIATRICS'))-26]

  grand_total = result[result.index('<td colspan="7"',result.index('GRAND TOTAL'))+54:result.index("</strong>",result.index('GRAND TOTAL'))].replace("<strong>","")

  result = result[result.index('<td colspan="7"',result.index('RESULT'))+54:result.index("</tr>",result.index('RESULT'))-15]

  row = [name, college, seat_num,  general_med, general_surgery, obst_gyna, pediatrics, grand_total, result]
  
  rows.append(row)

  print(name)
  print(college)
  print(seat_num)
  print(general_med)
  print(general_surgery)
  print(obst_gyna)
  print(pediatrics)
  print(grand_total)
  print(result)

  print("\n")

import pandas as pd

df = pd.DataFrame(rows, columns=['Name of the Student', 'College', 'Seat No', 'GENERAL MEDICINE', 'GENERAL SURGERY', 'OBST. & GYNA.', 'PAEDIATRICS', 'GRAND TOTAL', 'RESULT'])

df.to_excel("MBBS_UG_WINTER_2020.xlsx")