import csv
import sys

from imdbpie import Imdb


def main():
	show = Imdb()
	print("Enter a tv show:")
	input_user = input()
	print("Please wait.....")
	show_id = show.search_for_title(input_user)
	if(len(show_id) == 0):
		return print("No Keywords Match")
	imdb_id = show_id[0]["imdb_id"]
	type_of = show.get_title_by_id(imdb_id).type
	if(type_of != str("tv_series")):
		return("Not A TV Series")
	episodes = show.get_episodes(imdb_id)
	show_title = show.get_title_by_id(imdb_id).title
	show_rating = show.get_title_by_id(imdb_id).rating
	year = show.get_title_by_id(imdb_id).year
	ep_list = []
	len_l = len(episodes)
	for i in range(0,len_l):
		id_id = episodes[i].imdb_id
		ini_epi = show.get_title_by_id(id_id)
		val = ini_epi.title
		val2 = ini_epi.rating
		ep_list.append([val,val2])

	filered_ep_list = []

	for i in ep_list:
		if(None not in i):
			filered_ep_list.append(i)

	aver_rating = 0
	for i in range(0,len(filered_ep_list)):
		aver_rating += float(filered_ep_list[i][1])
	aver_rating = round(aver_rating/len(filered_ep_list),1)
	sor_low = sorted(filered_ep_list,key=lambda x: x[1])
	sor_high = sorted(filered_ep_list,key=lambda x: x[1],reverse=True)

	length = 10

	if(len(sor_low) < 10):
		length = int(len(sor_low))

		
	with open('imdb.csv','w') as csv:
		csv.write("Show Title: "+ str(show_title))
		csv.write('\n')
		csv.write("Show Rating: "+ str(show_rating))
		csv.write('\n')
		csv.write("Year: "+ str(year))
		csv.write('\n')
		csv.write("Average Rating: "+ str(aver_rating))
		csv.write('\n')
		csv.write("Lowest Rated Episodes")
		csv.write('\n')
		for i in range(0,length):
			csv.write(str(i + 1) + " " + str(sor_low[i][0]) + " , "+ str(sor_low[i][1])) 
			csv.write('\n')
		csv.write('\n')

		csv.write("Highest Rated Episodes")
		csv.write('\n')
		for i in range(0,length):
			csv.write(str(i + 1) + " " + str(sor_high[i][0]) + " , "+ str(sor_high[i][1])) 
			csv.write('\n')

		print("CSV now available")

if __name__ == "__main__":
	main()






