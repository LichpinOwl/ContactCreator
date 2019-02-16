import sys

# argv[1] = input file
# argv[2] = Contact Name
# argv[3] = Label
# argv[4] =  City
# argv[4] =  Region

with open(sys.argv[1], 'r') as Input:
	if  len(Input.readlines()) / 12000 == 0:
		i = 0
		FullNumberList = Input.readlines()
		with open(str(sys.argv[2]) + '.csv', 'w') as Output:
				Output.write('Name,Given Name,Additional Name,Family Name,Yomi Name,Given Name Yomi,Additional Name Yomi,Family Name Yomi,Name Prefix,Name Suffix,Initials,Nickname,Short Name,Maiden Name,Birthday,Gender,Location,Billing Information,Directory Server,Mileage,Occupation,Hobby,Sensitivity,Priority,Subject,Notes,Language,Photo,Group Membership,Phone 1 - Type,Phone 1 - Value,Phone 2 - Type,Phone 2 - Value,Phone 3 - Type,Phone 3 - Value,Address 1 - Type,Address 1 - Formatted,Address 1 - Street,Address 1 - City,Address 1 - PO Box,Address 1 - Region,Address 1 - Postal Code,Address 1 - Country,Address 1 - Extended Address,Event 1 - Type,Event 1 - Value,Event 2 - Type,Event 2 - Value\n')
				with open(sys.argv[1], 'r') as Input:
					FullNumberList = Input.readlines()
					for PhoneNumber in FullNumberList :
						if i < 10 : 
							Output.write('0000' + str(i) + '_' + str(sys.argv[2]) + ',,,,,,,,,,,,,,,,,,,,,,,,,,,,' + sys.argv[3] + ' ::: * myContacts,mobile,' + str(PhoneNumber)[:-1] + ',,,,,,,,' + sys.argv[4] + ',,' + sys.argv[5] + ',,,,,,,\n')
						elif i < 100 :
							Output.write('000' + str(i) + '_' + str(sys.argv[2]) + ',,,,,,,,,,,,,,,,,,,,,,,,,,,,' + sys.argv[3] + ' ::: * myContacts,mobile,' + str(PhoneNumber)[:-1] + ',,,,,,,,' + sys.argv[4] + ',,' + sys.argv[5] + ',,,,,,,\n')
						elif i < 1000 :
							Output.write('00' + str(i) + '_' + str(sys.argv[2]) + ',,,,,,,,,,,,,,,,,,,,,,,,,,,,' + sys.argv[3] + ' ::: * myContacts,mobile,' + str(PhoneNumber)[:-1] + ',,,,,,,,' + sys.argv[4] + ',,' + sys.argv[5] + ',,,,,,,\n')
						elif i < 10000 : 
							Output.write('0' + str(i) + '_' + str(sys.argv[2]) + ',,,,,,,,,,,,,,,,,,,,,,,,,,,,' + sys.argv[3] + ' ::: * myContacts,mobile,' + str(PhoneNumber)[:-1] + ',,,,,,,,' + sys.argv[4] + ',,' + sys.argv[5] + ',,,,,,,\n')
						else : 
							Output.write(str(i) + '_' + str(sys.argv[2]) + ',,,,,,,,,,,,,,,,,,,,,,,,,,,,' + sys.argv[3] + ' ::: * myContacts,,mobile,' + str(PhoneNumber)[:-1] + ',,,,,,,,' + sys.argv[4] + ',,' + sys.argv[5] + ',,,,,,,\n')
						i += 1
	else:
		i = 0
		with open(sys.argv[1], 'r') as Input:
			FullNumberList = Input.readlines()
			OutputFileCount = (len(FullNumberList) / 12000) + 1
			start = 0
			end = 12000
			for c in range(0, OutputFileCount) :
				print 'start : ' + str(start)
				print 'end : ' + str(end)
				with open(str(sys.argv[2]) + '_' + str(c) + '.csv', 'w') as Output:
					Output.write('Name,Given Name,Additional Name,Family Name,Yomi Name,Given Name Yomi,Additional Name Yomi,Family Name Yomi,Name Prefix,Name Suffix,Initials,Nickname,Short Name,Maiden Name,Birthday,Gender,Location,Billing Information,Directory Server,Mileage,Occupation,Hobby,Sensitivity,Priority,Subject,Notes,Language,Photo,Group Membership,Phone 1 - Type,Phone 1 - Value,Phone 2 - Type,Phone 2 - Value,Phone 3 - Type,Phone 3 - Value,Address 1 - Type,Address 1 - Formatted,Address 1 - Street,Address 1 - City,Address 1 - PO Box,Address 1 - Region,Address 1 - Postal Code,Address 1 - Country,Address 1 - Extended Address,Event 1 - Type,Event 1 - Value,Event 2 - Type,Event 2 - Value\n')
					with open(sys.argv[1], 'r') as Input:
						FullNumberList = Input.readlines()
						PartialNumberList = FullNumberList[start:end]
						for PhoneNumber in PartialNumberList : 
							if i < 10 : 
								Output.write('0000' + str(i) + '_' + str(sys.argv[2]) + ',,,,,,,,,,,,,,,,,,,,,,,,,,,,' + sys.argv[3] + ' ::: * myContacts,mobile,' + str(PhoneNumber)[:-1] + ',,,,,,,,' + sys.argv[4] + ',,' + sys.argv[5] + ',,,,,,,\n')
							elif i < 100 :
								Output.write('000' + str(i) + '_' + str(sys.argv[2]) + ',,,,,,,,,,,,,,,,,,,,,,,,,,,,' + sys.argv[3] + ' ::: * myContacts,mobile,' + str(PhoneNumber)[:-1] + ',,,,,,,,' + sys.argv[4] + ',,' + sys.argv[5] + ',,,,,,,\n')
							elif i < 1000 :
								Output.write('00' + str(i) + '_' + str(sys.argv[2]) + ',,,,,,,,,,,,,,,,,,,,,,,,,,,,' + sys.argv[3] + ' ::: * myContacts,mobile,' + str(PhoneNumber)[:-1] + ',,,,,,,,' + sys.argv[4] + ',,' + sys.argv[5] + ',,,,,,,\n')
							elif i < 10000 : 
								Output.write('0' + str(i) + '_' + str(sys.argv[2]) + ',,,,,,,,,,,,,,,,,,,,,,,,,,,,' + sys.argv[3] + ' ::: * myContacts,mobile,' + str(PhoneNumber)[:-1] + ',,,,,,,,' + sys.argv[4] + ',,' + sys.argv[5] + ',,,,,,,\n')
							else : 
								Output.write(str(i) + '_' + str(sys.argv[2]) + ',,,,,,,,,,,,,,,,,,,,,,,,,,,,' + sys.argv[3] + ' ::: * myContacts,,mobile,' + str(PhoneNumber)[:-1] + ',,,,,,,,' + sys.argv[4] + ',,' + sys.argv[5] + ',,,,,,,\n')
							i += 1
				start = (c + 1) * 12000
				if (c == OutputFileCount - 2) :
					end = len(FullNumberList)
				else:
					end = ((c + 2) * 12000)


