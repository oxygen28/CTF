new_flag = "!?}De!e3d_5n_nipaOw_3eTR3bt4{_THB"
old_flag = ""
for i in range (0,len(new_flag),3):
	old_flag += new_flag[i+2]
	old_flag += new_flag[i]
	old_flag += new_flag[i+1]
	
print(old_flag[::-1])
