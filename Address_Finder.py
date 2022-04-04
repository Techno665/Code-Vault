# Name :	Address Finder
# Author :	Reece Doktor
# Date :	31/03/2022
# Version :	1.0
# Takes GPS Coordinates And Finds The Address without using the Google Maps API

import pyperclip
import requests
from bs4 import BeautifulSoup


def Find_Address(Coordinates):
	Google_Maps_URL = "https://www.google.com/maps/place/"
	Google_Maps_Search = Google_Maps_URL + Coordinates + "/"
	Google_Maps_Search_Result = requests.get(Google_Maps_Search).text
	Google_Maps_Search_Result_Parsed = BeautifulSoup(Google_Maps_Search_Result, "html.parser")
	Google_Maps_Search_Result_Parsed = Google_Maps_Search_Result_Parsed.find_all("meta")
	Google_Maps_Search_Result_Parsed = str(Google_Maps_Search_Result_Parsed)
	Google_Maps_Search_Result_Parsed = Google_Maps_Search_Result_Parsed.split("<meta")
	Google_Maps_Search_Result_Parsed = [x for x in Google_Maps_Search_Result_Parsed if 'property="og:description' in x]
	Google_Maps_Search_Result_Parsed = str(Google_Maps_Search_Result_Parsed)
	# Replace used to cut down on unnecessary/unwanted content
	Google_Maps_Search_Result_Parsed = Google_Maps_Search_Result_Parsed.replace("'", "").replace('"', '').replace("[ content=", "").replace(" property=og:description/>, ]", "")
	# Changes abbreviation to full
	Google_Maps_Search_Result_Parsed = Google_Maps_Search_Result_Parsed.replace("St,", "Street,").replace("Ct,", "Court,").replace("Cres,", "Crescent,").replace("Dr,", "Drive,").replace("Rd,", "Road,")
	# Changes state abbreviation to full state name
	Google_Maps_Search_Result_Parsed = Google_Maps_Search_Result_Parsed.replace("NSW", ", New South Wales,").replace("QLD", ", Queensland,").replace("SA", ", South Australia,").replace("TAS", ", Tasmania,").replace("VIC", ", Victoria,").replace("WA", ", Western Australia,").replace("ACT", ", Australian Capital Territory,").replace("NT", ", Northern Territory,").replace("JBT", ", Jervis Bay Territory,")
	# Fixes Grammer Error that can occur for addresses
	Google_Maps_Search_Result_Parsed = Google_Maps_Search_Result_Parsed.replace(" , ", ", ")
	return Google_Maps_Search_Result_Parsed


if __name__ == '__main__':
	TESTING = False
	if TESTING == False:
		while True:
			# Coordinates Input Area, Can be changed at a later point
			Coordinates = input("Please Input Coordinates:\n")
			Coordinates = Coordinates.replace(" / ", ", ")
			Address = Find_Address(Coordinates)
			print("\n\n" + Address + "\n\n")
			pyperclip.copy(Address)


	# Internal Testing Function
	Coordinates = "-27.631077397001572, 153.1187359009946"
	Test_Address = "Slacks Creek, Queensland, 4127"
	Test = Find_Address(Coordinates)
	if Test.upper() == Test_Address.upper():
		# print("Success")
		pass
	else:
		# print("Failed")
		raise ValueError("TEST 1 FAILED!\nExpecting " + Test_Address + "\nResult " + Test)



	Coordinates = "-27.653355415707292, 153.10244581500717"
	Test_Address = "47 Birch Street, Kingston, Queensland, 4114"
	Test = Find_Address(Coordinates)
	if Test.upper() == Test_Address.upper():
		# print("Success")
		pass
	else:
		# print("Failed")
		raise ValueError("TEST 2 FAILED!\nExpecting " + Test_Address + "\nResult " + Test)



	Coordinates = "-27.71656464422887, 153.18788476658082"
	Test_Address = "16 Tweed Street, Beenleigh, Queensland, 4207"
	Test = Find_Address(Coordinates)
	if Test.upper() == Test_Address.upper():
		# print("Success")
		pass
	else:
		# print("Failed")
		raise ValueError("TEST 3 FAILED!\nExpecting " + Test_Address + "\nResult " + Test)



	Coordinates = "-27.597366023675708, 153.12676739182382"
	Test_Address = "14 Delsia Street, Rochedale South, Queensland, 4123"
	Test = Find_Address(Coordinates)
	if Test.upper() == Test_Address.upper():
		# print("Success")
		pass
	else:
		# print("Failed")
		raise ValueError("TEST 4 FAILED!\nExpecting " + Test_Address + "\nResult " + Test)



	Coordinates = "-27.618185965549664, 153.13633463825994"
	Test_Address = "5 Jillian Court, Springwood, Queensland, 4127"
	Test = Find_Address(Coordinates)
	if Test.upper() == Test_Address.upper():
		# print("Success")
		pass
	else:
		# print("Failed")
		raise ValueError("TEST 5 FAILED!\nExpecting " + Test_Address + "\nResult " + Test)



	Coordinates = "-27.663557421386272, 153.1933464831534"
	Test_Address = "9 Innes Crescent, Cornubia, Queensland, 4130"
	Test = Find_Address(Coordinates)
	if Test.upper() == Test_Address.upper():
		# print("Success")
		pass
	else:
		# print("Failed")
		raise ValueError("TEST 6 FAILED!\nExpecting " + Test_Address + "\nResult " + Test)



	print("ALL TEST SUCCESSFULL")
